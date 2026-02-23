"""Abstract base class defining the network driver interface.

Every vendor driver must implement all abstract methods or raise
NotImplementedError for operations the platform does not support.
Tools in server.py call these methods — they never reference vendors directly.
"""

from abc import ABC, abstractmethod
from typing import Any


class NetworkDriver(ABC):
    """Abstract base for all network device drivers."""

    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        timeout: int = 30,
        optional_args: dict[str, Any] | None = None,
    ) -> None:
        self.hostname = hostname
        self.username = username
        self.password = password
        self.timeout = timeout
        self.optional_args = optional_args or {}

    # ── Connection lifecycle ──────────────────────────────────────────

    @abstractmethod
    async def connect(self) -> None:
        """Open a connection to the device."""
        ...

    @abstractmethod
    async def disconnect(self) -> None:
        """Close the connection to the device."""
        ...

    async def __aenter__(self) -> "NetworkDriver":
        await self.connect()
        return self

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        await self.disconnect()

    # ── Read-only getters (Phase 1) ───────────────────────────────────

    @abstractmethod
    async def get_facts(self) -> dict[str, Any]:
        """Return device facts.

        Expected keys: vendor, model, os_version, hostname,
        serial_number, uptime, interface_list.
        """
        ...

    @abstractmethod
    async def get_interfaces(self) -> dict[str, Any]:
        """Return all interfaces with operational state.

        Expected per-interface keys: is_up, is_enabled, description,
        speed, mtu, mac_address, last_flapped.
        """
        ...

    @abstractmethod
    async def get_bgp_neighbors(self) -> dict[str, Any]:
        """Return BGP neighbor table.

        Expected structure: {vrf: {router_id, peers: {ip: {local_as,
        remote_as, is_up, is_enabled, uptime, address_family: {...}}}}}.
        """
        ...

    @abstractmethod
    async def get_lldp_neighbors(self) -> dict[str, Any]:
        """Return LLDP neighbor table.

        Expected structure: {local_port: [{hostname, port}]}.
        """
        ...

    @abstractmethod
    async def get_route_summary(self) -> dict[str, Any]:
        """Return IP routing table summary.

        Expected keys: total_routes, plus per-protocol counts
        (connected, static, bgp, ospf, isis).
        """
        ...

    # ── Config operations (Phase 3 — raise until implemented) ─────────

    @abstractmethod
    async def generate_config_diff(self, config: str) -> str:
        """Load candidate config and return a diff string. Does NOT apply.

        Must be called before commit_config.
        """
        ...

    @abstractmethod
    async def commit_config(self, config: str) -> dict[str, Any]:
        """Apply configuration after generate_config_diff was reviewed.

        Must only be called after the user has seen and confirmed the diff.
        """
        ...
