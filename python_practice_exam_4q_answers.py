# ========================================
# PYTHON UYGULAMA SINAVI CEVAP ANAHTARI
# 4 Soru - 40 Puan
# ========================================

print("=" * 70)
print("PYTHON UYGULAMA SINAVI - CEVAP ANAHTARI")
print("=" * 70)
print()

# ========================================
# SORU 1 (8 Puan) - EN KOLAY
# Kişisel Bilgi Kartı
# ========================================
print("=" * 70)
print("SORU 1 (8 Puan) - EN KOLAY: KİŞİSEL BİLGİ KARTI")
print("=" * 70)

# Kullanıcıdan bilgi alma
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = input("Yaşınız: ")

# Formatlı çıktı
print()
print("╔═══════════════════════════╗")
print("║   KİŞİSEL BİLGİ KARTI    ║")
print("╚═══════════════════════════╝")
print(f"Ad Soyad: {ad} {soyad}")
print(f"Yaş: {yas}")

print()
print("📝 PUANLAMA DETAYI:")
print("  • 3 input kullanımı: 3 puan")
print("  • F-string formatlaması: 3 puan")
print("  • Düzgün çıktı: 2 puan")
print()
print("💡 DİKKAT EDİLECEKLER:")
print("  - input() parantezleri unutulmamalı")
print("  - f-string'de {} içinde değişken adı doğru yazılmalı")
print("  - Print satırları düzgün hizalanmalı")
print()

# ========================================
# SORU 2 (10 Puan) - KOLAY
# Basit Alışveriş Hesabı
# ========================================
print("=" * 70)
print("SORU 2 (10 Puan) - KOLAY: ALIŞVERİŞ HESABI")
print("=" * 70)

# Fiyatları alma
urun1 = float(input("1. ürün fiyatı: "))
urun2 = float(input("2. ürün fiyatı: "))
urun3 = float(input("3. ürün fiyatı: "))

# Toplam hesaplama
toplam = urun1 + urun2 + urun3

# İndirim kontrolü
if toplam >= 100:
    indirim = toplam * 0.10
else:
    indirim = 0

# Ödenecek tutar
odenecek = toplam - indirim

# Çıktı
print()
print("─" * 25)
print(f"Toplam: {toplam} TL")
print(f"İndirim (%10): {indirim} TL")
print("─" * 25)
print(f"ÖDENECEK: {odenecek} TL")

print()
print("📝 PUANLAMA DETAYI:")
print("  • 3 input ve float dönüşümü: 3 puan")
print("  • Toplam hesaplama: 2 puan")
print("  • if-else ile indirim kontrolü: 3 puan")
print("  • Doğru hesaplama ve çıktı: 2 puan")
print()
print("💡 DİKKAT EDİLECEKLER:")
print("  - float() kullanılmalı (ondalıklı sayı için)")
print("  - if toplam >= 100: (>= işareti önemli)")
print("  - İndirim = toplam * 0.10 (veya toplam * 10 / 100)")
print("  - else durumunda indirim = 0 olmalı")
print()
print("❌ YAPILAN HATALAR:")
print("  - int() yerine float() kullanmamak")
print("  - İndirim hesabını unutmak")
print("  - >= yerine > kullanmak (100 dahil olmalı)")
print()

# ========================================
# SORU 3 (12 Puan) - ORTA
# Kelime Analiz Programı
# ========================================
print("=" * 70)
print("SORU 3 (12 Puan) - ORTA: KELİME ANALİZ PROGRAMI")
print("=" * 70)

# Kelime alma
kelime = input("Bir kelime girin: ").lower()

# 1. Harf sayısı
harf_sayisi = len(kelime)

# 2. Tersi
ters = kelime[::-1]

# 3. Palindrome kontrolü
if kelime == ters:
    palindrome = "EVET ✓"
else:
    palindrome = "HAYIR ✗"

# 4. Sesli harf sayma
sesli_harfler = "aeıioöuü"
sesli_sayisi = 0

for harf in kelime:
    if harf in sesli_harfler:
        sesli_sayisi += 1

# Çıktı
print()
print("═" * 31)
print("    KELİME ANALİZİ")
print("═" * 31)
print(f"Kelime: {kelime}")
print(f"Harf Sayısı: {harf_sayisi}")
print(f"Tersi: {ters}")
print(f"Palindrome: {palindrome}")
print(f"Sesli Harf: {sesli_sayisi}")

print()
print("📝 PUANLAMA DETAYI:")
print("  • Input ve lower() kullanımı: 1 puan")
print("  • len() ile harf sayısı: 2 puan")
print("  • [::-1] ile ters çevirme: 2 puan")
print("  • Palindrome kontrolü (if karşılaştırma): 3 puan")
print("  • for döngüsü ile sesli harf sayma: 4 puan")
print()
print("💡 DİKKAT EDİLECEKLER:")
print("  - .lower() kullanılmalı (büyük/küçük harf sorunu önlemek için)")
print("  - [::-1] doğru yazılmalı (tire ve iki nokta)")
print("  - if kelime == ters: karşılaştırması doğru yapılmalı")
print("  - Sesli harfler tanımlanmalı: 'aeıioöuü'")
print("  - for harf in kelime: döngüsü kurulmalı")
print("  - if harf in sesli_harfler: kontrolü yapılmalı")
print()
print("❌ YAPILAN HATALAR:")
print("  - [::-1] yerine farklı yöntem denemek")
print("  - Palindrome kontrolünde == yerine = kullanmak")
print("  - Sesli harf döngüsünde += 1 unutmak")
print("  - for döngüsünde girinti yapmamak")
print()

