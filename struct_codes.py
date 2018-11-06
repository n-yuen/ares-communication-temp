# Constants from the python documentation
# SIZES WILL DIFFER BASED ON ARDUINO UNO OR DUE
# values given are for DUE
# Map as Arduino Name => (Python struct code, byte length)
STRUCT_CODES = { 
    "float": ("f", 4),
    "double": ("d", 8),
    "int": ("i", 4),
    "unsigned int": ("I", 4),
    "char": ("c", 1),
    "byte": ("B", 1),
    "short": ("h", 2),
    "unsigned short": ("H", 2)
}