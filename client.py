import telnetlib
from config import service

tn = telnetlib.Telnet('localhost', service['port'])
for phrase in ['hello']:
    tn.write(phrase)
    print tn.read_some()
tn.close()
