# Python 4. Hafta
**String İşlemleri**

---

## 📚 Öğrenme Hedefleri
- String (metin) veri tipi detaylı kullanımı
- String birleştirme ve çoğaltma
- String indexleme ve slicing (dilimleme)
- String metodları (upper, lower, replace, split, strip, vb.)
- F-string ile gelişmiş formatlama
- String üzerinde döngüler (temel seviye)
- Metin işleme projeleri

---

## 🎓 ÖNEMLİ BİLGİLENDİRMELER

### 1️⃣ STRING NEDİR?

String, metin verilerini saklamak için kullanılan veri tipidir. Tek tırnak `'` veya çift tırnak `"` ile oluşturulur.

```python
# Farklı string tanımlama yöntemleri
isim = "Ahmet"
sehir = 'İstanbul'
mesaj = """Bu bir
çok satırlı
metindir"""

# Boş string
bos = ""

# String içinde tırnak kullanma
metin1 = "Python'da string öğreniyorum"
metin2 = 'Kitabın adı "Python"'
```

---

### 2️⃣ STRING BİRLEŞTİRME (CONCATENATION)

```python
# + operatörü ile birleştirme
ad = "Ahmet"
soyad = "Yılmaz"
tam_isim = ad + " " + soyad
print(tam_isim)  # Ahmet Yılmaz

# Sayı ile string birleştirilemez! (Önce dönüştürün)
yas = 25
# metin = "Yaşım " + yas  # HATA! ❌
metin = "Yaşım " + str(yas)  # DOĞRU ✅

# f-string ile (En pratik yöntem)
isim = "Zeynep"
yas = 22
mesaj = f"Merhaba, ben {isim} ve {yas} yaşındayım"
print(mesaj)
```

---

### 3️⃣ STRING ÇOĞALTMA

```python
# * operatörü ile çoğaltma
yildiz = "*" * 10
print(yildiz)  # **********

cizgi = "=" * 50
print(cizgi)

# Pratik kullanım
print("-" * 30)
print("BAŞLIK")
print("-" * 30)
```

---

### 4️⃣ STRING İNDEXLEME (INDEXING)

Python'da indexler **0'dan** başlar!

```python
metin = "Python"

# İndexleme
print(metin[0])  # P (ilk karakter)
print(metin[1])  # y
print(metin[5])  # n (son karakter)

# Negatif indexleme (sondan başlar)
print(metin[-1])  # n (son karakter)
print(metin[-2])  # o (sondan 2. karakter)
print(metin[-6])  # P (ilk karakter)

# Index numaraları:
# P  y  t  h  o  n
# 0  1  2  3  4  5    (pozitif)
#-6 -5 -4 -3 -2 -1    (negatif)
```

⚠️ **DİKKAT:** Olmayan bir indexe erişmeye çalışırsanız hata alırsınız!

```python
metin = "Python"
# print(metin[10])  # IndexError! ❌
```

---

### 5️⃣ STRING DİLİMLEME (SLICING)

```python
metin = "Python Programlama"

# [başlangıç:bitiş] - bitiş dahil değil!
print(metin[0:6])    # Python
print(metin[7:18])   # Programlama

# Başlangıç belirtilmezse 0'dan başlar
print(metin[:6])     # Python

# Bitiş belirtilmezse sona kadar alır
print(metin[7:])     # Programlama

# Negatif index ile
print(metin[-10:])   # ramlama

# Adım (step) kullanımı [başlangıç:bitiş:adım]
print(metin[::2])    # Pto rgalm (2'şer atlayarak)
print(metin[::-1])   # amalmargoPnohtyP (tersten)
```

**Pratik Örnekler:**
```python
cumle = "Merhaba Dünya"

# İlk 7 karakter
print(cumle[:7])     # Merhaba

# Son 5 karakter
print(cumle[-5:])    # Dünya

# Ortadaki karakterler
print(cumle[3:7])    # haba

# String'i ters çevirme
print(cumle[::-1])   # ayınüD abahreM
```

---

### 6️⃣ STRING UZUNLUĞU - len()

```python
metin = "Python"
uzunluk = len(metin)
print(uzunluk)  # 6

# Pratik kullanım
isim = input("İsminiz: ")
if len(isim) < 3:
    print("İsim çok kısa!")
```

---

### 7️⃣ STRING METODLARI

#### **Büyük/Küçük Harf Dönüşümleri**

```python
metin = "Python Programlama"

# Tümünü büyük harfe
print(metin.upper())        # PYTHON PROGRAMLAMA

# Tümünü küçük harfe
print(metin.lower())        # python programlama

# Her kelimenin ilk harfi büyük
print(metin.title())        # Python Programlama

# İlk harf büyük, diğerleri küçük
print(metin.capitalize())   # Python programlama

# Büyük-küçük harfleri değiştir
print(metin.swapcase())     # pYTHON PROGRAMLAMA
```

