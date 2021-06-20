inp = input()

words = inp.split(',')
nonhex = []
nonbin = []
nonascii = []

for x in words:
    nonhex.append(str(int(x, 16)))
for x in nonhex:
    nonbin.append(int(x, 2))
for x in nonbin:
    nonascii.append(chr(x))

out = ''
for x in nonascii:
    out += x
print(out)
        
