from typing import List
from struct import unpack
from gen import STRUCT_ORDER, STRUCT_LENGTH

parse_buffer: bytearray = bytearray(STRUCT_LENGTH)
contig_ff = 0 #counts the number of contiguous FF's
write_index = STRUCT_LENGTH+1 #counts which index to write the next byte into

def parse_struct(bytes: bytearray) -> List[tuple]:
    global write_index, contig_ff
    tuple_list = []
    for b in bytes:
        if b == 255:
            contig_ff = contig_ff + 1
        else:
            contig_ff = 0
        if contig_ff == 8:
            if write_index == STRUCT_LENGTH:
                tuple_list.append(
                    unpack(STRUCT_ORDER, parse_buffer)
                )
            write_index = 0
            contig_ff = 0
            continue # don't write the FF into the 0 slot
        if write_index < STRUCT_LENGTH:
            parse_buffer[write_index] = b
            write_index = write_index + 1
    return tuple_list

        
