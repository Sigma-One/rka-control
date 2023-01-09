from enum import Enum

class Basic(Enum):
    USER    = 0x00
    RAINBOW = 0x01
    BLUE    = 0x02

class Advanced(Enum):
    OFF     = 0x00
    SOLID   = 0x01
    BLINK   = 0x02
    BREATH  = 0x03
    ORANGE  = 0x06

    __UNKNOWN_1 = 0x04
    __UNKNOWN_2 = 0x05
