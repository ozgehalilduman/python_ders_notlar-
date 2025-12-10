# Python 5. Hafta
**Döngüler - for Döngüsü**

---

## 📚 Öğrenme Hedefleri
- Döngü kavramı ve önemi
- for döngüsü yapısı
- range() fonksiyonu
- String ile for döngüsü
- Liste ile for döngüsü
- İç içe (nested) for döngüleri
- break ve continue ifadeleri
- Döngü ile matematiksel işlemler

---

## 🎓 ÖNEMLİ BİLGİLENDİRMELER

### 1️⃣ DÖNGÜ NEDİR?

Döngü, bir kod bloğunu belirli bir koşul sağlandığı sürece veya belirli sayıda tekrar etmemizi sağlar.

**Neden Döngü Kullanırız?**
```python
# Döngü OLMADAN ❌ (kötü yöntem)
print("1")
print("2")
print("3")
print("4")
print("5")

# Döngü ile ✅ (iyi yöntem)
for i in range(1, 6):
    print(i)
```

---

### 2️⃣ FOR DÖNGÜSÜ TEMEL YAPISI

```python
# Basit for döngüsü
for i in range(5):
    print(i)

# Çıktı:
# 0
# 1
# 2
# 3
# 4
```

**Syntax (Sözdizimi):**
```python
for değişken in aralık/koleksiyon:
    # Tekrar edilecek kod
    # Girintili yazılmalı (4 boşluk)
```

⚠️ **ÖNEMLİ:** 
- for'dan sonra `:` (iki nokta üst üste) koymayı unutmayın
- Döngü içindeki kodlar girintili olmalı (4 boşluk)

---

### 3️⃣ range() FONKSİYONU

range() fonksiyonu sayı dizisi oluşturur.

#### **range(bitiş)** - 0'dan başlar
```python
for i in range(5):
    print(i)
# Çıktı: 0, 1, 2, 3, 4 (5 dahil değil!)
```

#### **range(başlangıç, bitiş)** - Özel başlangıç
```python
for i in range(1, 6):
    print(i)
# Çıktı: 1, 2, 3, 4, 5 (6 dahil değil!)
```

#### **range(başlangıç, bitiş, adım)** - Atlama ile
```python
# 2'şer 2'şer say
for i in range(0, 11, 2):
    print(i)
# Çıktı: 0, 2, 4, 6, 8, 10

# Geriye doğru say
for i in range(10, 0, -1):
    print(i)
# Çıktı: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

⚠️ **DİKKAT:** Bitiş değeri döngüye **dahil değildir**!
```python
range(1, 5)  # 1, 2, 3, 4 (5 yok!)
```

---

### 4️⃣ STRING İLE FOR DÖNGÜSÜ

String'in her karakteri üzerinde dolaşabiliriz.

```python
isim = "Python"

for harf in isim:
    print(harf)

# Çıktı:
# P
# y
# t
# h
# o
# n
```

**Index ile birlikte:**
```python
isim = "Python"

for i in range(len(isim)):
    print(f"{i}. karakter: {isim[i]}")

# Çıktı:
# 0. karakter: P
# 1. karakter: y
# 2. karakter: t
# ...
```

**enumerate() ile (daha pratik):**
```python
isim = "Python"

for index, harf in enumerate(isim):
    print(f"{index}: {harf}")

# Çıktı:
# 0: P
# 1: y
# 2: t
# ...
```

---

### 5️⃣ LİSTE İLE FOR DÖNGÜSÜ

```python
meyveler = ["elma", "armut", "muz", "çilek"]

for meyve in meyveler:
    print(meyve)

# Çıktı:
# elma
# armut
# muz
# çilek
```

**Index ile:**
```python
meyveler = ["elma", "armut", "muz"]

for i in range(len(meyveler)):
    print(f"{i+1}. meyve: {meyveler[i]}")

# Çıktı:
# 1. meyve: elma
# 2. meyve: armut
# 3. meyve: muz
```

---

### 6️⃣ DÖNGÜ İÇİNDE TOPLAMA VE SAYMA

```python
# Toplama
toplam = 0
for i in range(1, 11):
    toplam += i  # toplam = toplam + i
