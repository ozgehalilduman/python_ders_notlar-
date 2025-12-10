# Python Uygulama Sınavı
**4 Soru - 40 Puan - 40 Dakika**

---

## 📋 SINAV BİLGİLERİ

**Süre:** 40 Dakika  
**Toplam Puan:** 40  
**Geçme Notu:** 20 Puan (50%)

**Sınav Kuralları:**
- Her soruyu dikkatlice okuyun
- Kodlarınızı test edin
- Girinti ve iki nokta üst üste kullanımına dikkat edin
- Değişken isimlerini anlamlı yazın

---

## ✅ SORU 1 (8 Puan) - EN KOLAY SEVİYE
### Kişisel Bilgi Kartı

Kullanıcıdan **ad**, **soyad** ve **yaş** bilgilerini alın. Bu bilgileri aşağıdaki formatta ekrana yazdırın:

**Örnek Çalıştırma:**
```
Adınız: Mehmet
Soyadınız: Yılmaz
Yaşınız: 22

╔═══════════════════════════╗
║   KİŞİSEL BİLGİ KARTI    ║
╚═══════════════════════════╝
Ad Soyad: Mehmet Yılmaz
Yaş: 22
```

**Puanlama:**
- Input kullanımı (3 adet): 3 puan
- F-string formatlaması: 3 puan
- Düzgün çıktı: 2 puan

**İpuçları:**
- input() fonksiyonunu kullanın
- f-string ile birleştirme yapın
- Çizgiler için print() kullanabilirsiniz

---

## ✅ SORU 2 (10 Puan) - KOLAY SEVİYE
### Basit Alışveriş Hesabı

Kullanıcıdan **3 ürünün fiyatını** alın. Bu ürünlerin:
1. **Toplam tutarını** hesaplayın
2. Eğer toplam **100 TL ve üzeriyse** %10 indirim uygulayın
3. **Ödenecek tutarı** gösterin

**Örnek Çalıştırma 1:**
```
1. ürün fiyatı: 45
2. ürün fiyatı: 35
3. ürün fiyatı: 30

─────────────────────
Toplam: 110.0 TL
İndirim (%10): 11.0 TL
─────────────────────
ÖDENECEK: 99.0 TL
```

**Örnek Çalıştırma 2:**
```
1. ürün fiyatı: 20
2. ürün fiyatı: 30
3. ürün fiyatı: 25

─────────────────────
Toplam: 75.0 TL
İndirim: 0.0 TL
─────────────────────
ÖDENECEK: 75.0 TL
```

**Puanlama:**
- Input ve float dönüşümü (3 adet): 3 puan
- Toplam hesaplama: 2 puan
- if-else ile indirim kontrolü: 3 puan
- Doğru hesaplama ve çıktı: 2 puan

**İpuçları:**
- float(input()) kullanın
- if toplam >= 100: şeklinde kontrol edin
- İndirim = toplam * 0.10

---

## ✅ SORU 3 (12 Puan) - ORTA SEVİYE
### Kelime Analiz Programı

Kullanıcıdan bir **kelime** alın ve aşağıdaki analizleri yapın:

1. Kelimenin **kaç harfli** olduğunu
2. Kelimenin **tersini**
3. Kelimenin **palindrome** olup olmadığını (tersten okunuşu aynı mı?)
4. Kelimede **kaç sesli harf** olduğunu (a, e, ı, i, o, ö, u, ü)

**Örnek Çalıştırma 1:**
```
Bir kelime girin: kayak

═══════════════════════════
    KELİME ANALİZİ
═══════════════════════════
Kelime: kayak
Harf Sayısı: 5
Tersi: kayak
Palindrome: EVET ✓
Sesli Harf: 3
```

**Örnek Çalıştırma 2:**
```
Bir kelime girin: python

═══════════════════════════
    KELİME ANALİZİ
═══════════════════════════
Kelime: python
Harf Sayısı: 6
Tersi: nohtyp
Palindrome: HAYIR ✗
Sesli Harf: 1
```

**Puanlama:**
- Input ve lower() kullanımı: 1 puan
- len() ile harf sayısı: 2 puan
- [::-1] ile ters çevirme: 2 puan
- Palindrome kontrolü (if karşılaştırma): 3 puan
- for döngüsü ile sesli harf sayma: 4 puan

**İpuçları:**
- kelime.lower() ile küçük harfe çevirin
- ters = kelime[::-1]
- if kelime == ters: için palindrome kontrolü
- sesli = "aeıioöuü" tanımlayın
- for harf in kelime: ile döngü kurun

---

## ✅ SORU 4 (10 Puan) - ZOR SEVİYE
### 1-100 Arası Çarpım Tablosu Bulucu

Kullanıcıdan **1-10 arası** bir sayı alın (geçersiz girişlerde tekrar isteyin).

Geçerli sayı girildikten sonra, o sayının **1'den 10'a kadar çarpım tablosunu** gösterin.

Daha sonra, **1-100 arası** bu sayının **katlarının toplamını** hesaplayıp gösterin.

**Örnek Çalıştırma:**
```
1-10 arası bir sayı girin: 15
Geçersiz! 1-10 arası olmalı.
1-10 arası bir sayı girin: 5

═══════════════════════════
  5'İN ÇARPIM TABLOSU
═══════════════════════════
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

═══════════════════════════
1-100 ARASI 5'İN KATLARI
═══════════════════════════
5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100

Toplamları: 1050
```

