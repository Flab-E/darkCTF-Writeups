from binascii import unhexlify

def fixIt(i,j):
    src = f"flags/flag_{i}_{j}.jpg"
    dest = f"fixed/flag_{i}_{j}.png"

    file = open(src, "rb")
    data = file.read()
    file.close()

    png_header_int = ['89', '50', '4e', '47', '0d', '0a', '1a', '0a']
    png_header = b''.join(unhexlify(i) for i in png_header_int)
    fixed = png_header + data[10:]

    file = open(dest, "wb")
    file.write(fixed)
    file.close()

for i in range(100):
    for j in range(100):
        fixIt(i, j)
