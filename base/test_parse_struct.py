from parse_struct import parse_struct

print("Expect to be 420 x 8")
info = parse_struct(b'\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\xFF\xFF\xFF\xFF\xFF\xFF\xFF') #prints 7 delims
for data in info:
    print(data)
print("adding 8th delim byte")
info = parse_struct(b'\xff') #adding the 8th will trigger a print
for data in info:
    print(data)
print("Performing cutup test")
info = parse_struct(b'\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43')
info = parse_struct(b'\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43')
info = parse_struct(b'\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF')
for data in info:
    print(data)

print("Performing multiple test")
info = parse_struct(
    b'\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'+
    b'\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\00\00\xd2\x43\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF'
)
for data in info:
    print(data)