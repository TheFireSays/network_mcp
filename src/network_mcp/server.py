"""MCP server exposing network monitoring tools to Claude.

All tools use the DeviceRouter to obtain a driver — they never reference
vendor-specific classes. Each tool connects, runs the operation, and
disconnects via the async context manager pattern.
"""

import json
import logging

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

from network_mcp.inventory import Inventory
from network_mcp.router import DeviceRouter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

# ── Bootstrap ─────────────────────────────────────────────────────────

inventory = Inventory()
router = DeviceRouter(inventory)

mcp = FastMCP("network-automation")


# ── Tools ─────────────────────────────────────────────────────────────


@mcp.tool()
async def list_devices() -> str:
    """List all devices in the network inventory.

    Returns hostname, platform, site, and role for every device.
    No device connection is made — this reads from the YAML inventory.
    """
    devices = router.list_devices()
    return json.dumps(devices, indent=2)


@mcp.tool()
async def get_device_facts(device_id: str) -> str:
    """Get basic facts about a network device.

    Returns hostname, vendor, model, OS version, serial number,
    uptime, and interface list.

    Args:
        device_id: Device identifier from inventory (e.g. 'spine-01')
    """
    async with router.get_driver(device_id) as driver:
        facts = await driver.get_facts()
    return json.dumps(facts, indent=2, default=str)


@mcp.tool()
async def get_device_interfaces(device_id: str) -> str:
    """Get all interfaces and their operational state on a device.

    Returns interface name, up/down status, speed, MTU, MAC address,
    and description for every interface.

    Args:
        device_id: Device identifier from inventory (e.g. 'spine-01')
    """
    async with router.get_driver(device_id) as driver:
        interfaces = await driver.get_interfaces()
    return json.dumps(interfaces, indent=2, default=str)


@mcp.tool()
async def get_bgp_neighbors(device_id: str) -> str:
    """Get the BGP neighbor table for a device.

    Returns each BGP peer with local/remote AS, session state,
    uptime, and prefix counts per address family.

    Args:
        device_id: Device identifier from inventory (e.g. 'spine-01')
    """
    async with router.get_driver(device_id) as driver:
        neighbors = await driver.get_bgp_neighbors()
    return json.dumps(neighbors, indent=2, default=str)


@mcp.tool()
async def get_lldp_neighbors(device_id: str) -> str:
    """Get LLDP neighbor discovery results for a device.

    Returns local port → remote hostname and port mappings.
    Useful for verifying physical cabling and topology.

    Args:
        device_id: Device identifier from inventory (e.g. 'spine-01')
    """
    async with router.get_driver(device_id) as driver:
        neighbors = await driver.get_lldp_neighbors()
    return json.dumps(neighbors, indent=2, default=str)


@mcp.tool()
async def get_route_summary(device_id: str) -> str:
    """Get the IP routing table summary for a device.

    Returns total route count and per-protocol breakdown
    (connected, static, BGP, OSPF, IS-IS).

    Args:
        device_id: Device identifier from inventory (e.g. 'spine-01')
    """
    async with router.get_driver(device_id) as driver:
        summary = await driver.get_route_summary()
    return json.dumps(summary, indent=2, default=str)


# ── Entrypoint ────────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
