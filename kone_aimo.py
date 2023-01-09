import typing

from colour import Colour

def ledPacket(
    wheel       : Colour,
    leftRibbon  : Colour,
    rightRibbon : Colour,
    leftPanel   : Colour,
    rightPanel  : Colour,
    brightness  : int
) -> bytes:
    """
    Takes in colours for the mouse's lighting zones and returns bytes that can be sent as a HID feature report
    Credit to Squ1dd13 on GitHub for the original LED mappings (bytes 2F-64) and the initial report structure this is derived from

    See research directory in project root for more info

    @param  wheel       The mouse wheel light colour. Should be a colour.Colour instance
    @param  leftRibbon  The colours of the left light ribbon. Should be a List of four colour.Colour instances
    @param  rightRibbon Right light ribbon. see leftRibbon
    @param  leftPanel   The left light panel colour. Should be a colour.Colour instance
    @param  rightPanel  Right light panel. see leftPanel
    @param  brightness  An integer between 0 and 255 for the general lighting intensity
    @return             Bytes ready to be sent to the mouse as a HID feature report
    """
    return bytes.fromhex(
          "06"                              # 01-01 Unknown, Must be 0x06 for things to work
        + "00"                              # 02-02 ??
        + "00"                              # 03-03 Unknown, Must be 0x00 or nothing happens
        + "00"                              # 04-04 ??
        + "1f 08 10 18"                     # 05-08 Something to do with sensitivity
        + "20 40 04 03"                     # 09-0C Also affects sensitivity
        + "00 00 00"                        # 0D-0F ??
        + "ff 07"                           # 10-11 Lights toggle bitmask, see lights_bitmask.txt in research directory, 0xff07-0xffff enables all
        + "00 01 00"                        # 12-14 Light pattern, see lights_patterns.txt in research directory, 0x000100 is user defined solid
        + hex(brightness)[2:].rjust(2, "0") # 15-15 General brightness
        + "1d 13 ff 00"                     # 16-19 ┬ Unknown, See 16-2E.txt in research directory
        + "ff 59 ff 00"                     # 1A-1D │
        + "00 ff fd fd"                     # 1E-21 │
        + "00 00 ff f4"                     # 22-25 │
        + "64 00 00 ff"                     # 26-29 │
        + "f4 00 00 00"                     # 2A-2D │
        + "ff"                              # 2E-2E ┘
        + wheel.asSpacedARGB()              # 2F-32 Wheel LED
        + "00"                              # 33-33 Padding
        + leftRibbon[0].asSpacedARGB()      # 34-37 Left Ribbon 1
        + "00"                              # 38-38 Padding
        + leftRibbon[1].asSpacedARGB()      # 39-3C Left Ribbon 2
        + "00"                              # 3D-3D Padding
        + leftRibbon[2].asSpacedARGB()      # 3E-41 Left Ribbon 3
        + "00"                              # 42-42 Padding
        + leftRibbon[3].asSpacedARGB()      # 43-46 Left Ribbon 4
        + "00"                              # 47-47 Padding
        + rightRibbon[0].asSpacedARGB()     # 48-4B Right Ribbon 1
        + "00"                              # 4C-4C Padding
        + rightRibbon[1].asSpacedARGB()     # 4D-50 Right Ribbon 2
        + "00"                              # 51-51 Padding
        + rightRibbon[2].asSpacedARGB()     # 52-55 Right Ribbon 3
        + "00"                              # 56-56 Padding
        + rightRibbon[3].asSpacedARGB()     # 57-5A Right Ribbon 4
        + "00"                              # 5B-5B Padding
        + leftPanel.asSpacedARGB()          # 5C-5F Left Panel
        + "00"                              # 60-60 Padding
        + rightPanel.asSpacedARGB()         # 61-64 Right Panel
        )
