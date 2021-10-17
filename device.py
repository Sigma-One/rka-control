import subprocess


def findDevicesByVID(vid):
    """
    Finds info on specific vendor's USB devices connected to the system.
    Please note that the given vendor ID is direcly passed to lsusb unsanitised.

    @param  vid The vendor ID to look for, preferably as a hex string
    @return     A List of devices with specified vendor ID, includes bus and device ID, device product ID, and device name
    """

    # Grab lsusb output, filtered to only devices with right vendor ID using -d
    # Linux, BSD, and possibly MacOS only, but why would you need this software on windows anyways
    lsusbOutput = subprocess.check_output(["lsusb", "-d", f"{vid}:"]).decode()
    deviceList = []

    # Go through output lines, each line has one device's details
    for line in lsusbOutput.split("\n"):
        # Handle last line, which is empty
        if not line:
            break

        # Extract details from output line
        # e.g. "Bus 001 Device 017: ID 1e7d:2e27 ROCCAT Kone AIMO Mouse"
        # Bus number (001)
        bus = int(line.split(" ")[1])
        # Device number (017)
        dev = int(line.split(" ")[3].strip(":"))
        # Product ID (2e27)
        pid = line.split(" ")[5].split(":")[1]
        # Product name (ROCCAT Kone AIMO Mouse)
        name = " ".join(line.split(" ")[6:])

        deviceList.append((bus, dev, pid, name))

    return deviceList

