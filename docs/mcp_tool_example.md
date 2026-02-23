# MCP Tool Definition Reference

Minimal examples of correct MCP tool definitions using the Python SDK.
All tools in this project follow these patterns.

## Basic read-only tool
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("network-automation")

@mcp.tool()
async def get_device_facts(device_id: str) -> str:
    """
    Get basic facts about a network device including hostname, model,
    OS version, serial number, and uptime.
    
    Args:
        device_id: Device identifier matching inventory (e.g. 'spine-01')
    """
    driver = get_driver(device_id)
    result = await driver.get_facts()
    return json.dumps(result, indent=2)
```

## Tool with multiple parameters
```python
@mcp.tool()
async def get_bgp_neighbor_detail(device_id: str, neighbor_ip: str) -> str:
    """
    Get detailed BGP state for a specific neighbor on a device.

    Args:
        device_id: Device identifier matching inventory
        neighbor_ip: IP address of the BGP neighbor
    """
    driver = get_driver(device_id)
    result = await driver.get_bgp_neighbors()
    # Extract specific neighbor
    ...
    return json.dumps(result, indent=2)
```

## Two-tool config pattern (always use this for any write operation)
```python
@mcp.tool()
async def preview_config_change(device_id: str, config: str) -> str:
    """
    Preview a configuration change as a diff WITHOUT applying it.
    Always call this before commit_config_change. Show the diff to the
    user and require explicit confirmation before proceeding.

    Args:
        device_id: Device identifier matching inventory
        config: Configuration snippet to merge
    """
    driver = get_driver(device_id)
    diff = await driver.generate_config_diff(config)
    return json.dumps({"diff": diff, "device": device_id})


@mcp.tool()
async def commit_config_change(device_id: str, config: str) -> str:
    """
    Apply a configuration change. Only call this after preview_config_change
    has been shown to the user and they have explicitly confirmed.

    Args:
        device_id: Device identifier matching inventory
        config: Configuration snippet to merge (must match what was previewed)
    """
    driver = get_driver(device_id)
    result = await driver.commit_config(config)
    return json.dumps(result)
```

## Server entrypoint
```python
if __name__ == "__main__":
    mcp.run()
```
