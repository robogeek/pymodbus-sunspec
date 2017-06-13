# pymodbus-sunspec
Helper classes, in Python, written for _pymodbus_, to manage a list of SunSpec models within a `ModbusSequentialDataBlock`.  

One instantiates a `ModbusServerContext` and `ModbusSlaveContext` containing a `ModbusSequentialDataBlock` to hold the device memory.  With these classes, a SunSpec-conformant MODBUS map is maintained.

See `mock-device.py` for an example.
