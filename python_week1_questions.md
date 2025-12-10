# Python 1. Hafta Soruları
**Değişkenler, Print Formatlaması ve Input Komutları**

---

## 🎯 Öğrenme Hedefleri
- Değişken tanımlama (int, float, string)
- print() fonksiyonu ve f-string formatlaması
- input() ile kullanıcıdan veri alma
- Temel matematiksel işlemler
- Formatlı ekran çıktıları oluşturma

---

## ⭐ Kolay Seviye Sorular (1-15)

### ✅ Soru 1: Market Alışverişi Hesaplama
Bir market alışverişinde, bir ürünün fiyatı **12.5 TL** ve **4 adet** alınmıştır. Bu alışverişin toplam tutarını hesaplayan bir Python programı yazınız.

**Beklenen Çıktı:**
```
=== MARKET FİŞİ ===
Ürün Fiyatı: 12.5 TL
Adet: 4
------------------
Toplam Tutar: 50.0 TL
```

**İpucu:** f-string kullanın: `print(f"Toplam: {toplam} TL")`

---

### ✅ Soru 2: Kredi Kartı Borcu Hesaplama
Bir kişinin kredi kartı borcu **1500 TL**'dir. Aylık faiz oranı **%2**'dir. Faiz ile birlikte toplam borcunu hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
💳 KREDİ KARTI BORÇ HESAPLAMA
Borç: 1500 TL
Faiz Oranı: %2
Faiz Tutarı: 30.0 TL
━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam Borç: 1530.0 TL
```

---

### ✅ Soru 3: Seyahat Mesafesi Hesaplama
Bir araba **80 km/saat** hızla **3 saat** boyunca hareket etmektedir. Aracın aldığı toplam mesafeyi hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🚗 SEYAHAT BİLGİLERİ
Hız: 80 km/saat
Süre: 3 saat
Alınan Mesafe: 240 km
```

**Formül:** Mesafe = Hız × Zaman

---

### ✅ Soru 4: Sinema Bileti Fiyatı Hesaplama
Bir sinemada öğrenci bileti **20 TL**, yetişkin bileti **35 TL**'dir. **3 öğrenci** ve **2 yetişkin** bileti alınıyor. Toplam fiyatı hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🎬 SİNEMA BİLET HESABI
Öğrenci Biletleri: 3 x 20 TL = 60 TL
Yetişkin Biletleri: 2 x 35 TL = 70 TL
────────────────────────────
TOPLAM: 130 TL
```

---

### ✅ Soru 5: Yolculuk Süresi Hesaplama
Bir tren **500 km** mesafeyi **100 km/saat** hızla gitmektedir. Yolculuk süresini hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🚄 TREN YOLCULUĞU
Mesafe: 500 km
Hız: 100 km/saat
Süre: 5.0 saat
```

**Formül:** Süre = Mesafe ÷ Hız

---

### ✅ Soru 6: Sınıfın Ortalama Notunu Hesaplama
Bir sınıftaki 4 öğrencinin notları sırasıyla **85.5**, **90.0**, **78.5** ve **88.0**'dir. Bu notların ortalamasını hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
📚 SINIF NOT ORTALAMASI
Öğrenci 1: 85.5
Öğrenci 2: 90.0
Öğrenci 3: 78.5
Öğrenci 4: 88.0
─────────────────
Ortalama: 85.5
```

---

### ✅ Soru 7: Araba Yakıt Tüketimi Hesaplama
Bir araba 100 kilometrede **7 litre** yakıt tüketmektedir. **350 km** yol gidildiğinde toplam yakıt tüketimini hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
⛽ YAKIT TÜKETİMİ HESABI
Gidilen Mesafe: 350 km
100 km'de Tüketim: 7 litre
Toplam Tüketim: 24.5 litre
```

---

### ✅ Soru 8: Telefon Faturası Hesaplama
Bir telefon hattının aylık sabit ücreti **50 TL**'dir. Dakika başına ücret **0.1 TL**'dir. **300 dakika** konuşma yapılmıştır. Toplam faturayı hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
📱 TELEFON FATURASI
Sabit Ücret: 50 TL
Konuşma: 300 dakika x 0.1 TL = 30.0 TL
═══════════════════════════════
TOPLAM: 80.0 TL
```

---

### ✅ Soru 9: Çalışan Maaşı ve Ek Ödeme Hesaplama
Bir çalışanın temel maaşı **3500 TL**'dir. **20 saat** fazla mesai yapmıştır ve fazla mesai saatlik ücreti **25 TL**'dir. Toplam maaşını hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
💼 MAAŞ HESABI
Temel Maaş: 3500 TL
Fazla Mesai: 20 saat x 25 TL = 500 TL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Toplam Maaş: 4000 TL
```

