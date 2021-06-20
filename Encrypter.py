inS = "NULL"

inS = input(" ")
ASCIIwords = []
binASCIIwords = []
HexBinASCIIwords = []

ASCIIwords = [ord(c) for c in inS]
for x in ASCIIwords:
    word = bin(x)
    word = word[2:]
    binASCIIwords.append(word)

for x in binASCIIwords:
    word = hex(int(x))
    word = word[2:]
    HexBinASCIIwords.append(word)
    
out = ''

for x in HexBinASCIIwords:
    out += x
    out += ','
    
print(out)


