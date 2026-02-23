"""Arista EOS driver extending the NAPALM base.

Uses NAPALM for common getters and pyeapi for Arista-specific operations
(EVPN, VXLAN, richer interface data, route summary). Phase 2 will add
EVPN/VXLAN tools; this module provides the Phase 1 foundation plus
get_route_summary which is not available in NAPALM.
"""

import asyncio
import logging
from typing import Any

import pyeapi

from network_mcp.drivers.napalm_base import NapalmDriver

logger = logging.getLogger(__name__)


class AristaDriver(NapalmDriver):
    """Arista EOS driver — NAPALM base + pyeapi extensions."""

    napalm_driver_name = "eos"

    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        timeout: int = 30,
        optional_args: dict[str, Any] | None = None,
    ) -> None:
        # Default to eAPI over HTTPS for Arista
        optional_args = optional_args or {}
        optional_args.setdefault("transport", "https")
        super().__init__(hostname, username, password, timeout, optional_args)
        self._eapi: pyeapi.client.Node | None = None

    # ── Connection lifecycle ──────────────────────────────────────────

    async def connect(self) -> None:
        # Open NAPALM connection (gives us standard getters)
        await super().connect()

        # Also set up a direct pyeapi connection for EOS-specific commands
        transport = self.optional_args.get("transport", "https")

        def _connect_eapi() -> pyeapi.client.Node:
            connection = pyeapi.connect(
                transport=transport,
                host=self.hostname,
                username=self.username,
                password=self.password,
                timeout=self.timeout,
            )
            return pyeapi.client.Node(connection)

        self._eapi = await asyncio.to_thread(_connect_eapi)
        logger.info("eAPI session established to %s", self.hostname)

    async def disconnect(self) -> None:
        self._eapi = None
        await super().disconnect()

    # ── eAPI helper ───────────────────────────────────────────────────

    async def _run_eapi_commands(
        self, commands: list[str], encoding: str = "json"
    ) -> list[dict[str, Any]]:
        """Run one or more EOS commands via eAPI and return parsed output."""
        if self._eapi is None:
            raise RuntimeError(
                f"Not connected to {self.hostname}. Call connect() first."
            )
        node = self._eapi

        def _run() -> list[dict[str, Any]]:
            return node.enable(commands, encoding=encoding)

        results = await asyncio.to_thread(_run)
        return [r["result"] for r in results]

    # ── Arista-specific overrides ─────────────────────────────────────

    async def get_route_summary(self) -> dict[str, Any]:
        """Get IP route summary via eAPI 'show ip route summary'."""
        raw = await self._run_eapi_commands(["show ip route summary"])
        data = raw[0]

        bgp_counts = data.get("bgpCounts", {})
        ospf_counts = data.get("ospfCounts", {})
        isis_counts = data.get("isisCounts", {})

        return {
            "total_routes": data.get("totalRoutes", 0),
            "connected": data.get("connected", 0),
            "static": data.get("static", 0),
            "bgp": {
                "total": bgp_counts.get("bgpTotal", 0),
                "external": bgp_counts.get("bgpExternal", 0),
                "internal": bgp_counts.get("bgpInternal", 0),
            },
            "ospf": {
                "total": ospf_counts.get("ospfTotal", 0),
                "intra_area": ospf_counts.get("ospfIntraArea", 0),
                "inter_area": ospf_counts.get("ospfInterArea", 0),
                "external_1": ospf_counts.get("ospfExternal1", 0),
                "external_2": ospf_counts.get("ospfExternal2", 0),
            },
            "isis": {
                "total": isis_counts.get("isisTotal", 0),
                "level_1": isis_counts.get("isisLevel1", 0),
                "level_2": isis_counts.get("isisLevel2", 0),
            },
            "internal": data.get("internal", 0),
        }
