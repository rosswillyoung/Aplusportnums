import random

def portTester():
    portNums = {'LDAP': 389, 'POP3': 110, 'IMAP4': 143, 'SLP': 427, 'FTP': '20/21',
            'SSH': 22, 'SMB': 445, 'DHCP': 67, 'AFP': 548, 'RDP': 3389, 'HTTP': 80,
            'DNS': 53, 'SMTP': 25, 'Telnet': 23, 'HTTPS': 443, 'SNMP': 161}
    for key in portNums.keys():
        if input(key + ': ') == str(portNums[key]):
            print('Correct!')
        else:
            print('Wrong: ' + str(portNums[key]))

portTester()
