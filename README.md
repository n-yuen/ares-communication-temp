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
ALWAYS BE UPDATING THIS SECTION
1. arbitrary float
2. arbitrary float
3. arbitrary float
4. arbitrary float
5. arbitrary float
6. arbitrary float
7. arbitrary float
8. arbitrary float