#### **Arama ve Kontrol Metodları**

```python
cumle = "Python öğrenmek çok eğlenceli"

# Kelime arama (var mı yok mu)
print("Python" in cumle)          # True
print("Java" in cumle)            # False
print("Python" not in cumle)      # False

# find() - Kelimenin index numarasını bulur (-1 bulamazsa)
print(cumle.find("öğrenmek"))     # 7
print(cumle.find("Java"))         # -1

# count() - Kelimenin kaç kere geçtiğini sayar
print(cumle.count("e"))           # 4

# startswith() - Belirtilen kelime ile başlıyor mu?
print(cumle.startswith("Python")) # True

# endswith() - Belirtilen kelime ile bitiyor mu?
print(cumle.endswith("eğlenceli"))# True
```

#### **Değiştirme ve Temizleme**

```python
metin = "  Python Programlama  "

# strip() - Baş ve sondaki boşlukları siler
print(metin.strip())        # "Python Programlama"

# lstrip() - Soldaki boşlukları siler
print(metin.lstrip())       # "Python Programlama  "

# rstrip() - Sağdaki boşlukları siler
print(metin.rstrip())       # "  Python Programlama"

# replace() - Değiştir
cumle = "Python çok zor"
yeni = cumle.replace("zor", "kolay")
print(yeni)  # Python çok kolay

# Birden fazla değiştirme
metin = "Java Java Java"
yeni = metin.replace("Java", "Python")
print(yeni)  # Python Python Python
```

#### **Bölme ve Birleştirme**

```python
# split() - String'i listeye böler
cumle = "Python çok güzel bir dildir"
kelimeler = cumle.split()  # Boşluklara göre böler
print(kelimeler)  # ['Python', 'çok', 'güzel', 'bir', 'dildir']

# Özel ayıraçla bölme
tarih = "15-05-2025"
parcalar = tarih.split("-")
print(parcalar)  # ['15', '05', '2025']

# join() - Liste elemanlarını birleştirir
kelimeler = ["Python", "öğrenmek", "kolay"]
cumle = " ".join(kelimeler)
print(cumle)  # Python öğrenmek kolay

# Özel ayıraçla birleştirme
tarih_parcalari = ["2025", "05", "15"]
tarih = "-".join(tarih_parcalari)
print(tarih)  # 2025-05-15
```

---

### 8️⃣ F-STRING GELİŞMİŞ KULLANIM

```python
isim = "Ahmet"
yas = 25
boy = 1.75
para = 1234.56789

# Temel kullanım
print(f"İsim: {isim}, Yaş: {yas}")

# Matematiksel işlemler
print(f"5 yıl sonra: {yas + 5} yaşında")

# Ondalık basamak kontrolü
print(f"Boy: {boy:.2f} m")          # 1.75 m
print(f"Para: {para:.2f} TL")       # 1234.57 TL

# Hizalama
print(f"{isim:>10}")    # Sağa hizala (    Ahmet)
print(f"{isim:<10}")    # Sola hizala (Ahmet    )
print(f"{isim:^10}")    # Ortala (  Ahmet  )

# Bin ayracı
sayi = 1000000
print(f"{sayi:,}")      # 1,000,000
```

---

### 9️⃣ STRING İMMUTABLE (DEĞİŞTİRİLEMEZ)

⚠️ **ÖNEMLİ:** Python'da stringler değiştirilemez!

```python
metin = "Python"

# Hatalı kullanım ❌
# metin[0] = "J"  # TypeError!

# Doğru kullanım ✅
metin = "J" + metin[1:]  # Jython
print(metin)

# Veya replace kullanın
metin = "Python"
yeni_metin = metin.replace("P", "J")
print(yeni_metin)  # Jython
```

---

### 🔟 KAÇIŞ KARAKTERLERİ (ESCAPE CHARACTERS)

```python
# \n - Yeni satır
print("Birinci satır\nİkinci satır")

# \t - Tab (sekme)
print("İsim:\tAhmet\nYaş:\t25")

# \\ - Ters slash
print("C:\\Users\\Desktop")

# \' ve \" - Tırnak işaretleri
print("Python'da \"string\" öğreniyorum")

# Çoklu satır (üçlü tırnak)
metin = """
Bu bir
çok satırlı
metindir
"""
```

---

### 1️⃣1️⃣ YAYGIN HATALAR VE ÇÖZÜMLER

#### **Hata 1: String + Sayı**
```python
# YANLIŞ ❌
yas = 25
# print("Yaşım " + yas)  # TypeError!

# DOĞRU ✅
print("Yaşım " + str(yas))
# VEYA
print(f"Yaşım {yas}")
```

