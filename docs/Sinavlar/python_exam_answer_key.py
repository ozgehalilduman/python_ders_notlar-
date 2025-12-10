# ========================================
# PYTHON İLK 5 HAFTA SINAV CEVAP ANAHTARI
# Toplam: 10 Soru - 100 Puan
# ========================================

print("=" * 70)
print("PYTHON SINAV CEVAP ANAHTARI")
print("=" * 70)
print()

# ========================================
# SORU 1 (8 Puan) - KOLAY
# Kullanıcıdan ad ve yaş alıp formatlı çıktı
# ========================================
print("=" * 70)
print("SORU 1 (8 Puan) - KOLAY")
print("=" * 70)

ad = input("Adınız: ")
yas = input("Yaşınız: ")

print(f"Merhaba {ad}, sen {yas} yaşındasın!")

print()
print("📝 PUANLAMA:")
print("  • Input kullanımı: 2 puan")
print("  • F-string formatlaması: 3 puan")
print("  • Doğru çıktı: 3 puan")
print()

# ========================================
# SORU 2 (8 Puan) - KOLAY
# 3 ders notunun ortalaması
# ========================================
print("=" * 70)
print("SORU 2 (8 Puan) - KOLAY")
print("=" * 70)

not1 = 75
not2 = 82
not3 = 90

ortalama = (not1 + not2 + not3) / 3

print("📊 NOTLAR VE ORTALAMA")
print("━" * 70)
print(f"Ders 1: {not1}")
print(f"Ders 2: {not2}")
print(f"Ders 3: {not3}")
print(f"Ortalama: {ortalama}")

print()
print("📝 PUANLAMA:")
print("  • Değişken tanımlama: 2 puan")
print("  • Ortalama hesaplama: 4 puan")
print("  • Çıktı gösterme: 2 puan")
print()

# ========================================
# SORU 3 (10 Puan) - ORTA
# Yaş kategorisi belirleme
# ========================================
print("=" * 70)
print("SORU 3 (10 Puan) - ORTA")
print("=" * 70)

yas_kategori = int(input("Yaşınız: "))

print()
print("👤 KATEGORİ BELİRLEME")
print("━" * 70)

if yas_kategori >= 0 and yas_kategori <= 12:
    kategori = "Çocuk"
elif yas_kategori >= 13 and yas_kategori <= 17:
    kategori = "Genç"
elif yas_kategori >= 18 and yas_kategori <= 64:
    kategori = "Yetişkin"
else:
    kategori = "Yaşlı"

print(f"Yaş: {yas_kategori}")
print(f"Kategori: {kategori}")

print()
print("📝 PUANLAMA:")
print("  • Input ve tip dönüşümü: 2 puan")
print("  • if-elif-else yapısı: 5 puan")
print("  • Doğru aralık kontrolü: 2 puan")
print("  • Çıktı: 1 puan")
print()

# ========================================
# SORU 4 (10 Puan) - ORTA
# Sesli harf sayma
# ========================================
print("=" * 70)
print("SORU 4 (10 Puan) - ORTA")
print("=" * 70)

kelime = input("Kelime girin: ")
sesli_harfler = "aeıioöuüAEIİOÖUÜ"
sesli_sayisi = 0

for harf in kelime:
    if harf in sesli_harfler:
        sesli_sayisi += 1

print()
print("🔤 SESLİ HARF ANALİZİ")
print("━" * 70)
print(f"Kelime: {kelime}")
print(f"Sesli harf sayısı: {sesli_sayisi}")

print()
print("📝 PUANLAMA:")
print("  • Input alma: 1 puan")
print("  • Sesli harfler tanımlama: 2 puan")
print("  • for döngüsü: 3 puan")
print("  • if kontrolü ve sayma: 3 puan")
print("  • Çıktı: 1 puan")
print()

# ========================================
# SORU 5 (10 Puan) - ORTA
# 5 satırlık yıldız üçgeni
# ========================================
print("=" * 70)
print("SORU 5 (10 Puan) - ORTA")
print("=" * 70)

print("⭐ YILDIZ ÜÇGENİ:")
for i in range(1, 6):
    print("*" * i)

