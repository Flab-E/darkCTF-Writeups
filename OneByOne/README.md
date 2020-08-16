# OneByOne
## Misc

### Description
```
Mr.Fun stole the flag from us and is not giving it back. Probably you can get it for us?
He won't give it right away that easily though, I can tell you that.
You've gotta ask him the flag one by one.
```

### Solution:
The given netcat connection asks you a set of easy maths problems (all are addition based problems).
A total of 46 quesations are asked.
For each problem though the numbers in the problem itself are random the final answers are always same. By same I mnean that the first question always gives the result `100`.
And each of these results are within ascii range.

##### Script:
```
#!/usr/bin/python3
from pwn import *

r = remote('1by1.darkarmy.xyz', 7001)
flag = ''

print(r.recvline().decode('utf-8'))

for i in range(46):
    ques = r.recvuntil(b'> ').decode('utf-8')
    print(ques,end=' ')
    ordinate = str(int(ques.split()[0]) + int(ques.split()[2]))
    r.sendline(ordinate.encode())
    flag += chr(int(ordinate))

print(flag)
```

### Flag:
>  darkCTF{y0U_r3Ally_w4n7_tHe_flaGG_th4T_b4Dly?}
