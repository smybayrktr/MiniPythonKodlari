def hesapMakinesi (sayi1 , sayi2, islem):
    if islem==1:
        sonuc=sayi1+sayi2
    elif islem==2:
        sonuc=sayi1-sayi2
    elif islem==3:
        sonuc=sayi1*sayi2
    elif islem==4:
        if sayi2!=0:
            sonuc=sayi1/sayi2
        else:
            print("Payda 0 olamaz")
    else:
        print("Hatalı işlem girdiniz.")
sayi1=int(input("Birinci sayıyı giriniz."))
sayi2=int(input("İkinci sayıyı giriniz."))
islem=int(input("İşlemi giriniz. 1-Toplama, 2-Çıkarma, 3-Çarpma, 4-Bölme"))
hesapMakinesi(sayi1,sayi2,islem)