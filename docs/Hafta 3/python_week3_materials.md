# Python 3. Hafta
**Koşullu İfadeler (if/elif/else)**

---

## 📚 Öğrenme Hedefleri
- Karşılaştırma operatörleri (==, !=, <, >, <=, >=)
- Mantıksal operatörler (and, or, not)
- if yapısı
- if-else yapısı
- if-elif-else yapısı
- İç içe (nested) if yapıları
- Koşullu ifadelerle karar verme mekanizmaları

---

## 🎓 ÖNEMLİ BİLGİLENDİRMELER

### 1️⃣ KARŞILAŞTIRMA OPERATÖRLERİ

```python
# Eşittir
5 == 5  # True
5 == 3  # False

# Eşit değildir
5 != 3  # True
5 != 5  # False

# Küçüktür
3 < 5   # True
5 < 3   # False

# Büyüktür
5 > 3   # True
3 > 5   # False

# Küçük veya eşittir
3 <= 5  # True
5 <= 5  # True
5 <= 3  # False

# Büyük veya eşittir
5 >= 3  # True
5 >= 5  # True
3 >= 5  # False
```

⚠️ **ÖNEMLİ:** 
- Karşılaştırma için `==` (çift eşittir)
- Atama için `=` (tek eşittir)

```python
# YANLIŞ ❌
if yas = 18:  # Hata verir!

# DOĞRU ✅
if yas == 18:  # Doğru kullanım
```

---

### 2️⃣ MANTIKSAL OPERATÖRLER

#### **and (ve)** - Her iki koşul da True olmalı
```python
yas = 20
para = 100

# Her iki koşul da True ise True
if yas >= 18 and para >= 50:
    print("Sinemaya gidebilirsiniz")

# Truth Table (Doğruluk Tablosu)
True and True   # True
True and False  # False
False and True  # False
False and False # False
```

#### **or (veya)** - En az bir koşul True olmalı
```python
gun = "Cumartesi"
tatil = True

# En az biri True ise True
if gun == "Pazar" or tatil == True:
    print("Bugün tatil!")

# Truth Table
True or True    # True
True or False   # True
False or True   # True
False or False  # False
```

#### **not (değil)** - Koşulu tersine çevirir
```python
yagmur = False

if not yagmur:  # yagmur False ise
    print("Dışarı çıkabilirsiniz")

# Örnekler
not True   # False
not False  # True
```

---

### 3️⃣ IF YAPISI (Temel Kullanım)

```python
# Basit if
yas = 18

if yas >= 18:
    print("Reşitsiniz")
    print("Ehliyet alabilirsiniz")

# ⚠️ GİRİNTİ (INDENTATION) ÖNEMLİ!
# Python'da girintiler kod bloklarını belirler
# 4 boşluk veya 1 tab kullanın
```

#### **Girinti Hataları:**
```python
# YANLIŞ ❌
if yas >= 18:
print("Hata!")  # Girinti yok!

# DOĞRU ✅
if yas >= 18:
    print("Doğru!")  # 4 boşluk girinti
```

---

### 4️⃣ IF-ELSE YAPISI

```python
yas = 16

if yas >= 18:
    print("Reşitsiniz")
    print("Oy kullanabilirsiniz")
else:
    print("Reşit değilsiniz")
    print("Henüz oy kullanamazsınız")

# else kendi başına koşul almaz!
```

---

### 5️⃣ IF-ELIF-ELSE YAPISI

```python
not_ortalamasi = 75

if not_ortalamasi >= 85:
    print("Takdir Belgesi")
elif not_ortalamasi >= 70:
    print("Teşekkür Belgesi")
elif not_ortalamasi >= 50:
    print("Geçtin")
else:
    print("Kaldın")

# ⚠️ İLK DOĞRU KOŞUL ÇALIŞIR, DİĞERLERİ ATLANIR!
```

#### **elif Kullanım Kuralları:**
- `elif` sadece `if`'ten sonra kullanılır
- İstediğiniz kadar `elif` ekleyebilirsiniz
- `else` isteğe bağlıdır (olmasa da olur)
- Sadece **bir tane** kod bloğu çalışır

---

### 6️⃣ İÇ İÇE (NESTED) IF YAPILARI

```python
yas = 20
ehliyet = True

if yas >= 18:
    print("Yaş uygun")
    
    if ehliyet == True:
        print("Araba kiralayabilirsiniz")
    else:
        print("Önce ehliyet almalısınız")
else:
    print("18 yaşından küçüksünüz")
```

