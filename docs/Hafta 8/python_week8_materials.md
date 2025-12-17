# Python 8. Hafta
**Sözlükler (Dictionaries)**

---

## 📚 Öğrenme Hedefleri
- Dictionary (sözlük) kavramı ve key-value mantığı
- Dictionary oluşturma yöntemleri
- Dictionary'ye erişim ve değiştirme
- Dictionary metodları (keys, values, items, get, pop, update, vb.)
- Dictionary ile döngüler
- İç içe dictionary yapıları
- Dictionary pratik kullanım örnekleri
- **Proje:** Öğrenci Not Sistemi

---

## 🎯 DERS PLANI (4 Saat)

### ⏰ Saat 1-2: Dictionary Temel Kavramlar
- Dictionary nedir? Neden kullanırız?
- Key-Value (Anahtar-Değer) mantığı
- Dictionary oluşturma yöntemleri
- Elemanlara erişim
- Eleman ekleme, değiştirme, silme
- in operatörü ile kontrol
- Pratik örnekler

### ⏰ Saat 3: Dictionary Metodları
- keys() - Tüm anahtarları alma
- values() - Tüm değerleri alma
- items() - Anahtar-değer çiftlerini alma
- get() - Güvenli erişim
- pop() - Silme ve döndürme
- update() - Birleştirme
- clear() - Temizleme
- copy() - Kopyalama
- Döngülerle dictionary kullanımı

### ⏰ Saat 4: Proje - Öğrenci Not Sistemi
- Proje analizi ve planlama
- Öğrenci bilgilerini dictionary ile saklama
- CRUD işlemleri (Create, Read, Update, Delete)
- Menü sistemi tasarımı
- Not ortalaması hesaplama
- Öğrenci arama ve filtreleme
- Kod yazımı ve test

---

## 📖 SAAT 1-2: DICTIONARY TEMEL KAVRAMLAR

### 1️⃣ DICTIONARY NEDİR?

Dictionary, **anahtar-değer (key-value)** çiftlerini saklayan veri yapısıdır. Her bir anahtara karşılık bir değer bulunur.

**Neden Dictionary Kullanırız?**

```python
# Liste ile (KARMAŞIK) ❌
ogrenci_isim = "Ahmet"
ogrenci_yas = 20
ogrenci_bolum = "Bilgisayar Mühendisliği"
ogrenci_not = 85

# Dictionary ile (KOLAY) ✅
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "bolum": "Bilgisayar Mühendisliği",
    "not": 85
}
```

**Avantajları:**
- Veriler anlamlı isimlerle saklanır
- Hızlı erişim (O(1) karmaşıklık)
- Esnek yapı (değer ekleyip çıkarabilirsiniz)
- Gerçek hayat verilerini modellemek kolay

---

### 2️⃣ KEY-VALUE MANTĞI

```python
# Temel yapı:
sozluk = {
    "anahtar1": "değer1",
    "anahtar2": "değer2",
    "anahtar3": "değer3"
}

# Gerçek örnek:
telefon_rehberi = {
    "Ahmet": "0555 123 4567",
    "Mehmet": "0532 987 6543",
    "Ayşe": "0505 555 1234"
}
```

**Önemli Kurallar:**
- ✅ Anahtarlar (keys) **benzersiz** olmalı
- ✅ Anahtarlar **değiştirilemez** tipte olmalı (string, int, tuple)
- ✅ Değerler (values) **her tip** olabilir (string, int, list, dict, vb.)
- ❌ Liste anahtar olamaz (değiştirilebilir)

---

### 3️⃣ DICTIONARY OLUŞTURMA

#### **Yöntem 1: Süslü Parantez {}**
```python
# Boş dictionary
bos_sozluk = {}

# Değerlerle
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "not": 85
}

# Farklı veri tipleri
karisik = {
    "isim": "Ali",           # string
    "yas": 25,              # int
    "boy": 1.75,            # float
    "aktif": True,          # bool
    "dersler": ["Mat", "Fiz"]  # list
}
```

#### **Yöntem 2: dict() Fonksiyonu**
```python
# Boş dictionary
bos_sozluk = dict()

# Değerlerle
ogrenci = dict(isim="Ahmet", yas=20, not=85)

# Tuple listesinden
liste = [("isim", "Ahmet"), ("yas", 20)]
ogrenci = dict(liste)
```

