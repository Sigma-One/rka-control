class Colour:
    def __init__(self, r, g, b, a=255):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a

    def asSpacedARGB(self):
        argb = " " \
            + hex(self.alpha)[2:].rjust(2, "0") + " " \
            + hex(self.red  )[2:].rjust(2, "0") + " " \
            + hex(self.green)[2:].rjust(2, "0") + " " \
            + hex(self.blue )[2:].rjust(2, "0") 
        return argb

    def fromHex(hexCode):
        rgba = hexToRGBA(hexCode)
        return Colour(rgba[0], rgba[1], rgba[2], rgba[3])


def hexToRGBA(hexCode):
    """
    Converts hexadecimal string to a List containing individual colour values (0-255).

    @param  hexCode the hexadecimal string to decode
    @return         a List of ints for red, green, blue, and alpha
    """

    hexCode = hexCode.strip("#")
    if (len(hexCode) not in [6, 8]):
        raise ValueError("Colour code must be 6 or 8 characters without #")

    # Get separate colours from hex
    red   = int(hexCode[0:2], 16)
    green = int(hexCode[2:4], 16)
    blue  = int(hexCode[4:6], 16)

    # Default alpha to 255, only parse if 8 digits
    alpha = 255
    if (len(hexCode) == 8):
        alpha = int(hexCode[6:8], 16)

    return [red, green, blue, alpha]
