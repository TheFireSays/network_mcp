# Network Automation MCP Server — Project Brief

## Goal
Build a production-worthy MCP server that exposes network monitoring and 
configuration tools to Claude. Initially Arista-only, designed from day one 
to support Cisco and Juniper via a driver pattern.

## Architecture
Driver pattern with a common abstract interface. NAPALM handles multi-vendor 
common operations (BGP neighbors, interfaces, LLDP, config diff/deploy). 
Arista driver extends NAPALM base with EOS-specific tools (EVPN, VXLAN, 
CloudVision). Future Cisco/Juniper drivers follow the same pattern.

## Current Lab Environment
- 16 Arista switches across 3 Dublin sites
- 4 superspines, 6 spines, 6 leafs
- EVPN/VXLAN multi-site topology
- NX-OS also present (Oracle lab context)
- Development on Ubuntu/WSL2

## Development Principles
1. Abstract driver interface defined first — tools never reference vendors directly
2. NAPALM as base implementation for common getters and config operations
3. Arista-specific tools (EVPN/VXLAN state) extend the NAPALM base
4. Read-only tools first, config tools later with dry-run/diff/commit pattern
5. YAML inventory as source of truth for device platform routing
6. Async throughout (MCP Python SDK is async-first)
7. Secrets via environment variables, never hardcoded

## Build Sequence
- Phase 1: MCP skeleton + abstract driver + AristaDriver (eAPI) + 5 read-only tools
- Phase 2: EVPN/VXLAN specific tools, CloudVision integration
- Phase 3: Config tools with dry-run safety pattern
- Phase 4: CiscoDriver and JuniperDriver extending NapalmDriver base

## Key Libraries
- mcp (Anthropic Python SDK)
- pyeapi (Arista eAPI)
- napalm (multi-vendor base)
- asyncio (async patterns throughout)
- pyyaml (inventory)

## Non-Negotiables
- Two-tool config pattern: generate_diff() must be called before commit_config()
- Claude must never commit config without explicit user confirmation
- All drivers must implement the full abstract base or raise NotImplementedError
```

---
