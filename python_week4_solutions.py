# ========================================
# PYTHON 4. HAFTA - ÖRNEK ÇÖZÜMLER
# String İşlemleri
# ========================================

print("=" * 70)
print("PYTHON 4. HAFTA - STRING İŞLEMLERİ ÖRNEK ÇÖZÜMLER")
print("=" * 70)
print()
print("📊 KELIME ANALİZİ")
print("━" * 70)
print(f"Cümle: {cumle}")
print(f"Kelime Sayısı: {kelime_sayisi}")
print(f"Kelimeler: {kelimeler}")
print()

# ========================================
# SORU 12: Telefon Numarası Format
# ========================================
print("=" * 70)
print("SORU 12: TELEFON NUMARASI FORMAT")
print("=" * 70)

telefon = input("Telefon numarası (10 haneli): ")

if len(telefon) == 10:
    # Slicing ile formatla
    formatli = f"{telefon[:3]} {telefon[3:6]} {telefon[6:8]} {telefon[8:]}"
    
    print()
    print("📱 FORMATLI TELEFON")
    print("━" * 70)
    print(f"Orijinal: {telefon}")
    print(f"Formatlı: {formatli}")
else:
    print("❌ Telefon numarası 10 haneli olmalı!")

print()

# ========================================
# SORU 14: Kelime Değiştirme
# ========================================
print("=" * 70)
print("SORU 14: KELIME DEĞİŞTİRME")
print("=" * 70)

cumle_deg = input("Bir cümle girin: ")
eski_kelime = input("Değiştirilecek kelime: ")
yeni_kelime = input("Yeni kelime: ")

yeni_cumle = cumle_deg.replace(eski_kelime, yeni_kelime)

print()
print("🔄 DEĞİŞTİRME SONUCU")
print("━" * 70)
print(f"Eski Cümle: {cumle_deg}")
print(f"Yeni Cümle: {yeni_cumle}")
print()

# ========================================
# SORU 16: Palindrome Kontrolü
# ========================================
print("=" * 70)
print("SORU 16: PALINDROME KONTROLÜ")
print("=" * 70)

kelime_pal = input("Bir kelime girin: ").lower()
ters = kelime_pal[::-1]

print()
print("🔍 PALINDROME KONTROLÜ")
print("━" * 70)
print(f"Kelime: {kelime_pal}")
print(f"Tersi: {ters}")

if kelime_pal == ters:
    print("✅ Bu kelime PALİNDROME'dur!")
    print("(Tersten okunuşu aynı)")
else:
    print("❌ Bu kelime palindrome değil")

print()

# ========================================
# SORU 17: Email Ayrıştırma
# ========================================
print("=" * 70)
print("SORU 17: EMAIL AYRIŞTIRMA")
print("=" * 70)

email_ayir = input("Email adresiniz: ")

if "@" in email_ayir:
    parcalar = email_ayir.split("@")
    kullanici_adi = parcalar[0]
    domain = parcalar[1]
    
    print()
    print("📧 EMAIL AYRIŞTIRMA")
    print("━" * 70)
    print(f"Tam Email: {email_ayir}")
    print(f"Kullanıcı Adı: {kullanici_adi}")
    print(f"Domain: {domain}")
else:
    print("❌ Geçersiz email formatı!")

print()

# ========================================
# SORU 18: İsim Formatlama
# ========================================
print("=" * 70)
print("SORU 18: İSİM FORMATLAMA")
print("=" * 70)

tam_isim = input("Ad soyadınızı girin: ")

# Tüm harfleri küçük yap, sonra title() ile düzelt
formatli_isim = tam_isim.lower().title()

print()
print("✨ FORMATLI İSİM")
print("━" * 70)
print(f"Girilen: {tam_isim}")
print(f"Formatlı: {formatli_isim}")
print()

# ========================================
# SORU 20: Kelime Gizleme
# ========================================
print("=" * 70)
print("SORU 20: KELIME GİZLEME")
print("=" * 70)

kelime_giz = input("Bir kelime girin: ")

if len(kelime_giz) > 2:
    # İlk ve son harf + ortası yıldız
    gizli = kelime_giz[0] + "*" * (len(kelime_giz) - 2) + kelime_giz[-1]
    
    print()
    print("🔒 GİZLENMİŞ KELİME")
    print("━" * 70)
    print(f"Orijinal: {kelime_giz}")
    print(f"Gizli: {gizli}")
else:
    print("Kelime çok kısa!")

print()

# ========================================
# SORU 22: Sesli Harf Sayma
# ========================================
print("=" * 70)
print("SORU 22: SESLİ HARF SAYMA")
print("=" * 70)

