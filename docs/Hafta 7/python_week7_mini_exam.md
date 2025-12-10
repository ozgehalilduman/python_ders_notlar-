# Python 7. Hafta Mini Sınav
**Listeler - 5 Soru - 50 Puan - 50 Dakika**

---

## 📋 SINAV BİLGİLERİ

**Süre:** 50 Dakika  
**Toplam Puan:** 50  
**Geçme Notu:** 25 Puan (50%)

**Konu:** Listeler (Lists)

---

## ✅ SORU 1 (8 Puan) - KOLAY
### Alışveriş Listesi Oluşturucu

Kullanıcıdan **5 ürün adı** alın ve bunları bir listeye ekleyin. Ardından:
1. Tüm ürünleri **numaralandırarak** listeleyin
2. Listenin **uzunluğunu** gösterin
3. **İlk ve son** ürünü ekrana yazdırın

**Örnek Çalıştırma:**
```
1. ürün: ekmek
2. ürün: süt
3. ürün: yumurta
4. ürün: peynir
5. ürün: zeytin

═══════════════════════════
   ALIŞVERİŞ LİSTESİ
═══════════════════════════
1. ekmek
2. süt
3. yumurta
4. peynir
5. zeytin

Toplam ürün: 5
İlk ürün: ekmek
Son ürün: zeytin
```

**Puanlama:**
- 5 ürünü listeye ekleme: 3 puan
- Numaralı listeleme (döngü): 2 puan
- len() kullanımı: 1 puan
- İlk ve son eleman erişimi: 2 puan

**Kullanılacak Kavramlar:**
- Boş liste oluşturma
- append() metodu
- for döngüsü
- len() fonksiyonu
- Index erişimi [0] ve [-1]

---

## ✅ SORU 2 (10 Puan) - KOLAY-ORTA
### Sayı Listesi Analizi

Kullanıcıdan **6 adet sayı** alın ve bir listeye ekleyin. Ardından:
1. Tüm sayıların **toplamını** hesaplayın
2. **Ortalamasını** hesaplayın
3. **En büyük** ve **en küçük** sayıyı bulun
4. **Çift sayıları** ayrı bir listede gösterin

**Örnek Çalıştırma:**
```
1. sayı: 45
2. sayı: 12
3. sayı: 78
4. sayı: 23
5. sayı: 56
6. sayı: 34

═══════════════════════════
      ANALİZ SONUÇLARI
═══════════════════════════
Liste: [45, 12, 78, 23, 56, 34]
Toplam: 248
Ortalama: 41.33
En Büyük: 78
En Küçük: 12
Çift Sayılar: [12, 78, 56, 34]
```

**Puanlama:**
- 6 sayıyı listeye ekleme: 2 puan
- Toplam hesaplama: 2 puan
- Ortalama hesaplama: 1 puan
- Max ve min bulma: 2 puan
- Çift sayıları filtreleme: 3 puan

**Kullanılacak Kavramlar:**
- Liste oluşturma ve append()
- sum(), len() fonksiyonları
- max(), min() fonksiyonları
- for döngüsü ile filtreleme
- if koşulu ile çift sayı kontrolü (% 2 == 0)

---

## ✅ SORU 3 (12 Puan) - ORTA
### Not Defteri Uygulaması

Kullanıcıya bir menü sunun:
1. **Not ekle** - Listeye yeni not ekler
2. **Notları listele** - Tüm notları numaralı gösterir
3. **Not sil** - Kullanıcının seçtiği notu siler
4. **Çıkış** - Programı sonlandırır

Program, kullanıcı "Çıkış" seçene kadar çalışmalı.

