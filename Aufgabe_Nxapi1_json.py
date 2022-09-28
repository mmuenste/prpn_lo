import requests
import json

"""
Modify these please
"""
switchuser='admin'
switchpassword='cisco'

url='http://192.168.181.21/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show version",
    "output_format": "json"
  }
}
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

print(response["ins_api"]["outputs"]["output"]["body"]["proc_board_id"])


with open("nxapi_cli_show_version.json", "w") as fobj:
    json.dump(response, fobj)

