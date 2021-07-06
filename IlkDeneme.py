print ("Merhaba")
print(2**4) #2 üssü 4 alır.
print(15//2) #15i 2ye böler ama tam kısmını sonuç verir.
x, y, name, isStudent =(1, 2.4, "Süm", True) #şeklinde değer ataması da yapılabilir.

"""
Buda çoklu
yorum satırı 
için kullanılıyo """
#Tip dönüşümü:
print("#inti floata çevirme:")
x=5
print(type(x))
x=float(x)
print(type(x))
print("#floatı inte çevirme:")
y=2.5
print(type(y))
y = int(y)
print(type(y))
print(y)
print("#stringe çevirme:")
result=str(x)+str(y) #x ve y yi stringe çevirdi
print(result)
print(type(result))
print("#booldan inte dönüşüm:")
dogruMu=True
print(type(dogruMu))
dogruMu=int(dogruMu)
print(dogruMu)
print(type(dogruMu))