kelime_sesli = input("Bir kelime girin: ").lower()
sesli_harfler = "aeıioöuü"
sesli_sayisi = 0

for harf in kelime_sesli:
    if harf in sesli_harfler:
        sesli_sayisi += 1

print()
print("🔤 SESLİ HARF ANALİZİ")
print("━" * 70)
print(f"Kelime: {kelime_sesli}")
print(f"Sesli Harf Sayısı: {sesli_sayisi}")
print(f"Sessiz Harf Sayısı: {len(kelime_sesli) - sesli_sayisi}")
print()

# ========================================
# SORU 23: Baş Harfleri Alma
# ========================================
print("=" * 70)
print("SORU 23: BAŞ HARFLERİ ALMA")
print("=" * 70)

tam_isim_bas = input("Tam isim girin: ")
kelimeler_bas = tam_isim_bas.split()
bas_harfler = ""

for kelime in kelimeler_bas:
    if len(kelime) > 0:
        bas_harfler += kelime[0].upper()

print()
print("🔤 KISALTMA")
print("━" * 70)
print(f"Tam İsim: {tam_isim_bas}")
print(f"Baş Harfler: {bas_harfler}")
print()

# ========================================
# SORU 26: Kimlik No Gizleme
# ========================================
print("=" * 70)
print("SORU 26: KİMLİK NO GİZLEME")
print("=" * 70)

kimlik = input("TC Kimlik No (11 haneli): ")

if len(kimlik) == 11:
    # İlk 3 ve son 2 hane görünsün
    gizli_kimlik = kimlik[:3] + "*" * 6 + kimlik[-2:]
    
    print()
    print("🔒 GİZLİ KİMLİK")
    print("━" * 70)
    print(f"Orijinal: {kimlik}")
    print(f"Gizli: {gizli_kimlik}")
else:
    print("❌ TC Kimlik No 11 haneli olmalı!")

print()

# ========================================
# SORU 27: Dosya Uzantısı Bulma
# ========================================
print("=" * 70)
print("SORU 27: DOSYA UZANTISI BULMA")
print("=" * 70)

dosya_adi = input("Dosya adı girin: ")

if "." in dosya_adi:
    parcalar_dosya = dosya_adi.split(".")
    uzanti = parcalar_dosya[-1]
    isim = ".".join(parcalar_dosya[:-1])
    
    print()
    print("📁 DOSYA BİLGİSİ")
    print("━" * 70)
    print(f"Tam Dosya Adı: {dosya_adi}")
    print(f"Dosya İsmi: {isim}")
    print(f"Uzantı: {uzanti}")
else:
    print("❌ Dosya uzantısı bulunamadı!")

print()

# ========================================
# SORU 31: Karakter Frekansı
# ========================================
print("=" * 70)
print("SORU 31: KARAKTER FREKANSI")
print("=" * 70)

kelime_frek = input("Bir kelime girin: ").lower()

print()
print("📊 KARAKTER FREKANSI")
print("━" * 70)

# Her benzersiz karakter için sayma
karakterler = set(kelime_frek)
for karakter in sorted(karakterler):
    sayi = kelime_frek.count(karakter)
    print(f"{karakter}: {sayi} kere")

print()

# ========================================
# SORU 34: En Uzun Kelime
# ========================================
print("=" * 70)
print("SORU 34: EN UZUN KELİME")
print("=" * 70)

cumle_uzun = input("Bir cümle girin: ")
kelimeler_uzun = cumle_uzun.split()

en_uzun = ""
for kelime in kelimeler_uzun:
    if len(kelime) > len(en_uzun):
        en_uzun = kelime

print()
print("📏 EN UZUN KELİME")
print("━" * 70)
print(f"Cümle: {cumle_uzun}")
print(f"En Uzun Kelime: {en_uzun}")
print(f"Uzunluk: {len(en_uzun)} harf")
print()

# ========================================
# SORU 35: Metin Düzenleme Programı
# ========================================
print("=" * 70)
print("SORU 35: METİN DÜZENLEME PROGRAMI")
print("=" * 70)

metin_duzen = input("Bir metin girin: ")

print()
print("📝 METİN DÜZENLEME MENÜSÜ")
print("━" * 70)
print("1. Büyük harfe çevir")
print("2. Küçük harfe çevir")
print("3. Kelime sayısı")
print("4. Karakter sayısı")
print("5. Ters çevir")
print("━" * 70)

secim_duzen = input("Seçiminiz (1-5): ")

print()
print("SONUÇ:")
print("━" * 70)

if secim_duzen == "1":
    print(metin_duzen.upper())
elif secim_duzen == "2":
    print(metin_duzen.lower())