---

### ✅ Soru 10: Bir Ürünün İndirimli Fiyatı
Bir ürünün orijinal fiyatı **250 TL**'dir. **%15** indirim uygulanmaktadır. İndirimli fiyatı hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🏷️  İNDİRİM HESAPLAMA
Orijinal Fiyat: 250 TL
İndirim Oranı: %15
İndirim Tutarı: 37.5 TL
─────────────────────
İndirimli Fiyat: 212.5 TL
```

---

### ✅ Soru 11: Bir Kişinin Yaşını Hesaplama
Bir kişinin doğum yılı **1995**'tir. Mevcut yıl **2025**'tir. Yaşını hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🎂 YAŞ HESAPLAMA
Doğum Yılı: 1995
Şu Anki Yıl: 2025
Yaşınız: 30
```

---

### ✅ Soru 12: Taksi Ücret Hesaplama
Taksi açılış ücreti **15 TL**, kilometre başı ücret **5 TL**'dir. **12 km** yol gidilmiştir. Toplam taksi ücretini hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🚕 TAKSİ ÜCRETİ
Açılış: 15 TL
Mesafe: 12 km x 5 TL = 60 TL
═════════════════════
TOPLAM: 75 TL
```

---

### ✅ Soru 13: Pizza Sipariş Maliyeti
Bir pizza siparişinde pizza **85 TL**, içecek **15 TL**, teslimat **10 TL**'dir. Toplam sipariş maliyetini hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🍕 SİPARİŞ ÖZETİ
Pizza: 85 TL
İçecek: 15 TL
Teslimat: 10 TL
────────────────
TOPLAM: 110 TL
```

---

### ✅ Soru 14: Spor Salonu Aylık Ücret
Günlük antrenman ücreti **50 TL**'dir. **22 gün** antrenmana gidilmiştir. Aylık toplam ücreti hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🏋️  SPOR SALONU HESABI
Günlük Ücret: 50 TL
Gidilen Gün: 22
Toplam Tutar: 1100 TL
```

---

### ✅ Soru 15: Kitap Okuma Hızı
Bir kişi **3 saatte** **120 sayfa** kitap okumuştur. Saatte kaç sayfa okuduğunu hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
📖 OKUMA HIZI
Okunan Sayfa: 120
Geçen Süre: 3 saat
Saatlik Hız: 40.0 sayfa/saat
```

---

## 🌟 Orta Seviye Sorular (16-30)

### ✅ Soru 16: Elektrik Faturası Hesaplama
Bir evde **280 kWh** elektrik tüketilmiştir. kWh başına fiyat **1.2 TL**'dir. Elektrik faturasını hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
⚡ ELEKTRİK FATURASI
Tüketim: 280 kWh
Birim Fiyat: 1.2 TL/kWh
═══════════════════════
ÖDENECEK TUTAR: 336.0 TL
```

---

### ✅ Soru 17: Dolar/TL Kuru ile Döviz Bozdurma
Bir kişinin **1000 dolar**ı vardır. 1 dolar **18.50 TL**'dir. Kaç TL alacağını hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
💵 DÖVİZ BOZDURMA
Miktar: 1000 USD
Kur: 18.50 TL
━━━━━━━━━━━━━━━━━━━━
Alacağınız: 18500.0 TL
```

---

### ✅ Soru 18: Restaurant Hesabı ve Bahşiş
Bir restoranda hesap tutarı **350 TL**'dir. **%15** bahşiş bırakılacaktır. Bahşiş miktarını ve toplam ödemeyi hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🍽️  RESTAURANT HESABI
Hesap: 350 TL
Bahşiş (%15): 52.5 TL
─────────────────────
TOPLAM: 402.5 TL
```

---

### ✅ Soru 19: Araba Kiralama Toplam Maliyet
Günlük araba kirası **75 TL**'dir. **3 günlüğüne** kiralanacaktır. Sigorta ücreti **20 TL**'dir. Toplam maliyeti hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🚗 ARABA KİRALAMA
Günlük Kira: 75 TL x 3 gün = 225 TL
Sigorta: 20 TL
═════════════════════════════════
TOPLAM MALİYET: 245 TL
```

---

