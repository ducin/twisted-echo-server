import telnetlib
from config import service

import logging
logging.basicConfig(format='%(operation)s:%(message)s', filename='client.log', filemode='w', level=logging.INFO)

def run():
    tn = telnetlib.Telnet('localhost', service['port'])
    for phrase in ['hello', 'from', 'twisted', 'client', 'exit']:
        logging.info(phrase, extra={'operation': 'OUT'})
        print '>', phrase
        tn.write(phrase)
        res = tn.read_some()
        logging.info(res, extra={'operation': 'IN'})
        print '<', res
    tn.close()

if __name__ == '__main__':
    run()