---

### 4️⃣ DICTIONARY'YE ERİŞİM

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "bolum": "Bilgisayar"
}

# Köşeli parantez ile
print(ogrenci["isim"])  # Ahmet
print(ogrenci["yas"])   # 20

# ⚠️ DİKKAT: Olmayan anahtar hata verir!
# print(ogrenci["not"])  # KeyError!

# get() ile (güvenli)
print(ogrenci.get("isim"))    # Ahmet
print(ogrenci.get("not"))     # None (hata vermez)
print(ogrenci.get("not", 0))  # 0 (varsayılan değer)
```

---

### 5️⃣ ELEMAN EKLEME VE DEĞİŞTİRME

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20
}

# Yeni eleman ekleme
ogrenci["bolum"] = "Bilgisayar"
ogrenci["not"] = 85

print(ogrenci)
# {'isim': 'Ahmet', 'yas': 20, 'bolum': 'Bilgisayar', 'not': 85}

# Mevcut elemanı değiştirme
ogrenci["yas"] = 21
ogrenci["not"] = 90

print(ogrenci)
# {'isim': 'Ahmet', 'yas': 21, 'bolum': 'Bilgisayar', 'not': 90}
```

---

### 6️⃣ ELEMAN SİLME

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "bolum": "Bilgisayar",
    "not": 85
}

# del ile silme
del ogrenci["bolum"]
print(ogrenci)  # bolum silindi

# pop() ile silme (değeri döndürür)
not_degeri = ogrenci.pop("not")
print(f"Silinen not: {not_degeri}")  # 85
print(ogrenci)  # not silindi

# popitem() - Son eklenen çifti siler
son = ogrenci.popitem()
print(son)  # ('yas', 20)
```

---

### 7️⃣ in OPERATÖRÜ İLE KONTROL

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "not": 85
}

# Anahtar kontrolü
if "isim" in ogrenci:
    print("İsim bilgisi var")

if "bolum" not in ogrenci:
    print("Bölüm bilgisi yok")

# Değer kontrolü (keys, values kullan)
if "Ahmet" in ogrenci.values():
    print("Ahmet değeri var")
```

---

### 8️⃣ PRATİK ÖRNEKLER (Saat 1-2)

#### **Örnek 1: Telefon Rehberi**
```python
rehber = {
    "Ahmet": "0555 123 4567",
    "Mehmet": "0532 987 6543",
    "Ayşe": "0505 555 1234"
}

# Telefon arama
isim = input("Kimin telefonunu aramak istiyorsunuz? ")

if isim in rehber:
    print(f"{isim}: {rehber[isim]}")
else:
    print("Bu isim rehberde yok")
```

#### **Örnek 2: Ürün Fiyatları**
```python
urunler = {
    "Ekmek": 5,
    "Süt": 15,
    "Yumurta": 30,
    "Peynir": 80
}

# Alışveriş sepeti
sepet = ["Ekmek", "Süt", "Süt", "Yumurta"]

toplam = 0
for urun in sepet:
    toplam += urunler[urun]
    print(f"{urun}: {urunler[urun]} TL")

print(f"Toplam: {toplam} TL")
```

#### **Örnek 3: Kelime Sayacı**
```python
metin = "python python java python java java java"
kelimeler = metin.split()

sayac = {}
for kelime in kelimeler:
    if kelime in sayac:
        sayac[kelime] += 1
    else:
        sayac[kelime] = 1

print(sayac)
# {'python': 3, 'java': 4}
```

---

## 📖 SAAT 3: DICTIONARY METODLARI

### 1️⃣ keys() - Tüm Anahtarları Alma

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "not": 85
}

# Tüm anahtarlar
anahtarlar = ogrenci.keys()
print(anahtarlar)  # dict_keys(['isim', 'yas', 'not'])

# Liste'ye çevirme
anahtar_listesi = list(ogrenci.keys())
print(anahtar_listesi)  # ['isim', 'yas', 'not']

# Döngü ile
for anahtar in ogrenci.keys():
    print(anahtar)
