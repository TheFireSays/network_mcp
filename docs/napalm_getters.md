# NAPALM Getter Reference

Key getter methods available on all NAPALM drivers. Return schemas are
normalized across vendors — your driver interface should mirror these.

## get_interfaces()
```python
{
    "Management1": {
        "is_up": True,
        "is_enabled": True,
        "description": "OOB",
        "speed": 1000,
        "mtu": 1500,
        "mac_address": "AA:BB:CC:DD:EE:FF",
        "last_flapped": 1234567890.0
    }
}
```

## get_bgp_neighbors()
```python
{
    "global": {
        "router_id": "10.0.0.1",
        "peers": {
            "10.0.0.2": {
                "local_as": 65001,
                "remote_as": 65002,
                "is_up": True,
                "is_enabled": True,
                "uptime": 12345,
                "address_family": {
                    "ipv4": {"sent_prefixes": 10, "received_prefixes": 20}
                }
            }
        }
    }
}
```

## get_lldp_neighbors()
```python
{
    "Ethernet1": [
        {"hostname": "spine-01", "port": "Ethernet3"}
    ]
}
```

## get_facts()
```python
{
    "vendor": "Arista",
    "model": "DCS-7050CX3-32S",
    "os_version": "4.28.0F",
    "hostname": "leaf-01",
    "serial_number": "ABC123",
    "uptime": 123456.0,
    "interface_list": ["Ethernet1", "Ethernet2", "Management1"]
}
```

## get_config(retrieve="all")
```python
{
    "running": "hostname leaf-01\n...",
    "startup": "hostname leaf-01\n...",
    "candidate": ""
}
```

## Config deployment pattern
```python
device.open()
device.load_merge_candidate(config=config_string)  # or load_replace_candidate
diff = device.compare_config()   # always call before commit
device.commit_config()           # or device.discard_config()
device.close()
```
