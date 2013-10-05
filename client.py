import telnetlib

tn = telnetlib.Telnet('localhost', 1236)
for phrase in ['hello']:
    tn.write(phrase)
    print tn.read_some()
tn.close()
