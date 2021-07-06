sayı=int(input("Hangi sayıya kadarki sayıların toplamı alınsın?"))
toplam=0;
for i in range(1,sayı,1): #sayı+1 olarak yazsaydık sayıyı da dahil ederdi.
    toplam+=i
print("Sayıların toplamı",str(toplam))

