import pattern

from colour import Colour


class FeatureReport(object):
    def __init__(self):
        self.__lights_bitmask = 0xffff                    # Bytes 10-11, light control bitmask, not used for now so defaults to all on
        self.pattern_basic    = pattern.Basic.USER        # Byte 12, basic light pattern
        self.pattern_adv      = pattern.Advanced.SOLID    # Byte 13, advanced light pattern
        self.pattern_speed    = 0x00                      # Byte 14, pattern speed
        self.brightness       = 0xff                      # Byte 15, overall brightness

        # Colours
        self.wheel    = Colour(0, 0, 0)
        self.ribbon_l = [Colour(0, 0, 0)] * 4
        self.ribbon_r = [Colour(0, 0, 0)] * 4
        self.panel_l  = Colour(0, 0, 0)
        self.panel_r  = Colour(0, 0, 0)

    def getBytes(self):
        return bytes.fromhex( 
              "06"                                              # 01-01 - Unknown, Must be 0x06 for things to work
            + "00"                                              # 02-02 - ??
            + "00"                                              # 03-03 - Unknown, Must be 0x00 or nothing happens
            + "00"                                              # 04-04 - ??
            + "1f 08 10 18 20 40 04 03"                         # 05-0C - Something to do with sensitivity
            + "00 00 00"                                        # 0D-0F - ??
            + hex(self.__lights_bitmask)[2:].rjust(4, "0")      # 10-11 - Lights toggle bitmask, see lights_bitmask.txt in research directory, 0xff07-0xffff enables all
            + hex(self.pattern_basic.value)[2:].rjust(2, "0")   # 12-12 ┬ Light pattern, see lights_patterns.txt in research directory, 0x000100 is user defined solid
            + hex(self.pattern_adv.value)[2:].rjust(2, "0")     # 13-13 │
            + hex(self.pattern_speed)[2:].rjust(2, "0")         # 14-14 ┘
            + hex(self.brightness)[2:].rjust(2, "0")            # 15-15 - General brightness
            + "1d 13 ff 00"                                     # 16-19 ┬ Unknown, See 16-2E.txt in research directory
            + "ff 59 ff 00"                                     # 1A-1D │
            + "00 ff fd fd"                                     # 1E-21 │
            + "00 00 ff f4"                                     # 22-25 │
            + "64 00 00 ff"                                     # 26-29 │
            + "f4 00 00 00"                                     # 2A-2D │
            + "ff"                                              # 2E-2E ┘
            + self.wheel.asSpacedARGB()                         # 2F-32 - Wheel LED
            + "00"                                              # 33-33 - Padding
            + self.ribbon_l[0].asSpacedARGB()                   # 34-37 - Left Ribbon 1
            + "00"                                              # 38-38 - Padding
            + self.ribbon_l[1].asSpacedARGB()                   # 39-3C - Left Ribbon 2
            + "00"                                              # 3D-3D - Padding
            + self.ribbon_l[2].asSpacedARGB()                   # 3E-41 - Left Ribbon 3
            + "00"                                              # 42-42 - Padding
            + self.ribbon_l[3].asSpacedARGB()                   # 43-46 - Left Ribbon 4
            + "00"                                              # 47-47 - Padding
            + self.ribbon_r[0].asSpacedARGB()                   # 48-4B - Right Ribbon 1
            + "00"                                              # 4C-4C - Padding
            + self.ribbon_r[1].asSpacedARGB()                   # 4D-50 - Right Ribbon 2
            + "00"                                              # 51-51 - Padding
            + self.ribbon_r[2].asSpacedARGB()                   # 52-55 - Right Ribbon 3
            + "00"                                              # 56-56 - Padding
            + self.ribbon_r[3].asSpacedARGB()                   # 57-5A - Right Ribbon 4
            + "00"                                              # 5B-5B - Padding
            + self.panel_l.asSpacedARGB()                       # 5C-5F - Left Panel
            + "00"                                              # 60-60 - Padding
            + self.panel_r.asSpacedARGB()                       # 61-64 - Right Panel
        )