**Örnek Çalıştırma:**
```
═══════════════════════════
      NOT DEFTERİ
═══════════════════════════
1. Not ekle
2. Notları listele
3. Not sil
4. Çıkış
Seçim: 1

Not: Python öğreniyorum
✅ Not eklendi!

═══════════════════════════
1. Not ekle
2. Notları listele
3. Not sil
4. Çıkış
Seçim: 2

📝 NOTLARIM:
1. Python öğreniyorum

═══════════════════════════
1. Not ekle
2. Notları listele
3. Not sil
4. Çıkış
Seçim: 4

👋 Çıkış yapılıyor...
```

**Puanlama:**
- Boş liste oluşturma: 1 puan
- while True döngüsü ve menü: 2 puan
- Not ekleme (append): 2 puan
- Notları listeleme (for döngüsü): 2 puan
- Not silme (pop veya remove): 3 puan
- Çıkış (break): 1 puan
- Formatlı çıktı: 1 puan

**Kullanılacak Kavramlar:**
- Liste oluşturma
- while True döngüsü
- append() metodu
- for döngüsü ile listeleme
- pop() veya remove() metodu
- break ifadesi

---

## ✅ SORU 4 (10 Puan) - ORTA
### Kelime Oyunu - Palindrome Listesi

Kullanıcıdan **5 kelime** alın. Her kelime için:
1. Kelimenin **tersini** bulun
2. **Palindrome** olup olmadığını kontrol edin
3. Palindrome olanları **ayrı bir listeye** ekleyin
4. Sonunda **kaç tane palindrome** olduğunu gösterin

**Örnek Çalıştırma:**
```
1. kelime: kayak
"kayak" tersi "kayak" - PALİNDROME ✓

2. kelime: python
"python" tersi "nohtyp" - Palindrome değil

3. kelime: ada
"ada" tersi "ada" - PALİNDROME ✓

4. kelime: level
"level" tersi "level" - PALİNDROME ✓

5. kelime: hello
"hello" tersi "olleh" - Palindrome değil

═══════════════════════════
      SONUÇLAR
═══════════════════════════
Girilen Kelimeler: ['kayak', 'python', 'ada', 'level', 'hello']
Palindrome Kelimeler: ['kayak', 'ada', 'level']
Toplam Palindrome: 3
```

**Puanlama:**
- 5 kelimeyi listeye ekleme: 2 puan
- Kelime ters çevirme ([::-1]): 2 puan
- Palindrome kontrolü (if karşılaştırma): 2 puan
- Palindrome listesi oluşturma: 2 puan
- Formatlı çıktı ve sayma: 2 puan

**Kullanılacak Kavramlar:**
- Liste oluşturma
- append() metodu
- String slicing [::-1]
- if-else koşulu
- İki liste yönetimi
- len() fonksiyonu

---

## ✅ SORU 5 (10 Puan) - ORTA-ZOR
### Öğrenci Not Sistemi

Öğrenci bilgilerini tutacak bir program yazın:

1. **3 öğrencinin** ismini ve notunu alın (iki ayrı liste: isimler ve notlar)
2. Her öğrenci için **harf notunu** hesaplayın:
   - 85-100: A
   - 70-84: B
   - 50-69: C
   - 0-49: F
3. Tüm öğrencileri **not ortalamasına göre** (büyükten küçüğe) sıralayarak gösterin
4. **Sınıf ortalamasını** hesaplayın

**Örnek Çalıştırma:**
```
1. öğrenci:
İsim: Ahmet
Not: 85

2. öğrenci:
İsim: Ayşe
Not: 92

3. öğrenci:
İsim: Mehmet
Not: 78

═══════════════════════════
   SINIF NOT TABLOSU
═══════════════════════════
1. Ayşe    : 92 (A)
2. Ahmet   : 85 (A)
3. Mehmet  : 78 (B)
═══════════════════════════
Sınıf Ortalaması: 85.0
```

**Puanlama:**
- İki liste oluşturma (isim, not): 2 puan
- 3 öğrenci bilgisi alma: 1 puan
- Harf notu hesaplama (if-elif-else): 3 puan
- Sıralama (sorted veya sort kullanarak): 2 puan
- Sınıf ortalaması: 1 puan
- Formatlı tablo çıktısı: 1 puan

