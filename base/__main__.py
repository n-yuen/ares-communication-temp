# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from digi.xbee.devices import XBeeDevice, XBeeMessage
from parse_struct import parse_struct
from gen import STRUCT_FIELDS

# TODO: Replace with the serial port where your local module is connected to. 
PORT = "/dev/tty.usbserial-DN04AJCW" #"/dev/tty.usbserial-DN04AJCW" "306" 
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

def main():
    print(STRUCT_FIELDS)

    device = XBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        def data_receive_callback(xbee_message: XBeeMessage):
            info = parse_struct(xbee_message.data)
            if info:
                for data in info:
                    print(','.join(str(i) for i in data))

        device.add_data_received_callback(data_receive_callback)
        input()

    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()