#### **Hata 2: Index Hatası**
```python
metin = "Python"
# print(metin[10])  # IndexError! ❌

# DOĞRU ✅
if len(metin) > 10:
    print(metin[10])
```

#### **Hata 3: String Değiştirme**
```python
# YANLIŞ ❌
metin = "Python"
# metin[0] = "J"  # TypeError!

# DOĞRU ✅
metin = "J" + metin[1:]
```

---

### 1️⃣2️⃣ PRATİK İPUÇLARI

```python
# 1. String içinde değişken var mı kontrolü
email = "ahmet@gmail.com"
if "@" in email and "." in email:
    print("Geçerli email formatı")

# 2. String'i ters çevirme (palindrome kontrolü)
kelime = "kayak"
if kelime == kelime[::-1]:
    print("Palindrome!")

# 3. Boşlukları kaldırma
metin = "  Python  "
temiz = metin.strip()

# 4. Tüm boşlukları kaldırma
cumle = "Python çok güzel"
bosluksuz = cumle.replace(" ", "")
print(bosluksuz)  # Pythonçokgüzel

# 5. İlk harfi büyük yapma
isim = "ahmet"
duzgun_isim = isim.capitalize()

# 6. Email kontrolü
email = input("Email: ").lower().strip()
```

---

## 📝 SORULAR

### ⭐ Kolay Seviye (1-15)

#### ✅ Soru 1: String Uzunluğu Bulma
Kullanıcıdan bir kelime alın ve kaç harfli olduğunu söyleyin.

**Örnek Çıktı:**
```
Bir kelime girin: Python
"Python" kelimesi 6 harflidir.
```

---

#### ✅ Soru 2: Büyük/Küçük Harf Dönüşümü
Kullanıcıdan bir metin alın, hem tamamen büyük hem tamamen küçük harf olarak gösterin.

---

#### ✅ Soru 3: String Birleştirme
Ad ve soyad alın, tam ismi oluşturun.

---

#### ✅ Soru 4: String Çoğaltma
Kullanıcıdan bir karakter ve tekrar sayısı alın, karakteri o kadar kez yazdırın.

**Örnek:** `*` karakteri 10 kez → `**********`

---

#### ✅ Soru 5: İlk ve Son Karakter
Bir kelime alın, ilk ve son karakterini gösterin.

---

#### ✅ Soru 6: String Ters Çevirme
Kullanıcıdan bir kelime alın ve tersini yazdırın.

**Örnek:** `Python` → `nohtyP`

---

#### ✅ Soru 7: Email Adresi Kontrolü
Email içinde `@` ve `.` var mı kontrol edin.

---

#### ✅ Soru 8: Kelime Sayma
Bir cümle alın, kaç kelime olduğunu sayın. (split kullanın)

---

#### ✅ Soru 9: Boşluk Temizleme
Başında ve sonunda boşluk olan metin alın, temizlenmiş halini gösterin.

---

#### ✅ Soru 10: Karakter Arama
Bir kelime ve aranacak harf alın, harf kelimede var mı kontrol edin.

---

#### ✅ Soru 11: Başlık Formatı
Bir cümle alın, her kelimenin ilk harfini büyük yapın (title).

---

#### ✅ Soru 12: Telefon Numarası Format
`5551234567` formatındaki numarayı `555 123 45 67` formatına çevirin (slicing).

---

#### ✅ Soru 13: Kullanıcı Adı Oluşturma
Ad ve soyadın ilk harflerini alıp kullanıcı adı oluşturun.

**Örnek:** `Ahmet Yılmaz` → `AY`

---

#### ✅ Soru 14: Kelime Değiştirme
Bir cümle alın, belirli bir kelimeyi başka kelime ile değiştirin (replace).

---

#### ✅ Soru 15: Harf Sayma
Bir kelime ve harf alın, harfin kelimede kaç kere geçtiğini bulun (count).

---

### 🌟 Orta Seviye (16-30)

#### ✅ Soru 16: Palindrome Kontrolü
Bir kelime alın, tersten okunuşu aynı mı kontrol edin.

**Örnek:** `kayak`, `aba`, `12321`

---

#### ✅ Soru 17: Email Ayrıştırma
Email adresi alın, kullanıcı adı ve domain'i ayırın.

**Örnek:** `ahmet@gmail.com` → Kullanıcı: `ahmet`, Domain: `gmail.com`

---

#### ✅ Soru 18: İsim Formatlama
Küçük harfle yazılmış ad-soyad alın, düzgün formatlayın.

**Örnek:** `ahmet yılmaz` → `Ahmet Yılmaz`

---

#### ✅ Soru 19: Şifre Güvenlik Kontrolü
Şifre uzunluğu en az 8 karakter mi kontrol edin.

