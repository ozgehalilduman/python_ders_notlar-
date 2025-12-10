# Python 2. Hafta
**Veri Tipleri ve Matematiksel İşlemler**

---

## 📚 Öğrenme Hedefleri
- Veri tiplerini anlama (int, float, string, bool)
- type() fonksiyonu kullanımı
- Matematiksel operatörler (+, -, *, /, //, %, **)
- Tip dönüşümleri (int(), float(), str())
- Basit hesap makinesi projesi

---

## 🎓 ÖNEMLİ BİLGİLENDİRMELER

### 1️⃣ VERİ TİPLERİ (Data Types)

#### **int (Tam Sayı)**
```python
yas = 25
sayi = -10
sifir = 0

print(type(yas))  # <class 'int'>
```

#### **float (Ondalıklı Sayı)**
```python
fiyat = 19.99
sicaklik = -5.5
pi = 3.14

print(type(fiyat))  # <class 'float'>
```

#### **string (Metin)**
```python
isim = "Ahmet"
sehir = 'İstanbul'
mesaj = """Çok satırlı
metin yazabilirsiniz"""

print(type(isim))  # <class 'str'>
```

#### **bool (Mantıksal)**
```python
dogrumu = True
yanlismi = False

print(type(dogrumu))  # <class 'bool'>
```

---

### 2️⃣ MATEMATİKSEL OPERATÖRLER

```python
# Toplama
5 + 3  # Sonuç: 8

# Çıkarma
10 - 4  # Sonuç: 6

# Çarpma
6 * 7  # Sonuç: 42

# Bölme (sonuç her zaman float)
10 / 3  # Sonuç: 3.333...

# Tam Bölme (sadece tamsayı kısmı)
10 // 3  # Sonuç: 3

# Mod (Kalan bulma)
10 % 3  # Sonuç: 1

# Üs alma
2 ** 3  # Sonuç: 8 (2'nin 3. kuvveti)
```

---

### 3️⃣ TİP DÖNÜŞÜMLERİ (Type Conversion)

#### **int() - Tam sayıya çevirme**
```python
# String'den int'e
sayi = int("25")  # 25
print(type(sayi))  # <class 'int'>

# Float'tan int'e (ondalık kısmı atar)
sayi = int(3.99)  # 3
```

#### **float() - Ondalıklı sayıya çevirme**
```python
# String'den float'a
sayi = float("3.14")  # 3.14

# Int'ten float'a
sayi = float(5)  # 5.0
```

#### **str() - Metne çevirme**
```python
# Sayıdan string'e
metin = str(42)  # "42"
metin = str(3.14)  # "3.14"

# String birleştirmede kullanımı
yas = 25
mesaj = "Ben " + str(yas) + " yaşındayım"
```

---

### 4️⃣ INPUT İLE TİP DÖNÜŞÜMLERİ

⚠️ **ÇOK ÖNEMLİ:** input() fonksiyonu her zaman **string** döndürür!

```python
# YANLIŞ KULLANIM ❌
yas = input("Yaşınız: ")  # "25" (string)
gelecek = yas + 5  # HATA! String ile sayı toplanamaz

# DOĞRU KULLANIM ✅
yas = int(input("Yaşınız: "))  # 25 (int)
gelecek = yas + 5  # 30 (doğru çalışır)

# Float için
fiyat = float(input("Fiyat: "))  # 19.99 (float)
```

---

### 5️⃣ HATALI KULANIMLAR VE ÇÖZÜMLER

#### **Hata 1: String ile sayı toplama**
```python
# YANLIŞ ❌
sayi = "5"
toplam = sayi + 3  # TypeError!

# DOĞRU ✅
sayi = int("5")
toplam = sayi + 3  # 8
```

#### **Hata 2: Bölme işlemi karışıklığı**
```python
# Normal bölme (/) - float döner
10 / 2  # 5.0

# Tam bölme (//) - int döner
10 // 2  # 5

# Hangisini ne zaman kullanmalı?
# - Ondalıklı sonuç istiyorsanız: /
# - Sadece tam sayı istiyorsanız: //
```

#### **Hata 3: Mod operatörü yanlış anlaşılması**
```python
# % (mod) operatörü KALAN bulur, yüzde hesaplamaz!
10 % 3  # 3 (10'u 3'e böldüğünde kalan 1)

# Yüzde hesabı için:
fiyat = 100
yuzde15 = fiyat * 15 / 100  # 15.0
```

---

### 6️⃣ PRATIK İPUÇLARI

```python
# 1. İşlem önceliği (parantez kullanın)
sonuc = 5 + 3 * 2  # 11 (önce çarpma)
sonuc = (5 + 3) * 2  # 16 (parantez önce)

# 2. Çoklu atama
a, b, c = 10, 20, 30
print(a, b, c)  # 10 20 30

# 3. Değer değiştirme
x, y = 5, 10
x, y = y, x  # Değerler yer değiştirir
print(x, y)  # 10 5

# 4. F-string ile tip gösterme
sayi = 42
print(f"Sayı: {sayi}, Tipi: {type(sayi)}")
```

---

## 📝 SORULAR

### ⭐ Kolay Seviye (1-15)

#### ✅ Soru 1: Veri Tipi Belirleme
Aşağıdaki değişkenlerin veri tiplerini ekrana yazdıran program yazın:
- `isim = "Python"`
- `yas = 30`
- `boy = 1.75`
- `ogrenci_mi = True`

**Beklenen Çıktı:**
```
VERİ TİPLERİ TABLOSU
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Değişken: isim
Değer: Python
Tip: <class 'str'>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Değişken: yas
Değer: 30
Tip: <class 'int'>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

#### ✅ Soru 2: Bölme İşlemleri Karşılaştırma
100 sayısını 3'e hem normal bölme (/) hem de tam bölme (//) ile bölün. Ayrıca kalanı (%) bulun.

**Beklenen Çıktı:**
```
BÖLME İŞLEMLERİ
━━━━━━━━━━━━━━━━━━━━━
100 / 3 = 33.333...
100 // 3 = 33
100 % 3 = 1
```

---

#### ✅ Soru 3: Üs Alma İşlemleri
2'nin 1'den 10'a kadar olan kuvvetlerini hesaplayın.

**Beklenen Çıktı:**
```
ÜS ALMA TABLOSU
━━━━━━━━━━━━━━━
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
```
*(İpucu: Manuel olarak yazın, döngü henüz öğrenilmedi)*

---

#### ✅ Soru 4: String'den Sayıya Dönüşüm
`"123"` ve `"45.6"` stringlerini sayıya çevirip toplayın.

---

#### ✅ Soru 5: Yaş Hesaplama (Input)
Kullanıcıdan doğum yılını isteyin (string olarak gelir) ve yaşını hesaplayın.

**Örnek Çıktı:**
```
Doğum yılınız: 1995

📅 YAŞ HESAPLAMA
Doğum Yılı: 1995 (tip: <class 'int'>)
Şu Anki Yıl: 2025
Yaşınız: 30
```

---

#### ✅ Soru 6: Sıcaklık Dönüştürücü
Celsius'u Fahrenheit'a çeviren program. *(F = C × 9/5 + 32)*

---

#### ✅ Soru 7: Alan ve Çevre Hesaplama
Dikdörtgenin kenarlarını alıp hem alan hem çevre hesaplayın.

---

#### ✅ Soru 8: Mod Operatörü Kullanımı
Kullanıcıdan bir sayı alın ve 5'e bölümünden kalanı gösterin.

**Örnek Çıktı:**
```
Bir sayı girin: 23

23 ÷ 5 = 4 (Kalan: 3)
```

---

#### ✅ Soru 9: Ortalama Hesaplama
3 sınav notu alıp ortalamasını hesaplayın. Notlar float olarak girilecek.

---

#### ✅ Soru 10: Basit Hesap Makinesi (Toplama)
İki sayı alıp toplayın, sonucu ve işlem tipini gösterin.

---

#### ✅ Soru 11: String Birleştirme vs Sayı Toplama
`"5" + "3"` ile `5 + 3` arasındaki farkı gösteren program.

---

#### ✅ Soru 12: Tam Bölme Uygulaması
Bir market 125 TL'lik alışverişi 4 kişiye eşit böleceğ. Kişi başı tam ücret ve artan parayı hesaplayın.

---

#### ✅ Soru 13: Kare ve Küp Hesaplama
Kullanıcıdan bir sayı alıp karesini ve küpünü hesaplayın.

---

#### ✅ Soru 14: Float Hassasiyet
`10 / 3` işlemini yapın ve sonucu 2 ondalık basamakla gösterin. *(round() veya f-string:.2f)*

---

#### ✅ Soru 15: Tip Dönüşüm Zinciri
`"42"` → int → float → string dönüşümlerini gösterin.

---

### 🌟 Orta Seviye (16-30)

#### ✅ Soru 16: KDV Hesaplama
Ürün fiyatı alın, %18 KDV ekleyin. Hem KDV tutarını hem toplam fiyatı gösterin.

---

#### ✅ Soru 17: Maaş Bordrosu
Brüt maaş alın, %15 kesinti yapın, net maaşı hesaplayın.

---

#### ✅ Soru 18: Kredi Hesaplama
Kredi miktarı, faiz oranı (%) ve vade (ay) alın. Toplam geri ödeme tutarını hesaplayın.

---

#### ✅ Soru 19: Yakıt Menzili
Depo kapasitesi (litre) ve 100km'deki tüketim alın. Tam depoyla kaç km gidileceğini hesaplayın.

---

#### ✅ Soru 20: Pizza Dilimi Hesabı
Pizza çapı (cm) alın, 8 dilime bölün. Her dilimin yaklaşık kaç cm² olduğunu hesaplayın. *(Alan = π × r²)*

---

#### ✅ Soru 21: Çalışma Saati Hesabı
Başlangıç saati (örn: 9.30) ve bitiş saati (örn: 17.45) alın (float olarak). Toplam çalışma süresini hesaplayın.

---

#### ✅ Soru 22: İki Sayı Arasındaki İşlemler
İki sayı alın ve 7 farklı işlemi (+, -, *, /, //, %, **) gösterin.

---

#### ✅ Soru 23: Döviz Çevirici
TL miktarı ve döviz kuru (float) alın. Hem alış hem satış kurunu gösterin.

---

#### ✅ Soru 24: Mağaza İndirim Hesabı
Fiyat ve indirim oranı alın. İndirim tutarı, indirimli fiyat ve aradaki farkı gösterin.

---

#### ✅ Soru 25: Üçgen Alan Hesabı
Taban ve yükseklik alın. *(Alan = taban × yükseklik ÷ 2)*

---

#### ✅ Soru 26: Elektrik Faturası Kademeli
0-100 kWh: 1 TL, 100+ kWh: 1.5 TL. Kullanıcıdan tüketim alın, tutarı hesaplayın.

---

#### ✅ Soru 27: Zaman Dönüştürücü
Saniye cinsinden süre alın (int), saat-dakika-saniye formatına çevirin.

---

#### ✅ Soru 28: Beden Kitle İndeksi (BMI) Detaylı
Kilo ve boy alın, BMI hesaplayın ve sonucu 1 ondalıkla gösterin.

---

#### ✅ Soru 29: Ürün Kâr Hesabı
Alış fiyatı ve satış fiyatı alın. Kâr tutarı ve kâr yüzdesini hesaplayın.

---

#### ✅ Soru 30: Pil Şarj Süresi
Pil kapasitesi (mAh) ve şarj gücü (A) alın. Tam şarj süresini saat cinsinden hesaplayın.

---

### 🎯 Zorlayıcı Sorular (31-40)

#### ✅ Soru 31: Karma İşlemler
`(5 + 3) * 2 ** 3 / 4 - 10 % 3` işleminin sonucunu adım adım gösterin.

---

#### ✅ Soru 32: Sayı Basamak Ayırma
3 basamaklı sayı alın (örn: 456), yüzler-onlar-birler basamağını ayırın. *(// ve % kullanın)*

---

#### ✅ Soru 33: Daire Hesaplamaları
Yarıçap alın, hem alanı hem çevreyi hesaplayın. *(π = 3.14)*

---

#### ✅ Soru 34: Çoklu Tip Dönüşümü
String olarak 3 sayı alın, ikisini float, birini int yapın ve matematiksel işlemler uygulayın.

---

#### ✅ Soru 35: Mini Hesap Makinesi
İki sayı ve bir operatör (+, -, *, /) alın, sonucu gösterin.

---

#### ✅ Soru 36: Yaş Grubu Hesaplayıcı
Doğum yılı alın, kaç gün yaşadığını hesaplayın. *(1 yıl = 365 gün)*

---

#### ✅ Soru 37: İskonto Zinciri
Fiyat alın, önce %20 sonra %10 indirim uygulayın. Son fiyatı ve toplam indirim oranını gösterin.

---

#### ✅ Soru 38: Kutu Hacmi ve Ağırlık
Kutu boyutları (cm) ve yoğunluk (g/cm³) alın. Hacmi ve toplam ağırlığı hesaplayın.

---

#### ✅ Soru 39: Basınç Dönüştürücü
Bar cinsinden basınç alın, PSI ve ATM'ye çevirin.
*(1 Bar = 14.5 PSI = 0.987 ATM)*

---

#### ✅ Soru 40: Faiz Hesaplama (Bileşik)
Ana para, yıllık faiz oranı ve yıl alın. Bileşik faiz ile toplam tutarı hesaplayın.
*(Tutar = Ana Para × (1 + Faiz) ^ Yıl)*

---

## 💡 BONUS: Hata Ayıklama Soruları

#### ✅ Bonus 1: Hatalı Kodu Düzelt
```python
# Bu kod hatalı, neden?
yas = input("Yaşınız: ")
gelecek_yas = yas + 10
print(gelecek_yas)
```

#### ✅ Bonus 2: Hatalı Kodu Düzelt
```python
# Bu kod hatalı, neden?
fiyat = 100
indirim = fiyat * 20%
print(indirim)
```

---

## 📊 NOTLAR

### Değişken İsimlendirme Kuralları:
- ✅ Türkçe karakter kullanma: `fiyat`, `toplam`
- ✅ Alt çizgi kullan: `toplam_fiyat`, `kullanici_adi`
- ❌ Boşluk kullanma: `toplam fiyat` (YANLIŞ)
- ❌ Sayı ile başlama: `1sayi` (YANLIŞ)
- ❌ Özel karakter kullanma: `fiyat$`, `toplam%` (YANLIŞ)

### Okunabilir Kod İçin:
```python
# İyi kod
toplam_fiyat = urun_fiyati * adet
kdv_tutari = toplam_fiyat * 0.18
odenecek_tutar = toplam_fiyat + kdv_tutari

# Kötü kod
t = u * a
k = t * 0.18
o = t + k
```

---

**Başarılar! 🚀**