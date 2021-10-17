# rka-control-python
Python program for lighting control of the Roccat Kone AIMO mouse on Linux. Based on [Squ1dd13's rka-control](https://github.com/Squ1dd13/rka-control).

## Dependencies
* Python 3
* libhidapi-libusb.so (Should come with all distributions, this software looks for it under `/lib/`)

## Usage
Set the desired light colours in hexadecimal RGB or RGBA in a JSON file. An example file, `lights.json`, is provided. Then run main.py with Python 3, giving the json file as the only argument: 
```shell
python main.py lights.json
```
Depending on your distribution, you may need to substitute `python3` in place of `python` in the above command.

## Future
Currently the software is at a very early stage, and I have several plans for it's future:
* Simple GUI
* Simple CLI
* Better configuration files
* Better error reporting
* Fetching current configuration

For more long term goals, I am considering the possibility of expanding the software to handle all configuration of the mouse and not only lights. Depending on what hardware I will have in the future, it may also be expanded to handle other devices, however currently there are no plans for that.

## Credits
* Squ1dd13 : Original rka-control Go program, which this is based on

## Disclaimer
This software should be regarded as **experimental** and as such, any damage caused to your hardware as an outcome
of the use of this software is **not my responsibility**. 

**Use at your own risk.**
