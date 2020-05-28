"""
NETMIKO script para SSH aos equipamentos

"""

from netmiko import ConnectHandler
import netmiko


Router_1 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32771',
    'username': 'cisco',
    'password': 'cisco',
}

Router_2 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32783',
    'username': 'cisco',
    'password': 'cisco',
}
Router_3 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32781',
    'username': 'cisco',
    'password': 'cisco',
}
Router_4 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32772',
    'username': 'cisco',
    'password': 'cisco',
}
Router_5 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32773',
    'username': 'cisco',
    'password': 'cisco',
}
Router_7 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32775',
    'username': 'cisco',
    'password': 'cisco',
}
Router_8 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32776',
    'username': 'cisco',
    'password': 'cisco',
}
Router_9 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32777',
    'username': 'cisco',
    'password': 'cisco',
}
Router_10 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.146.128',
    'port': '32778',
    'username': 'cisco',
    'password': 'cisco',
}


all_devices = [Router_1, Router_2, Router_3, Router_4, Router_5, Router_7, Router_8, Router_9, Router_10]

for a_devices in all_devices:
    net_connect = ConnectHandler(**a_devices)
    net_connect.enable("enable")
    output = net_connect.send_command("show ip int brief")
    print("Telneting...")
    print(net_connect.find_prompt())
    print(net_connect.find_prompt())
    print(net_connect.find_prompt())
    print(output)
    print("--------- End ---------")
    # mandar configurações para o router  EXEMPLO:
    config_commands = ['int loop 0', 'ip address 10.10.10.10 255.255.255.255']
    output = net_connect.send_config_set(config_commands)
    print(output)
    # CRIAR um LOOP de Config para este caso configura as interfacer eth0/0 ate á 0/3 individualmente
    for n in range(0, 4):
        print('Creating something int interfaces ethernet0/' + str(n))
        config_commands = ['interface eth0/' + str(n), 'desc testes' + str(n), 'no shut']
        output = net_connect.send_config_set(config_commands)
    print(output)
    file = open(a_devices + '_output.txt', 'w')
    output = net_connect.send_command('show run')
    print('-------------- Output from ' + a_devices + '------------------')
    print(output)
    print()
    print()
    file.write(output)
    file.close()



    