---

#### ✅ Soru 20: Kelime Gizleme
Bir kelime alın, ortadaki harfleri `*` ile değiştirin.

**Örnek:** `Python` → `P****n`

---

#### ✅ Soru 21: Tarih Formatı Değiştirme
`15-05-2025` formatını `15/05/2025` formatına çevirin.

---

#### ✅ Soru 22: Sesli Harf Sayma
Bir kelime alın, içindeki sesli harf sayısını bulun (a, e, ı, i, o, ö, u, ü).

---

#### ✅ Soru 23: Baş Harfleri Alma
Tam isim alın, baş harfleri ile kısaltma oluşturun.

**Örnek:** `Türkiye Cumhuriyeti` → `TC`

---

#### ✅ Soru 24: URL Temizleme
URL'den `https://` ve `www.` kısımlarını kaldırın.

**Örnek:** `https://www.google.com` → `google.com`

---

#### ✅ Soru 25: Cümle Ters Çevirme
Cümleyi kelime kelime ters çevirin.

**Örnek:** `Python çok güzel` → `güzel çok Python`

---

#### ✅ Soru 26: Kimlik No Gizleme
TC Kimlik no'nun ortadaki rakamlarını `*` ile gizleyin.

**Örnek:** `12345678901` → `123******01`

---

#### ✅ Soru 27: Dosya Uzantısı Bulma
Dosya adı alın, uzantısını bulun.

**Örnek:** `document.pdf` → `pdf`

---

#### ✅ Soru 28: Kelime Uzunluğu Kontrolü
Cümledeki her kelimenin uzunluğunu gösterin.

---

#### ✅ Soru 29: Kullanıcı Adı Geçerliliği
Kullanıcı adı sadece harf ve rakam içermeli (boşluk olmamalı).

---

#### ✅ Soru 30: Kredi Kartı Maskeleme
Kredi kartı numarasının ilk 12 hanesini `*` ile gösterin.

**Örnek:** `1234567890123456` → `************3456`

---

### 🎯 İleri Seviye (31-40)

#### ✅ Soru 31: Karakter Frekansı
Bir kelime alın, her harfin kaç kere geçtiğini gösterin.

**Örnek:** `merhaba` → m:1, e:1, r:1, h:1, a:2, b:1

---

#### ✅ Soru 32: Anagram Kontrolü
İki kelime alın, anagram mı kontrol edin (aynı harfler farklı sırada).

**Örnek:** `listen` ve `silent`

---

#### ✅ Soru 33: Caesar Şifreleme
Bir kelimeyi 3 harf kaydırarak şifreleyin.

**Örnek:** `abc` → `def`

---

#### ✅ Soru 34: En Uzun Kelime
Bir cümle alın, en uzun kelimeyi bulun.

---

#### ✅ Soru 35: Metin Düzenleme Programı
Kullanıcıya menü sunun:
1. Büyük harfe çevir
2. Küçük harfe çevir
3. Kelime sayısı
4. Karakter sayısı
5. Ters çevir

---

#### ✅ Soru 36: Email Validasyonu
Email geçerli mi tam kontrol edin:
- `@` içermeli
- `@` önce ve sonra karakter olmalı
- Nokta içermeli
- Boşluk olmamalı

---

#### ✅ Soru 37: Plaka Kodu Şehir Bulma
Basit bir sistem: Kullanıcı plaka kodu girsin (örn: 06, 34, 35), şehir adını söyleyin.

---

#### ✅ Soru 38: Kelime Oyunu
Kullanıcıdan kelime alın, her harfi `-` ile ayırarak gösterin.

**Örnek:** `Python` → `P-y-t-h-o-n`

---

#### ✅ Soru 39: Şifre Oluşturucu
İsim ve doğum yılından otomatik şifre oluşturun.

**Örnek:** `Ahmet 1995` → `Ahmet@1995`

---

#### ✅ Soru 40: Metin İstatistikleri
Bir metin alın, şunları gösterin:
- Toplam karakter sayısı
- Boşluksuz karakter sayısı
- Kelime sayısı
- Sesli harf sayısı
- Rakam sayısı

---

## 💡 BONUS: PROJELERString işlemlerini pratiğe dökecek mini projeler:

### 🎮 Proje 1: Basit Metin Editörü
Kullanıcıdan metin alın ve çeşitli işlemler yapın (büyük/küçük harf, kelime sayısı, vb.)

### 🎮 Proje 2: Şifre Kontrol Sistemi
Güçlü şifre kontrolü (uzunluk, büyük harf, küçük harf, rakam)

### 🎮 Proje 3: İsim Kartı Oluşturucu
Kullanıcıdan bilgi alıp güzel formatlı kartvizit oluşturun

---

**Başarılar! 🎉**