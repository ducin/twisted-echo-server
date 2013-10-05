from twisted.internet import protocol, reactor
from config import service

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        if data == 'exit':
            self.transport.loseConnection()

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

def run():
    reactor.listenTCP(service['port'], EchoFactory())
    reactor.run()

if __name__ == '__main__':
    run()
