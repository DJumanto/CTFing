dat = "391e95a15847cfd95ecee8f7fe7efd668473dcb86bc12c6b6087619c00b6657e"
for i in range(0,len(dat),2):
    val = int(dat[i:i+2],16)
    print(chr(val),end='')
    