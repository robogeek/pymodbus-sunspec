
class SunSMarkerBlock(SunSpecHelper):
    def __init__(self, block, address):
        self.baseAddress = address
        self.block = block
        self.writeStringValue(address, 'SunS', 2)
