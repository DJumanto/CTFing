key = "!@#$%^&*()"
val = "1234567890"
_in = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"
new_dat = ""
for i in _in:
    index = key.find(i)
    new_dat += val[index]
print('')
i =2
print(chr(int(new_dat[0:2])),end='')
while(i<len(new_dat)):
    if(new_dat[i+1]=='1'):
        dat = int(new_dat[i:i+4])
        i+=4
    else:
        dat = int(new_dat[i:i+3])
        i+=3
    print(chr(dat),end='')