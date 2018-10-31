from typing import List
from struct import unpack

STRUCT_FORMAT = "<"+(8*"f") #https://docs.python.org/3/library/struct.html#struct-alignment
FLOAT_SIZE = 4
parse_buffer: bytearray = [0] * (8 * FLOAT_SIZE) #8 to store 8 floats, 2 to store delim
BUFFER_SIZE = len(parse_buffer)
contig_ff = 0 #counts the number of contiguous FF's
write_index = 0 #counts which index to write the next byte into

def parse_struct(bytes: bytearray) -> List[tuple]:
    global write_index, contig_ff
    tuple_list = []
    for b in bytes:
        if write_index < BUFFER_SIZE:
            parse_buffer[write_index] = b
            write_index += 1
        if b == 255: #is FF
            contig_ff += 1
            if contig_ff == 8:
                #message complete, begind serializing
                tuple_list.append(
                    unpack(
                        STRUCT_FORMAT, 
                        bytearray (
                            parse_buffer[0:BUFFER_SIZE]
                        )
                    )
                )
                contig_ff = 0
                write_index = 0
        else:
            contig_ff = 0
    return tuple_list

        
