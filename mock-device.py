#!/usr/bin/env python

from pymodbus.server.async import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSparseDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

# TODO Model objects for each model
# TODO Each Model object provides useful functions
# TODO Mechanism to protect certain registers against being written-to
# TODO Mechanism to assign the base address for a Model based on the previously assigned Model


# set up the data storage

# This provides a data array for the entire device memory
ir = ModbusSequentialDataBlock(40000, [0]*20000)
# MODBUS server objects to serve out the data in the device memory
# For SunSpec purposes, we only need input registers
store = ModbusSlaveContext(di=None, co=None, hr=None, ir=ir)
context = ModbusServerContext(slaves=store, single=True)

sunspecMap = SunSpecModbusMap(ir, 40000)
sunspecMap.placeSunSMarker()

sunspecMap.addModel(SunSpecCommonBlock(manufacturer="Joes Inverters", model="1", options="None", version="22.4", serialNumber="100", deviceAddress=22))

#---------------------------------------------------------------------------#
# initialize the server information
#---------------------------------------------------------------------------#
identity = ModbusDeviceIdentification()
identity.VendorName  = 'pymodbus'
identity.ProductCode = 'PM'
identity.VendorUrl   = 'http://github.com/bashwork/pymodbus/'
identity.ProductName = 'pymodbus Server'
identity.ModelName   = 'pymodbus Server'
identity.MajorMinorRevision = '1.0'

StartTcpServer(context, identity=identity, address=("0.0.0.0", 5020))
