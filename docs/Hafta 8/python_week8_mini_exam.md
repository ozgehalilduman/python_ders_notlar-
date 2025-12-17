# Python 8. Hafta Mini Sınav
**Sözlükler (Dictionaries) - 5 Soru - 50 Puan - 50 Dakika**

---

## 📋 SINAV BİLGİLERİ

**Süre:** 50 Dakika  
**Toplam Puan:** 50  
**Geçme Notu:** 25 Puan (50%)

**Konu:** Sözlükler (Dictionaries)

---

## ✅ SORU 1 (8 Puan) - KOLAY
### Kişisel Bilgi Kartı (Dictionary)

Kullanıcıdan aşağıdaki bilgileri alın ve bir dictionary'de saklayın:
- İsim
- Soyad
- Yaş
- Şehir
- Meslek

Ardından tüm bilgileri **key: value** formatında ekrana yazdırın.

**Örnek Çalıştırma:**
```
İsim: Ahmet
Soyad: Yılmaz
Yaş: 28
Şehir: İstanbul
Meslek: Mühendis

═══════════════════════════
   KİŞİSEL BİLGİLER
═══════════════════════════
isim: Ahmet
soyad: Yılmaz
yas: 28
sehir: İstanbul
meslek: Mühendis
```

**Puanlama:**
- Dictionary oluşturma: 2 puan
- 5 bilgiyi dictionary'e ekleme: 3 puan
- items() ile döngü kurma: 2 puan
- Formatlı çıktı: 1 puan

**Kullanılacak Kavramlar:**
- Dictionary oluşturma {}
- Key-value ataması
- items() metodu
- for döngüsü

---

## ✅ SORU 2 (10 Puan) - KOLAY-ORTA
### Ürün Fiyat Listesi ve Alışveriş Sepeti

Aşağıdaki ürün fiyatlarını bir dictionary'de saklayın:
```
Ekmek: 5 TL
Süt: 15 TL
Yumurta: 30 TL
Peynir: 80 TL
Zeytin: 60 TL
```

Kullanıcıdan **3 ürün** isteyin. Her ürün için:
1. Ürün fiyatını gösterin
2. **Toplam tutarı** hesaplayın
3. Eğer ürün yoksa **"Bu ürün stokta yok"** yazdırın

**Örnek Çalıştırma:**
```
1. ürün: Ekmek
Ekmek: 5 TL ✓

2. ürün: Süt
Süt: 15 TL ✓

3. ürün: Domates
❌ Bu ürün stokta yok!

═══════════════════════════
Geçerli Ürünler: 2
Toplam Tutar: 20 TL
```

**Puanlama:**
- Ürün dictionary'si oluşturma: 2 puan
- 3 ürün alma döngüsü: 2 puan
- Ürün kontrolü (in operatörü): 2 puan
- Fiyat gösterme: 2 puan
- Toplam hesaplama: 2 puan

**Kullanılacak Kavramlar:**
- Dictionary oluşturma
- in operatörü
- for döngüsü
- Koşullu kontrol (if-else)
- Toplama işlemi

---

## ✅ SORU 3 (12 Puan) - ORTA
### Telefon Rehberi

Bir telefon rehberi programı yazın. Kullanıcıya menü sunun:
1. **Kişi Ekle** - İsim ve telefon numarası kaydet
2. **Kişi Ara** - İsme göre numara bul
3. **Tüm Kişileri Listele** - Tüm rehberi göster
4. **Kişi Sil** - İsme göre kişiyi sil
5. **Çıkış**

**Örnek Çalıştırma:**
```
═══════════════════════════
    TELEFON REHBERİ
═══════════════════════════
1. Kişi Ekle
2. Kişi Ara
3. Tüm Kişileri Listele
4. Kişi Sil
5. Çıkış
Seçim: 1

İsim: Ahmet
Telefon: 0555 123 4567
✅ Ahmet eklendi!

═══════════════════════════
Seçim: 2

Aranacak isim: Ahmet
📞 Ahmet: 0555 123 4567

═══════════════════════════
Seçim: 3

📖 TELEFON REHBERİ:
1. Ahmet: 0555 123 4567

═══════════════════════════
Seçim: 5
👋 Çıkış yapılıyor...
```

