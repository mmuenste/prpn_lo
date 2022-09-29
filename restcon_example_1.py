import requests
from pprint import pprint

well_known_url = "https://192.168.181.11/.well-known/host-meta"
restconf_url = "https://192.168.181.11/restconf"
cap_url = "https://192.168.181.11/restconf/data/ietf-restconf-monitoring:restconf-state"
yang_url = "https://192.168.181.11/restconf/data/ietf-yang-library:modules-state"

# Bei Restconf API-Path

oc_url = ("https://192.168.181.11/restconf/data/openconfig-interfaces:interfaces" +
         f"/interface=GigabitEthernet2/state")

cpu_url = ("https://192.168.181.11/restconf/data/Cisco-IOS-XE-process-cpu-oper:" +
          "cpu-usage/cpu-utilization/five-seconds")

cred = ("cisco", "cisco")

# headers = {"Accept": "application/yang-data+xml"}
headers = {"Accept": "application/yang-data+json"}

response = requests.get(yang_url, headers=headers, auth=cred, verify=False)

print(response.status_code)
pprint(response.json())
