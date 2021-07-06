name = "Sümeyye"
print(name[5]) #5.indisi yazdırır.
print(len(name)) #name in kaç indeksten oluştuğunu verir.
print(name[len(name)-1]) #son indekstekini yazdırır.1 çıkardık çünkü 7 karakterliyse 0 dan başladığı için son indis 6.indistir.
print(name[-1]) #buda son indisi verir. İndisi sondan saymaya başlarsan -li değerli say -1, -2. indis gibi
print(name[2:5]) #2.indeksten 5.indekse kadar yazdırma yapar.
print(name[:5]) #5.indekse kadar yazdırır.
print(name[2:]) #2.indeksten sona kadar yazdırır.
print(name[0:5:2]) #0.indisten 5.indise kadarki indisleri 2şer atlayarak yazdırır.
print("--------------------------------------------------------------------------------")
name="Sümeyye"
surname="Bayraktar"
print(f"My name is {name} and my surname is {surname}")
print("My name is {} and my surname is {}".format(name,surname)) 
 