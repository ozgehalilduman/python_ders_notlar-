# Python 7. Hafta
**Listeler (Lists)**

---

## 📚 Öğrenme Hedefleri
- Liste kavramı ve kullanımı
- Liste oluşturma yöntemleri
- Liste indexleme ve slicing
- Liste metodları (append, remove, pop, insert, sort, vb.)
- Liste ile döngüler
- İç içe listeler (2D listeler)
- Liste comprehension (liste oluşturma)
- Listeler ile pratik uygulamalar

---

## 🎓 ÖNEMLİ BİLGİLENDİRMELER

### 1️⃣ LİSTE NEDİR?

Liste, birden fazla değeri tek bir değişkende saklamamızı sağlayan veri yapısıdır. **Sıralıdır, değiştirilebilir (mutable) ve farklı veri tiplerini içerebilir.**

**Neden Liste Kullanırız?**
```python
# Liste OLMADAN ❌ (kötü yöntem)
ogrenci1 = "Ahmet"
ogrenci2 = "Mehmet"
ogrenci3 = "Ayşe"
ogrenci4 = "Fatma"
ogrenci5 = "Ali"

# Liste ile ✅ (iyi yöntem)
ogrenciler = ["Ahmet", "Mehmet", "Ayşe", "Fatma", "Ali"]
```

---

### 2️⃣ LİSTE OLUŞTURMA

#### **Boş Liste:**
```python
# Yöntem 1: Köşeli parantez
liste1 = []

# Yöntem 2: list() fonksiyonu
liste2 = list()
```

#### **Değerlerle Liste:**
```python
# Sayılar
sayilar = [1, 2, 3, 4, 5]

# String'ler
isimler = ["Ali", "Veli", "Ayşe"]

# Karışık tipler
karisik = [1, "Merhaba", 3.14, True]

# Çok satırlı (okunabilir)
meyveler = [
    "elma",
    "armut",
    "muz",
    "çilek"
]
```

---

### 3️⃣ LİSTE İNDEXLEME VE ERİŞİM

Listeler **0'dan** başlar!

```python
meyveler = ["elma", "armut", "muz", "çilek"]

# Pozitif indexleme
print(meyveler[0])   # elma (ilk eleman)
print(meyveler[1])   # armut
print(meyveler[3])   # çilek (son eleman)

# Negatif indexleme (sondan başlar)
print(meyveler[-1])  # çilek (son eleman)
print(meyveler[-2])  # muz (sondan 2.)

# Index numaraları:
# "elma"  "armut"  "muz"  "çilek"
#   0       1       2       3      (pozitif)
#  -4      -3      -2      -1      (negatif)
```

⚠️ **DİKKAT:** Olmayan indexe erişmeye çalışırsanız hata alırsınız!
```python
meyveler = ["elma", "armut"]
# print(meyveler[5])  # IndexError!
```

---

### 4️⃣ LİSTE SLİCİNG (DİLİMLEME)

```python
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [başlangıç:bitiş] - bitiş dahil değil!
print(sayilar[2:5])     # [2, 3, 4]
print(sayilar[:5])      # [0, 1, 2, 3, 4] (baştan)
print(sayilar[5:])      # [5, 6, 7, 8, 9] (sonuna kadar)
print(sayilar[-3:])     # [7, 8, 9] (son 3 eleman)

# [başlangıç:bitiş:adım]
print(sayilar[::2])     # [0, 2, 4, 6, 8] (2'şer atla)
print(sayilar[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (ters)
```

---

### 5️⃣ LİSTE UZUNLUĞU - len()

```python
meyveler = ["elma", "armut", "muz"]
print(len(meyveler))  # 3

# Pratik kullanım
if len(meyveler) > 0:
    print("Liste boş değil")
```

---

### 6️⃣ LİSTE DEĞİŞTİRME

Listeler **mutable** (değiştirilebilir):

```python
meyveler = ["elma", "armut", "muz"]

# Tek eleman değiştirme
meyveler[1] = "çilek"
print(meyveler)  # ["elma", "çilek", "muz"]

# Çoklu eleman değiştirme
meyveler[0:2] = ["portakal", "kivi"]
print(meyveler)  # ["portakal", "kivi", "muz"]
```

---

### 7️⃣ LİSTE METODLARI

#### **append() - Sona Ekleme**
```python
meyveler = ["elma", "armut"]
meyveler.append("muz")
print(meyveler)  # ["elma", "armut", "muz"]

# Döngü ile çoklu ekleme
for i in range(1, 4):
    meyveler.append(i)
# ["elma", "armut", "muz", 1, 2, 3]
```

