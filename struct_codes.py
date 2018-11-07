# Constants from the python documentation
# SIZES WILL DIFFER BASED ON ARDUINO UNO OR DUE
# values given are for UNO
# Map as Arduino Name => (Python struct code, byte length)
STRUCT_CODES = { 
    "float": ("f", 4),
    "double": ("d", 8),
    "int": ("i", 2),
    "unsigned int": ("I", 2),
    "char": ("c", 1),
    "byte": ("B", 1)
}