elif secim_duzen == "3":
    print(f"Kelime Sayısı: {len(metin_duzen.split())}")
elif secim_duzen == "4":
    print(f"Karakter Sayısı: {len(metin_duzen)}")
elif secim_duzen == "5":
    print(metin_duzen[::-1])
else:
    print("Geçersiz seçim!")

print()

# ========================================
# SORU 40: Metin İstatistikleri
# ========================================
print("=" * 70)
print("SORU 40: METİN İSTATİSTİKLERİ")
print("=" * 70)

metin_ist = input("Bir metin girin: ")

# Hesaplamalar
toplam_karakter = len(metin_ist)
bosluksuz = metin_ist.replace(" ", "")
bosluksuz_karakter = len(bosluksuz)
kelime_sayisi_ist = len(metin_ist.split())

# Sesli harf sayma
sesli = "aeıioöuü"
sesli_sayisi_ist = 0
for harf in metin_ist.lower():
    if harf in sesli:
        sesli_sayisi_ist += 1

# Rakam sayma
rakam_sayisi = 0
for karakter in metin_ist:
    if karakter.isdigit():
        rakam_sayisi += 1

print()
print("📊 DETAYLI METİN İSTATİSTİKLERİ")
print("━" * 70)
print(f"Metin: {metin_ist}")
print("━" * 70)
print(f"Toplam Karakter: {toplam_karakter}")
print(f"Boşluksuz Karakter: {bosluksuz_karakter}")
print(f"Boşluk Sayısı: {toplam_karakter - bosluksuz_karakter}")
print(f"Kelime Sayısı: {kelime_sayisi_ist}")
print(f"Sesli Harf Sayısı: {sesli_sayisi_ist}")
print(f"Rakam Sayısı: {rakam_sayisi}")
print()

# ========================================
# BONUS: Şifre Güvenlik Kontrolü
# ========================================
print("=" * 70)
print("BONUS: ŞİFRE GÜVENLİK KONTROLÜ")
print("=" * 70)

sifre = input("Bir şifre oluşturun: ")

print()
print("🔐 ŞİFRE GÜVENLİK DEĞERLENDİRMESİ")
print("━" * 70)

# Kontroller
uzunluk_ok = len(sifre) >= 8
buyuk_harf_var = any(c.isupper() for c in sifre)
kucuk_harf_var = any(c.islower() for c in sifre)
rakam_var = any(c.isdigit() for c in sifre)

puan = 0
if uzunluk_ok:
    puan += 25
    print("✅ Uzunluk (8+ karakter)")
else:
    print("❌ Uzunluk yetersiz (en az 8 karakter)")

if buyuk_harf_var:
    puan += 25
    print("✅ Büyük harf içeriyor")
else:
    print("❌ Büyük harf yok")

if kucuk_harf_var:
    puan += 25
    print("✅ Küçük harf içeriyor")
else:
    print("❌ Küçük harf yok")

if rakam_var:
    puan += 25
    print("✅ Rakam içeriyor")
else:
    print("❌ Rakam yok")

print("━" * 70)
print(f"Güvenlik Puanı: {puan}/100")

if puan == 100:
    print("🌟 Şifre çok güçlü!")
elif puan >= 75:
    print("✅ Şifre güçlü")
elif puan >= 50:
    print("⚠️  Şifre orta güçlükte")
else:
    print("❌ Şifre zayıf!")

print()

# ========================================
# BİTİŞ MESAJI VE ÖNEMLİ NOTLAR
# ========================================
print("=" * 70)
print("✅ TÜM STRING İŞLEMLERİ ÇÖZÜMLER TAMAMLANDI!")
print("=" * 70)
print()
print("💡 ÖNEMLİ STRING NOTLARI:")
print()
print("1️⃣  INDEX'LER 0'DAN BAŞLAR:")
print("   • 'Python'[0] → 'P'")
print("   • 'Python'[-1] → 'n' (sondan)")
print()
print("2️⃣  SLICING [başlangıç:bitiş:adım]:")
print("   • metin[:5] → İlk 5 karakter")
print("   • metin[-3:] → Son 3 karakter")
print("   • metin[::-1] → Ters çevir")
print()
print("3️⃣  ÖNEMLİ METODLAR:")
print("   • upper() / lower() → Büyük/küçük harf")
print("   • strip() → Boşlukları temizle")
print("   • replace() → Değiştir")
print("   • split() → Böl (liste döner)")
print("   • count() → Say")
print("   • find() → Bul (index döner)")
print()
print("4️⃣  STRING + SAYI:")
print("   • String ile sayı toplanamaz!")
print("   • 'Yaş: ' + str(25) veya f'Yaş: {25}' kullanın")
print()
print("5️⃣  STRING IMMUTABLE (DEĞİŞTİRİLEMEZ):")
print("   • metin[0] = 'X' → HATA!")
print("   • Yeni string oluşturmalısınız")
print()
print("6️⃣  F-STRING EN PRATİK YÖNTEM:")
print("   • f'Merhaba {isim}, {yas} yaşındasın'")
print()
print("=" * 70)
print("🎉 String işlemlerinde ustalaştınız! Tebrikler!")
print("=" * 70)