print(f"1'den 10'a kadar toplam: {toplam}")  # 55

# Sayma
cift_sayisi = 0
for i in range(1, 21):
    if i % 2 == 0:
        cift_sayisi += 1
print(f"1-20 arası çift sayı: {cift_sayisi}")  # 10
```

---

### 7️⃣ İÇ İÇE (NESTED) FOR DÖNGÜLERI

```python
# Basit örnek
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# Çıktı:
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# ...
```

**Çarpım Tablosu Örneği:**
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
    print("---")
```

**Yıldız Desenleri:**
```python
# Üçgen şekli
for i in range(1, 6):
    print("*" * i)

# Çıktı:
# *
# **
# ***
# ****
# *****
```

---

### 8️⃣ break ve continue İFADELERİ

#### **break** - Döngüyü tamamen sonlandırır
```python
for i in range(1, 11):
    if i == 5:
        break  # 5'te dur
    print(i)

# Çıktı: 1, 2, 3, 4 (5 yazdırılmaz)
```

#### **continue** - O adımı atlar, devam eder
```python
for i in range(1, 6):
    if i == 3:
        continue  # 3'ü atla
    print(i)

# Çıktı: 1, 2, 4, 5 (3 yok)
```

**Pratik Örnek:**
```python
# Tek sayıları atla, sadece çiftleri yazdır
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

# Çıktı: 2, 4, 6, 8, 10
```

---

### 9️⃣ DÖNGÜ İLE MATEMATİKSEL İŞLEMLER

```python
# Faktöriyel hesaplama (5! = 5×4×3×2×1)
sayi = 5
faktoriyel = 1

for i in range(1, sayi + 1):
    faktoriyel *= i  # faktoriyel = faktoriyel * i

print(f"{sayi}! = {faktoriyel}")  # 120

# Üslü sayı hesaplama (2^10)
taban = 2
us = 10
sonuc = 1

for i in range(us):
    sonuc *= taban

print(f"{taban}^{us} = {sonuc}")  # 1024
```

---

### 🔟 DÖNGÜ İLE STRING İŞLEMLERİ

```python
# Sesli harfleri sayma
cumle = "Python programlama"
sesli = "aeıioöuü"
sesli_sayisi = 0

for harf in cumle.lower():
    if harf in sesli:
        sesli_sayisi += 1

print(f"Sesli harf sayısı: {sesli_sayisi}")

# String ters çevirme ([::-1] olmadan)
kelime = "Python"
ters = ""

for harf in kelime:
    ters = harf + ters

print(f"Ters: {ters}")  # nohtyP
```

---

### 1️⃣1️⃣ YAYGIN HATALAR VE ÇÖZÜMLER

#### **Hata 1: İki nokta üst üste unutma**
```python
# YANLIŞ ❌
for i in range(5)
    print(i)

# DOĞRU ✅
for i in range(5):
    print(i)
```

#### **Hata 2: Girinti hatası**
```python
# YANLIŞ ❌
for i in range(5):
print(i)  # Girinti yok!

# DOĞRU ✅
for i in range(5):
    print(i)  # 4 boşluk girinti
```

#### **Hata 3: range() bitiş değeri dahil**
```python
# YANLIŞ düşünce ❌
# "1'den 5'e kadar" demek range(1, 5) değil!
for i in range(1, 5):
    print(i)  # 1, 2, 3, 4 (5 yok!)

# DOĞRU ✅
# 5'i de dahil etmek için:
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5
```

#### **Hata 4: Döngü içinde değişken değiştirme**
```python
# DİKKATLİ OLUN ⚠️
for i in range(5):
    i = 10  # Döngü değişkenini değiştirme!
    print(i)  # Her zaman 10 yazar (yanlış kullanım)
```

---

### 1️⃣2️⃣ PRATİK İPUÇLARI

