file = open("file.txt",'r')
data = file.read()
decKnown = "ALEXCTF{HERE_GOES_THE_KEY}"
print(data)
j=0
for i in range(len(decKnown)):
    print(chr(ord(decKnown[i])^int(data[j:j+2],16)),end='')
    j+=2