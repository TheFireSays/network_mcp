"""MCP server exposing network monitoring tools to Claude.

All tools use the DeviceRouter to obtain a driver — they never reference
vendor-specific classes. Each tool connects, runs the operation, and
disconnects via the async context manager pattern.
"""

import json
import logging
import sys

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()

from network_mcp.inventory import Inventory
from network_mcp.router import DeviceRouter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# ── Constants ────────────────────────────────────────────────────────

CHARACTER_LIMIT = 25_000

# ── Bootstrap ────────────────────────────────────────────────────────

inventory = Inventory()
router = DeviceRouter(inventory)

mcp = FastMCP("network_mcp")


# ── Helpers ──────────────────────────────────────────────────────────


def _truncate(result: str) -> str:
    """Truncate response if it exceeds CHARACTER_LIMIT."""
    if len(result) <= CHARACTER_LIMIT:
        return result
    truncated = result[:CHARACTER_LIMIT]
    return (
        truncated
        + "\n\n--- TRUNCATED ---\n"
        + f"Response truncated from {len(result)} to {CHARACTER_LIMIT} characters. "
        + "Use more specific filters or query individual devices to reduce output."
    )


def _format_result(
    data: dict | list,
    response_format: str = "json",
    title: str = "",
) -> str:
    """Format tool output as JSON or Markdown."""
    raw = json.dumps(data, indent=2, default=str)
    if response_format == "markdown":
        return _to_markdown(data, title)
    return _truncate(raw)


def _to_markdown(data: dict | list, title: str = "") -> str:
    """Convert structured data to a human-readable Markdown string."""
    lines: list[str] = []
    if title:
        lines.append(f"## {title}")
        lines.append("")

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                summary = " | ".join(f"**{k}**: {v}" for k, v in item.items())
                lines.append(f"- {summary}")
            else:
                lines.append(f"- {item}")
    elif isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                lines.append(f"### {key}")
                for k, v in value.items():
                    lines.append(f"- **{k}**: {v}")
                lines.append("")
            elif isinstance(value, list):
                lines.append(f"### {key}")
                for item in value:
                    if isinstance(item, dict):
                        summary = " | ".join(
                            f"**{k}**: {v}" for k, v in item.items()
                        )
                        lines.append(f"- {summary}")
                    else:
                        lines.append(f"- {item}")
                lines.append("")
            else:
                lines.append(f"- **{key}**: {value}")

    result = "\n".join(lines)
    return _truncate(result)


# ── Tools ────────────────────────────────────────────────────────────


@mcp.tool(
    annotations={
        "title": "List Network Devices",
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": False,
    }
)
async def network_list_devices(response_format: str = "json") -> str:
    """List all devices in the network inventory.

    Returns hostname, platform, site, and role for every device.
    No device connection is made — this reads from the YAML inventory.

    Args:
        response_format: Output format — 'json' for structured data,
            'markdown' for human-readable text. Defaults to 'json'.
    """
    try:
        devices = router.list_devices()
        return _format_result(devices, response_format, "Network Inventory")
    except Exception as exc:
        logger.exception("network_list_devices failed")
        return json.dumps({"error": str(exc)})


@mcp.tool(
    annotations={
        "title": "Get Device Facts",
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
    }
)
async def network_get_device_facts(
    device_id: str, response_format: str = "json"
) -> str:
    """Get basic facts about a network device.

    Returns hostname, vendor, model, OS version, serial number,
    uptime, and interface list.

    Args:
        device_id: Device identifier from inventory (e.g. 's1', 'l1').
        response_format: Output format — 'json' or 'markdown'.
    """
    try:
        async with router.get_driver(device_id) as driver:
            facts = await driver.get_facts()
        return _format_result(facts, response_format, f"Facts: {device_id}")
    except Exception as exc:
        logger.exception("network_get_device_facts failed for %s", device_id)
        return json.dumps({"error": str(exc), "device_id": device_id})


@mcp.tool(
    annotations={
        "title": "Get Device Interfaces",
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
    }
)
async def network_get_device_interfaces(
    device_id: str, response_format: str = "json"
) -> str:
    """Get all interfaces and their operational state on a device.

    Returns interface name, up/down status, speed, MTU, MAC address,
    and description for every interface.

    Args:
        device_id: Device identifier from inventory (e.g. 's1', 'l1').
        response_format: Output format — 'json' or 'markdown'.
    """
    try:
        async with router.get_driver(device_id) as driver:
            interfaces = await driver.get_interfaces()
        return _format_result(
            interfaces, response_format, f"Interfaces: {device_id}"
        )
    except Exception as exc:
        logger.exception(
            "network_get_device_interfaces failed for %s", device_id
        )
        return json.dumps({"error": str(exc), "device_id": device_id})


@mcp.tool(
    annotations={
        "title": "Get BGP Neighbors",
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
    }
)
async def network_get_bgp_neighbors(
    device_id: str, response_format: str = "json"
) -> str:
    """Get the BGP neighbor table for a device.

    Returns each BGP peer with local/remote AS, session state,
    uptime, and prefix counts per address family.

    Args:
        device_id: Device identifier from inventory (e.g. 's1', 'l1').
        response_format: Output format — 'json' or 'markdown'.
    """
    try:
        async with router.get_driver(device_id) as driver:
            neighbors = await driver.get_bgp_neighbors()
        return _format_result(
            neighbors, response_format, f"BGP Neighbors: {device_id}"
        )
    except Exception as exc:
        logger.exception(
            "network_get_bgp_neighbors failed for %s", device_id
        )
        return json.dumps({"error": str(exc), "device_id": device_id})


@mcp.tool(
    annotations={
        "title": "Get LLDP Neighbors",
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
    }
)
async def network_get_lldp_neighbors(
    device_id: str, response_format: str = "json"
) -> str:
    """Get LLDP neighbor discovery results for a device.

    Returns local port to remote hostname and port mappings.
    Useful for verifying physical cabling and topology.

    Args:
        device_id: Device identifier from inventory (e.g. 's1', 'l1').
        response_format: Output format — 'json' or 'markdown'.
    """
    try:
        async with router.get_driver(device_id) as driver:
            neighbors = await driver.get_lldp_neighbors()
        return _format_result(
            neighbors, response_format, f"LLDP Neighbors: {device_id}"
        )
    except Exception as exc:
        logger.exception(
            "network_get_lldp_neighbors failed for %s", device_id
        )
        return json.dumps({"error": str(exc), "device_id": device_id})


@mcp.tool(
    annotations={
        "title": "Get Route Summary",
        "readOnlyHint": True,
        "destructiveHint": False,
        "openWorldHint": True,
    }
)
async def network_get_route_summary(
    device_id: str, response_format: str = "json"
) -> str:
    """Get the IP routing table summary for a device.

    Returns total route count and per-protocol breakdown
    (connected, static, BGP, OSPF, IS-IS).

    Args:
        device_id: Device identifier from inventory (e.g. 's1', 'l1').
        response_format: Output format — 'json' or 'markdown'.
    """
    try:
        async with router.get_driver(device_id) as driver:
            summary = await driver.get_route_summary()
        return _format_result(
            summary, response_format, f"Route Summary: {device_id}"
        )
    except Exception as exc:
        logger.exception(
            "network_get_route_summary failed for %s", device_id
        )
        return json.dumps({"error": str(exc), "device_id": device_id})


# ── Entrypoint ───────────────────────────────────────────────────────

if __name__ == "__main__":
    mcp.run()