```python
# 1. Kısa döngü değişkeni isimleri
for i in range(10):  # i, j, k yaygın kullanılır
    pass

# 2. Anlamlı değişken isimleri
for sayi in range(1, 11):
    print(sayi)

for ogrenci in ogrenciler:
    print(ogrenci)

# 3. Döngüden hemen çıkmak
for i in range(1000):
    if i == 10:
        break  # Performans için erken çık

# 4. Boş döngü (placeholder)
for i in range(5):
    pass  # Henüz kod yazılmadı

# 5. else ile döngü
for i in range(5):
    print(i)
else:
    print("Döngü bitti!")  # break ile çıkılmazsa çalışır
```

---

## 📝 SORULAR

### ⭐ Kolay Seviye (1-15)

#### ✅ Soru 1: 1'den 10'a Kadar Sayılar
1'den 10'a kadar (10 dahil) sayıları ekrana yazdırın.

**Beklenen Çıktı:**
```
1
2
3
...
10
```

---

#### ✅ Soru 2: İsminizi 5 Kere Yazdırma
Kullanıcıdan isim alın, 5 kere ekrana yazdırın.

---

#### ✅ Soru 3: Yıldız Çizgisi
`*` karakterini 20 kere yan yana yazdırın.

---

#### ✅ Soru 4: 0-20 Arası Çift Sayılar
0'dan 20'ye kadar sadece çift sayıları yazdırın.

---

#### ✅ Soru 5: Geri Sayım
10'dan 1'e kadar geri sayım yapın.

**Beklenen Çıktı:**
```
10
9
8
...
1
```

---

#### ✅ Soru 6: Kelime Harflerini Tek Tek Yazdırma
Kullanıcıdan kelime alın, her harfi alt alta yazdırın.

---

#### ✅ Soru 7: 1-10 Arası Toplam
1'den 10'a kadar sayıların toplamını hesaplayın.

**Beklenen Çıktı:**
```
1 + 2 + 3 + ... + 10 = 55
```

---

#### ✅ Soru 8: Çarpım Tablosu (Tek Sayı)
Kullanıcıdan bir sayı alın, o sayının 1-10 arası çarpım tablosunu gösterin.

**Örnek:** Sayı 5 ise:
```
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
```

---

#### ✅ Soru 9: Karakter Sayma
Kullanıcıdan kelime ve harf alın, harfin kelimede kaç kere geçtiğini bulun (döngü ile).

---

#### ✅ Soru 10: Tek Sayıları Toplama
1'den 50'ye kadar olan tek sayıların toplamını bulun.

---

#### ✅ Soru 11: Liste Elemanlarını Yazdırma
`["Python", "Java", "C++", "JavaScript"]` listesindeki her elemanı numaralı yazdırın.

**Beklenen Çıktı:**
```
1. Python
2. Java
3. C++
4. JavaScript
```

---

#### ✅ Soru 12: Yıldız Üçgeni
5 satırlık yıldız üçgeni çizin.

**Beklenen Çıktı:**
```
*
**
***
****
*****
```

---

#### ✅ Soru 13: Sayıların Karesi
1'den 10'a kadar sayıların karelerini gösterin.

**Örnek Çıktı:**
```
1² = 1
2² = 4
3² = 9
...
```

---

#### ✅ Soru 14: Sesli Harf Sayma (Döngü ile)
Kullanıcıdan cümle alın, sesli harf sayısını for döngüsü ile bulun.

---

#### ✅ Soru 15: 5'in Katlarını Bulma
1'den 100'e kadar 5'in katlarını yazdırın.

---

### 🌟 Orta Seviye (16-30)

#### ✅ Soru 16: Faktöriyel Hesaplama
Kullanıcıdan sayı alın, faktöriyelini hesaplayın.

**Örnek:** 5! = 5 × 4 × 3 × 2 × 1 = 120

---

#### ✅ Soru 17: Asal Sayı Kontrolü
Kullanıcıdan sayı alın, asal mı değil mi kontrol edin (döngü ile).

---

