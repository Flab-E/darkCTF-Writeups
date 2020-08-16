# RGBA
## Forensics


### Description:
```
r - red
g - green
b - blue
a - ???
```

### Solution:
the description gives a hint towards `alpha` of the image.
Looking at the image itself you can see that certain pixels have different levels of opacity.
You can use python's PIL module to look at RGBA values, and the values in alpha channel seem to be within the ascii printable range!

##### Script:
```
from PIL import Image

im = Image.open("chall.png", 'r')
im = im.convert("RGBA")
pixel = list(im.getdata())
print(pixel)
flag = ''

for i in pixel:
    flag += chr(i[3])

print(flag)
```

And thus you have your flag!

### Flag:
> darkCTF{th3_fl4g_1s_tran5par3nt}
