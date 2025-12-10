# Python 6. Hafta
**Döngüler - while Döngüsü**

---

## 📚 Öğrenme Hedefleri
- while döngüsü kavramı ve kullanımı
- while vs for farkları
- Sonsuz döngüler ve nasıl önlenir
- break ve continue ile while kullanımı
- Kullanıcı kontrolü ile döngüler
- Sayaç ve bayrak (flag) değişkenleri
- İç içe while döngüleri
- Döngü ile veri doğrulama

---

## 🎓 ÖNEMLİ BİLGİLENDİRMELER

### 1️⃣ WHILE DÖNGÜSÜ NEDİR?

while döngüsü, bir koşul **True** olduğu sürece çalışmaya devam eden döngü türüdür.

**Temel Yapı:**
```python
while koşul:
    # Koşul True olduğu sürece çalışır
    # Kodlar buraya yazılır
```

**Basit Örnek:**
```python
sayac = 1

while sayac <= 5:
    print(sayac)
    sayac += 1  # sayac = sayac + 1

# Çıktı: 1, 2, 3, 4, 5
```

---

### 2️⃣ WHILE vs FOR FARKI

#### **for Döngüsü:**
- Kaç kere döneceği **önceden belli**
- Genellikle belirli bir aralık için
- Liste, string gibi koleksiyonlar için ideal

```python
# for örneği
for i in range(5):
    print(i)
```

#### **while Döngüsü:**
- Kaç kere döneceği **belirsiz**
- Bir koşul sağlandığı sürece
- Kullanıcı girişi, oyunlar için ideal

```python
# while örneği
devam = "evet"
while devam == "evet":
    print("Çalışıyor...")
    devam = input("Devam? (evet/hayır): ")
```

---

### 3️⃣ WHILE DÖNGÜSÜ TEMEL KULLANIM

#### **Sayaç ile While:**
```python
sayac = 0

while sayac < 5:
    print(f"Sayaç: {sayac}")
    sayac += 1

print("Döngü bitti!")
```

#### **Kullanıcı Kontrolü ile While:**
```python
sifre = ""

while sifre != "python":
    sifre = input("Şifre girin: ")
    
print("Giriş başarılı!")
```

#### **Bayrak (Flag) Değişkeni ile:**
```python
devam_et = True

while devam_et:
    islem = input("İşlem yap (çıkış için 'q'): ")
    
    if islem == "q":
        devam_et = False
    else:
        print("İşlem yapılıyor...")

print("Program sonlandı")
```

---

### 4️⃣ SONSUZ DÖNGÜLER VE ÖNLEME

⚠️ **TEHLİKE:** Koşul hiçbir zaman False olmazsa sonsuz döngü oluşur!

#### **Yanlış Kullanım (Sonsuz Döngü):**
```python
# YANLIŞ - SONSUZ DÖNGÜ! ❌
sayac = 0
while sayac < 5:
    print(sayac)
    # sayac artırılmadı! Hep 0 kalır!
```

#### **Doğru Kullanım:**
```python
# DOĞRU ✅
sayac = 0
while sayac < 5:
    print(sayac)
    sayac += 1  # Mutlaka artırılmalı!
```

#### **İsteyerek Sonsuz Döngü (while True):**
```python
while True:
    cevap = input("Çıkmak için 'q' yazın: ")
    
    if cevap == "q":
        break  # Döngüden çık
    
    print("Devam ediliyor...")
```

---

### 5️⃣ BREAK ve CONTINUE İLE WHILE

#### **break - Döngüyü Sonlandırır:**
```python
sayac = 1

while sayac <= 10:
    print(sayac)
    
    if sayac == 5:
        print("5'te durdu!")
        break
    
    sayac += 1

# Çıktı: 1, 2, 3, 4, 5
```

#### **continue - O Adımı Atlar:**
```python
sayac = 0

while sayac < 5:
    sayac += 1
    
    if sayac == 3:
        continue  # 3'ü atla
    
    print(sayac)

# Çıktı: 1, 2, 4, 5 (3 yok)
```

---