**Puanlama:**
- Boş dictionary oluşturma: 1 puan
- while döngüsü ve menü: 2 puan
- Kişi ekleme: 2 puan
- Kişi arama (get veya in): 2 puan
- Listeleme (items ile döngü): 2 puan
- Kişi silme (pop veya del): 2 puan
- Çıkış (break): 1 puan

**Kullanılacak Kavramlar:**
- Dictionary oluşturma
- while True döngüsü
- Dictionary'ye ekleme (sozluk[key] = value)
- get() veya in ile arama
- items() ile listeleme
- pop() veya del ile silme

---

## ✅ SORU 4 (10 Puan) - ORTA
### Kelime Frekans Sayacı

Kullanıcıdan bir **cümle** alın. Bu cümledeki:
1. Her kelimenin **kaç kere geçtiğini** hesaplayın
2. Kelimeleri **frekansa göre** (çoktan aza) sıralayın
3. Sonuçları gösterin

**Örnek Çalıştırma:**
```
Bir cümle girin: python python java python java java java c

═══════════════════════════
   KELİME FREKANSI
═══════════════════════════
java: 4 kere
python: 3 kere
c: 1 kere
```

**Puanlama:**
- Cümleyi split() ile ayırma: 1 puan
- Boş dictionary oluşturma: 1 puan
- Döngü ile kelime sayma: 4 puan
- Sıralama (sorted): 2 puan
- Formatlı çıktı: 2 puan

**Kullanılacak Kavramlar:**
- split() metodu
- Dictionary oluşturma
- for döngüsü
- if-else ile sayma
- sorted() fonksiyonu
- items() metodu

**İpucu:**
```python
# Sıralama için
sorted(sozluk.items(), key=lambda x: x[1], reverse=True)
# VEYA manuel sıralama
```

---

## ✅ SORU 5 (10 Puan) - ORTA-ZOR
### Mini Öğrenci Not Sistemi

**3 öğrencinin** bilgilerini saklayan bir sistem yapın. Her öğrenci için:
- İsim
- Numara
- 3 ders notu (Matematik, Fizik, Kimya)

Programınız:
1. Öğrencileri ve notlarını **dictionary içinde dictionary** olarak saklayın
2. Her öğrencinin **not ortalamasını** hesaplayın
3. **En yüksek ortalamaya** sahip öğrenciyi bulun
4. Tüm bilgileri **düzenli bir tablo** şeklinde gösterin

**Örnek Çalıştırma:**
```
1. Öğrenci:
Numara: 101
İsim: Ahmet
Matematik: 85
Fizik: 90
Kimya: 78

2. Öğrenci:
Numara: 102
İsim: Ayşe
Matematik: 92
Fizik: 88
Kimya: 95

3. Öğrenci:
Numara: 103
İsim: Mehmet
Matematik: 70
Fizik: 75
Kimya: 80

═══════════════════════════════════════
        ÖĞRENCİ NOT TABLOSU
═══════════════════════════════════════
No    İsim      Mat   Fiz   Kim   Ort
101   Ahmet     85    90    78    84.33
102   Ayşe      92    88    95    91.67
103   Mehmet    70    75    80    75.00
═══════════════════════════════════════
En Başarılı: Ayşe (91.67)
```

**Puanlama:**
- İç içe dictionary oluşturma: 2 puan
- 3 öğrenci bilgisi alma: 2 puan
- Ortalama hesaplama: 2 puan
- En yüksek ortalamayı bulma: 2 puan
- Tablo formatında çıktı: 2 puan

**Veri Yapısı Örneği:**
```python
ogrenciler = {
    "101": {
        "isim": "Ahmet",
        "notlar": {
            "Matematik": 85,
            "Fizik": 90,
            "Kimya": 78
        }
    }
}
```

**Kullanılacak Kavramlar:**
- İç içe dictionary
- items() metodu
- İç içe döngüler
- values() metodu
- sum() ve len() fonksiyonları
- max() fonksiyonu

---

## 📊 PUAN DAĞILIMI

| Soru | Seviye | Puan | Konu |
|------|--------|------|------|
| 1 | Kolay | 8 | Dictionary temel işlemler |
| 2 | Kolay-Orta | 10 | Dictionary erişim, toplam |
| 3 | Orta | 12 | CRUD işlemleri, menü |
| 4 | Orta | 10 | Kelime sayma, sıralama |
| 5 | Orta-Zor | 10 | İç içe dictionary |
| **TOPLAM** | | **50** | |

