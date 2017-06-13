
class SunSpecBasicAggregator(SunSpecModelBase):
    def __init__(self, aggregatedModelID, numModels):
        self.aggregatedModelID = aggregatedModelID
        self.numModels = numModels

    def insertModel(self, sunspecMap, modelAddress):
        self.modelAddress = modelAddress
        self.sunspecMap = sunspecMap
        sunspecMap.writeWord(modelAddress, self.id())
        sunspecMap.writeWord(modelAddress+1, 14)
        self.sunspecMap.writeWord(modelAddress+2, self.aggregatedModelID)
        self.sunspecMap.writeWord(modelAddress+3, self.numModels)

    # TBD require methods to cover the other fields