### ✅ Soru 20: Diyet Kalori Hesaplama
Bir kişinin günlük öğün kalorileri: Kahvaltı **350 kcal**, Öğle **650 kcal**, Akşam **550 kcal**, Atıştırmalık **200 kcal**. Günlük toplam kaloriyi hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🍎 GÜNLÜK KALORİ TAKIBI
Kahvaltı:      350 kcal
Öğle Yemeği:   650 kcal
Akşam Yemeği:  550 kcal
Atıştırmalık:  200 kcal
───────────────────────
TOPLAM:       1750 kcal
```

---

### ✅ Soru 21: Havuz Doldurma Süresi
Bir havuzun hacmi **15000 litre**dir. Musluk debisi **50 litre/dakika**dır. Havuzun dolma süresini (dakika cinsinden) hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
💧 HAVUZ DOLDURMA
Havuz Hacmi: 15000 litre
Musluk Debisi: 50 litre/dk
Dolma Süresi: 300.0 dakika (5.0 saat)
```

---

### ✅ Soru 22: Tatil Paketi Maliyet
Bir tatil paketinde Uçak bileti **1200 TL**, Otel (5 gece) **2500 TL**, Tur paketi **800 TL**. Toplam tatil maliyetini hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
✈️  TATİL PAKETİ
Uçak Bileti:    1200 TL
Otel (5 gece):  2500 TL
Tur Paketi:      800 TL
━━━━━━━━━━━━━━━━━━━━━━━
TOPLAM:         4500 TL
```

---

### ✅ Soru 23: Online Kurs Gelir Hesaplama
Bir eğitmen 3 online kurs vermektedir. Kurs 1: **45 öğrenci**, Kurs 2: **30 öğrenci**, Kurs 3: **60 öğrenci**. Her kursun fiyatı **200 TL**'dir. Toplam geliri hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
💻 ONLİNE KURS GELİRİ
Kurs 1: 45 öğrenci x 200 TL = 9000 TL
Kurs 2: 30 öğrenci x 200 TL = 6000 TL
Kurs 3: 60 öğrenci x 200 TL = 12000 TL
═══════════════════════════════════════
TOPLAM GELİR: 27000 TL
```

---

### ✅ Soru 24: Bisiklet Kiralama
Saatlik bisiklet kiralama ücreti **25 TL**'dir. Bisiklet **4.5 saat** kiralanmıştır. Toplam ücreti hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
🚴 BİSİKLET KİRALAMA
Saatlik Ücret: 25 TL
Süre: 4.5 saat
TOPLAM: 112.5 TL
```

---

### ✅ Soru 25: Proje Tamamlanma Yüzdesi
Bir projede toplam **50 görev** vardır. **35 görev** tamamlanmıştır. Projenin tamamlanma yüzdesini hesaplayan bir program yazınız.

**Beklenen Çıktı:**
```
📊 PROJE İLERLEMESİ
Tamamlanan: 35 görev
Toplam: 50 görev
İlerleme: %70.0
```

**Formül:** (Tamamlanan / Toplam) × 100

---

## 🎯 INPUT Kullanımlı Sorular (26-35)

### ✅ Soru 26: Kullanıcıdan İsim ve Yaş Alma
Kullanıcıdan adını ve yaşını isteyen, sonra formatlı bir karşılama mesajı veren program yazınız.

**Örnek Çıktı:**
```
İsminiz: Ali
Yaşınız: 25

╔════════════════════════╗
║  HOŞ GELDİNİZ!        ║
║  Ad: Ali              ║
║  Yaş: 25              ║
╚════════════════════════╝
```

---

### ✅ Soru 27: Dikdörtgen Alan Hesaplama (Input)
Kullanıcıdan dikdörtgenin uzun ve kısa kenarını isteyen, alanını hesaplayan program yazınız.

**Örnek Çıktı:**
```
Uzun kenar (cm): 10
Kısa kenar (cm): 5

📐 DİKDÖRTGEN ALAN HESABI
Uzun Kenar: 10 cm
Kısa Kenar: 5 cm
ALAN: 50 cm²
```

---

### ✅ Soru 28: Sıcaklık Dönüştürücü (Celsius → Fahrenheit)
Kullanıcıdan Celsius cinsinden sıcaklık isteyen ve Fahrenheit'a çeviren program yazınız.

**Formül:** F = (C × 9/5) + 32

**Örnek Çıktı:**
```
Celsius: 25

