import hidapi as hid
from magic import *
import kone_aimo
from colour import Colour 
import sys
import json

device = hid.open(
    ROCCAT_VENDOR_ID,
    DEVICE_IDS.KONE_AIMO
)

with open(sys.argv[1], "r") as lightFile:
    lights = json.load(lightFile)

    packet = kone_aimo.ledPacket(
        Colour.fromHex(lights["wheel"]),
        [
            Colour.fromHex(lights["left-ribbon"][0]),
            Colour.fromHex(lights["left-ribbon"][1]),
            Colour.fromHex(lights["left-ribbon"][2]),
            Colour.fromHex(lights["left-ribbon"][3]),
        ],
        [
            Colour.fromHex(lights["right-ribbon"][0]),
            Colour.fromHex(lights["right-ribbon"][1]),
            Colour.fromHex(lights["right-ribbon"][2]),
            Colour.fromHex(lights["right-ribbon"][3]),
        ],
        Colour.fromHex(lights["left-panel"]),
        Colour.fromHex(lights["right-panel"]),
        lights["brightness"]
    )

hid.sendFeatureReport(device, packet)
# Get a feature report, usually all zeroes, to prevent mouse from being unresponsive
# No idea what causes that, but this seems to fix it for some reason
hid.getFeatureReport(device)

hid.close(device)