**Puanlama:**
- Input ve doğrulama döngüsü (1-10 arası kontrol): 3 puan
- Çarpım tablosu (for döngüsü 1-10): 3 puan
- 1-100 arası katları bulma (for ve if): 2 puan
- Katların toplamını hesaplama: 2 puan

**İpuçları:**
- while döngüsü ile geçerli sayı alın
- İlk for döngüsü: for i in range(1, 11):
- İkinci for döngüsü: for i in range(1, 101):
- if i % sayi == 0: ile kat kontrolü
- toplam += i ile toplama

---

## 📊 PUAN DAĞILIMI

| Soru | Seviye | Puan | Konu |
|------|--------|------|------|
| 1 | En Kolay | 8 | Input, F-string |
| 2 | Kolay | 10 | Float, if-else, hesaplama |
| 3 | Orta | 12 | String işlemleri, döngü, palindrome |
| 4 | Zor | 10 | Doğrulama, çarpım tablosu, mod |
| **TOPLAM** | | **40** | |

---

## 🎯 BAŞARI KRİTERLERİ

| Puan | Değerlendirme |
|------|---------------|
| 36-40 | Mükemmel ⭐⭐⭐ |
| 32-35 | Çok İyi ⭐⭐ |
| 28-31 | İyi ⭐ |
| 24-27 | Orta |
| 20-23 | Geçer |
| 0-19 | Yetersiz (Daha fazla çalışma gerekli) |

---

## ⚠️ ÖNEMLİ HATIRLATMALAR

### Sınav Sırasında Dikkat Edilecekler:

1. **Girinti (Indentation)**
   ```python
   # YANLIŞ ❌
   if sayi > 0:
   print("Pozitif")
   
   # DOĞRU ✅
   if sayi > 0:
       print("Pozitif")  # 4 boşluk!
   ```

2. **İki Nokta Üst Üste (:)**
   ```python
   # YANLIŞ ❌
   for i in range(5)
       print(i)
   
   # DOĞRU ✅
   for i in range(5):  # : koymayı unutmayın!
       print(i)
   ```

3. **Input Tip Dönüşümü**
   ```python
   # YANLIŞ ❌
   yas = input("Yaş: ")  # String olarak gelir!
   if yas >= 18:  # HATA!
   
   # DOĞRU ✅
   yas = int(input("Yaş: "))  # int'e çevir
   if yas >= 18:  # Doğru çalışır
   ```

4. **= ile == Farkı**
   ```python
   # YANLIŞ ❌
   if sayi = 10:  # Atama operatörü!
   
   # DOĞRU ✅
   if sayi == 10:  # Karşılaştırma operatörü
   ```

5. **range() Bitiş Değeri**
   ```python
   # 1-10 arası için
   for i in range(1, 11):  # 11 yazmalısınız! (10 dahil)
       print(i)
   ```

---

## 💡 SORU ÇÖZME STRATEJİSİ

### Adım Adım Yaklaşım:

1. **Soruyu İki Kez Okuyun**
   - Ne istendiğini tam anlayın
   - Örneklere bakın

2. **Kağıda Plan Çizin**
   - Hangi değişkenler gerekli?
   - Hangi yapılar kullanılacak? (if, for, vb.)
   - Adım adım ne yapılmalı?

3. **Kod Yazarken**
   - Önce basit kısmı yazın
   - Test edin
   - Sonra karmaşık kısmı ekleyin
   - Tekrar test edin

4. **Hata Ayıklama**
   - Çalışmıyorsa print() ile kontrol edin
   - Girinti ve : kontrolü yapın
   - Değişken isimlerini kontrol edin

5. **Son Kontrol**
   - Örnek çıktılarla karşılaştırın
   - Tüm durumları test edin
   - Kod okunaklı mı?

---

## 📝 SINAVDAN ÖNCE KONTROL

Sınava girmeden önce bu soruları kendinize sorun:

- [ ] Input kullanabiliyorum
- [ ] int(), float() dönüşümlerini yapabiliyorum
- [ ] f-string kullanabiliyorum
- [ ] if-else yapısını kurabiliyorum
- [ ] for döngüsü yazabiliyorum
- [ ] String işlemleri yapabiliyorum (len, [::-1])
- [ ] Girinti (indentation) yapabiliyorum
- [ ] : (iki nokta) koymayı unutmuyorum

Hepsine "EVET" diyorsanız, hazırsınız! 💪

---

## 🎓 SON TAVSİYELER

1. **Acele Etmeyin** - 40 dakikanız var, dikkatli olun
2. **Kolay Sorularla Başlayın** - Özgüveniniz artsın
3. **Her Soruyu Test Edin** - Çalıştığından emin olun
4. **Yorumlar Ekleyin** - Kodunuzu açıklayın
5. **Pes Etmeyin** - Takılırsanız basitleştirin

**Başarılar! 🚀**

---

## 💻 SINAVDAN SONRA

Sınav bittiğinde:
1. Cevaplarınızı kontrol edin
2. Hatalarınızı analiz edin
3. Anlamadığınız kısımları sorun
4. Doğru çözümleri bir daha yazın

**Unutmayın:** Her sınav bir öğrenme fırsatıdır! 🌟