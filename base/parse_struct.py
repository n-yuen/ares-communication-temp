from typing import List
from struct import unpack
from gen import STRUCT_ORDER, STRUCT_LENGTH

parse_buffer: bytearray = bytearray(STRUCT_LENGTH)
contig_ff = 0 #counts the number of contiguous FF's
write_index = 0 #counts which index to write the next byte into

def parse_struct(bytes: bytearray) -> List[tuple]:
    global write_index, contig_ff
    tuple_list = []
    for b in bytes:
        if write_index < STRUCT_LENGTH:
            parse_buffer[write_index] = b
            write_index += 1
        if b == 255: #is FF
            contig_ff += 1
            if contig_ff == 8:
                #message complete, begin deserializing
                tuple_list.append(
                    unpack(
                        STRUCT_ORDER, 
                        parse_buffer
                    )
                )
                contig_ff = 0
                write_index = 0
        else:
            contig_ff = 0
    return tuple_list

        
