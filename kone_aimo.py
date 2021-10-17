def ledPacket(
    wheel,
    leftRibbon,
    rightRibbon,
    leftPanel,
    rightPanel,
    brightness 
):
    """
    Takes in colours for the mouse's lighting zones and returns bytes that can be sent as a HID feature report
    Credit to Squ1dd13 for the original LED mappings

    @param  wheel       The mouse wheel light colour. Should be a colour.Colour instance
    @param  leftRibbon  The colours of the left light ribbon. Should be a List of four colour.Colour instances
    @param  rightRibbon Right light ribbon. see leftRibbon
    @param  leftPanel   The left light panel colour. Should be a colour.Colour instance
    @param  rightPanel  Right light panel. see leftPanel
    @param  brightness  An integer between 0 and 255 for the general lighting intensity
    @return             Bytes ready to be sent to the mouse as a HID feature report
    """
    return bytes.fromhex(
          "06 69 00 06"                     # ??
        + "1f 08 10 18"                     # ??
        + "20 40 04 03"                     # ??
        + "00 00 08 ff"                     # ??
        + "07 00 01 01"                     # ??
        + hex(brightness)[2:].rjust(2, "0") # General brightness
        + "1d 13 ff 00"                     # ??
        + "ff 59 ff 00"                     # ??
        + "00 ff fd fd"                     # ??
        + "00 00 ff f4"                     # ??
        + "64 00 00 ff"                     # ??
        + "f4 00 00 00"                     # ??
        + "ff"                              # ??
        + wheel.asSpacedARGB()              # Wheel LED
        + "00"                              # Pad 
        + leftRibbon[0].asSpacedARGB()      # Left Ribbon 1
        + "00"                              # Pad
        + leftRibbon[1].asSpacedARGB()      # Left Ribbon 2
        + "00"                              # Pad
        + leftRibbon[2].asSpacedARGB()      # Left Ribbon 3
        + "00"                              # Pad
        + leftRibbon[3].asSpacedARGB()      # Left Ribbon 4
        + "00"                              # Pad
        + rightRibbon[0].asSpacedARGB()     # Right Ribbon 1
        + "00"                              # Pad
        + rightRibbon[1].asSpacedARGB()     # Right Ribbon 2
        + "00"                              # Pad
        + rightRibbon[2].asSpacedARGB()     # Right Ribbon 3
        + "00"                              # Pad
        + rightRibbon[3].asSpacedARGB()     # Right Ribbon 4
        + "00"                              # Pad
        + leftPanel.asSpacedARGB()          # Left Panel
        + "00"                              # Pad
        + rightPanel.asSpacedARGB()         # Right Panel
    )
