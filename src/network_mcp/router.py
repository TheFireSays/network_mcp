"""Device router — maps device_id to the correct driver instance.

Looks up the device in inventory, resolves the platform to a driver class,
and returns a connected (or connectable) driver. Tools in server.py call
get_driver() and never import vendor-specific classes directly.
"""

import logging
from typing import Any

from network_mcp.drivers.base import NetworkDriver
from network_mcp.drivers.arista import AristaDriver
from network_mcp.inventory import DeviceInfo, Inventory

logger = logging.getLogger(__name__)

# Platform string → driver class. Extend this as new vendors are added.
PLATFORM_DRIVERS: dict[str, type[NetworkDriver]] = {
    "arista_eos": AristaDriver,
    # "cisco_ios": CiscoDriver,       # Phase 4
    # "cisco_nxos": CiscoNxosDriver,  # Phase 4
    # "juniper_junos": JuniperDriver, # Phase 4
}


class DeviceRouter:
    """Resolves device_id → configured driver instance."""

    def __init__(self, inventory: Inventory) -> None:
        self._inventory = inventory

    def get_driver(self, device_id: str) -> NetworkDriver:
        """Create a driver instance for the given device.

        The returned driver is NOT yet connected — callers must use it as
        an async context manager:

            async with router.get_driver("spine-01") as driver:
                facts = await driver.get_facts()

        Args:
            device_id: Inventory device ID (e.g. 'spine-01').

        Returns:
            NetworkDriver subclass instance (not yet connected).

        Raises:
            KeyError: Device not in inventory.
            ValueError: Platform not supported.
        """
        device: DeviceInfo = self._inventory.get_device(device_id)
        driver_cls = PLATFORM_DRIVERS.get(device.platform)
        if driver_cls is None:
            supported = ", ".join(sorted(PLATFORM_DRIVERS.keys()))
            raise ValueError(
                f"Unsupported platform '{device.platform}' for device "
                f"'{device_id}'. Supported: {supported}"
            )

        username, password = self._inventory.get_credentials()

        # Build optional_args from inventory extras (e.g. transport override)
        optional_args: dict[str, Any] = dict(device.extra)

        logger.info(
            "Routing %s (%s) → %s",
            device_id,
            device.platform,
            driver_cls.__name__,
        )

        return driver_cls(
            hostname=device.hostname,
            username=username,
            password=password,
            optional_args=optional_args,
        )

    def list_devices(self) -> list[dict[str, str]]:
        """Return a summary list of all devices in inventory."""
        return [
            {
                "device_id": d.device_id,
                "hostname": d.hostname,
                "platform": d.platform,
                "site": d.site,
                "role": d.role,
            }
            for d in self._inventory.list_devices()
        ]