### 6️⃣ KULLANICI GİRİŞİ İLE DÖNGÜLER

#### **Menü Sistemi:**
```python
while True:
    print("\n--- MENÜ ---")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çıkış")
    
    secim = input("Seçim: ")
    
    if secim == "1":
        print("Toplama işlemi")
    elif secim == "2":
        print("Çıkarma işlemi")
    elif secim == "3":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim!")
```

#### **Veri Doğrulama:**
```python
yas = -1

while yas < 0 or yas > 120:
    yas = int(input("Yaşınızı girin (0-120): "))
    
    if yas < 0 or yas > 120:
        print("Geçersiz yaş! Tekrar deneyin.")

print(f"Yaşınız: {yas}")
```

---

### 7️⃣ SAYAÇ VE TOPLAMA İŞLEMLERİ

#### **Toplam Hesaplama:**
```python
toplam = 0
sayac = 1

while sayac <= 10:
    toplam += sayac
    sayac += 1

print(f"1-10 arası toplam: {toplam}")  # 55
```

#### **Ortalama Hesaplama:**
```python
toplam = 0
adet = 0

while True:
    sayi = int(input("Sayı girin (0 için çıkış): "))
    
    if sayi == 0:
        break
    
    toplam += sayi
    adet += 1

if adet > 0:
    ortalama = toplam / adet
    print(f"Ortalama: {ortalama}")
else:
    print("Hiç sayı girilmedi!")
```

---

### 8️⃣ TAHMIN OYUNLARI

#### **Sayı Tahmin Oyunu:**
```python
import random

gizli_sayi = random.randint(1, 100)
tahmin_hakki = 5

while tahmin_hakki > 0:
    tahmin = int(input("Tahmin (1-100): "))
    
    if tahmin == gizli_sayi:
        print("🎉 Tebrikler! Doğru tahmin!")
        break
    elif tahmin < gizli_sayi:
        print("⬆️  Daha büyük bir sayı")
    else:
        print("⬇️  Daha küçük bir sayı")
    
    tahmin_hakki -= 1
    print(f"Kalan hak: {tahmin_hakki}")

if tahmin_hakki == 0:
    print(f"😢 Oyun bitti! Sayı: {gizli_sayi}")
```

---

### 9️⃣ İÇ İÇE WHILE DÖNGÜLERI

```python
satir = 1

while satir <= 3:
    sutun = 1
    
    while sutun <= 3:
        print(f"({satir},{sutun})", end=" ")
        sutun += 1
    
    print()  # Yeni satır
    satir += 1

# Çıktı:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)
```

---

### 🔟 DO-WHILE YAPISI (Python'da Yok Ama Benzer)

Python'da do-while yoktur ama benzerini yapabiliriz:

```python
# İlk kontrolden önce en az 1 kere çalışır
while True:
    sifre = input("Şifre: ")
    
    if sifre == "python":
        break
    
    print("Yanlış şifre!")

print("Giriş başarılı!")
```

---

### 1️⃣1️⃣ YAYGIN HATALAR VE ÇÖZÜMLER

#### **Hata 1: Sonsuz Döngü**
```python
# YANLIŞ ❌
x = 0
while x < 5:
    print(x)
    # x artırılmadı!

# DOĞRU ✅
x = 0
while x < 5:
    print(x)
    x += 1
```

#### **Hata 2: Yanlış Koşul**
```python
# YANLIŞ ❌
sayi = 10
while sayi > 0:
    print(sayi)
    sayi += 1  # Hep büyüyor, hiç bitmez!

# DOĞRU ✅
sayi = 10
while sayi > 0:
    print(sayi)
    sayi -= 1  # Küçültülmeli
```

#### **Hata 3: Girinti Hatası**
```python
# YANLIŞ ❌
x = 0
while x < 5:
print(x)  # Girinti yok!
x += 1

# DOĞRU ✅
x = 0
while x < 5:
    print(x)
    x += 1
```

---

### 1️⃣2️⃣ PRATİK İPUÇLARI

