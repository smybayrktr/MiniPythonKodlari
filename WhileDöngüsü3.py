sayi = int(input("Hangi sayıya kadarki tüm sayılar toplansın?"))
sonuc = sayi * (int(sayi+1)/2)
print(sonuc)
print("----------------------2.YOL-------------------------")
toplam=0
i=1
while i<=sayi:
    toplam+=i
    i+=1
print(toplam)
