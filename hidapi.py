from ctypes import *
hid = cdll.LoadLibrary("/lib/libhidapi-libusb.so")
hid.hid_open.restype = c_void_p


def open(vendorID, productID):
    """
    Opens a HID device

    @param  vendorID    The desired device's vendor ID as an Int
    @param  productID   The desired device's product ID as an Int
    @return             A c_void_p (Void Pointer) to the opened HID device
    """
    return c_void_p(hid.hid_open(
        c_ushort(vendorID),
        c_ushort(productID),
        None
    ))


def sendFeatureReport(device, data):
    """
    Sends a HID feature report with some data

    @param  device  A c_void_p (Void Pointer) to the device to send the report to
    @param  data    Bytes to send to the device
    """
    if type(device) != type(c_void_p()):
        raise TypeError("Device must be a pointer to a HID device")
    if type(data) != type(b''):
        raise TypeError(f"Data must be bytes, not {type(data).__name__}")

    data = create_string_buffer(data)
    hid.hid_send_feature_report(device, data, sizeof(data))


def getFeatureReport(device):
    """
    Receives a HID feature report
    
    @param  device  A c_void_p (Void Pointer) to the target device
    @return         Bytes containing the received feature report
    """
    if type(device) != type(c_void_p()):
        raise TypeError("Device must be a pointer to a HID device")

    data = create_string_buffer(512)
    hid.hid_get_feature_report(device, data, sizeof(data))
    return data.raw


def close(device):
    """
    Closes a HID device

    @param  device  A c_void_p (Void Pointer) to the device to close
    @return         0 on success, -1 on failure
    """
    if type(device) != type(c_void_p()):
        raise TypeError("Device must be a pointer to a HID device")

    return hid.hid_close(device)