print()
print("📝 PUANLAMA:")
print("  • for döngüsü: 4 puan")
print("  • range kullanımı (1,6): 3 puan")
print("  • String çarpma: 2 puan")
print("  • Doğru çıktı: 1 puan")
print()

# ========================================
# SORU 6 (12 Puan) - ORTA
# Çarpım tablosu
# ========================================
print("=" * 70)
print("SORU 6 (12 Puan) - ORTA")
print("=" * 70)

sayi = int(input("Sayı: "))

print()
print(f"📊 {sayi} ÇARPIM TABLOSU")
print("━" * 70)

for i in range(1, 11):
    sonuc = sayi * i
    print(f"{sayi} x {i} = {sonuc}")

print()
print("📝 PUANLAMA:")
print("  • Input ve tip dönüşümü: 2 puan")
print("  • for döngüsü (1-10): 4 puan")
print("  • Çarpma işlemi: 3 puan")
print("  • Formatlı çıktı: 3 puan")
print()

# ========================================
# SORU 7 (12 Puan) - ORTA-İLERİ
# Palindrome kontrolü
# ========================================
print("=" * 70)
print("SORU 7 (12 Puan) - ORTA-İLERİ")
print("=" * 70)

kelime_pal = input("Kelime girin: ").lower()
ters = kelime_pal[::-1]

print()
print("🔄 PALINDROME KONTROLÜ")
print("━" * 70)
print(f"Kelime: {kelime_pal}")
print(f"Tersi: {ters}")

if kelime_pal == ters:
    print("✅ Bu kelime PALINDROME'dur!")
else:
    print("❌ Bu kelime palindrome değildir.")

print()
print("📝 PUANLAMA:")
print("  • Input ve lower(): 2 puan")
print("  • String ters çevirme [::-1]: 4 puan")
print("  • Karşılaştırma: 3 puan")
print("  • Çıktı: 3 puan")
print()

# ========================================
# SORU 8 (12 Puan) - İLERİ
# Basamak toplamı
# ========================================
print("=" * 70)
print("SORU 8 (12 Puan) - İLERİ")
print("=" * 70)

sayi_basamak = int(input("Bir sayı girin: "))
toplam_basamak = 0
gecici = sayi_basamak

# Yöntem 1: while ile
while gecici > 0:
    basamak = gecici % 10
    toplam_basamak += basamak
    gecici //= 10

print()
print("🔢 BASAMAK TOPLAMI")
print("━" * 70)
print(f"Sayı: {sayi_basamak}")
print(f"Basamaklar toplamı: {toplam_basamak}")

# Alternatif Yöntem 2: String dönüşümü ile
print("\n--- ALTERNATİF ÇÖZÜM ---")
sayi_str = str(sayi_basamak)
toplam_alt = 0
for rakam in sayi_str:
    toplam_alt += int(rakam)
print(f"Alternatif sonuç: {toplam_alt}")

print()
print("📝 PUANLAMA:")
print("  • Input ve tip dönüşümü: 2 puan")
print("  • Döngü yapısı: 4 puan")
print("  • Basamak ayırma (% ve //): 4 puan")
print("  • Toplama ve çıktı: 2 puan")
print("  • NOT: String yöntemi de tam puan alır")
print()

# ========================================
# SORU 9 (14 Puan) - İLERİ
# Geçme/Kalma durumu (çoklu koşul)
# ========================================
print("=" * 70)
print("SORU 9 (14 Puan) - İLERİ")
print("=" * 70)

not_ortalama = float(input("Not ortalamanız: "))
devamsizlik = float(input("Devamsızlık (%): "))

print()
print("📊 SONUÇ DEĞERLENDİRMESİ")
print("━" * 70)
print(f"Not Ortalaması: {not_ortalama}")
print(f"Devamsızlık: %{devamsizlik}")
print("━" * 70)

if not_ortalama >= 50 and devamsizlik < 20:
    print("✅ SONUÇ: GEÇTİ")
else:
    print("❌ SONUÇ: KALDI")
    
    # Hangi koşullar sağlanmadı?
    if not_ortalama < 50:
        print("  • Not ortalaması yetersiz (50'den az)")
    if devamsizlik >= 20:
        print("  • Devamsızlık çok yüksek (%20 ve üzeri)")

