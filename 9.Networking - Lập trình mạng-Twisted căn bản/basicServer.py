from twisted.internet.protocol import Factory
from twisted.internet.protocol import Protocol
from twisted.internet import reactor

class BasicProtocol(Protocol):
    def __init__(self):
        self.name = "Basic Protocol"

    def connectionMade(self):
        print("connection is made")

    def connectionLost(self, reason):
        print("connection is lost")

class BasicFactory(Factory):
    def buildProtocol(self, addr):
        return BasicProtocol()

reactor.listenTCP(8001, BasicFactory())
reactor.run()