---

### 7️⃣ KARMAŞIK KOŞULLAR

```python
# Çoklu and kullanımı
yas = 25
gelir = 5000
kredi_notu = 700

if yas >= 18 and gelir >= 3000 and kredi_notu >= 600:
    print("Kredi başvurusu onaylandı")

# and ve or karışımı (parantez kullanın!)
if (yas >= 18 and gelir >= 3000) or kredi_notu >= 800:
    print("Özel kredi hakkınız var")

# Aralık kontrolü
sayi = 50
if 0 <= sayi <= 100:  # Python'a özel pratik kullanım
    print("Sayı 0-100 arasında")
```

---

### 8️⃣ STRING KARŞILAŞTIRMALARI

```python
isim = "Ahmet"

# Eşitlik kontrolü (büyük/küçük harf duyarlı)
if isim == "Ahmet":  # True
    print("Merhaba Ahmet")

if isim == "ahmet":  # False (küçük harf)
    print("Bu çalışmaz")

# Büyük/küçük harf duyarsız
if isim.lower() == "ahmet":  # True
    print("Bu çalışır")

# String içinde arama
if "met" in isim:
    print("İsimde 'met' var")
```

---

### 9️⃣ YAYGIN HATALAR VE ÇÖZÜMLER

#### **Hata 1: = yerine == kullanmak**
```python
# YANLIŞ ❌
if yas = 18:  # SyntaxError!
    print("Hata")

# DOĞRU ✅
if yas == 18:
    print("Doğru")
```

#### **Hata 2: Girinti hatası**
```python
# YANLIŞ ❌
if yas >= 18:
print("Hata")  # IndentationError

# DOĞRU ✅
if yas >= 18:
    print("Doğru")
```

#### **Hata 3: İki nokta üst üste unutmak**
```python
# YANLIŞ ❌
if yas >= 18  # SyntaxError!
    print("Hata")

# DOĞRU ✅
if yas >= 18:  # : (colon) gerekli!
    print("Doğru")
```

#### **Hata 4: else'e koşul yazmak**
```python
# YANLIŞ ❌
else yas < 18:  # SyntaxError!
    print("Hata")

# DOĞRU ✅
else:  # else koşul almaz
    print("Doğru")
```

---

### 🔟 PRATİK İPUÇLARI

```python
# 1. Kısa if-else (Ternary Operator)
yas = 20
durum = "Reşit" if yas >= 18 else "Reşit değil"
print(durum)

# 2. Çoklu karşılaştırma
sayi = 50
if 10 < sayi < 100:  # Çok pratik!
    print("Sayı 10-100 arası")

# 3. Boolean değişkenler
yagmur_yagiyor = True

# Gereksiz karşılaştırma ❌
if yagmur_yagiyor == True:
    print("Şemsiye al")

# Daha iyi ✅
if yagmur_yagiyor:
    print("Şemsiye al")

# 4. Boş string kontrolü
isim = ""
if isim:  # Boş string False sayılır
    print("İsim var")
else:
    print("İsim boş")

# 5. 0 kontrolü
sayi = 0
if sayi:  # 0 False sayılır
    print("Sayı var")
else:
    print("Sayı sıfır")
```

---

## 📝 SORULAR

### ⭐ Kolay Seviye (1-15)

#### ✅ Soru 1: Pozitif/Negatif Sayı Kontrolü
Kullanıcıdan bir sayı alın. Sayı pozitif ise "Pozitif", negatif ise "Negatif", sıfır ise "Sıfır" yazdırın.

**Örnek Çıktı:**
```
Bir sayı girin: 5
✅ Sayı POZİTİF
```

---

#### ✅ Soru 2: Tek/Çift Kontrol
Kullanıcıdan bir sayı alın ve tek mi çift mi olduğunu söyleyin.

**İpucu:** `sayi % 2 == 0` ise çifttir

---

#### ✅ Soru 3: Yaş Kontrolü (Reşit mi?)
Kullanıcıdan yaş alın, 18 ve üzeri ise "Reşitsiniz", değilse "Reşit değilsiniz" yazdırın.

---

#### ✅ Soru 4: Sınav Geçme Durumu
Kullanıcıdan sınav notu alın (0-100). 50 ve üzeri ise "Geçtiniz", altında ise "Kaldınız".

