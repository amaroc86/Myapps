"""
Acesso TElnet

"""


import getpass
import netmiko
import telnetlib



user = input('Username: ')
password = getpass.getpass()

f = open('IPS')
for IP in f:
    IP = IP.strip()
    print('Configuring ' + (IP))
    HOST = IP
    tn = telnetlib.TELNET(HOST)
    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    if password:
        tn.read_until(b'Password: ')
        tn.write(password.encode('ascii') + b'\n')
    tn.write(b'terminal length 0\n')
    tn.write(b'show run\n')
    tn.write(b'exit\n')

    readoutput = tn.read_all()
    saveoutput = open('router' + HOST, 'w')
    saveoutput.write(readoutput.decode('ascii'))
    saveoutput.write('\n')
    saveoutput.close
    print(tn.read_all().decode('ascii'))
