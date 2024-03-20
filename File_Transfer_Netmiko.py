#!usr/bin/env python

"""
Author: Chris Oyuga
Purpose: Demostrate SCP file transfer using Netmiko.
"""

import sys
from yaml import safe_load
from netmiko import Netmiko, file_transfer

def main():
    """
    Execution starts here
    """

    #Read hosts file into structured data, mau raise YAMLError
    with open("hosts.yml", "r") as handle:
        host_root = safe_load(handle)

    platform_map = {"ios": "cisco_ios", "iosxr": "cisco_xr"}

    #Iterate over the list of hosts(list of dictionaries)
    for host in host_root["host_list"]:

        #Use the map to get proper Netmiko platform
        platform = platform_map[host["platform"]]

        #Initialize the SSH connection
        print(f"Connecting to {host['name']}")
        conn = Netmiko(
            host = host["name"],
            username = "landa",
            password = "landa",
            device_type = platform,
        )

        #Upload the file specified. The dict.get(key) fucntion tries
        #to retrieve the value at the specified key and returns None
        #if it does not exist. 
        print(f" Uploading {argv[1]}")
        result = file_transfer(
            conn,
            source_file=argv[1],
            dest_file=argv[1],
            file_system=host.get("file_system"),
        )
        #print resulting details
        print(f" Details: {result}\n")
        conn.disconnect()
    
if __name__ == "__main__":
    main(sys.argv)
    