#### ✅ Soru 18: Fibonacci Serisi
İlk 10 Fibonacci sayısını yazdırın. (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

---

#### ✅ Soru 19: Mükemmel Sayı Kontrolü
Bir sayı, pozitif bölenlerinin toplamına eşitse mükemmel sayıdır.

**Örnek:** 6 = 1 + 2 + 3 (mükemmel sayı)

---

#### ✅ Soru 20: Basamak Toplamı
Kullanıcıdan sayı alın, basamaklarının toplamını bulun.

**Örnek:** 123 → 1 + 2 + 3 = 6

---

#### ✅ Soru 21: Ters Çevrilmiş Üçgen
5 satırlık ters yıldız üçgeni çizin.

**Beklenen Çıktı:**
```
*****
****
***
**
*
```

---

#### ✅ Soru 22: EBOB Bulma (En Büyük Ortak Bölen)
İki sayının EBOB'unu for döngüsü ile bulun.

---

#### ✅ Soru 23: Armstrong Sayı Kontrolü
3 basamaklı Armstrong sayı kontrolü. (153 = 1³ + 5³ + 3³)

---

#### ✅ Soru 24: Sayı Tahmin Oyunu (Sınırlı Deneme)
1-100 arası rastgele sayı, kullanıcı 5 denemede bulsun.

---

#### ✅ Soru 25: Piramit Şekli
Ortalanmış yıldız piramidi çizin.

**Beklenen Çıktı:**
```
    *
   ***
  *****
 *******
*********
```

---

#### ✅ Soru 26: Palindrome Sayı Kontrolü
Sayı tersten de aynı mı kontrol edin.

**Örnek:** 121, 12321 palindrome

---

#### ✅ Soru 27: İç İçe Döngü - Çarpım Tablosu
1-10 arası tüm çarpım tablosunu gösterin.

---

#### ✅ Soru 28: Kuvvet Hesaplama
Taban ve üs alın, üslü sayıyı döngü ile hesaplayın (** kullanmadan).

---

#### ✅ Soru 29: Kelime Analizi
Bir cümledeki en uzun kelimeyi for döngüsü ile bulun.

---

#### ✅ Soru 30: Rakam Sayma
Bir sayıdaki rakam sayısını döngü ile bulun (len kullanmadan).

---

### 🎯 İleri Seviye (31-40)

#### ✅ Soru 31: Asal Sayı Listesi
1-100 arası tüm asal sayıları bulun ve listeleyin.

---

#### ✅ Soru 32: Elmas Şekli
Yıldızlardan elmas şekli çizin.

**Beklenen Çıktı:**
```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

#### ✅ Soru 33: Collatz Sanısı
Bir sayıyla başlayın:
- Çift ise 2'ye bölün
- Tek ise 3 ile çarpıp 1 ekleyin
- 1'e ulaşana kadar devam edin

---

#### ✅ Soru 34: Pascal Üçgeni
İlk 5 satır Pascal üçgenini çizin.

---

#### ✅ Soru 35: Sayı Sistemleri Dönüştürme
Ondalık sayıyı ikili (binary) sisteme çevirin (döngü ile).

---

#### ✅ Soru 36: Matris Yazdırma
3x3 matris oluşturup yazdırın (iç içe döngü).

---

#### ✅ Soru 37: En Büyük Ortak Bölen ve En Küçük Ortak Kat
İki sayının hem EBOB hem EKOK'unu bulun.

---

#### ✅ Soru 38: Sayı Desenli Piramit
Sayılardan piramit oluşturun.

**Beklenen Çıktı:**
```
1
12
123
1234
12345
```

---

#### ✅ Soru 39: Kelime Frekansı
Bir cümledeki her kelimenin kaç kere geçtiğini bulun.

---

#### ✅ Soru 40: Mini Hesap Makinesi (Döngülü)
Kullanıcı "çıkış" yazana kadar işlem yapsın.

---

## 💡 BONUS: Algoritma Örnekleri

### 🔢 Bubble Sort (Kabarcık Sıralaması)
```python
liste = [64, 34, 25, 12, 22]
n = len(liste)

for i in range(n):
    for j in range(0, n-i-1):
        if liste[j] > liste[j+1]:
            liste[j], liste[j+1] = liste[j+1], liste[j]

print(liste)  # [12, 22, 25, 34, 64]
```

---

**Başarılar! 🚀**