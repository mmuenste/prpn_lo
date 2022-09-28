"""Paralleles Sichern der Config"""

from netmiko import ConnectHandler
import concurrent.futures
from getpass import getpass
import time

def save_config(*args, **kwargs):
    
    with ConnectHandler(args, kwargs) net_connect:
        host = kwargs["ip"]
        print(f"{host}...connected")
        config = net_connect.send_command("show run")
        filename = f"{host.replace('.', '_'}_{time.strftime()}"
    
    

def main():
    
    devices = [{'ip': '192.168.181.21',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.22',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.23',
            'device_type': 'cisco_nxos'},
           {'ip': '192.168.181.24',
            'device_type': 'cisco_nxos'}
           ]

    user = input('Username: ')
    passw = getpass()

    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        e1 = executor.submit(pow, 2, 3)
        e2 = executor.submit(pow, 2, 4)
        
    print(e1.result(), e2.result())

if __name__ == '__main__':
    main()