```

---

### 2️⃣ values() - Tüm Değerleri Alma

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "not": 85
}

# Tüm değerler
degerler = ogrenci.values()
print(degerler)  # dict_values(['Ahmet', 20, 85])

# Liste'ye çevirme
deger_listesi = list(ogrenci.values())
print(deger_listesi)  # ['Ahmet', 20, 85]

# Pratik kullanım: Toplam
notlar = {
    "Ahmet": 85,
    "Mehmet": 90,
    "Ayşe": 78
}

ortalama = sum(notlar.values()) / len(notlar)
print(f"Ortalama: {ortalama}")  # 84.33
```

---

### 3️⃣ items() - Anahtar-Değer Çiftlerini Alma

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "not": 85
}

# Tüm çiftler
ciftler = ogrenci.items()
print(ciftler)
# dict_items([('isim', 'Ahmet'), ('yas', 20), ('not', 85)])

# En çok kullanılan: for döngüsü ile
for anahtar, deger in ogrenci.items():
    print(f"{anahtar}: {deger}")

# Çıktı:
# isim: Ahmet
# yas: 20
# not: 85
```

---

### 4️⃣ get() - Güvenli Erişim

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20
}

# Normal erişim (riskli)
# print(ogrenci["not"])  # KeyError!

# get() ile (güvenli)
not_degeri = ogrenci.get("not")
print(not_degeri)  # None

# Varsayılan değer ile
not_degeri = ogrenci.get("not", 0)
print(not_degeri)  # 0

# Pratik kullanım
if ogrenci.get("not"):
    print(f"Not: {ogrenci['not']}")
else:
    print("Not bilgisi yok")
```

---

### 5️⃣ update() - Birleştirme ve Güncelleme

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20
}

# Yeni elemanlar ekleme
yeni_bilgiler = {
    "bolum": "Bilgisayar",
    "not": 85
}

ogrenci.update(yeni_bilgiler)
print(ogrenci)
# {'isim': 'Ahmet', 'yas': 20, 'bolum': 'Bilgisayar', 'not': 85}

# Mevcut elemanı güncelleme
ogrenci.update({"yas": 21, "not": 90})
print(ogrenci)
# {'isim': 'Ahmet', 'yas': 21, 'bolum': 'Bilgisayar', 'not': 90}
```

---

### 6️⃣ DÖNGÜLERLE DICTIONARY

```python
notlar = {
    "Ahmet": 85,
    "Mehmet": 90,
    "Ayşe": 78,
    "Fatma": 92
}

# Yöntem 1: Sadece anahtarlar
for isim in notlar:
    print(isim)

# Yöntem 2: Anahtarlar ve değerler
for isim in notlar:
    print(f"{isim}: {notlar[isim]}")

# Yöntem 3: items() ile (EN PRATİK)
for isim, not_degeri in notlar.items():
    print(f"{isim}: {not_degeri}")

# Filtreleme
print("\n80'den yüksek notlar:")
for isim, not_degeri in notlar.items():
    if not_degeri >= 80:
        print(f"{isim}: {not_degeri}")
```

---

### 7️⃣ DİĞER METODLAR

```python
ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "not": 85
}

# clear() - Tüm elemanları sil
ogrenci_kopya = ogrenci.copy()
ogrenci_kopya.clear()
print(ogrenci_kopya)  # {}
print(ogrenci)        # Orijinal etkilenmez

# copy() - Kopya oluştur
ogrenci2 = ogrenci.copy()
ogrenci2["isim"] = "Mehmet"
print(ogrenci["isim"])   # Ahmet (değişmedi)
print(ogrenci2["isim"])  # Mehmet

# setdefault() - Yoksa ekle, varsa değer döndür
deger = ogrenci.setdefault("bolum", "Belirsiz")
print(deger)  # Belirsiz
print(ogrenci)  # bolum eklendi

# fromkeys() - Aynı değerle dictionary oluştur
isimler = ["Ahmet", "Mehmet", "Ayşe"]
notlar = dict.fromkeys(isimler, 0)
print(notlar)  # {'Ahmet': 0, 'Mehmet': 0, 'Ayşe': 0}
```

---

## 📖 SAAT 4: PROJE - ÖĞRENCİ NOT SİSTEMİ

### 🎯 Proje Analizi

**Özellikler:**
1. Öğrenci ekleme (isim, numara, notlar)
2. Öğrenci listeleme
3. Öğrenci arama
4. Not güncelleme
5. Öğrenci silme
6. Ortalama hesaplama
7. En başarılı öğrenci

**Veri Yapısı:**
```python
ogrenciler = {
    "101": {
        "isim": "Ahmet Yılmaz",
        "notlar": {
            "Matematik": 85,
            "Fizik": 90,
            "Kimya": 78
        }
    },
    "102": {
        "isim": "Ayşe Demir",
        "notlar": {
            "Matematik": 92,
            "Fizik": 88,
            "Kimya": 95
        }
    }
}
```

---

### 💻 Proje Kodu (Adım Adım)

```python
# Öğrenci Not Sistemi
# İç içe dictionary kullanımı

