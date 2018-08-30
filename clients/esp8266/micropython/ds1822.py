# DS1822temperature sensor driver for MicroPython.
# MIT license; Copyright (c) 2018 Mike Swan

from micropython import const

_CONVERT = const(0x44)
_RD_SCRATCH = const(0xbe)
_WR_SCRATCH = const(0x4e)

class DS1822:
    def __init__(self, onewire):
        self.ow = onewire
        self.buf = bytearray(9)

    def scan(self):
        return [rom for rom in self.ow.scan() if rom[0] == 0x22]

    def convert_temp(self):
        self.ow.reset(True)
        self.ow.writebyte(self.ow.SKIP_ROM)
        self.ow.writebyte(_CONVERT)

    def read_scratch(self, rom):
        self.ow.reset(True)
        self.ow.select_rom(rom)
        self.ow.writebyte(_RD_SCRATCH)
        self.ow.readinto(self.buf)
        if self.ow.crc8(self.buf):
            raise Exception('CRC error')
        return self.buf

    def write_scratch(self, rom, buf):
        self.ow.reset(True)
        self.ow.select_rom(rom)
        self.ow.writebyte(_WR_SCRATCH)
        self.ow.write(buf)

    def read_temp(self, rom):
        buf = self.read_scratch(rom)
        if rom[0] == 0x22:
            t = buf[1] << 8 
            t = t + buf[0]
            t = t >> 4

            return t 
    def return_buffer(self,rom):
        buf = self.read_scratch(rom)
        return buf