dosya=open("sayilar.txt","r") #r parametresiyle açınca okuma modunda açar.
icerik=dosya.read()
dosya.close()
for i in icerik.splitlines(): #burda dosyayı satır satır okuyup i değişkenine atar.
    print(i) #burda da sayılar.txt dosyasındaki herşey yazdırılır.