from typing import List
from struct import unpack
from gen import STRUCT_ORDER, STRUCT_LENGTH

parse_buffer: bytearray = bytearray(STRUCT_LENGTH)
contig_ff = 0 #counts the number of contiguous FF's
write_index = STRUCT_LENGTH #counts which index to write the next byte into
throwaway = True #throwaway the first data (is junk)
def parse_struct(bytes: bytearray) -> List[tuple]:
    global write_index, contig_ff, throwaway
    tuple_list = []
    for b in bytes:
        if write_index < STRUCT_LENGTH:
            parse_buffer[write_index] = b
            write_index = write_index + 1
        if b == 255:
            contig_ff = contig_ff + 1
        else:
            contig_ff = 0
        if contig_ff == 8:
            if write_index == STRUCT_LENGTH:
                if not throwaway:
                    tuple_list.append(
                        unpack(STRUCT_ORDER, parse_buffer)
                    )
                throwaway = False
                contig_ff = 0 
                write_index = 0
    return tuple_list

        
