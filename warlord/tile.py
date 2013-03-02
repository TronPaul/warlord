class Tile(object):
    def __init__(self):
        self.type = None
        self.unit = None
        self.location = (0, 0)

    def __contains__(self, item):
        return item is self.unit
