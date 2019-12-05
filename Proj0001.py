

from netmiko import ConnectHandler
from netmiko import redispatch
from getpass import getpass
import time

class main:
    """
    This shows the set of commands to connect to a Terminal Server and perform SSH to a Huawei NE device.
    """

    #THIS METHOD WILL CONNECT TO A TERMINAL SERVER

    SERVER_IP = '10.103.23.133'
    USERNAME = 'tpebackbone'
    username = 'tpe'
    router_ip = '10.112.116.1'

    jumpserver = {
        'device_type': 'terminal_server',
        'ip': SERVER_IP,
        'username': USERNAME,
        'password': getpass(),
        "global_delay_factor": 1
    }

    net_connect = ConnectHandler(**jumpserver)
    print(net_connect.find_prompt())
    time.sleep(3)
    net_connect.write_channel('ssh {}@{}'.format(username, router_ip))
    print(net_connect.find_prompt())
    net_connect.write_channel(getpass())

    redispatch(net_connect, device_type='huawei')
    net_connect.username(username)
    net_connect.ip(router_ip)
    net_connect.password(getpass())
    net_connect.global_delay_factor(1)
    net_connect.find_prompt()

    output = net_connect.send_command("display version")
    print(output)
    net_connect.disconnect()

"""

### 
    user01 = 'tpe'
    ip = '10.112.101.6'
    net_connect.send_command('ssh {}@{}'.format(user01,ip))
    #net_connect.write_channel('ssh {cli_username}@{ip}'.format(cli_username= user01, ip= ip))
    #time.sleep(1)
    #net_connect.write_channel('yes')
    net_connect.read_channel()
    
    
    router = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': user01,
        'password': getpass(),
        'global_delay_factor': 3
    }

    net_connect2 = ConnectHandler(**router)
    print(net_connect2.find_prompt())
    net_connect2.send_command("sh version")
    net_connect2.disconnect()
"""

if __name__ == '__main__':
    main()