**Kullanılacak Kavramlar:**
- İki paralel liste kullanımı
- append() metodu
- if-elif-else yapısı
- Sıralama (sorted veya sort)
- zip() fonksiyonu (opsiyonel)
- sum() ve len() fonksiyonları

---

## 📊 PUAN DAĞILIMI

| Soru | Seviye | Puan | Konu |
|------|--------|------|------|
| 1 | Kolay | 8 | Liste temel işlemler |
| 2 | Kolay-Orta | 10 | Liste analizi, filtreleme |
| 3 | Orta | 12 | Menü sistemi, CRUD işlemleri |
| 4 | Orta | 10 | Palindrome, çoklu liste |
| 5 | Orta-Zor | 10 | Paralel liste, sıralama |
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

### Liste İşlemleri:

```python
# ✅ DOĞRU Kullanımlar:

# 1. Boş liste oluşturma
liste = []

# 2. Eleman ekleme
liste.append("eleman")

# 3. Eleman silme
liste.remove("eleman")  # Değer ile
liste.pop(0)           # Index ile
liste.pop()            # Son elemanı sil

# 4. Erişim
ilk = liste[0]
son = liste[-1]

# 5. Uzunluk
uzunluk = len(liste)

# 6. Döngü
for eleman in liste:
    print(eleman)

# 7. Index ile döngü
for i in range(len(liste)):
    print(liste[i])
```

### Yaygın Hatalar:

```python
# ❌ YANLIŞ:
liste = [1, 2, 3]
print(liste[5])  # IndexError!

# ✅ DOĞRU:
if len(liste) > 5:
    print(liste[5])

# ❌ YANLIŞ:
liste.append([4, 5])  # İç içe liste olur!

# ✅ DOĞRU:
liste.extend([4, 5])  # Listeyi genişletir

# ❌ YANLIŞ:
liste2 = liste  # Referans kopyalama!

# ✅ DOĞRU:
liste2 = liste.copy()  # Gerçek kopya
```

---

## 💡 SORU ÇÖZME İPUÇLARI

### Genel Strateji:

1. **Önce Listeyi Oluşturun**
   ```python
   liste = []  # veya liste = [1, 2, 3]
   ```

2. **Eleman Eklemek İçin**
   ```python
   for i in range(5):
       eleman = input("Değer: ")
       liste.append(eleman)
   ```

3. **Liste Üzerinde Gezme**
   ```python
   for eleman in liste:
       print(eleman)
   ```

4. **Filtreleme İşlemleri**
   ```python
   yeni_liste = []
   for eleman in liste:
       if kosul:
           yeni_liste.append(eleman)
   ```

5. **Menü Sistemi**
   ```python
   while True:
       print("MENÜ")
       secim = input("Seçim: ")
       
       if secim == "çıkış":
           break
   ```

---

## 📝 SINAVDAN ÖNCE KONTROL

- [ ] Boş liste oluşturabiliyorum: `liste = []`
- [ ] append() kullanabiliyorum
- [ ] for döngüsü ile liste gezebiliyorum
- [ ] [0] ve [-1] ile erişim yapabiliyorum
- [ ] len() kullanabiliyorum
- [ ] remove() ve pop() farkını biliyorum
- [ ] while True ve break kullanabiliyorum
- [ ] İki listeyi paralel kullanabiliyorum

---

## 🎓 SON TAVSİYELER

1. **Her Soruyu Test Edin** - Çalıştığından emin olun
2. **Basit Başlayın** - Önce temel işlevselliği yazın
3. **Print ile Kontrol Edin** - Liste içeriğini görerek ilerleyin
4. **Index Hatalarına Dikkat** - len() kontrolü yapın
5. **Menü Sorularında** - Her seçeneği test edin

**İyi Şanslar! 🍀**