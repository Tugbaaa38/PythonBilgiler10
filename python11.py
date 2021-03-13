#while & for dongusu

#while dongusu

while True: # Aksi belirtilmedigi surece dongu calisir.
    isim=input("Adinizi girin:(cikmak icin -1 tuslayiniz.):")
    print("\n")
    if isim=="-1":
        print("Cikiliyor..")
        break;


#Bir liste olusturalim ve elemanlari while ile ekleyelim daha sonra kucukten buyuge bu sayilari siralayalim.

sayiListesi=[]
elemanS=int(input("Kac elemanli olsun="))
i=0
while i<elemanS:                                                      
    sayi=int(input("Eklemek istediginiz sayiyi giriniz:"))
    sayiListesi.append(sayi)
    i+=1

sayiListesi.sort()
print(sayiListesi)


#for dongusu

#for degisken_adi in degisken:     #Yapi budur.
#    yapilacak_islem

#ciftRakam=2468
#for cift in ciftRakam:            #Burada degiskenimiz int turunden oldugu icin kodumuz hata verecektir.
#    print(cift)

ciftRakam="2468"                   #Bu sekil(string olarak)yazdigimizda ise alt alta 2,4,6,8 ciktilarini bize verecektir.
for cift in ciftRakam:
    print(cift)

#kullanicidan kullanici adini girmesini isteyelim ve bu kullanici adinda turkce harf kullanip kullanmadigini
#kontrol edelim,kullandiysa  hata mesaji gonderelim..

tr_harfler="şçöğüİı"
kullanici_adi=input("Kullanici adiniz:")
for harf in kullanici_adi:
    print(harf)
    if harf in tr_harfler:
        print("Kullanici adinda turkce karakter kullanmayiniz..!")
        break;



for yaz in range(1,50):
    if yaz==5:
        continue
    print(yaz)
    
    #burada continue asagi satira inmeden basa don ve devam et demektir.Yani bu kod 5 disindaki 50 ye kadar olan
    #sayilari yazarken 5 i yazmayacak.

for yaz in range(1,50):
    if yaz==5:
        break
    print(yaz)

    #break: 5 i gorene kadar tum sayilar yazilacak 5 i gorunce break  donguyu kirip donguden cikacak..
