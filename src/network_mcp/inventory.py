"""YAML inventory loader.

Reads the device inventory file and provides lookup by device_id.
Credentials are resolved from environment variables, never from YAML.
"""

import logging
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

# Default inventory path relative to project root
_DEFAULT_INVENTORY = Path(__file__).resolve().parent.parent.parent / "inventory" / "lab.yaml"


@dataclass(frozen=True)
class DeviceInfo:
    """Parsed device entry from inventory."""

    device_id: str
    hostname: str
    platform: str
    site: str
    role: str
    extra: dict[str, Any] = field(default_factory=dict)


class Inventory:
    """Loads and queries the device inventory."""

    def __init__(self, path: str | Path | None = None) -> None:
        self._path = Path(path) if path else _DEFAULT_INVENTORY
        self._devices: dict[str, DeviceInfo] = {}
        self._loaded = False

    def load(self) -> None:
        """Parse the YAML inventory file."""
        logger.info("Loading inventory from %s", self._path)
        with open(self._path) as fh:
            raw = yaml.safe_load(fh) or {}

        devices_raw = raw.get("devices", {})
        for device_id, attrs in devices_raw.items():
            self._devices[device_id] = DeviceInfo(
                device_id=device_id,
                hostname=attrs["hostname"],
                platform=attrs["platform"],
                site=attrs.get("site", ""),
                role=attrs.get("role", ""),
                extra={
                    k: v
                    for k, v in attrs.items()
                    if k not in ("hostname", "platform", "site", "role")
                },
            )

        logger.info("Loaded %d devices from inventory", len(self._devices))
        self._loaded = True

    def get_device(self, device_id: str) -> DeviceInfo:
        """Look up a device by its ID. Raises KeyError if not found."""
        if not self._loaded:
            self.load()
        if device_id not in self._devices:
            available = ", ".join(sorted(self._devices.keys()))
            raise KeyError(
                f"Device '{device_id}' not in inventory. "
                f"Available: {available}"
            )
        return self._devices[device_id]

    def list_devices(self) -> list[DeviceInfo]:
        """Return all devices in the inventory."""
        if not self._loaded:
            self.load()
        return list(self._devices.values())

    @staticmethod
    def get_credentials() -> tuple[str, str]:
        """Read device credentials from environment variables.

        Returns:
            (username, password) tuple.

        Raises:
            EnvironmentError: If NETWORK_USERNAME or NETWORK_PASSWORD is unset.
        """
        username = os.environ.get("NETWORK_USERNAME")
        password = os.environ.get("NETWORK_PASSWORD")
        if not username or not password:
            raise EnvironmentError(
                "Set NETWORK_USERNAME and NETWORK_PASSWORD environment variables."
            )
        return username, password
