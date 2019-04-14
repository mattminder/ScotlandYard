class Actor():
    def __init__(self, position, taxi, bus, metro, black, double):
        self.position = position
        self.taxi = taxi
        self.bus = bus
        self.metro = metro
        self.black = black
        self.double = double


class Detective(Actor):
    def __init__(self, position, taxi=10, bus=8, metro=4, black=0, double=0):
        super().__init__(position, taxi, bus, metro, black, double)

class MisterX(Actor):
    def __init__(self, position, taxi=4, bus=3, metro=3, black=4, double=2):
        super().__init__(position, taxi, bus, metro, black, double)