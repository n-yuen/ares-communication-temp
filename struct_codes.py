# Constants from the python documentation
# SIZES WILL DIFFER BASED ON ARDUINO UNO OR DUE
# values given are for UNO
# Map as Arduino Name => (Python struct code, byte length)
STRUCT_CODES = { 
    "float": ("f", 4),
    "double": ("d", 8),
    "int": ("h", 2),
    "unsigned int": ("H", 2),
    "char": ("c", 1),
    "byte": ("B", 1)
}
# A UNO's int corresponds to python's short