import pattern

from colour import Colour


class FeatureReport(object):
    def __init__(self):
        self.profile = 0x00    # 0x02  Profile index

        self.__lights_bitmask = 0xffff                    # 0x0F-0x10   Light control bitmask, not used for now so defaults to all on
        self.pattern_basic    = pattern.Basic.USER        # 0x11        Basic light pattern
        self.pattern_adv      = pattern.Advanced.SOLID    # 0x12        Advanced light pattern
        self.pattern_speed    = 0x00                      # 0x13        Pattern speed
        self.brightness       = 0xff                      # 0x14        Overall brightness

        # Colours
        self.wheel    = Colour(0, 0, 0)
        self.ribbon_l = [Colour(0, 0, 0)] * 4
        self.ribbon_r = [Colour(0, 0, 0)] * 4
        self.panel_l  = Colour(0, 0, 0)
        self.panel_r  = Colour(0, 0, 0)

    def getBytes(self):
        return bytes.fromhex( 
              "06"                                              # 0x00-0x00 - Unknown, Must be 0x06 or nothing happens, probably a header?
            + "00"                                              # 0x01-0x01 - Unknown, Possibly padding?
            + hex(self.profile)[2:].rjust(2, "0")               # 0x02-0x02 - Profile selection
            + "00"                                              # 0x03-0x03 - Unknown, Possibly padding?
            + "1f"                                              # 0x04-0x04 - Some kind of sensitivity multiplier, maybe a maximum?
            + "00 33 66 99 cc"                                  # 0x05-0x09 - Sensitivity/DPI steps from low to high
            + "00"                                              # 0x0A-0x0A - Something to do with sensitivity too, setting to not 0x00 breaks adjustment in unknown ways
            + "00"                                              # 0x0A-0x0B - ??
            + "00 00 00"                                        # 0x0C-0x0E - ??
            + hex(self.__lights_bitmask)[2:].rjust(4, "0")      # 0x0F-0x10 - Lights toggle bitmask, see 0F-10_lights_bitmask.txt in research directory, 0xff07-0xffff enables all
            + hex(self.pattern_basic.value)[2:].rjust(2, "0")   # 0x11-0x11 ┬ Light pattern, see lights_patterns.txt in research directory, 0x000100 is user defined solid
            + hex(self.pattern_adv.value)[2:].rjust(2, "0")     # 0x12-0x12 │
            + hex(self.pattern_speed)[2:].rjust(2, "0")         # 0x13-0x13 ┘
            + hex(self.brightness)[2:].rjust(2, "0")            # 0x14-0x14 - General brightness
            + "00 00 00 00"                                     # 0x15-0x18 ┬ Unknown, See 15-2D_unknown.txt in research directory
            + "00 00 00 00"                                     # 0x19-0x1C │
            + "00 00 00 00"                                     # 0x1D-0x20 │
            + "00 00 00 00"                                     # 0x21-0x24 │
            + "00 00 00 00"                                     # 0x25-0x28 │
            + "00 00 00 00"                                     # 0x29-0x2C │
            + "00"                                              # 0x2D-0x2D ┘
            + self.wheel.asSpacedARGB()                         # 0x2E-0x31 - Wheel LED
            + "00"                                              # 0x32-0x32 - Padding
            + self.ribbon_l[0].asSpacedARGB()                   # 0x33-0x36 - Left Ribbon 1
            + "00"                                              # 0x37-0x37 - Padding
            + self.ribbon_l[1].asSpacedARGB()                   # 0x38-0x3B - Left Ribbon 2
            + "00"                                              # 0x3C-0x3C - Padding
            + self.ribbon_l[2].asSpacedARGB()                   # 0x3D-0x40 - Left Ribbon 3
            + "00"                                              # 0x41-0x41 - Padding
            + self.ribbon_l[3].asSpacedARGB()                   # 0x42-0x45 - Left Ribbon 4
            + "00"                                              # 0x46-0x46 - Padding
            + self.ribbon_r[0].asSpacedARGB()                   # 0x47-0x4A - Right Ribbon 1
            + "00"                                              # 0x4B-0x4B - Padding
            + self.ribbon_r[1].asSpacedARGB()                   # 0x4C-0x4f - Right Ribbon 2
            + "00"                                              # 0x50-0x50 - Padding
            + self.ribbon_r[2].asSpacedARGB()                   # 0x51-0x54 - Right Ribbon 3
            + "00"                                              # 0x55-0x55 - Padding
            + self.ribbon_r[3].asSpacedARGB()                   # 0x56-0x59 - Right Ribbon 4
            + "00"                                              # 0x5A-0x5A - Padding
            + self.panel_l.asSpacedARGB()                       # 0x5B-0x5E - Left Panel
            + "00"                                              # 0x5F-0x5F - Padding
            + self.panel_r.asSpacedARGB()                       # 0x60-0x63 - Right Panel
        )