print()
print("📝 PUANLAMA:")
print("  • Input ve tip dönüşümü: 2 puan")
print("  • and operatörü kullanımı: 4 puan")
print("  • İki koşulun doğru kontrolü: 4 puan")
print("  • Geçti/Kaldı çıktısı: 2 puan")
print("  • Ek detay (hangi koşul): +2 puan (bonus)")
print()

# ========================================
# SORU 10 (14 Puan) - İLERİ
# Şifre güvenlik kontrolü
# ========================================
print("=" * 70)
print("SORU 10 (14 Puan) - İLERİ")
print("=" * 70)

sifre = input("Bir şifre oluşturun: ")

print()
print("🔐 ŞİFRE GÜVENLİK DEĞERLENDİRMESİ")
print("━" * 70)

# Kontroller
uzunluk_ok = len(sifre) >= 8
buyuk_harf_var = False
rakam_var = False

# Büyük harf kontrolü
for karakter in sifre:
    if karakter.isupper():
        buyuk_harf_var = True
        break

# Rakam kontrolü
for karakter in sifre:
    if karakter.isdigit():
        rakam_var = True
        break

# Sonuçları göster
if uzunluk_ok:
    print("✅ Uzunluk yeterli (8+ karakter)")
else:
    print("❌ Uzunluk yetersiz (en az 8 karakter gerekli)")

if buyuk_harf_var:
    print("✅ Büyük harf var")
else:
    print("❌ Büyük harf yok")

if rakam_var:
    print("✅ Rakam var")
else:
    print("❌ Rakam yok")

print("━" * 70)

# Final karar
if uzunluk_ok and buyuk_harf_var and rakam_var:
    print("SONUÇ: GÜÇLÜ ŞİFRE 💪")
else:
    print("SONUÇ: ZAYIF ŞİFRE ⚠️")

print()
print("📝 PUANLAMA:")
print("  • Input alma: 1 puan")
print("  • Uzunluk kontrolü (len >= 8): 3 puan")
print("  • Büyük harf kontrolü (döngü+isupper): 4 puan")
print("  • Rakam kontrolü (döngü+isdigit): 4 puan")
print("  • Tüm koşulları birleştirme (and): 2 puan")
print()
print("ALTERNATİF ÇÖZÜM (daha kısa):")
print("buyuk_var = any(c.isupper() for c in sifre)")
print("rakam_var = any(c.isdigit() for c in sifre)")
print("(Bu yöntem de tam puan alır)")
print()

# ========================================
# SINAV SONU - GENEL DEĞERLENDİRME
# ========================================
print("=" * 70)
print("SINAV TAMAMLANDI!")
print("=" * 70)
print()
print("📊 PUAN DAĞILIMI ÖZETİ:")
print("━" * 70)
print("Soru 1:  8 Puan  (Kolay)    - Ad/Yaş formatlama")
print("Soru 2:  8 Puan  (Kolay)    - Not ortalaması")
print("Soru 3: 10 Puan  (Orta)     - Yaş kategorisi")
print("Soru 4: 10 Puan  (Orta)     - Sesli harf sayma")
print("Soru 5: 10 Puan  (Orta)     - Yıldız üçgeni")
print("Soru 6: 12 Puan  (Orta)     - Çarpım tablosu")
print("Soru 7: 12 Puan  (Orta-İleri) - Palindrome")
print("Soru 8: 12 Puan  (İleri)    - Basamak toplamı")
print("Soru 9: 14 Puan  (İleri)    - Geçme/Kalma")
print("Soru 10: 14 Puan (İleri)    - Şifre kontrolü")
print("━" * 70)
print("TOPLAM: 100 PUAN")
print()
print("🎯 BAŞARI KRİTERLERİ:")
print("  90-100: Mükemmel ⭐⭐⭐")
print("  80-89:  Çok İyi ⭐⭐")
print("  70-79:  İyi ⭐")
print("  60-69:  Orta")
print("  50-59:  Geçer")
print("  0-49:   Yetersiz")
print()
print("=" * 70)
print("CEVAP ANAHTARI SONU")
print("=" * 70)