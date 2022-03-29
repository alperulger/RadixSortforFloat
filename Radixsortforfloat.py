
from datetime import datetime 
    # Gelen dosya adına sahip dosyanın içindeki verileri listeye alıp bu listeyi döndürüyoruz.
def dosyaokuma(gelendosyaadi):
    liste=[]
    dosya=open(gelendosyaadi,'r')
    for gelen in dosya:
        liste.append(float(gelen.strip()))
    dosya.close()
    return liste
    # Counting  sort işlemlerinin yapıldığı fonksiyon.
def countingSort(gelen_liste, gelen_basamak):
    # Gelen listenin eleman sayısını aldık.
    liste_uzunluk = len(gelen_liste)
 
    # Gelen listenin uzunluğunda yeni bir liste tanımladık. Bu listede, 
    # Gelen listenin basamak değerine göre sıralanmış halini tutacağız.
    output = [0] * (liste_uzunluk)
 
    # Bu listenin uzunluğunu basamakların alabileceği farklı değerlerin 
    # sayısı kadar ayarladık. 0-9 yani 10 farklı değer.
    count = [0] * (10)
 
    # Bu döngüde listenin konturol ettiğimiz basamağında karşılaştığımız rakamı
    # indis olarak alırız. count dizisinin o indisteki elemanını 1 arttırırız. Böylece
    # hangi rakamın kaç kere tekrar ettiğini belirleriz.
    for i in range(liste_uzunluk):
        index = int(gelen_liste[i] / gelen_basamak)
        count[index % 10] += 1
 
    # Bu döngüde count listesinin her elemanını bir önceki elemanla toplarız.
    # Bu bize sayıları output listesinde hangi konuma yerleştireceğimiz konusunda
    # yardımcı olacak.
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Bu döngüde gelen listenin son elemanından başlayarak kontrol ettiğimiz basamak
    # değerini(rakamını) indis olarak alırız. daha sonra cout dizisinde bu indisin 
    # değerini alırız. output listesinin bu değerin 1 eksik indisine kontrol ettiğimiz
    # sayıyı ekleriz ve bu konuma başka değer gelmesin diye 1 eksiltiriz.
    # Bu uygulamayı son basamaklara yaptığımızda listemiz sıralanmış olacaktır.
    i = liste_uzunluk - 1
    while i >= 0:
        index = int(gelen_liste[i] / gelen_basamak)
        output[count[index % 10]-1] = gelen_liste[i]
        count[index % 10] -= 1
        i -= 1
 
    # Burada gelen listeyi boşaltıp içine o anki basamak değerine göre
    # sıralanmış listeyi attık.
    gelen_liste.clear()
    gelen_liste.extend(output)
 
    # Radixsort fonksiyonu
def radixSort(gelen_liste, baslangic_basamagi): 
    # Maksimum sayıyı buluyoruz.(Hangi basamağa kadar sıralama 
    # yapacağımızı bilmek için gerekli(örneğin bu sayı 100.0 ise algoritma,
    #baslangic_basamagindan  100ler 
    # basamağına kadar sıralama yapacaktır.))
    max1 = max(gelen_liste)
    basamak = baslangic_basamagi
    while max1 /basamak>= 1:
        countingSort(gelen_liste, basamak)
        basamak *= 10
 
    # Öncelikle Virgülden sonraki basamak sayısı en uzun olan elemanı buluyoruz. 
    # Bu uzunluğu kullanarak sıralamaya başlanacak olan en değersiz basamağı döndürüyoruz.
def baslangicBasamagiTespit(gelen_liste):                                        
    max_uzunluk = 0
    for sayi in gelen_liste:
        stringsayi=(str(sayi))
        ondalikkonum=stringsayi.find(".")
        aktif_uzunluk = (len(stringsayi)-ondalikkonum-1)
        if (aktif_uzunluk> max_uzunluk):
            max_uzunluk = aktif_uzunluk
    baslangic_basamagi = 10 ** (- max_uzunluk)
    return baslangic_basamagi

    
# Dosyadan okuma işlemleri   
liste100k=dosyaokuma('100000likliste.txt')
liste100=dosyaokuma('100lükliste.txt')
liste10=dosyaokuma('10lukliste.txt')

# Zaman hesaplama ve radix sort  işlemleri
start_time=datetime.now()
radixSort(liste100k,baslangicBasamagiTespit(liste100k))
time_elapsed = datetime.now() - start_time 
print('Geçen süre (hh:mm:ss.ms) {}'.format(time_elapsed))

start_time=datetime.now()
radixSort(liste100,baslangicBasamagiTespit(liste100))
time_elapsed = datetime.now() - start_time 
print('Geçen süre (hh:mm:ss.ms) {}'.format(time_elapsed))

start_time=datetime.now()
radixSort(liste10,baslangicBasamagiTespit(liste10))
time_elapsed = datetime.now() - start_time 
print('Geçen süre (hh:mm:ss.ms) {}'.format(time_elapsed))

# Sıralanmış listeleri yazdırma
print(liste10)
print(liste100)
"""print(liste100k)"""





         








         