🌡️  SICAKLIK DÖNÜŞTÜRMESİ
25°C = 77.0°F
```

---

### ✅ Soru 29: Alışveriş Sepeti Hesaplama (Input)
Kullanıcıdan 3 ürünün fiyatını isteyen ve toplam tutarı hesaplayan program yazınız.

**Örnek Çıktı:**
```
1. Ürün fiyatı: 50
2. Ürün fiyatı: 75
3. Ürün fiyatı: 30

🛒 ALIŞVERİŞ SEPETİ
Ürün 1: 50.0 TL
Ürün 2: 75.0 TL
Ürün 3: 30.0 TL
──────────────────
TOPLAM: 155.0 TL
```

---

### ✅ Soru 30: Vücut Kitle İndeksi (BMI) Hesaplama
Kullanıcıdan kilo (kg) ve boy (m) isteyen, BMI'yi hesaplayan program yazınız.

**Formül:** BMI = Kilo ÷ (Boy × Boy)

**Örnek Çıktı:**
```
Kilonuz (kg): 70
Boyunuz (m): 1.75

⚕️  VKİ HESAPLAMA
Kilo: 70 kg
Boy: 1.75 m
VKİ: 22.86
```

---

### ✅ Soru 31: Yol Masrafı Hesaplama (Input)
Kullanıcıdan gidilecek mesafe (km) ve benzin fiyatını isteyen, toplam yakıt masrafını hesaplayan program yazınız. (Araç 100 km'de 7 litre yakar)

**Örnek Çıktı:**
```
Mesafe (km): 350
Benzin fiyatı (TL/litre): 30

⛽ YOL MASRAFI
Mesafe: 350 km
Tüketim: 24.5 litre
Litre Fiyatı: 30 TL
════════════════════
TOPLAM: 735.0 TL
```

---

### ✅ Soru 32: Film Süresi Hesaplama
Kullanıcıdan film süresini dakika cinsinden isteyen, bunu saat ve dakikaya çeviren program yazınız.

**Örnek Çıktı:**
```
Film süresi (dakika): 145

🎬 FİLM SÜRESİ
Toplam: 145 dakika
= 2 saat 25 dakika
```

---

### ✅ Soru 33: Not Ortalaması Hesaplama (Input)
Kullanıcıdan 4 ders notunu isteyen ve ortalamasını hesaplayan program yazınız.

**Örnek Çıktı:**
```
Matematik notu: 85
Fizik notu: 90
Kimya notu: 75
Biyoloji notu: 80

📚 NOT ORTALAMASI
Matematik: 85
Fizik: 90
Kimya: 75
Biyoloji: 80
──────────────────
ORTALAMA: 82.5
```

---

### ✅ Soru 34: Maaş Zammı Hesaplama (Input)
Kullanıcıdan mevcut maaşını ve zam oranını (%) isteyen, yeni maaşı hesaplayan program yazınız.

**Örnek Çıktı:**
```
Mevcut maaş: 15000
Zam oranı (%): 12

💰 MAAŞ ZAMMI
Eski Maaş: 15000 TL
Zam Oranı: %12
Zam Tutarı: 1800.0 TL
━━━━━━━━━━━━━━━━━━━━
Yeni Maaş: 16800.0 TL
```

---

### ✅ Soru 35: Kafe Hesabı (Input + Cowsay)
Kullanıcıdan kahve ve kek adedini isteyen, toplam hesabı cowsay ile gösteren program yazınız. (Kahve: 35 TL, Kek: 25 TL)

**Örnek Çıktı:**
```
Kaç kahve: 2
Kaç kek: 1

 _____________________
< Toplam: 95 TL >
 ---------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

---

## 📝 Önemli Notlar

### Print Formatlaması İpuçları:
```python
# F-string kullanımı
isim = "Ahmet"
yas = 25
print(f"Merhaba {isim}, {yas} yaşındasın!")

# Çoklu satır print
print("Satır 1")
print("Satır 2")
print("Satır 3")

# Özel karakterler
print("═" * 30)  # Çizgi çizer
print("─" * 30)  # Başka çizgi
print("━" * 30)  # Kalın çizgi

# Boşluk bırakma
print()  # Boş satır
```

### Input Kullanımı:
```python
# String olarak alma
isim = input("Adınız: ")

# Sayı olarak alma
yas = int(input("Yaşınız: "))
fiyat = float(input("Fiyat: "))
```

### Cowsay Kullanımı:
```python
import cowsay

cowsay.cow("Merhaba Dünya!")
cowsay.tux("Python öğreniyorum!")
cowsay.dragon("Toplam: 100 TL")
```

---

**Başarılar! 🎉**