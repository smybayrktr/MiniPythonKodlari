sayi=int(input("Hangi sayıya kadarki asal sayılar yazdırılsın?"))
print(2)
for i in range(3,sayi,1):
    kontrol=False
    for j in range(2,i): #2den i ye kadar
        if i%j==0:
            kontrol=True
    if kontrol==False:
        print(i)
