#!/usr/bin/env python3

from ncclient import manager
from ncclient.operations.rpc import RPCError


def main():
    with manager.connect(host='192.168.181.21',
                         port=830,
                         username="admin",
                         password="cisco",
                         hostkey_verify=False,
                         device_params={'name': 'nexus'},
                         allow_agent=False,
                         look_for_keys=False
                         ) as cisco_manager:

        oc_int = '''
        <interfaces xmlns="http://openconfig.net/yang/interfaces">
            <interface>
                <name></name>
                <state>
                    <ifindex/>
                </state>
                
            </interface>
        </interfaces>
        '''

        try:
            oc_resp = cisco_manager.get(filter=('subtree',
                                                oc_int))
            print(oc_resp)
            print('*' * 30)
        except RPCError as err:
            for attr in dir(err):
                print(attr, ':   ', getattr(err, attr))


if __name__ == '__main__':
    main()

