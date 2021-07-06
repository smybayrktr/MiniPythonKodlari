import random
randomSayi=round(random.random()*100) #0-100 arası sayı üretmeye yarar.
print(randomSayi)
girilenSayi=int(input("Tahmin ettiğiniz sayı:"))
while girilenSayi!=randomSayi:
    if girilenSayi>randomSayi:
        print("Büyük bir sayı girdiniz.")
    elif girilenSayi<randomSayi:
        print("Küçük bir sayı girdiniz.")
    girilenSayi=int(input("Sayı tekrar:"))
print("Tebrikler oyunu kazandınız")