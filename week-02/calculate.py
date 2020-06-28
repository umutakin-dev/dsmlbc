def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return int(x / y)

print()
print("HESAP MAKINESI")
print("1. Toplama / 2. Cikarma / 3. Carpma / 4. Bolme")

islem = int(input("Hangi islemi yapmak istersiniz: "))

x = int(input("Birinci degeri giriniz: "))
y = int(input("Ikinci degeri giriniz: "))

if islem == 1:
    print("Toplam Sonucu: " + str(toplama(x, y)))
elif islem == 2:
    print("Cikarma Sonucu: " + str(cikarma(x, y)))
elif islem == 3:
    print("Carpim Sonucu: " + str(carpma(x, y)))
elif islem == 4:
    print("Bolme Sonucu: " + str(bolme(x, y)))

print()
