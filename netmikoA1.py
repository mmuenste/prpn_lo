from netmiko import ConnectHandler

with ConnectHandler(ip="192.168.181.24",
                    username="admin",
                    password="cisco",
                    device_type="cisco_nxos"
                    ) as net_connect:

    show_inventory = net_connect.send_command("show vlan")
    print(show_inventory)