enc = "\t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e"
key = "jowls"
know_text = "ctflearn{"
for i in range(9):
    print(chr(ord(enc[i])^ord(know_text[i])),end=' ')
print()
ki = 0
for i in enc:
    print(chr(ord(i)^ord(key[ki])),end='')
    if(ki+1 < 5):
        ki+=1
    else:
        ki=0  

