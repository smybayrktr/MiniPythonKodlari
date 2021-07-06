for i in range(1,10,1): #1den 10a kadarki sayıları 1-1 arttırıp i içinde saklandı
    dosya=open("sayilar.txt","a") #sayilar.txt dosyası oluşturdu-açtı
    veri= str(i) + "\n" #i yi str yani stringe çevirdi. alt satıra geçirdi.
    dosya.write(veri) #dosyayı yazdırıp alt satırda kapattı.
    dosya.close() #bu kod çalıştıktan sonra sol tarafta sayilar.txt diye belge oluştu.