# Ana veri yapısı
ogrenciler = {}

def menu_goster():
    """Ana menüyü gösterir"""
    print("\n" + "=" * 40)
    print("    ÖĞRENCİ NOT SİSTEMİ")
    print("=" * 40)
    print("1. Öğrenci Ekle")
    print("2. Öğrencileri Listele")
    print("3. Öğrenci Ara")
    print("4. Not Güncelle")
    print("5. Öğrenci Sil")
    print("6. İstatistikler")
    print("7. Çıkış")
    print("=" * 40)

def ogrenci_ekle():
    """Yeni öğrenci ekler"""
    print("\n--- YENİ ÖĞRENCİ EKLEME ---")
    
    numara = input("Öğrenci Numarası: ")
    
    if numara in ogrenciler:
        print("❌ Bu numara zaten kayıtlı!")
        return
    
    isim = input("Öğrenci Adı Soyadı: ")
    
    # Notları alma
    notlar = {}
    print("\nDers notlarını girin (bitirmek için 'q'):")
    
    while True:
        ders = input("Ders adı (veya 'q'): ")
        if ders.lower() == 'q':
            break
        
        try:
            not_degeri = float(input(f"{ders} notu: "))
            if 0 <= not_degeri <= 100:
                notlar[ders] = not_degeri
            else:
                print("Not 0-100 arası olmalı!")
        except ValueError:
            print("Geçersiz not!")
    
    # Öğrenciyi kaydet
    ogrenciler[numara] = {
        "isim": isim,
        "notlar": notlar
    }
    
    print(f"✅ {isim} başarıyla eklendi!")

def ogrencileri_listele():
    """Tüm öğrencileri listeler"""
    if not ogrenciler:
        print("\n❌ Henüz öğrenci kaydı yok!")
        return
    
    print("\n" + "=" * 60)
    print("    TÜM ÖĞRENCİLER")
    print("=" * 60)
    
    for numara, bilgi in ogrenciler.items():
        print(f"\nNumara: {numara}")
        print(f"İsim: {bilgi['isim']}")
        print("Notlar:")
        
        if bilgi['notlar']:
            toplam = 0
            for ders, not_degeri in bilgi['notlar'].items():
                print(f"  - {ders}: {not_degeri}")
                toplam += not_degeri
            
            ortalama = toplam / len(bilgi['notlar'])
            print(f"Ortalama: {ortalama:.2f}")
        else:
            print("  Not kaydı yok")
        
        print("-" * 60)

def ogrenci_ara():
    """Öğrenci numarası ile arama"""
    numara = input("\nÖğrenci Numarası: ")
    
    if numara in ogrenciler:
        bilgi = ogrenciler[numara]
        print(f"\n📚 {bilgi['isim']}")
        print(f"Numara: {numara}")
        print("Notlar:")
        
        for ders, not_degeri in bilgi['notlar'].items():
            print(f"  - {ders}: {not_degeri}")
        
        if bilgi['notlar']:
            ortalama = sum(bilgi['notlar'].values()) / len(bilgi['notlar'])
            print(f"\nOrtalama: {ortalama:.2f}")
    else:
        print("❌ Öğrenci bulunamadı!")

def not_guncelle():
    """Öğrenci notunu günceller"""
    numara = input("\nÖğrenci Numarası: ")
    
    if numara not in ogrenciler:
        print("❌ Öğrenci bulunamadı!")
        return
    
    print(f"\n{ogrenciler[numara]['isim']} - Mevcut Notlar:")
    for ders, not_degeri in ogrenciler[numara]['notlar'].items():
        print(f"  - {ders}: {not_degeri}")
    
    ders = input("\nGüncellenecek ders: ")
    
    if ders in ogrenciler[numara]['notlar']:
        try:
            yeni_not = float(input("Yeni not: "))
            if 0 <= yeni_not <= 100:
                ogrenciler[numara]['notlar'][ders] = yeni_not
                print("✅ Not güncellendi!")
            else:
                print("❌ Not 0-100 arası olmalı!")
        except ValueError:
            print("❌ Geçersiz not!")
    else:
        print("❌ Ders bulunamadı!")

