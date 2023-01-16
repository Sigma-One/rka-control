import hid # HID functions

from devices        import DEVICES       # Device vendor and product IDs
from colour         import Colour        # Colour object
from feature_report import FeatureReport # Feature report object

import sys  # Args reading
import json # JSON parsing

# TODO: Implement better arg parsing

# Parse arguments
arg_list = []
for a in sys.argv[1:]:
    if a.startswith("-"):
        arg_list.append((a, []))
    else:
        arg_list[-1][1].append(a)

# Convert to dict
arg_map = {}
for a in arg_list:
    arg_map[a[0]] = a[1]

report = FeatureReport()

# Profile selection
if "-p" in arg_map:
    report.profile = int(arg_map["-p"][0])

# File parsing and such
if "-c" in arg_map:
    with open(arg_map["-c"][0], "r") as lightFile:
        lights = json.load(lightFile)

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

# TODO: Get previous report and merge with new one to maintain everything unchanged

with hid.Device(
        DEVICES.ROCCAT.KONE_AIMO.vid,
        DEVICES.ROCCAT.KONE_AIMO.pid
) as hid_dev:
    hid_dev.send_feature_report(packet)
