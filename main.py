import hid # HID functions

from devices        import DEVICES       # Device vendor and product IDs
from colour         import Colour        # Colour object
from feature_report import FeatureReport # Feature report object

import sys                # Args reading
import json               # JSON parsing


with open(sys.argv[1], "r") as lightFile:
    lights = json.load(lightFile)

    report = FeatureReport()

    # Set colours
    # If statement disaster is to allow for omitted values, I miss kotlinx.serialization already
    report.wheel    = Colour.fromHex(lights["wheel"])                                if "wheel"        in lights else report.wheel
    report.ribbon_l = list(map(lambda c: Colour.fromHex(c), lights["left-ribbon"] )) if "left-ribbon"  in lights else report.ribbon_l
    report.ribbon_r = list(map(lambda c: Colour.fromHex(c), lights["right-ribbon"])) if "right-ribbon" in lights else report.ribbon_r
    report.panel_l  = Colour.fromHex(lights["left-panel"] )                          if "left-panel"   in lights else report.panel_l
    report.panel_r  = Colour.fromHex(lights["right-panel"])                          if "right-panel"  in lights else report.panel_r

    # Other light data
    report.brightness = min(lights["brightness"], 255) if "brightness" in lights else report.brightness
    # TODO: Patterns

# Get bytes from report
packet = report.getBytes()

with hid.Device(
        DEVICES.ROCCAT.KONE_AIMO.vid,
        DEVICES.ROCCAT.KONE_AIMO.pid
) as hid_dev:
    hid_dev.send_feature_report(packet)
