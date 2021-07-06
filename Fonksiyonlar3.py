def çiftSayilar (sayi):
    liste=[]
    for i in range (1,sayi,1):
        if i%2==0:
            liste.append(i)
    return liste
sayi=int(input("Hangi sayıya kadarki çift sayılar yazdırılsın."))
print(çiftSayilar(sayi))