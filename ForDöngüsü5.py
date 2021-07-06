veri = "Eğitim 101"
egitim=list(veri)
harfSayici=0
rakamSayici=0
for i in egitim:
    if str(i).isdecimal():
        rakamSayici+=1
    else:
        harfSayici+=1
print("Harf sayısı:",harfSayici)
print("Rakam sayısı:",rakamSayici)