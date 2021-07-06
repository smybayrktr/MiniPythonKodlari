taban = int(input("Taban kaç olsun?"))
üs = int(input("Üs kaç olsun?"))
sonuc=1
for i in range(1,üs+1,1):
    sonuc*=taban;
    i+=1
print("Sonuç:",sonuc)