# Arista eAPI JSON Schemas

Captured from 192.168.1.10 — use as reference for driver development.


## show version
```json
{
  "mfgName": "Arista",
  "modelName": "vEOS-lab",
  "hardwareRevision": "",
  "serialNumber": "5F6BC4D03506543E211EA99D4FE27DC7",
  "systemMacAddress": "0c:8b:ec:ea:71:72",
  "hwMacAddress": "00:00:00:00:00:00",
  "configMacAddress": "00:00:00:00:00:00",
  "version": "4.33.2F",
  "architecture": "x86_64",
  "internalVersion": "4.33.2F-40713977.4332F",
  "internalBuildId": "bb0a7f77-9bdd-4ede-92a0-7a42f1a6dda3",
  "imageFormatVersion": "1.0",
  "imageOptimization": "None",
  "bootupTimestamp": 1771798787.2624912,
  "uptime": 11635.67,
  "memTotal": 1979864,
  "memFree": 838632,
  "isIntlVersion": false
}
```


## show hostname
```json
{
  "hostname": "arista-01",
  "fqdn": "arista-01"
}
```


## show interfaces status
```json
{
  "interfaceStatuses": {
    "Ethernet1": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet2": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet3": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet4": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet5": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet6": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet7": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet8": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet9": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet10": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet11": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Ethernet12": {
      "description": "",
      "linkStatus": "notconnect",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": false,
      "autoNegotiateActive": false,
      "interfaceType": "EbraTestPhyPort",
      "vlanInformation": {
        "vlanId": 1,
        "interfaceMode": "bridged",
        "interfaceForwardingModel": "bridged"
      },
      "lineProtocolStatus": "down",
      "interfaceDamped": false
    },
    "Management1": {
      "description": "",
      "linkStatus": "connected",
      "duplex": "duplexFull",
      "bandwidth": 1000000000,
      "autoNegotigateActive": true,
      "autoNegotiateActive": true,
      "interfaceType": "10/100/1000",
      "vlanInformation": {
        "interfaceMode": "routed",
        "interfaceForwardingModel": "routed"
      },
      "lineProtocolStatus": "up",
      "interfaceDamped": false
    }
  }
}
```