---

#### ✅ Soru 5: Büyük Sayıyı Bulma
Kullanıcıdan iki sayı alın ve hangisinin büyük olduğunu söyleyin.

**Örnek Çıktı:**
```
İlk sayı: 15
İkinci sayı: 23

📊 SONUÇ: 23 daha büyüktür
```

---

#### ✅ Soru 6: Şifre Kontrolü
Şifre "python123" olsun. Kullanıcıdan şifre isteyin, doğruysa "Giriş başarılı", yanlışsa "Hatalı şifre".

---

#### ✅ Soru 7: İndirim Kontrolü
Alışveriş tutarı 100 TL ve üzeri ise %10 indirim, altında ise indirim yok.

---

#### ✅ Soru 8: Hız Limiti Kontrolü
Araç hızı alın. 120 km/s ve üzeri ise "Hız sınırı aşıldı", altında ise "Hız uygun".

---

#### ✅ Soru 9: Sıcaklık Değerlendirmesi
Sıcaklık 30 derece ve üzeri ise "Sıcak", altında ise "Serin" yazdırın.

---

#### ✅ Soru 10: Ürün Stok Kontrolü
Stok miktarı alın. 0 ise "Stokta yok", 0'dan büyük ise "Stokta var".

---

#### ✅ Soru 11: Kullanıcı Adı Kontrolü
Kullanıcı adı "admin" ise "Hoş geldin yönetici", değilse "Hoş geldin kullanıcı".

---

#### ✅ Soru 12: Sayı Sıfır mı?
Bir sayı alın, sıfırsa "Sıfır", değilse "Sıfır değil" yazdırın.

---

#### ✅ Soru 13: Harf Notu (Tek if-elif-else)
Not alın: 85+ → A, 70-84 → B, 50-69 → C, 0-49 → F

---

#### ✅ Soru 14: Üyelik Durumu
Yaş 18+ ve üyelik True ise "Sisteme giriş yapabilirsiniz" (and kullanın).

---

#### ✅ Soru 15: Hafta Sonu Kontrolü
Gün adı alın. "Cumartesi" veya "Pazar" ise "Hafta sonu", değilse "Hafta içi" (or kullanın).

---

### 🌟 Orta Seviye (16-30)

#### ✅ Soru 16: Not Ortalaması Belge Sistemi
3 ders notu alın, ortalamayı hesaplayın:
- 85+ → Takdir Belgesi
- 70-84 → Teşekkür Belgesi
- 50-69 → Geçti
- 50 altı → Kaldı

---

#### ✅ Soru 17: Sinema Bileti Fiyatı
Yaş alın:
- 0-6 yaş → Ücretsiz
- 7-17 yaş → 20 TL (Öğrenci)
- 18-64 yaş → 40 TL (Tam bilet)
- 65+ yaş → 25 TL (İndirimli)

---

#### ✅ Soru 18: Üçgenin Geçerliliği
3 kenar uzunluğu alın. Her kenar, diğer ikisinin toplamından küçükse geçerli üçgendir.

---

#### ✅ Soru 19: Kredi Başvuru Değerlendirmesi
Yaş >= 18 ve gelir >= 5000 ve kredi notu >= 600 ise "Başvuru onaylandı".

---

#### ✅ Soru 20: Kargo Ücreti Hesaplama
Ağırlık alın:
- 0-1 kg → 15 TL
- 1-5 kg → 25 TL
- 5-10 kg → 40 TL
- 10+ kg → 60 TL

---

#### ✅ Soru 21: Ehliyet Türü Belirleme
Yaş alın:
- 18+ → B sınıfı (otomobil)
- 21+ → C sınıfı (kamyon)
- 24+ → D sınıfı (otobüs)

---

#### ✅ Soru 22: BMI (Vücut Kitle İndeksi) Değerlendirme
BMI hesaplayın ve yorumlayın:
- BMI < 18.5 → Zayıf
- 18.5-24.9 → Normal
- 25-29.9 → Fazla kilolu
- 30+ → Obez

---

#### ✅ Soru 23: Mevsim Belirleme
Ay numarası alın (1-12):
- 12, 1, 2 → Kış
- 3, 4, 5 → İlkbahar
- 6, 7, 8 → Yaz
- 9, 10, 11 → Sonbahar

---