def ogrenci_sil():
    """Öğrenci kaydını siler"""
    numara = input("\nSilinecek Öğrenci Numarası: ")
    
    if numara in ogrenciler:
        isim = ogrenciler[numara]['isim']
        onay = input(f"{isim} silinecek. Emin misiniz? (e/h): ")
        
        if onay.lower() == 'e':
            del ogrenciler[numara]
            print("✅ Öğrenci silindi!")
        else:
            print("❌ İşlem iptal edildi!")
    else:
        print("❌ Öğrenci bulunamadı!")

def istatistikler():
    """Genel istatistikleri gösterir"""
    if not ogrenciler:
        print("\n❌ Henüz öğrenci kaydı yok!")
        return
    
    print("\n" + "=" * 40)
    print("    İSTATİSTİKLER")
    print("=" * 40)
    
    print(f"Toplam Öğrenci: {len(ogrenciler)}")
    
    # Tüm ortalamaları hesapla
    ortalamalar = {}
    for numara, bilgi in ogrenciler.items():
        if bilgi['notlar']:
            ort = sum(bilgi['notlar'].values()) / len(bilgi['notlar'])
            ortalamalar[numara] = ort
    
    if ortalamalar:
        # En yüksek ortalama
        en_yuksek_no = max(ortalamalar, key=ortalamalar.get)
        print(f"\nEn Başarılı: {ogrenciler[en_yuksek_no]['isim']}")
        print(f"Ortalama: {ortalamalar[en_yuksek_no]:.2f}")
        
        # Sınıf ortalaması
        sinif_ort = sum(ortalamalar.values()) / len(ortalamalar)
        print(f"\nSınıf Ortalaması: {sinif_ort:.2f}")

# Ana program döngüsü
def main():
    while True:
        menu_goster()
        
        secim = input("\nSeçiminiz: ")
        
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrencileri_listele()
        elif secim == "3":
            ogrenci_ara()
        elif secim == "4":
            not_guncelle()
        elif secim == "5":
            ogrenci_sil()
        elif secim == "6":
            istatistikler()
        elif secim == "7":
            print("\n👋 Program sonlandırılıyor...")
            break
        else:
            print("\n❌ Geçersiz seçim!")

# Programı başlat
if __name__ == "__main__":
    main()
```

---

### 🎯 Proje Özellikleri

**Kullanılan Kavramlar:**
- İç içe dictionary
- Dictionary metodları (items, keys, values)
- CRUD işlemleri
- Fonksiyonlar
- while döngüsü
- for döngüleri
- Hata yönetimi (try-except)
- Koşullu ifadeler

**Öğrenilen Beceriler:**
- Veri yapısı tasarımı
- Menü sistemi oluşturma
- Dictionary manipülasyonu
- İstatistik hesaplama
- Kullanıcı dostu arayüz

---

## 💡 ÖZET VE ÖNEMLİ NOTLAR

### Dictionary vs Liste

| Özellik | Liste | Dictionary |
|---------|-------|------------|
| Erişim | Index (0, 1, 2) | Anahtar (key) |
| Sıralama | Sıralı | Python 3.7+ sıralı |
| Arama Hızı | Yavaş O(n) | Hızlı O(1) |
| Kullanım | Aynı tip veriler | İlişkili veriler |

### Önemli Metodlar Özeti

```python
sozluk = {"a": 1, "b": 2}

# Erişim
sozluk["a"]           # 1
sozluk.get("c", 0)    # 0 (varsayılan)

# Ekleme/Güncelleme
sozluk["c"] = 3
sozluk.update({"d": 4})

# Silme
sozluk.pop("a")
del sozluk["b"]

# Bilgi
sozluk.keys()         # Anahtarlar
sozluk.values()       # Değerler
sozluk.items()        # Çiftler

# Kontrol
"a" in sozluk         # Anahtar var mı?
```

---

**Başarılar! 🚀**