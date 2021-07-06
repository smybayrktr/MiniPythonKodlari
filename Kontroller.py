
username = input("Kullanici Adi:") #Kullanıcıdan giriş aldık
password = input("Sifre: ")
if username == "smybayrktr" and password == "123":
        print("giriş başarılı")
else:
        print("Başarısız")

print("----------------------------------------------------")
islem = input("Lütfen işlemi giriniz:")
sayı1 = int(input("Lütfen birinci sayıyı giriniz:"))
sayı2 = int(input("Lütfen ikinci sayıyı giriniz:"))
if islem=="1" :
    sonuc = int(sayı1+sayı2)
    print(sonuc)
elif islem=="2" :
    sonuc=int(sayı1-sayı2)
    print(sonuc)
elif islem=="3" :
    sonuc= int(sayı1)*int(sayı2)
    print(sonuc)
elif islem=="4":
    sonuc = int(sayı1)/int(sayı2)
    print("Sonuç:",str(sonuc))
else :
    print("Hatalı işlem girişi")

