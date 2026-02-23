"""NAPALM-based driver implementing common getters across vendors.

Wraps NAPALM's synchronous methods with asyncio.to_thread() so the
MCP server event loop stays responsive. Vendor-specific drivers
(Arista, Cisco, Juniper) extend this class and can override any method.
"""

import asyncio
import logging
from typing import Any

from napalm import get_network_driver

from network_mcp.drivers.base import NetworkDriver

logger = logging.getLogger(__name__)


class NapalmDriver(NetworkDriver):
    """Common NAPALM implementation for multi-vendor operations.

    Subclasses set `napalm_driver_name` to the NAPALM driver string
    (e.g. "eos", "ios", "junos").
    """

    napalm_driver_name: str = ""

    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        timeout: int = 30,
        optional_args: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(hostname, username, password, timeout, optional_args)
        if not self.napalm_driver_name:
            raise ValueError(
                f"{type(self).__name__} must set napalm_driver_name"
            )
        driver_cls = get_network_driver(self.napalm_driver_name)
        self._device = driver_cls(
            hostname=self.hostname,
            username=self.username,
            password=self.password,
            timeout=self.timeout,
            optional_args=self.optional_args,
        )

    # ── Connection lifecycle ──────────────────────────────────────────

    async def connect(self) -> None:
        logger.info("Connecting to %s via NAPALM/%s", self.hostname, self.napalm_driver_name)
        await asyncio.to_thread(self._device.open)

    async def disconnect(self) -> None:
        logger.info("Disconnecting from %s", self.hostname)
        await asyncio.to_thread(self._device.close)

    # ── Read-only getters ─────────────────────────────────────────────

    async def get_facts(self) -> dict[str, Any]:
        return await asyncio.to_thread(self._device.get_facts)

    async def get_interfaces(self) -> dict[str, Any]:
        return await asyncio.to_thread(self._device.get_interfaces)

    async def get_bgp_neighbors(self) -> dict[str, Any]:
        return await asyncio.to_thread(self._device.get_bgp_neighbors)

    async def get_lldp_neighbors(self) -> dict[str, Any]:
        return await asyncio.to_thread(self._device.get_lldp_neighbors)

    async def get_route_summary(self) -> dict[str, Any]:
        """Route summary is not a standard NAPALM getter.

        Subclasses should override with platform-specific implementation.
        The base implementation raises NotImplementedError.
        """
        raise NotImplementedError(
            f"get_route_summary not available via NAPALM for "
            f"{self.napalm_driver_name}. Override in vendor driver."
        )

    # ── Config operations (Phase 3) ───────────────────────────────────

    async def generate_config_diff(self, config: str) -> str:
        def _diff() -> str:
            self._device.load_merge_candidate(config=config)
            return self._device.compare_config()

        return await asyncio.to_thread(_diff)

    async def commit_config(self, config: str) -> dict[str, Any]:
        def _commit() -> dict[str, Any]:
            self._device.load_merge_candidate(config=config)
            diff = self._device.compare_config()
            if not diff:
                self._device.discard_config()
                return {"changed": False, "diff": ""}
            self._device.commit_config()
            return {"changed": True, "diff": diff}

        return await asyncio.to_thread(_commit)
