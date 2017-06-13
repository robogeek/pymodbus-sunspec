
class SunSpecModbusMap(object):
    ''' Manages a list of SunSpec models within a ModbusSequentialDataBlock
    '''
    def __init__(self, dataBlock, baseAddress):
        self.baseAddress = baseAddress
        self.dataBlock = dataBlock
        self.models = []

    def placeSunSMarker(self):
        ''' Inserts the 'SunS' marker into the data buffer
        '''
        self.writeStringValue(self.dataBlock, self.baseAddress, 'SunS', 2)

    def hasSunSMarkerAtAddress(self):
        ''' Tests the data buffer to ensure the 'SunS' marker is there
        '''
        if (self.readString(self.baseAddress, 2) != 'SunS'):
            raise Exception, "No 'SunS' marker at ", self.baseAddress

    def addModel(self, model):
        ''' Add a model to the memory in dataBlock.
        '''
        # First, check the dataBlock to ensure the models match what we expect
        self.hasSunSMarkerAtAddress()
        modelAddress = self.baseAddress + 2
        for _model in self.models:
            # Read the model ID and length, to check against
            model_id_in_data = self.readWord(modelAddress)
            if (model_id_in_data == 0xffff):
                break
            model_length_in_data =  self.readWord(modelAddress+1)
            if (model_id_in_data != _model.id()):
                raise Exception, "Model number in data does not match model ", _model.id()
            modelAddress += model_length_in_data
        # We exit the loop with the modelAddress to use for this model
        # Instruct the model to insert itself into dataBlock
        model.insertModel(self, modelAddress)
        # And add this model to the list
        self.models.append(model)

    def writeString(self, address, s, length):
        ''' Write a string into the dataBlock using the SunSpec string encoding
        '''
        # First convert the string to a byte array
        # Also ensure to use only the bytes specified
        _bytes = [c for c in bytearray(s)[0:length]]
        towrite = []
        # Then pack the bytes into the towrite array
        i = 0
        while i < length:
            word = 0
            if (i < len(_bytes)):
                word = (_bytes[i] << 8)
            if ((i+1) < len(_bytes)):
                word += _bytes[i+1]
            towrite.append(word)
            i += 2
        # print " writeStringValue ", address, towrite
        self.dataBlock.setValues(address, towrite)

    def readString(self, address, length):
        ''' Read a string from the dataBlock, decoding it using the SunSpec string encoding
        '''
        return decodeStringValue(self.dataBlock.getValues(address, length))

    def decodeStringValue(self, registers):
        out = []
        for w in regs:
            out.append(w>>8)    # Decode characters stuffed into words
            out.append(w & 0xff)
        while (out[-1] == 0):
            out.pop()           # Eliminate trailing NULL's
        return array.array('B', out).tostring()

    def writeWord(self, address, value):
        self.dataBlock.setValues(address, [ value ])

    def readWord(self, address):
        return self.dataBlock.getValues(address, 1)[0]
