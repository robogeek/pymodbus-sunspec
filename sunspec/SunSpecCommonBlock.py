
class SunSpecCommonBlock(SunSpecModelBase):
    def __init__(self, manufacturer, model, options, version, serialNumber, deviceAddress):
        self.manufacturer = manufacturer
        self.model = model
        self.options = options
        self.version = version
        self.serialNumber = serialNumber
        self.deviceAddress = deviceAddress

    def insertModel(self, sunspecMap, modelAddress):
        self.modelAddress = modelAddress
        self.sunspecMap = sunspecMap
        sunspecMap.writeWord(modelAddress, self.id())
        sunspecMap.writeWord(modelAddress+1, 66)
        self.sunspecMap.writeString(modelAddress+2, self.manufacturer, 16)
        self.sunspecMap.writeString(modelAddress+18, self.model, 16)
        self.sunspecMap.writeString(modelAddress+34, self.options, 8)
        self.sunspecMap.writeString(modelAddress+42, self.version, 8)
        self.sunspecMap.writeString(modelAddress+50, self.serialNumber, 16)
        self.sunspecMap.writeWord(modelAddress+66, self.deviceAddress)

    def id(self):
        return 1
