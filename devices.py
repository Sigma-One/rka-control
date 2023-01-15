import typing

class Device(object):
    def __init__(
            self,
            vid  : int,
            pid  : int
    ):
        self.vid = vid
        self.pid = pid

class DEVICES:
    class ROCCAT:
        VENDOR_ID = 0x1e7d
        KONE_AIMO = Device(VENDOR_ID, 0x2e27)
