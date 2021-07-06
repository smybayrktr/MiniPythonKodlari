aSinifi = ["Süm","Üm"]
bSinifi = ["Hüs","Yaro"]
isim=input("Bir isim giriniz:")
if isim in aSinifi:
    print("Kişi A sınıfının üyesi")
elif isim in bSinifi:
    print("Kişi b sınıfı üyesi")
else:
    print("Kişi üye değil.")
