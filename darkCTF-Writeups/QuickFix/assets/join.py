from PIL import Image

def join():
    dest = "flag.png"

    pixels = []
    for i in range(100):
        p1 = []
        p2 = []
        p3 = []
        p4 = []
        p5 = []
        p6 = []
        p7 = []
        p8 = []
        p9 = []
        p10 = []
        p11 = []
        p12 = []
        p13 = []
        p14 = []
        p15 = []
        p16 = []
        p17 = []
        p18 = []
        p19 = []
        p20 = []
        for j in range(100):
            src = f"fixed/flag_{j}_{i}.png"
            img = Image.open(src, "r")
            ps = list(img.getdata())

            p1 += ps[0:20]
            p2 += ps[20:40]
            p3 += ps[40:60]
            p4 += ps[60:80]
            p5 += ps[80:100]
            p6 += ps[100:120]
            p7 += ps[120:140]
            p8 += ps[140:160]
            p9 += ps[160:180]
            p10+= ps[180:200]
            p11+= ps[200:220]
            p12+= ps[220:240]
            p13+= ps[240:260]
            p14+= ps[260:280]
            p15+= ps[280:300]
            p16+= ps[300:320]
            p17+= ps[320:340]
            p18+= ps[340:360]
            p19+= ps[360:380]
            p20+= ps[380:]

        pixels += p1+p2+p3+p4+p5+p6+p7+p8+p9+p10+p11+p12+p13+p14+p15+p16+p17+p18+p19+p20
    print(len(pixels))
    img2 = Image.new("RGBA", (2000,2000))
    img2.putdata(pixels)
    img2.save(dest)


def main():
    img = Image.open("fixed/flag_0_0.png")
    pixels = list(img.getdata())
    print(pixels)
    print(len(pixels))

#main()
join()