#### ✅ Soru 24: Elektrik Faturası Kademeli Ücretlendirme
Tüketim (kWh):
- 0-100 → 1 TL/kWh
- 101-200 → 1.5 TL/kWh
- 200+ → 2 TL/kWh

---

#### ✅ Soru 25: Şifre Güvenlik Kontrolü
Şifre uzunluğu:
- 12+ karakter → Çok güçlü
- 8-11 karakter → Güçlü
- 6-7 karakter → Orta
- 6 altı → Zayıf

---

#### ✅ Soru 26: İki Sayının Büyüklük Karşılaştırması (3 durum)
İki sayı alın: büyük, küçük veya eşit durumlarını kontrol edin.

---

#### ✅ Soru 27: Restoran Hesabı ve Bahşiş
Hesap tutarı:
- 0-50 TL → %5 bahşiş
- 51-100 TL → %10 bahşiş
- 100+ TL → %15 bahşiş

---

#### ✅ Soru 28: Oyun Karakteri Seçimi
Karakter puanı:
- 90+ → Efsanevi
- 70-89 → Epik
- 50-69 → Nadir
- 50 altı → Sıradan

---

#### ✅ Soru 29: Araç Muayene Kontrolü
Araç yaşı:
- 0-3 yıl → Muayene gerekmez
- 4-7 yıl → 2 yılda bir
- 8+ yıl → Her yıl

---

#### ✅ Soru 30: Kan Bağışı Uygunluğu
Yaş 18-65 arası VE kilo 50+ kg ise "Kan bağışı yapabilirsiniz".

---

### 🎯 İleri Seviye (31-40)

#### ✅ Soru 31: Hesap Makinesi (4 İşlem)
İki sayı ve işlem (+, -, *, /) alın, sonucu hesaplayın.

---

#### ✅ Soru 32: Günün Saatine Göre Selamlama
Saat alın:
- 6-11 → Günaydın
- 12-17 → İyi günler
- 18-21 → İyi akşamlar
- 22-5 → İyi geceler

---

#### ✅ Soru 33: Üç Sayının En Büyüğü
3 sayı alın, en büyüğünü if-elif ile bulun.

---

#### ✅ Soru 34: Yıl Artık mı? (Leap Year)
Yıl alın: 4'e bölünüyor ve (100'e bölünmüyor veya 400'e bölünüyor) ise artık yıl.

---

#### ✅ Soru 35: Maaş Zam Hesaplayıcı
Maaş ve çalışma süresi (yıl):
- 5+ yıl → %15 zam
- 3-4 yıl → %10 zam
- 1-2 yıl → %5 zam
- 1 yıl altı → Zam yok

---

#### ✅ Soru 36: Kullanıcı Girişi (Şifre ve Kullanıcı Adı)
Hem kullanıcı adı "admin" hem şifre "1234" ise giriş başarılı.

---

#### ✅ Soru 37: Geometrik Şekil Alan Hesabı
Şekil seçimi: 1-Kare, 2-Dikdörtgen, 3-Üçgen, 4-Daire. Seçime göre alan hesaplayın.

---

#### ✅ Soru 38: Not Sistemi (Devamsızlık dahil)
Not ortalaması 50+ VE devamsızlık %20'den az ise "Geçti".

---

#### ✅ Soru 39: Trafik Cezası Hesaplama
Hız limiti 120. Her 10 km fazla için 200 TL ceza (iç içe if kullanın).

---

#### ✅ Soru 40: Oyun Kazanma Sistemi
Puan >= 100 VE can > 0 VE süre > 0 ise "Kazandınız", değilse hangi koşul sağlanmadığını söyleyin.

---

## 💡 BONUS: Problem Çözme Stratejileri

### Karmaşık Koşulları Nasıl Yazmalı?

```python
# 1. Adım: Koşulları listeleyin
# - Yaş 18 ve üzeri olmalı
# - Gelir 5000 ve üzeri olmalı
# - Kredi notu 600 ve üzeri olmalı

# 2. Adım: Her koşulu ayrı kontrol edin
yas = 25
gelir = 6000
kredi_notu = 650

if yas >= 18:
    if gelir >= 5000:
        if kredi_notu >= 600:
            print("Başvuru onaylandı")

# 3. Adım: and ile birleştirin
if yas >= 18 and gelir >= 5000 and kredi_notu >= 600:
    print("Başvuru onaylandı")
```

---

**Başarılar! 🎉**