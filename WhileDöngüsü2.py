sayı=int(input("Faktöriyeli alınacak sayıyı giriniz."))
i = 1
yeniSayi=1
while(i<=sayı):
    sonuc=i*yeniSayi
    yeniSayi=sayı
    yeniSayi=sonuc
    i+=1
print(sonuc)