## show interfaces
```json
{
  "interfaces": {
    "Management1": {
      "name": "Management1",
      "forwardingModel": "routed",
      "lineProtocolStatus": "up",
      "interfaceStatus": "connected",
      "hardware": "ethernet",
      "interfaceAddress": [
        {
          "primaryIp": {
            "address": "192.168.1.10",
            "maskLen": 24
          },
          "secondaryIps": {},
          "secondaryIpsOrderedList": [],
          "virtualIp": {
            "address": "0.0.0.0",
            "maskLen": 0
          },
          "virtualSecondaryIps": {},
          "virtualSecondaryIpsOrderedList": [],
          "broadcastAddress": "255.255.255.255",
          "dhcp": false
        }
      ],
      "physicalAddress": "0c:8b:ec:5d:00:00",
      "burnedInAddress": "0c:8b:ec:5d:00:00",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 1500,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771807957.222013,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 1471.4836050330337,
        "inPktsRate": 0.9745147608520652,
        "outBitsRate": 1935.097980010915,
        "outPktsRate": 0.8947848215526684
      },
      "interfaceCounters": {
        "inOctets": 678348,
        "inUcastPkts": 3321,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 813,
        "inDiscards": 0,
        "inTotalPkts": 4134,
        "outOctets": 7886286,
        "outUcastPkts": 7029,
        "outMulticastPkts": 374,
        "outBroadcastPkts": 17,
        "outDiscards": 0,
        "outTotalPkts": 7420,
        "linkStatusChanges": 15,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.378356
      },
      "duplex": "duplexFull",
      "autoNegotiate": "success",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet7": {
      "name": "Ethernet7",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:07",
      "burnedInAddress": "0c:8b:ec:5d:00:07",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.221513,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3804324
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet8": {
      "name": "Ethernet8",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:08",
      "burnedInAddress": "0c:8b:ec:5d:00:08",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2215366,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3821757
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet12": {
      "name": "Ethernet12",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:0c",
      "burnedInAddress": "0c:8b:ec:5d:00:0c",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2214112,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3839822
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet2": {
      "name": "Ethernet2",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:02",
      "burnedInAddress": "0c:8b:ec:5d:00:02",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2216406,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.385569
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet9": {
      "name": "Ethernet9",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:09",
      "burnedInAddress": "0c:8b:ec:5d:00:09",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2214878,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3872828
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet4": {
      "name": "Ethernet4",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:04",
      "burnedInAddress": "0c:8b:ec:5d:00:04",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2215695,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3888514
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet1": {
      "name": "Ethernet1",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:01",
      "burnedInAddress": "0c:8b:ec:5d:00:01",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2214386,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3903644
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet3": {
      "name": "Ethernet3",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:03",
      "burnedInAddress": "0c:8b:ec:5d:00:03",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.221617,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3920302
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet5": {
      "name": "Ethernet5",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:05",
      "burnedInAddress": "0c:8b:ec:5d:00:05",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2215936,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3935437
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet11": {
      "name": "Ethernet11",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:0b",
      "burnedInAddress": "0c:8b:ec:5d:00:0b",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2216656,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.395132
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet6": {
      "name": "Ethernet6",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:06",
      "burnedInAddress": "0c:8b:ec:5d:00:06",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.221464,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3965936
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    },
    "Ethernet10": {
      "name": "Ethernet10",
      "forwardingModel": "bridged",
      "lineProtocolStatus": "down",
      "interfaceStatus": "notconnect",
      "hardware": "ethernet",
      "interfaceAddress": [],
      "physicalAddress": "0c:8b:ec:5d:00:0a",
      "burnedInAddress": "0c:8b:ec:5d:00:0a",
      "description": "",
      "bandwidth": 1000000000,
      "mtu": 9214,
      "l3MtuConfigured": false,
      "l2Mru": 0,
      "lastStatusChangeTimestamp": 1771798874.2213497,
      "interfaceStatistics": {
        "updateInterval": 300.0,
        "inBitsRate": 0.0,
        "inPktsRate": 0.0,
        "outBitsRate": 0.0,
        "outPktsRate": 0.0
      },
      "interfaceCounters": {
        "inOctets": 0,
        "inUcastPkts": 0,
        "inMulticastPkts": 0,
        "inBroadcastPkts": 0,
        "inDiscards": 0,
        "inTotalPkts": 0,
        "outOctets": 0,
        "outUcastPkts": 0,
        "outMulticastPkts": 0,
        "outBroadcastPkts": 0,
        "outDiscards": 0,
        "outTotalPkts": 0,
        "linkStatusChanges": 3,
        "totalInErrors": 0,
        "inputErrorsDetail": {
          "runtFrames": 0,
          "giantFrames": 0,
          "fcsErrors": 0,
          "alignmentErrors": 0,
          "symbolErrors": 0,
          "rxPause": 0
        },
        "totalOutErrors": 0,
        "outputErrorsDetail": {
          "collisions": 0,
          "lateCollisions": 0,
          "deferredTransmissions": 0,
          "txPause": 0
        },
        "counterRefreshTime": 1771810423.3980815
      },
      "duplex": "duplexFull",
      "autoNegotiate": "unknown",
      "loopbackMode": "loopbackNone",
      "lanes": 0
    }
  }
}
```


## show ip interface brief
```json
{
  "interfaces": {
    "Management1": {
      "name": "Management1",
      "interfaceStatus": "connected",
      "lineProtocolStatus": "up",
      "mtu": 1500,
      "ipv4Routable240": false,
      "ipv4Routable0": false,
      "interfaceAddress": {
        "ipAddr": {
          "address": "192.168.1.10",
          "maskLen": 24
        }
      },
      "nonRoutableClassEIntf": false
    }
  }
}
```


