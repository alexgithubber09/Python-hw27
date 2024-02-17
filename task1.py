from tcping import Ping
from contextlib import redirect_stdout

hosts = ['192.168.43.95', '192.168.43.118']
# Ping(host, port, timeout)
def pinsServers(hostIP):
    for i in hosts:
        ping = Ping(i, 22, 60)
        ping.ping(3)

def writeFile(fileName):
    with open(fileName, 'w') as pingServers:
        with redirect_stdout(pingServers):
            pinsServers(hosts)

writeFile('pingResults.txt')

