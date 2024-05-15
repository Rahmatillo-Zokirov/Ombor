wins = ['123', '147', '258', '369', '654', '987', '357', '159',]
templates = """ --- --- ---
| 1 | 2 | 3 |
--- --- ---
| 4 | 5 | 6 |
--- --- ---
| 7 | 8 | 9 |
 --- --- ---
"""
xlar = ''
olar = ''

i = 1
while True:
    if i % 2 == 1:
        x = input(templates + "(X) o'yinchi (1-9) oraligidagi sonni kiritng: ")
        while int(x) not in range(1, 10):
            x = input(templates + "(X) o'yinchi qaytadan (1-9) oralig'ida son kiriting:")
        while x in xlar + olar:
            print("Joy allaqachon mavjud !!")
            x = input(templates + "(X) o'yinchi qaytadan (1-9) oralig'ida son kiriting:")
        templates = templates.replace(x, "✖")
        xlar += x

        for win in wins:
            if win[0] in xlar and win[1] in xlar and win[2] in xlar:
                print("_____________________\n (X) o'yinchi g'alaba qozondi 🎉🎉")



    if i % 2 == 0:
        s = input(templates + "(0) o'yinchi 1-9 oraligidagi sonni kiritng: ")
        while int(s) not in range(1, 10):
            s = input(templates + "(0) o'yinchi qaytadan (1-9) oralig'ida son kiriting:")
        while s in xlar + olar:
            print("Joy allaqachon mavjud !!")
            s = input(templates + "(0) o'yinchi qaytadan (1-9) oralig'ida son kiriting:")
        templates = templates.replace(s, "0️⃣")
        olar += s


        for win in wins:
            if win[0] in olar and win[1] in olar and win[2] in olar:
                print("_____________________\n (0) o'yinchi g'alaba qozondi 🎉🎉")


    if i <= 9:
        print("")
        break
    i += 1
if i == 9:
    print("______________________________\nDurrang qayt etildi ")

print(templates)