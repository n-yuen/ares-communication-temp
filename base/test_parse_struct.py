from parse_struct import parse_struct

print("Enter your byte stream, or 'quit' to exit")
while True:
    inputStr = input()
    if inputStr == 'quit':
        break
    byteArr = bytearray()
    for i in range(0, len(inputStr) // 2):
        byteStr = inputStr[2*i:2*i+2]
        byteArr.append(int(byteStr, 16))
    data = parse_struct(byteArr)
    for line in data:
        print(line)
