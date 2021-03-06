from typing import List
from struct import unpack
import binascii
from gen import STRUCT_ORDER, STRUCT_LENGTH

parse_buffer: bytearray = bytearray(STRUCT_LENGTH)
contig_ff = 0 #counts the number of contiguous FF's
write_index = STRUCT_LENGTH #counts which index to write the next byte into
firstEncountered = False #throwaway the first data (is junk)
def parse_struct(bytes: bytearray) -> List[tuple]:
    if len(bytes) == 0:
        return []
    global write_index, contig_ff, firstEncountered
    tuple_list = []
    for b in bytes:
        if write_index < STRUCT_LENGTH and firstEncountered:
            parse_buffer[write_index] = b
            write_index += 1
        elif b == 255:
            contig_ff += 1
            if contig_ff >= 4 and write_index == STRUCT_LENGTH:
                if not firstEncountered:
                    firstEncountered = True
                else:
                    tuple_list.append(
                        unpack(STRUCT_ORDER, parse_buffer)
                    )
                contig_ff = 0 
                write_index = 0
        else:
            contig_ff = 0  
    return tuple_list

        
