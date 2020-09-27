# Algorithmn
## Misc
### flabby

###Description:
```
0 : 0x539
1 : 0x53b
1 : 0x53e
2 : 0x546
3 : 0x552
5 : 0x56b
8 : 0x59d
13 : 0x613
21 : 0x732
34 : 0xa0e

0x43b1941fa3149c2ceb0da0bc5c5bff56a797b508becb5fbd058aec845ff0060fdc463393be61850549371b5de1d73836bf646d9d78f86bba3847dd1e0111d18d9d63094154077cc446064310bab1a9b0aa8ffce5f429121fc1bafb72cad608d87cc37c40fd9b5374703f0898695d6185ffd4ecfb457b48a9f6577df27cbfe0605752ba9de8fd2e36bbd96c5237eeba3899add0d504edb2262d467cb6299c787a8536f3caf5c8037c447e23adae31a7878f50bc2cc564c35c850a61bc70e23f565d604245f761452ccde6f53b56a3e8ff9dde120673198b3c274848c75197029b4d756d2f7bd01b22
```

### Solution:
Looking at the A values for the given first few analogies:
The first value is `1337` a common number in the world of ctf's.
the second value is `1339`. and then it goes: `1342`,`1350`,`1362`,... and so on.
If we subtract 1337 from each value you get something like this: `0,2,5,13,25,...`
Let's subtract the corresponding N value from these new values we got: `0,1,4,9,16,...`
and now the algorithm used becomes clear...
On the other hand the left hand or the N values are just the values from the fibonacci sequence

The algorithm used here was:
```python
def algo(n):
    n1,n2 = 0,1
    few = 0
    for i in range(n):
        if few < 10:
             print(f"{n1} : {hex((n1*n1)+(i*i)+1337)}")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        few += 1
```

The given A value matched for 1337th fibonacci number, which is:
```
1166782782969257491619153740434791503598234290741291359406061212397345887252545157833399269855824772839341106446209993475918896282003637549042932817693993792294375837384925771418274778734420597627415942373411818041261373335700249267727594511569151368792111912361418558537679167117
```

### Flag
> darkCTF{7679167117}