#### **insert() - Belirli Konuma Ekleme**
```python
meyveler = ["elma", "muz"]
meyveler.insert(1, "armut")  # 1. indexe ekle
print(meyveler)  # ["elma", "armut", "muz"]
```

#### **remove() - Değer ile Silme**
```python
meyveler = ["elma", "armut", "muz"]
meyveler.remove("armut")  # İlk bulduğunu siler
print(meyveler)  # ["elma", "muz"]

# Yoksa hata verir!
# meyveler.remove("çilek")  # ValueError!
```

#### **pop() - Index ile Silme ve Döndürme**
```python
meyveler = ["elma", "armut", "muz"]

# Son elemanı sil ve döndür
son = meyveler.pop()
print(son)       # "muz"
print(meyveler)  # ["elma", "armut"]

# Belirli indexi sil
ilk = meyveler.pop(0)
print(ilk)       # "elma"
print(meyveler)  # ["armut"]
```

#### **clear() - Tüm Elemanları Sil**
```python
meyveler = ["elma", "armut", "muz"]
meyveler.clear()
print(meyveler)  # []
```

#### **sort() - Sıralama**
```python
sayilar = [3, 1, 4, 1, 5, 9, 2]
sayilar.sort()  # Küçükten büyüğe
print(sayilar)  # [1, 1, 2, 3, 4, 5, 9]

sayilar.sort(reverse=True)  # Büyükten küçüğe
print(sayilar)  # [9, 5, 4, 3, 2, 1, 1]

# String sıralama
isimler = ["Zeynep", "Ahmet", "Mehmet"]
isimler.sort()
print(isimler)  # ["Ahmet", "Mehmet", "Zeynep"]
```

#### **reverse() - Ters Çevirme**
```python
sayilar = [1, 2, 3, 4, 5]
sayilar.reverse()
print(sayilar)  # [5, 4, 3, 2, 1]
```

#### **count() - Sayma**
```python
sayilar = [1, 2, 2, 3, 2, 4]
print(sayilar.count(2))  # 3 (2 sayısı 3 kere var)
```

#### **index() - Değerin Konumunu Bulma**
```python
meyveler = ["elma", "armut", "muz"]
print(meyveler.index("armut"))  # 1

# Yoksa hata verir!
# print(meyveler.index("çilek"))  # ValueError!
```

#### **extend() - Liste Birleştirme**
```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste1.extend(liste2)
print(liste1)  # [1, 2, 3, 4, 5, 6]

# Alternatif: + operatörü
liste3 = liste1 + liste2
```

---

### 8️⃣ LİSTE İLE DÖNGÜLER

#### **for ile Liste Elemanları Üzerinde Gezme**
```python
meyveler = ["elma", "armut", "muz"]

# Yöntem 1: Direkt eleman
for meyve in meyveler:
    print(meyve)

# Yöntem 2: Index ile
for i in range(len(meyveler)):
    print(f"{i}: {meyveler[i]}")

# Yöntem 3: enumerate ile (en pratik)
for index, meyve in enumerate(meyveler):
    print(f"{index}: {meyve}")
```

#### **Liste Oluşturma (Döngü ile)**
```python
# 1-10 arası sayılar
sayilar = []
for i in range(1, 11):
    sayilar.append(i)
print(sayilar)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Kareler
kareler = []
for i in range(1, 6):
    kareler.append(i ** 2)
print(kareler)  # [1, 4, 9, 16, 25]
```

---

### 9️⃣ LİSTE COMPREHENSİON (KISA YÖNTEM)

Liste oluşturmanın kısa yolu:

```python
# Normal yöntem
sayilar = []
for i in range(1, 11):
    sayilar.append(i)

# List comprehension (tek satır!)
sayilar = [i for i in range(1, 11)]
print(sayilar)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Kareler
kareler = [i**2 for i in range(1, 6)]
print(kareler)  # [1, 4, 9, 16, 25]

# Koşullu (çift sayılar)
ciftler = [i for i in range(1, 11) if i % 2 == 0]
print(ciftler)  # [2, 4, 6, 8, 10]
```

---

### 🔟 İÇ İÇE LİSTELER (2D LİSTELER)

```python
# 2D Liste (Matrix)
matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Erişim
print(matris[0])      # [1, 2, 3] (ilk satır)
print(matris[0][0])   # 1 (ilk satır, ilk sütun)
print(matris[1][2])   # 6 (2. satır, 3. sütun)

# İç içe döngü ile gezme
for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
    print()
```

---

### 1️⃣1️⃣ LİSTE KOPYALAMA

⚠️ **DİKKAT:** Basit atama referans kopyalar!

