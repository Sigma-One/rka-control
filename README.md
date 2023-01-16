# rka-control-python
Python program for lighting control of the Roccat Kone AIMO mouse on Linux. Based on [Squ1dd13's rka-control](https://github.com/Squ1dd13/rka-control).

## Dependencies
* Python 3
* [`hid` Python module](https://pypi.org/project/hid/), packaged as `python3-hid` on Void Linux

## Usage
Set the desired light colours in hexadecimal RGB or RGBA in a JSON file. Examples can be found under `presets/`. Then run main.py with Python 3, giving the json file as the only argument: 
```shell
python main.py -c <filename>.json
```
Depending on your distribution, you may need to substitute `python3` in place of `python` in the above command. It may also have to be run as root, depending on permissions on your system.

The light config JSON can have values omitted from it, these will be substituted by defaults as set in `feature_report.py`, which is mostly disabled lighting.

## Future and Planned Features
The highest priority plan at this time is investigating the rest of the bytes in the HID feature report in `feature_report.py`.

Some planned features after that is done include:
* Better configuration, JSON is a bit clunky at times
* Better error reporting
* Fetching current configuration from the mouse

For more long term goals, I am considering the possibility of expanding the software to handle all configuration of the mouse and not only lights. Depending on what hardware I will have in the future, it may also be expanded to handle other devices, however currently there are no actively worked on plans for that.

## Credits
* Squ1dd13 : Original rka-control Go program, which this is based on

## Disclaimer
This software should be regarded as **experimental** and as such, any damage caused to your hardware as an outcome
of the use of this software is **not my responsibility**. 

**Use at your own risk.**
