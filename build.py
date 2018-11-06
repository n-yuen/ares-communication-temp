#!/usr/bin/env python3
import sys
import os
from typing import List, Tuple

def capitalizeFirstChar(s: str):
    return s[0].upper()+s[1:] # when they tell you it's just like pseudocode

FILE_PATH = os.path.abspath("./data_order.csv")
PYTHON_GEN_PATH = os.path.abspath("./base/gen.py")
INO_GEN_PATH = os.path.abspath('./rocket/gen.ino')
H_GEN_PATH = os.path.abspath('./rocket/gen.h')

print("READING FROM "+FILE_PATH)

# Generate python code
structOrder = "<" #Will store the byte order for the struct module (https://docs.python.org/3/library/struct.html#struct-alignment), prefix with < for little-endian
structSize = 0
structFields = ""
# Constants from the python documentation
STRUCT_CODES = { #SIZES WILL DIFFER BASED ON ARDUINO UNO OR DUE, values given are for DUE
    "float": ("f", 4),
    "double": ("d", 8),
    "int": ("i", 4),
    "unsigned int": ("I", 4),
    "char": ("c", 1),
    "byte": ("B", 1),
    "short": ("h", 2),
    "unsigned short": ("H", 2)
}

# Generate INO file
structDec = "struct DATA_TYPE {\n"
updateMeth = "void updateData() {\n\tpreUpdate();\n"
externs = "extern void preUpdate();\n"

# Begin read
FP = open(FILE_PATH)
lines = FP.readlines()
firstLine = True
for csvLine in lines:
    if firstLine:
        firstLine = False
        if csvLine != "name,type\n":
            raise Exception("CSV has no header, may be in an invalid format")
        continue
    line = csvLine.rstrip('\n').split(',')
    # Get the python struct letter keyword
    dataTuple = STRUCT_CODES[line[1]]
    structOrder += dataTuple[0]
    structSize += dataTuple[1]
    structFields += line[0]+","
    # Create INO struct decl
    structDec += "\t{} {};\n".format(line[1], line[0])
    updateMeth += "\tdata.{} = read{}();\n".format(line[0], capitalizeFirstChar(line[0]))
    externs += "extern {} read{}();\n".format(line[1], capitalizeFirstChar(line[0]))
FP.close()

# Write out python file
print("WRITING PYTHON OUTPUT TO "+PYTHON_GEN_PATH)
FP = open(PYTHON_GEN_PATH, 'w')
FP.write(
"""STRUCT_ORDER = \"{}\"
STRUCT_LENGTH = {}
STRUCT_FIELDS = \"{}\"
""".format(structOrder, structSize, structFields[:-1]) #strip last comma from structFields
)
FP.close()

# Write out INO file
# Finish off the C declarations
structDec += "} data;\n"
updateMeth += "}\n"
print("WRITING INO OUTPUT TO "+INO_GEN_PATH)
FP = open(INO_GEN_PATH, 'w')
FP.write('#include "gen.h"\n')
FP.write(externs)
FP.write('\n')
FP.write(updateMeth)
FP.write('\n')
FP.close()

print("WRITING H OUTPUT TO "+H_GEN_PATH)
FP = open(H_GEN_PATH, 'w')
FP.write("#pragma once\n\n")
FP.write(structDec)
FP.close()

print("BUILD COMPLETE")