# ========================================
# SORU 1: String Uzunluğu Bulma
# ========================================
print("=" * 70)
print("SORU 1: STRING UZUNLUĞU BULMA")
print("=" * 70)

kelime = input("Bir kelime girin: ")
uzunluk = len(kelime)

print()
print(f'"{kelime}" kelimesi {uzunluk} harflidir.')
print()

# ========================================
# SORU 2: Büyük/Küçük Harf Dönüşümü
# ========================================
print("=" * 70)
print("SORU 2: BÜYÜK/KÜÇÜK HARF DÖNÜŞÜMÜ")
print("=" * 70)

metin = input("Bir metin girin: ")

print()
print("📝 DÖNÜŞÜM SONUÇLARI")
print("━" * 70)
print(f"Orijinal: {metin}")
print(f"BÜYÜK HARF: {metin.upper()}")
print(f"küçük harf: {metin.lower()}")
print(f"Her Kelimenin İlk Harfi Büyük: {metin.title()}")
print()

# ========================================
# SORU 3: String Birleştirme
# ========================================
print("=" * 70)
print("SORU 3: STRING BİRLEŞTİRME")
print("=" * 70)

ad = input("Adınız: ")
soyad = input("Soyadınız: ")

# Yöntem 1: + operatörü
tam_isim1 = ad + " " + soyad

# Yöntem 2: f-string (önerilen)
tam_isim2 = f"{ad} {soyad}"

print()
print("━" * 70)
print(f"Tam İsim: {tam_isim2}")
print(f"Karakter Sayısı: {len(tam_isim2)}")
print()

# ========================================
# SORU 4: String Çoğaltma
# ========================================
print("=" * 70)
print("SORU 4: STRING ÇOĞALTMA")
print("=" * 70)

karakter = input("Bir karakter girin: ")
tekrar = int(input("Kaç kere tekrarlanacak: "))

sonuc = karakter * tekrar

print()
print("SONUÇ:")
print(sonuc)
print()

# ========================================
# SORU 5: İlk ve Son Karakter
# ========================================
print("=" * 70)
print("SORU 5: İLK VE SON KARAKTER")
print("=" * 70)

kelime_iks = input("Bir kelime girin: ")

if len(kelime_iks) > 0:
    ilk_harf = kelime_iks[0]
    son_harf = kelime_iks[-1]
    
    print()
    print(f"Kelime: {kelime_iks}")
    print(f"İlk karakter: {ilk_harf}")
    print(f"Son karakter: {son_harf}")
else:
    print("Boş string girildi!")

print()

# ========================================
# SORU 6: String Ters Çevirme
# ========================================
print("=" * 70)
print("SORU 6: STRING TERS ÇEVİRME")
print("=" * 70)

kelime_ters = input("Bir kelime girin: ")
ters_kelime = kelime_ters[::-1]

print()
print("🔄 TERS ÇEVİRME")
print("━" * 70)
print(f"Normal: {kelime_ters}")
print(f"Tersi: {ters_kelime}")
print()

# ========================================
# SORU 7: Email Adresi Kontrolü
# ========================================
print("=" * 70)
print("SORU 7: EMAIL ADRESİ KONTROLÜ")
print("=" * 70)

email = input("Email adresiniz: ")

# @ ve . kontrolü
if "@" in email and "." in email:
    print("✅ Geçerli email formatı")
    
    # Daha detaylı kontrol
    at_index = email.find("@")
    nokta_index = email.find(".", at_index)
    
    if at_index > 0 and nokta_index > at_index + 1:
        print("✅ Email formatı doğru görünüyor")
    else:
        print("⚠️  Email formatında sorun var")
else:
    print("❌ Geçersiz email formatı")
    if "@" not in email:
        print("  • @ işareti eksik")
    if "." not in email:
        print("  • Nokta (.) eksik")

print()

# ========================================
# SORU 8: Kelime Sayma
# ========================================
print("=" * 70)
print("SORU 8: KELIME SAYMA")
print("=" * 70)

cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()
kelime_sayisi = len(kelimeler)

print()