## show bgp summary
> ERROR: {'code': 1000, 'message': "CLI command 1 of 1 'show bgp summary' failed: could not run command", 'data': [{'errors': ['BGP inactive']}]}


## show bgp evpn summary
> ERROR: {'code': 1000, 'message': "CLI command 1 of 1 'show bgp evpn summary' failed: could not run command", 'data': [{'errors': ['BGP inactive']}]}


## show vxlan vtep
```json
{
  "vteps": {},
  "interfaces": {},
  "vtepTunnelTypes": {}
}
```


## show vxlan vni
```json
{
  "vxlanIntfs": {}
}
```


## show vxlan flood vtep
```json
{
  "floodMap": {}
}
```


## show lldp neighbors
```json
{
  "tablesInserts": 0,
  "tablesDeletes": 0,
  "tablesDrops": 0,
  "tablesAgeOuts": 0,
  "lldpNeighbors": []
}
```


## show ip route summary
```json
{
  "connected": 1,
  "static": 0,
  "vcs": 0,
  "staticNexthopGroup": 0,
  "dynamicPolicy": 0,
  "ospfCounts": {
    "ospfTotal": 0,
    "ospfIntraArea": 0,
    "ospfInterArea": 0,
    "ospfExternal1": 0,
    "ospfExternal2": 0,
    "nssaExternal1": 0,
    "nssaExternal2": 0
  },
  "ospfv3Counts": {
    "ospfv3Total": 0,
    "ospfv3IntraArea": 0,
    "ospfv3InterArea": 0,
    "ospfv3External1": 0,
    "ospfv3External2": 0,
    "ospfv3NssaExternal1": 0,
    "ospfv3NssaExternal2": 0
  },
  "bgpCounts": {
    "bgpTotal": 0,
    "bgpExternal": 0,
    "bgpInternal": 0,
    "bgpLocal": 0
  },
  "isisCounts": {
    "isisTotal": 0,
    "isisLevel1": 0,
    "isisLevel2": 0
  },
  "gribi": 0,
  "rip": 0,
  "internal": 5,
  "attached": 0,
  "aggregate": 0,
  "maskLen": {
    "24": 1,
    "32": 3,
    "8": 2
  },
  "totalRoutes": 6,
  "isis": 0
}
```


## show system environment all
> ERROR: {'code': 1000, 'message': "CLI command 1 of 1 'show system environment all' failed: could not run command", 'data': [{'temperature': {'systemStatus': 'unknownTemperatureAlarmLevel', 'shutdownOnOverheat': False, 'powercycleOnOverheat': False, 'actionOnOverheat': 'actionUnknown', 'recoveryModeOnOverheat': 'recoveryModeNA', 'ambientThreshold': 45, 'tempSensors': [], 'cardSlots': [], 'powerSupplySlots': []}, 'temperatureXcvr': {'tempSensors': [], 'cardSlots': []}, 'cooling': {'systemStatus': 'unknownCoolingAlarmLevel', 'fansStatus': 'unknownFanAlarmLevel', 'airflowDirection': 'unknownAirflowDirection', 'currentZones': 1, 'configuredZones': 0, 'defaultZones': False, 'numCoolingZones': [], 'shutdownOnInsufficientFans': True, 'overrideFanSpeed': 0, 'minFanSpeed': 0, 'coolingMode': 'automatic', 'fanTraySlots': [], 'powerSupplySlots': []}, 'extra': [], 'errors': ['There seem to be no power supplies connected.']}]}


## show logging last 20
> ERROR: {'code': 1002, 'message': "CLI command 1 of 1 'show logging last 20' failed: invalid command", 'data': [{'errors': ["Incomplete command (at token 3: '20')"]}]}
