"""
SCRIPT EVE-NG INE
"""

##imports python modules needed to work
from netmiko import Netmiko
import threading, time
import getpass
import sys
import telnetlib
from netmiko import ConnectHandler
from datetime import datetime




Router_1= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32771',
}

Router_2= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32783',
}
Router_3= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32781',
}
Router_4= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32772',
}
Router_5= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32773',
}
Router_6= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32774',
}
Router_7= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32775',
}
Router_8= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32776',
}
Router_9= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32777',
}
Router_10= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32778',
}
SWITCH= {
    'device_type':'cisco_ios_telnet',
    'ip':'192.168.146.128',
    'port':'32789',
}



all_devices = [Router_1, Router_2, Router_3, Router_4, Router_5, Router_6, Router_7, Router_8, Router_9, Router_10,
                SWITCH]


for a_devices in all_devices:
        net_connect = ConnectHandler(**a_devices)
        output = net_connect.send_command("cisco")
        output1 = net_connect.send_command("cisco")
        net_connect.enable("enable")
        print("Telneting...")
        print(net_connect.find_prompt())
        print(net_connect.find_prompt())
        print(net_connect.find_prompt())
        print(output)
        print(output1)
        print("--------- End ---------")
        tn.write(b"show ip int biref \n")
        for n in rage(2, 10):
            tn.write(b"vlan " + str(n).encode('ascii') + b'\n')
            tn.write(b"name Python_VLAN_" + str(n).encode('ascii') + b"\n")
        tn.write(b"end\n")
        tn.write(b"exit\n")
        print(tn.read_all().decode('ascii'))
