# Flag_Of_Life
## misc
### flabby

### Description
```
Help our adventurer in attaining the Flag of Life by defeating the Demon Guard Flageon
```

### Solution  
So this is a typical Data Type overflow challenge.  
Once you connect to the netcat port command given  
you can only connect and interact with the program  
it asks you for a random positive number greater than 0  
in the background it squares the number and checks if it is 0  
so you have to find a way to make the area (square) equal to 0.  
this can be done by overflowing the `int` type in C.  
The minimum and maximum int values that C can handle are:  
`-2147483648` to `2147483647`  
So to get 0, you have to give a number such that  
the square of that number gives you 0, or in other words,  
`2147483647+2147483648 +1` (+1 to get 0) which is `4,29,49,67,296`.  
root of `4,29,49,67,296` is `65536`. Therefore the value to  
get the flag is with the value `65536`  

### Flag
> darkCTF{-2147483648_c0m3s_aft3r_2147483647}
