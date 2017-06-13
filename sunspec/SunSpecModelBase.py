
class SunSpecModelBase(object):
    ''' Useful functions for mapping a sequence of SunSpec Model's onto
        a ModbusSequentialDataBlock
    '''
    def id(self):
        raise Exception("Implement this")

    def insertModel(self, baseAddress):
        raise Exception("Implement this")
