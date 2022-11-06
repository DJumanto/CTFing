num = "67847010810197110123678289808479718265807289125"
i=0
while(i<len(num)):
    if(num[i]=='1'):
        dat = int(num[i:i+3])
        i+=3
    else:
        dat = int(num[i:i+2])
        i+=2
    print(chr(dat),end='')