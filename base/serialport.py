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

import serial
from parse_struct import parse_struct
from gen import STRUCT_FIELDS

# TODO: Replace with the serial port where your local module is connected to. 
PORT = "COM6" #"/dev/tty.usbserial-DN04AJCW"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600

ser = serial.Serial(PORT, BAUD_RATE, timeout=0)

def main():
    print(STRUCT_FIELDS)
    try:
        ser.open()
        while True:
            byteList = ser.read_all()
            data = parse_struct(byteList)
            for line in data:
                print(line)
    finally:
        if ser is not None and ser.is_open:
            ser.close()

if __name__ == '__main__':
    main()