# ========================================
# SORU 4 (10 Puan) - ZOR
# Çarpım Tablosu ve Katlar Toplamı
# ========================================
print("=" * 70)
print("SORU 4 (10 Puan) - ZOR: ÇARPIM TABLOSU VE KATLAR")
print("=" * 70)

# Geçerli sayı alma (1-10 arası)
sayi = 0
while sayi < 1 or sayi > 10:
    sayi = int(input("1-10 arası bir sayı girin: "))
    if sayi < 1 or sayi > 10:
        print("Geçersiz! 1-10 arası olmalı.")

# Çarpım tablosu
print()
print("═" * 31)
print(f"  {sayi}'İN ÇARPIM TABLOSU")
print("═" * 31)

for i in range(1, 11):
    sonuc = sayi * i
    print(f"{sayi} x {i} = {sonuc}")

# 1-100 arası katlar ve toplamı
print()
print("═" * 31)
print(f"1-100 ARASI {sayi}'İN KATLARI")
print("═" * 31)

katlar = []
toplam_katlar = 0

for i in range(1, 101):
    if i % sayi == 0:
        katlar.append(i)
        toplam_katlar += i

# Katları yazdırma
print(", ".join(map(str, katlar)))
print()
print(f"Toplamları: {toplam_katlar}")

print()
print("📝 PUANLAMA DETAYI:")
print("  • Input ve doğrulama döngüsü (1-10 kontrol): 3 puan")
print("  • Çarpım tablosu (for 1-10): 3 puan")
print("  • 1-100 arası katları bulma (for ve if): 2 puan")
print("  • Katların toplamını hesaplama: 2 puan")
print()
print("💡 DİKKAT EDİLECEKLER:")
print("  - while döngüsü ile geçersiz girişler kontrol edilmeli")
print("  - İlk for: range(1, 11) (1'den 10'a kadar)")
print("  - İkinci for: range(1, 101) (1'den 100'e kadar)")
print("  - if i % sayi == 0: ile kat kontrolü")
print("  - toplam += i ile toplama")
print()
print("❌ YAPILAN HATALAR:")
print("  - while koşulunu yanlış yazmak (or yerine and)")
print("  - range(1, 10) yazmak (10 dahil değil!)")
print("  - % operatörünü yanlış kullanmak")
print("  - Toplama işlemini unutmak")
print()

# ALTERNATİF ÇÖZÜM (Daha Basit)
print("─" * 70)
print("ALTERNATİF ÇÖZÜM (Daha Basit - Liste Olmadan):")
print("─" * 70)
print("""
# Katları yazdırma ve toplama (liste olmadan)
toplam = 0
for i in range(sayi, 101, sayi):  # sayi'nin katları direkt
    print(i, end=', ' if i + sayi <= 100 else '')
    toplam += i
print()
print(f'Toplam: {toplam}')
""")
print()

# ========================================
# GENEL DEĞERLENDİRME
# ========================================
print("=" * 70)
print("SINAV BİTTİ - GENEL DEĞERLENDİRME")
print("=" * 70)
print()
print("📊 PUAN DAĞILIMI:")
print("━" * 70)
print("Soru 1 (En Kolay):  8 Puan  - Input, F-string")
print("Soru 2 (Kolay):    10 Puan  - Float, if-else, hesaplama")
print("Soru 3 (Orta):     12 Puan  - String, döngü, palindrome")
print("Soru 4 (Zor):      10 Puan  - Doğrulama, çarpım, mod")
print("━" * 70)
print("TOPLAM:            40 Puan")
print()
print("🎯 BAŞARI KRİTERLERİ:")
print("  36-40: Mükemmel ⭐⭐⭐")
print("  32-35: Çok İyi ⭐⭐")
print("  28-31: İyi ⭐")
print("  24-27: Orta")
print("  20-23: Geçer")
print("  0-19:  Yetersiz")
print()
print("=" * 70)
print("EN ÇOK YAPILAN 5 HATA:")
print("=" * 70)
print("1. GİRİNTİ HATASI - Döngü ve if'lerde 4 boşluk yapılmıyor")
print("2. : UNUTMA - if, for, while'dan sonra : konmuyor")
print("3. INPUT TİP DÖNÜŞÜMÜ - int(), float() kullanılmıyor")
print("4. = ve == KARIŞTIRMA - Atama ile karşılaştırma karışıyor")
print("5. range() BİTİŞ DEĞERİ - 1-10 için range(1,11) yazılmıyor")
print()
print("=" * 70)
print("ÖĞRENCİLERE TAVSİYELER:")
print("=" * 70)
print("✅ Her soruyu dikkatlice okuyun")
print("✅ Basit sorulardan başlayın")
print("✅ Kodunuzu test edin")
print("✅ Hata mesajlarını okuyun")
print("✅ Girinti ve : kontrolü yapın")
print("✅ Değişken isimlerini kontrol edin")
print("✅ Örnek çıktıyla karşılaştırın")
print()
print("=" * 70)
print("🎉 Başarılar! Bol bol pratik yapın!")
print("=" * 70)