```python
# YANLIŞ YÖNTEM ❌
liste1 = [1, 2, 3]
liste2 = liste1  # Referans kopyalama!
liste2.append(4)
print(liste1)  # [1, 2, 3, 4] (değişti!)

# DOĞRU YÖNTEM 1 ✅
liste1 = [1, 2, 3]
liste2 = liste1.copy()
liste2.append(4)
print(liste1)  # [1, 2, 3] (değişmedi)

# DOĞRU YÖNTEM 2 ✅
liste2 = liste1[:]  # Slicing ile kopyalama

# DOĞRU YÖNTEM 3 ✅
liste2 = list(liste1)
```

---

### 1️⃣2️⃣ PRATİK ÖRNEKLER

#### **Maksimum ve Minimum Bulma**
```python
sayilar = [45, 23, 67, 89, 12, 34]

# Hazır fonksiyonlar
print(max(sayilar))  # 89
print(min(sayilar))  # 12
print(sum(sayilar))  # 270

# Manuel bulma (döngü ile)
en_buyuk = sayilar[0]
for sayi in sayilar:
    if sayi > en_buyuk:
        en_buyuk = sayi
print(en_buyuk)  # 89
```

#### **Liste İçinde Arama**
```python
meyveler = ["elma", "armut", "muz"]

# in operatörü
if "armut" in meyveler:
    print("Armut listede var")

# Yoksa kontrolü
if "çilek" not in meyveler:
    print("Çilek listede yok")
```

#### **Liste Birleştirme**
```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# + operatörü
birlesik = liste1 + liste2
print(birlesik)  # [1, 2, 3, 4, 5, 6]

# extend metodu
liste1.extend(liste2)
print(liste1)  # [1, 2, 3, 4, 5, 6]
```

---

### 1️⃣3️⃣ YAYGIN HATALAR VE ÇÖZÜMLER

#### **Hata 1: Index Hatası**
```python
# YANLIŞ ❌
liste = [1, 2, 3]
# print(liste[5])  # IndexError!

# DOĞRU ✅
if len(liste) > 5:
    print(liste[5])
else:
    print("Index dışında!")
```

#### **Hata 2: Döngüde Liste Değiştirme**
```python
# YANLIŞ ❌ (sorunlu)
sayilar = [1, 2, 3, 4, 5]
for sayi in sayilar:
    sayilar.remove(sayi)  # Döngü bozulur!

# DOĞRU ✅
sayilar = [1, 2, 3, 4, 5]
sayilar.clear()  # Hepsini sil

# VEYA
sayilar = [1, 2, 3, 4, 5]
sayilar = []  # Yeni boş liste
```

#### **Hata 3: append vs extend**
```python
liste = [1, 2, 3]

# append - tek eleman ekler
liste.append([4, 5])
print(liste)  # [1, 2, 3, [4, 5]] (iç içe!)

# extend - listeyi genişletir
liste = [1, 2, 3]
liste.extend([4, 5])
print(liste)  # [1, 2, 3, 4, 5]
```

---

## 📝 SORULAR

### ⭐ Kolay Seviye (1-15)

#### ✅ Soru 1: Liste Oluşturma
5 adet meyve ismi içeren liste oluşturun ve ekrana yazdırın.

---

#### ✅ Soru 2: Liste Elemanına Erişim
Bir sayı listesi oluşturun, ilk ve son elemanı yazdırın.

---

#### ✅ Soru 3: Liste Uzunluğu
Kullanıcıdan 5 isim alın, listeye ekleyin ve kaç eleman olduğunu gösterin.

---

#### ✅ Soru 4: append() Kullanımı
Boş liste oluşturun, döngü ile 1-10 arası sayıları ekleyin.

---

#### ✅ Soru 5: for ile Liste Yazdırma
Bir liste oluşturun, her elemanı alt alta yazdırın.

---

#### ✅ Soru 6: Liste İçinde Arama
Bir isim listesi oluşturun, kullanıcıdan isim isteyin, listede var mı kontrol edin.

---

#### ✅ Soru 7: remove() Kullanımı
Bir liste oluşturun, kullanıcıdan silinecek elemanı isteyin ve silin.

---

#### ✅ Soru 8: Liste Toplam
Sayı listesi oluşturun, tüm elemanların toplamını hesaplayın.

---

#### ✅ Soru 9: Liste Ortalaması
Kullanıcıdan 5 not alın, listeye ekleyin, ortalamasını hesaplayın.

---

#### ✅ Soru 10: Liste Ters Çevirme
Bir liste oluşturun, reverse() ile ters çevirin.

---

#### ✅ Soru 11: Liste Sıralama
Karışık sayı listesi oluşturun, sort() ile sıralayın.

---

#### ✅ Soru 12: Liste Kopyalama
Bir liste oluşturun, kopyasını alın, kopyaya eleman ekleyin, orijinali gösterin.

