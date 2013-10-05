import telnetlib
from config import service

tn = telnetlib.Telnet('localhost', service['port'])
for phrase in ['hello']:
    print '>', phrase
    tn.write(phrase)
    print '<', tn.read_some()
tn.close()