```python
# 1. Sonsuz döngüden kaçınmak için hep çıkış yolu bırakın
while True:
    # ... kodlar ...
    if cikis_kosulu:
        break

# 2. Sayaç kullanıyorsanız mutlaka güncelleyin
sayac = 0
while sayac < 10:
    print(sayac)
    sayac += 1  # UNUTMAYIN!

# 3. Kullanıcı girdisi ile çalışırken doğrulama yapın
while True:
    try:
        sayi = int(input("Sayı: "))
        break  # Geçerli giriş, çık
    except ValueError:
        print("Geçersiz sayı!")

# 4. Bayrak değişkeni kullanın
bitti = False
while not bitti:
    # ... işlemler ...
    if kosul:
        bitti = True

# 5. İç içe döngülerde dikkatli olun
# Her döngünün kendi sayacı olmalı
```

---

### 1️⃣3️⃣ WHILE vs FOR KARŞILAŞTIRMASI

| Özellik | while | for |
|---------|-------|-----|
| Tekrar sayısı | Belirsiz | Belirli |
| Koşul kontrolü | Her turda | Başlangıçta |
| Kullanım alanı | Kullanıcı girdisi, oyunlar | Listeler, aralıklar |
| Sonsuz döngü riski | Yüksek | Düşük |
| Okunabilirlik | Daha az | Daha fazla |

**Ne Zaman while Kullanmalı?**
- ✅ Kullanıcı "dur" diyene kadar
- ✅ Oyun döngüleri
- ✅ Sunucu dinleme
- ✅ Doğru giriş alınana kadar

**Ne Zaman for Kullanmalı?**
- ✅ 1-100 arası sayılar
- ✅ Liste elemanları
- ✅ String karakterleri
- ✅ Belirli tekrar sayısı

---

## 📝 SORULAR

### ⭐ Kolay Seviye (1-15)

#### ✅ Soru 1: 1'den 10'a Sayma
while döngüsü ile 1'den 10'a kadar sayın.

---

#### ✅ Soru 2: Şifre Kontrolü
Kullanıcıdan şifre isteyin, "1234" girilene kadar tekrar isteyin.

---

#### ✅ Soru 3: 5 Kere Merhaba
"Merhaba" kelimesini 5 kere yazdırın (while ile).

---

#### ✅ Soru 4: Pozitif Sayı Alma
Kullanıcıdan pozitif sayı isteyin, negatif girilirse tekrar isteyin.

---

#### ✅ Soru 5: Geri Sayım
10'dan 1'e kadar geri sayım yapın (while ile).

---

#### ✅ Soru 6: Toplam 100'e Ulaşma
0'dan başlayıp 10'ar 10'ar artırarak 100'e kadar sayıları yazdırın.

---

#### ✅ Soru 7: Kullanıcı Adı Kontrolü
"admin" girilene kadar kullanıcı adı isteyin.

---

#### ✅ Soru 8: Tek Sayılar
1'den 20'ye kadar sadece tek sayıları yazdırın (while ile).

---

#### ✅ Soru 9: Devam Etme Kontrolü
Her turda kullanıcıya "Devam? (e/h)" sorun, "h" girilene kadar devam edin.

---

#### ✅ Soru 10: Sayı Toplama
Kullanıcıdan sayılar alın, toplam 50'yi geçince durun.

---

#### ✅ Soru 11: Basit Menü
1-Merhaba, 2-Hoşça kal, 3-Çıkış menüsü yapın.

---

#### ✅ Soru 12: 5'in Katları
5'in katlarını 50'ye kadar yazdırın (while ile).

---

#### ✅ Soru 13: Yaş Doğrulama
0-120 arası geçerli yaş girilene kadar isteyin.

---

#### ✅ Soru 14: Evet/Hayır Kontrolü
"evet" veya "hayır" girilene kadar tekrar isteyin.

---

#### ✅ Soru 15: 10 Sayı Toplama
Kullanıcıdan 10 sayı alın, toplamını gösterin (while ile).

---

### 🌟 Orta Seviye (16-30)

#### ✅ Soru 16: Ortalama Hesaplama
Kullanıcıdan sayılar alın (0 girilene kadar), ortalamasını hesaplayın.

