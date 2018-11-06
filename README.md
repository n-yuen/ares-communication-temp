# Rocket Telemetry
This system is set up to read and write arbitrary collections of memory
through the XBee antenna

## Current Protocol

**Structs are packed with a padding of 8 bits in little-endian order**

| Representation | Description |
| --- | --- |
| 8 High Bytes | MESSAGE_BEGIN |
| arbitrary bits | DATA (see data order) |

You can check for a new message by recieving 64 high bits in a row.

## Data Order
See [data_order.csv](data_order.csv) for a list of fields sent

## Build System
Execute `./build.py` with the CWD being the root directory of both projects. `build.py` will:
1. Read in `data_order.csv` to get a list of fields and their names/types, turning them into a struct `data`
2. Overwrite `base/gen.py` with the length to allocate for a buffer for `data`, and the order of the fields of `data` to pass into the `struct` module from python
3. Overwrite `rocket/gen.h` with the appropriate C struct that represents `data`
4. Overwrite `rocket/gen.ino` with an appropriate `updateData()` method

**ANYTHING NAMED GEN.\* IS SUBJECT TO OVERWRITING**