---

#### ✅ Soru 13: Liste Birleştirme
İki liste oluşturun, + ile birleştirin.

---

#### ✅ Soru 14: Liste Slicing
10 elemanlı liste oluşturun, ilk 5'ini ve son 3'ünü yazdırın.

---

#### ✅ Soru 15: count() Kullanımı
Bir listede belirli elemanın kaç kere geçtiğini bulun.

---

### 🌟 Orta Seviye (16-30)

#### ✅ Soru 16: En Büyük ve En Küçük
Sayı listesinde max() ve min() kullanmadan en büyük ve küçüğü bulun.

---

#### ✅ Soru 17: Çift Sayıları Filtrele
Bir listeden sadece çift sayıları yeni listeye aktarın.

---

#### ✅ Soru 18: Liste Elemanlarını Çarpma
Bir listedeki tüm sayıları 2 ile çarpıp yeni liste oluşturun.

---

#### ✅ Soru 19: Tekrar Eden Elemanları Silme
Bir listeden tekrar eden elemanları kaldırıp yeni liste oluşturun.

---

#### ✅ Soru 20: Liste Karşılaştırma
İki liste oluşturun, ortak elemanları bulun.

---

#### ✅ Soru 21: Liste Comprehension
List comprehension ile 1-20 arası çift sayılar listesi oluşturun.

---

#### ✅ Soru 22: İç İçe Liste
3x3 matris oluşturun, tüm elemanları yazdırın.

---

#### ✅ Soru 23: Notları Kategorize Etme
Not listesi alın, 50+ "Geçti", altı "Kaldı" olarak kategorize edin.

---

#### ✅ Soru 24: Liste İstatistikleri
Sayı listesi için toplam, ortalama, max, min değerleri gösterin.

---

#### ✅ Soru 25: Kelime Uzunlukları
Kelime listesi alın, her kelimenin uzunluğunu yeni listeye ekleyin.

---

#### ✅ Soru 26: Liste Elemanlarını Değiştirme
Bir listede negatif sayıları 0 yapın.

---

#### ✅ Soru 27: Sıralı Ekleme
Sıralı bir listeye yeni eleman eklerken sırayı bozmayin.

---

#### ✅ Soru 28: Liste İndex Bulma
Bir değerin listede kaçıncı sırada olduğunu bulun (tüm konumları).

---

#### ✅ Soru 29: İki Liste Senkronizasyonu
İki listeyi zipleyerek dictionary oluşturun.

---

#### ✅ Soru 30: Liste Döndürme
Listeyi N pozisyon sağa veya sola kaydırın.

---

### 🎯 İleri Seviye (31-40)

#### ✅ Soru 31: Fibonacci Listesi
İlk 20 Fibonacci sayısını liste olarak oluşturun.

---

#### ✅ Soru 32: Asal Sayılar Listesi
1-100 arası asal sayıları liste olarak bulun.

---

#### ✅ Soru 33: Liste Permütasyonları
Bir listenin tüm permütasyonlarını bulun (3 elemanlı).

---

#### ✅ Soru 34: Matris Toplama
İki 2D matrisi toplayın.

---

#### ✅ Soru 35: En Uzun Alt Dizi
Bir listede ardışık artan en uzun diziyi bulun.

---

#### ✅ Soru 36: Liste ile Stack (Yığın)
Liste kullanarak stack (push, pop) işlemleri yapın.

---

#### ✅ Soru 37: Liste ile Queue (Kuyruk)
Liste kullanarak queue (enqueue, dequeue) işlemleri yapın.

---

#### ✅ Soru 38: İkili Arama
Sıralı listede binary search uygulayın.

---

#### ✅ Soru 39: Liste Düzleştirme
İç içe listeyi tek düze liste haline getirin.

---

#### ✅ Soru 40: Histogram Çizme
Sayı listesinden basit histogram çizin (*'larla).

---

## 💡 BONUS: Liste İpuçları

### En Sık Kullanılan İşlemler:
```python
# Oluşturma
liste = [1, 2, 3]

# Ekleme
liste.append(4)       # Sona ekle
liste.insert(0, 0)    # Başa ekle

# Silme
liste.remove(2)       # Değer ile sil
liste.pop()          # Son elemanı sil
liste.pop(0)         # İlk elemanı sil

# Arama
"elma" in liste      # Var mı?
liste.index("elma")  # Nerede?
liste.count("elma")  # Kaç tane?

# Sıralama
liste.sort()         # Sırala
liste.reverse()      # Ters çevir

# Diğer
len(liste)           # Uzunluk
sum(liste)           # Toplam (sayılar için)
max(liste)           # En büyük
min(liste)           # En küçük
```

---

**Başarılar! 🚀**