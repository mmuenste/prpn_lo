import requests
from lxml import etree as et

"""
Modify these please
"""
switchuser='admin'
switchpassword='cisco'

url='http://192.168.181.21/ins'
myheaders={'content-type':'application/xml'}
payload="""<?xml version="1.0"?>
<ins_api>
  <version>1.0</version>
  <type>cli_show</type>
  <chunk>0</chunk>
  <sid>sid</sid>
  <input>show interface brief</input>
  <output_format>xml</output_format>
</ins_api>"""
response = requests.post(url,payload, headers=myheaders,auth=(switchuser,switchpassword))

tree = et.fromstring(response.text)

for i in tree.iter("ROW_interface"):
    interface = i.find("interface")
    pmode = i.find("portmode")
    vlan = i.find("vlan")
    if pmode is not None and pmode.text == "access":
        print(f"Access-Interface {interface.text} \t\tVLan: {vlan.text}")
    if pmode is not None and pmode.text == "trunk":
        print(f"Trunk-Interface {interface.text}\t\tVlan: {vlan.text}")