---

## 🎯 BAŞARI KRİTERLERİ

| Puan | Değerlendirme |
|------|---------------|
| 45-50 | Mükemmel ⭐⭐⭐ |
| 40-44 | Çok İyi ⭐⭐ |
| 35-39 | İyi ⭐ |
| 30-34 | Orta |
| 25-29 | Geçer |
| 0-24 | Yetersiz |

---

## ⚠️ ÖNEMLİ HATIRLATMALAR

### Dictionary Temel İşlemler:

```python
# ✅ DOĞRU Kullanımlar:

# 1. Dictionary oluşturma
sozluk = {}
sozluk = {"anahtar": "değer"}

# 2. Eleman ekleme/değiştirme
sozluk["yeni"] = "değer"

# 3. Erişim (2 yöntem)
deger = sozluk["anahtar"]        # Riskli (KeyError)
deger = sozluk.get("anahtar")    # Güvenli (None döner)

# 4. Kontrol
if "anahtar" in sozluk:
    print("Var")

# 5. Silme
sozluk.pop("anahtar")
del sozluk["anahtar"]

# 6. Metodlar
sozluk.keys()      # Anahtarlar
sozluk.values()    # Değerler
sozluk.items()     # Çiftler

# 7. Döngü
for anahtar, deger in sozluk.items():
    print(f"{anahtar}: {deger}")
```

### Yaygın Hatalar:

```python
# ❌ YANLIŞ:
sozluk = {"a": 1}
print(sozluk["b"])  # KeyError!

# ✅ DOĞRU:
print(sozluk.get("b", 0))  # 0 döner

# ❌ YANLIŞ:
sozluk = {"a": 1}
sozluk2 = sozluk  # Referans kopyalama!

# ✅ DOĞRU:
sozluk2 = sozluk.copy()  # Gerçek kopya

# ❌ YANLIŞ:
for anahtar in sozluk:
    print(sozluk[anahtar])  # Uzun yol

# ✅ DOĞRU:
for anahtar, deger in sozluk.items():
    print(deger)  # Kısa yol
```

---

## 💡 SORU ÇÖZME İPUÇLARI

### 1. Dictionary Oluşturma

```python
# Boş dictionary
sozluk = {}

# Input ile doldurma
for i in range(3):
    anahtar = input("Anahtar: ")
    deger = input("Değer: ")
    sozluk[anahtar] = deger
```

### 2. Arama İşlemleri

```python
# Güvenli arama
if anahtar in sozluk:
    print(sozluk[anahtar])
else:
    print("Bulunamadı")

# VEYA get() ile
deger = sozluk.get(anahtar, "Bulunamadı")
print(deger)
```

### 3. Döngü ile İşlemler

```python
# Tüm öğeleri listeleme
for key, value in sozluk.items():
    print(f"{key}: {value}")

# Toplam hesaplama (sayılar için)
toplam = sum(sozluk.values())

# Filtreleme
yeni = {k: v for k, v in sozluk.items() if v > 50}
```

### 4. İç İçe Dictionary

```python
# Oluşturma
veri = {
    "101": {
        "isim": "Ahmet",
        "yas": 20
    }
}

# Erişim
print(veri["101"]["isim"])  # Ahmet

# Döngü
for no, bilgi in veri.items():
    print(f"No: {no}")
    for key, value in bilgi.items():
        print(f"  {key}: {value}")
```

---

## 📝 SINAVDAN ÖNCE KONTROL

- [ ] Dictionary oluşturabiliyorum: `sozluk = {}`
- [ ] Key-value ataması yapabiliyorum: `sozluk["key"] = "value"`
- [ ] in operatörü kullanabiliyorum
- [ ] get() metodunu biliyorum
- [ ] items() ile döngü kurabiliyorum
- [ ] pop() ve del ile silme yapabiliyorum
- [ ] values() ile toplam hesaplayabiliyorum
- [ ] İç içe dictionary kullanabiliyorum

---

## 🎓 SON TAVSİYELER

1. **get() Kullanın** - KeyError'dan kaçının
2. **items() ile Döngü** - En pratik yöntem
3. **in ile Kontrol** - Emin olun, sonra erişin
4. **İç İçe Dictionary** - Adım adım ilerleyin
5. **Test Edin** - Her işlemden sonra print() yapın

**İyi Şanslar! 🍀**