---

#### ✅ Soru 17: En Büyük Sayı Bulma
Kullanıcıdan sayılar alın (-1 girilene kadar), en büyüğünü bulun.

---

#### ✅ Soru 18: Çift ve Tek Sayma
1-50 arası kaç tane çift, kaç tane tek olduğunu bulun (while ile).

---

#### ✅ Soru 19: Faktöriyel (while ile)
Kullanıcıdan sayı alın, faktöriyelini while ile hesaplayın.

---

#### ✅ Soru 20: Fibonacci (while ile)
İlk 10 Fibonacci sayısını while ile yazdırın.

---

#### ✅ Soru 21: ATM Simülasyonu
Başlangıç bakiye 1000 TL. Kullanıcı para çekebilir/yatırabilir. Bakiye 0 olunca veya "çıkış" denilince dursun.

---

#### ✅ Soru 22: Sayı Tahmin Oyunu
1-100 arası rastgele sayıyı bulana kadar tahmin ettirin.

---

#### ✅ Soru 23: Kullanıcı Girişi (3 Deneme)
Şifre için 3 deneme hakkı verin.

---

#### ✅ Soru 24: Çarpım Tablosu (while ile)
Kullanıcıdan sayı alın, çarpım tablosunu while ile gösterin.

---

#### ✅ Soru 25: Pozitif Sayı Toplama
Kullanıcıdan sayılar alın, negatif girilene kadar pozitif olanları toplayın.

---

#### ✅ Soru 26: Basamak Sayma
Bir sayının kaç basamaklı olduğunu while ile bulun.

---

#### ✅ Soru 27: Asal Sayı Kontrolü (while ile)
Kullanıcıdan sayı alın, asal mı değil mi kontrol edin (while ile).

---

#### ✅ Soru 28: İç İçe Menü
Ana menü ve alt menüler olan bir sistem yapın.

---

#### ✅ Soru 29: Liste Oluşturma
Kullanıcıdan kelimeler alın ("stop" girilene kadar), listeye ekleyin.

---

#### ✅ Soru 30: Mükemmel Sayı Bulma
1-1000 arası mükemmel sayıları bulun (while ile).

---

### 🎯 İleri Seviye (31-40)

#### ✅ Soru 31: Hesap Makinesi (Sürekli)
4 işlem yapan, kullanıcı "q" diyene kadar çalışan hesap makinesi.

---

#### ✅ Soru 32: Collatz Sanısı (while ile)
Bir sayı 1'e ulaşana kadar Collatz işlemini uygulayın.

---

#### ✅ Soru 33: EBOB Bulma (while ile)
İki sayının EBOB'unu Öklid algoritması ile bulun.

---

#### ✅ Soru 34: Dijital Kök
Bir sayının basamakları toplamının tek basamak kalana kadar toplamını alın.

---

#### ✅ Soru 35: To-Do List Uygulaması
Görev ekleme, silme, listeleme menüsü yapın.

---

#### ✅ Soru 36: Sayı Tabanı Dönüştürme
Ondalık sayıyı ikili sisteme çevirin (while ile).

---

#### ✅ Soru 37: Armstrong Sayıları (1-1000)
1-1000 arası tüm Armstrong sayılarını bulun (while ile).

---

#### ✅ Soru 38: Kelime Oyunu
Kullanıcıdan kelime alın, son harfle başlayan kelime isteyin, tekrar eden kelime girilince oyun bitsin.

---

#### ✅ Soru 39: Mini Quiz Uygulaması
Sorular sorun, cevap alın, doğru/yanlış sayısını tutun.

---

#### ✅ Soru 40: Basit Dosya Okuma Simülasyonu
Kullanıcıdan satır satır metin alın, "kaydet" denilince tüm metni gösterin.

---

## 💡 BONUS: FOR vs WHILE DÖNÜŞÜMÜ

Aynı işi iki şekilde yapma:

```python
# FOR ile
for i in range(1, 6):
    print(i)

# WHILE ile
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

**Başarılar! 🚀**