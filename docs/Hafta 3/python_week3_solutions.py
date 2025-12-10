# ========================================
# PYTHON 3. HAFTA - ÖRNEK ÇÖZÜMLER
# Koşullu İfadeler (if/elif/else)
# ========================================

print("=" * 70)
print("PYTHON 3. HAFTA - KOŞULLU İFADELER ÖRNEK ÇÖZÜMLER")
print("=" * 70)
print()

# ========================================
# SORU 1: Pozitif/Negatif Sayı Kontrolü
# ========================================
print("=" * 70)
print("SORU 1: POZİTİF/NEGATİF SAYI KONTROLÜ")
print("=" * 70)

sayi = float(input("Bir sayı girin: "))

if sayi > 0:
    print("✅ Sayı POZİTİF")
elif sayi < 0:
    print("❌ Sayı NEGATİF")
else:
    print("⚪ Sayı SIFIR")

print()

# ========================================
# SORU 2: Tek/Çift Kontrol
# ========================================
print("=" * 70)
print("SORU 2: TEK/ÇİFT KONTROL")
print("=" * 70)

sayi2 = int(input("Bir sayı girin: "))

print()
if sayi2 % 2 == 0:
    print(f"🔢 {sayi2} sayısı ÇİFTTİR")
else:
    print(f"🔢 {sayi2} sayısı TEKTİR")

print()
print(f"Açıklama: {sayi2} sayısının 2'ye bölümünden kalan {sayi2 % 2}")
print()

# ========================================
# SORU 4: Sınav Geçme Durumu
# ========================================
print("=" * 70)
print("SORU 4: SINAV GEÇME DURUMU")
print("=" * 70)

not_puan = float(input("Sınav notunuz (0-100): "))

print()
print("📊 SINAV SONUCU")
print("━" * 70)
print(f"Notunuz: {not_puan}")

if not_puan >= 50:
    print("✅ GEÇTİNİZ! Tebrikler! 🎉")
else:
    eksik = 50 - not_puan
    print(f"❌ KALDINIZ! Geçmek için {eksik} puan daha gerekiyordu.")

print()

# ========================================
# SORU 5: Büyük Sayıyı Bulma
# ========================================
print("=" * 70)
print("SORU 5: BÜYÜK SAYIYI BULMA")
print("=" * 70)

sayi_a = float(input("İlk sayı: "))
sayi_b = float(input("İkinci sayı: "))

print()
print("📊 KARŞILAŞTIRMA SONUCU")
print("━" * 70)

if sayi_a > sayi_b:
    print(f"✅ {sayi_a} sayısı {sayi_b} sayısından BÜYÜKTÜR")
elif sayi_b > sayi_a:
    print(f"✅ {sayi_b} sayısı {sayi_a} sayısından BÜYÜKTÜR")
else:
    print(f"⚖️  Her iki sayı da EŞİTTİR ({sayi_a} = {sayi_b})")

print()

# ========================================
# SORU 13: Harf Notu Sistemi
# ========================================
print("=" * 70)
print("SORU 13: HARF NOTU SİSTEMİ")
print("=" * 70)

ogrenci_notu = float(input("Notunuzu girin (0-100): "))

print()
print("🎓 HARF NOTU DEĞERLENDİRMESİ")
print("━" * 70)
print(f"Sayısal Not: {ogrenci_notu}")

if ogrenci_notu >= 85:
    harf = "A"
    yorum = "Mükemmel! 🌟"
elif ogrenci_notu >= 70:
    harf = "B"
    yorum = "İyi! 👍"
elif ogrenci_notu >= 50:
    harf = "C"
    yorum = "Geçer 📝"
else:
    harf = "F"
    yorum = "Başarısız ❌"

print(f"Harf Notu: {harf}")
print(f"Değerlendirme: {yorum}")
print()

# ========================================
# SORU 16: Not Ortalaması Belge Sistemi
# ========================================
print("=" * 70)
print("SORU 16: NOT ORTALAMASI BELGE SİSTEMİ")
print("=" * 70)

print("3 Ders Notu Girin:")
ders1 = float(input("Matematik: "))
ders2 = float(input("Fizik: "))
ders3 = float(input("Kimya: "))

ortalama = (ders1 + ders2 + ders3) / 3

print()
print("📚 BELGE DEĞERLENDİRMESİ")
print("━" * 70)
print(f"Matematik: {ders1}")
print(f"Fizik: {ders2}")
print(f"Kimya: {ders3}")
print(f"Ortalama: {ortalama:.2f}")
print("━" * 70)

if ortalama >= 85:
    print("🏆 TAKDİR BELGESİ")
    print("Harika bir başarı! Tebrikler!")
elif ortalama >= 70:
    print("⭐ TEŞEKKÜR BELGESİ")
    print("Güzel bir performans!")
elif ortalama >= 50:
    print("✅ GEÇTİ")
    print("Sınıfı geçtiniz.")
else:
    print("❌ KALDI")
    print("Maalesef sınıfta kaldınız.")

print()

# ========================================
# SORU 17: Sinema Bileti Fiyatı
# ========================================
print("=" * 70)
print("SORU 17: SİNEMA BİLETİ FİYAT HESAPLAMA")
print("=" * 70)

yas_sinema = int(input("Yaşınızı girin: "))

print()
print("🎬 SİNEMA BİLETİ")
print("━" * 70)

if yas_sinema <= 6:
    fiyat = 0
    kategori = "Çocuk (Ücretsiz)"
elif yas_sinema <= 17:
    fiyat = 20
    kategori = "Öğrenci"
elif yas_sinema <= 64:
    fiyat = 40
    kategori = "Tam Bilet"
else:
    fiyat = 25
    kategori = "65+ (İndirimli)"

print(f"Yaş: {yas_sinema}")
print(f"Kategori: {kategori}")
print(f"Bilet Fiyatı: {fiyat} TL")
print()

# ========================================
# SORU 19: Kredi Başvuru Değerlendirmesi
# ========================================
print("=" * 70)
print("SORU 19: KREDİ BAŞVURU DEĞERLENDİRMESİ")
print("=" * 70)

yas_kredi = int(input("Yaşınız: "))
gelir = float(input("Aylık geliriniz (TL): "))
kredi_notu = int(input("Kredi notunuz (0-1000): "))

print()
print("💳 KREDİ BAŞVURU SONUCU")
print("━" * 70)
print(f"Yaş: {yas_kredi}")
print(f"Gelir: {gelir} TL")
print(f"Kredi Notu: {kredi_notu}")
print("━" * 70)

# Üç koşul da sağlanmalı (and operatörü)
if yas_kredi >= 18 and gelir >= 5000 and kredi_notu >= 600:
    print("✅ BAŞVURUNUZ ONAYLANDI! 🎉")
    print("Kredi talebiniz değerlendirilecektir.")
else:
    print("❌ BAŞVURUNUZ REDDEDİLDİ")
    print("\nReddedilme Nedenleri:")
    
    if yas_kredi < 18:
        print("  • Yaş 18'den küçük")
    if gelir < 5000:
        print("  • Gelir 5000 TL'den az")
    if kredi_notu < 600:
        print("  • Kredi notu 600'den düşük")

print()

# ========================================
# SORU 22: BMI (Vücut Kitle İndeksi) Değerlendirme
# ========================================
print("=" * 70)
print("SORU 22: VKİ (BMI) DEĞERLENDİRME")
print("=" * 70)

kilo = float(input("Kilonuz (kg): "))
boy = float(input("Boyunuz (m, örn: 1.75): "))

bmi = kilo / (boy ** 2)

print()
print("⚕️  VÜC UT KİTLE İNDEKSİ")
print("━" * 70)
print(f"Kilo: {kilo} kg")
print(f"Boy: {boy} m")
print(f"BMI: {bmi:.2f}")
print("━" * 70)

if bmi < 18.5:
    kategori_bmi = "ZAYIF"
    tavsiye = "Daha fazla beslenmeli ve doktor kontrolü önerilir."
    emoji = "⚠️"
elif bmi < 25:
    kategori_bmi = "NORMAL"
    tavsiye = "Harika! Sağlıklı bir kiloda!"
    emoji = "✅"
elif bmi < 30:
    kategori_bmi = "FAZLA KİLOLU"
    tavsiye = "Dengeli beslenme ve egzersiz önerilir."
    emoji = "⚠️"
else:
    kategori_bmi = "OBEZ"
    tavsiye = "Doktor kontrolü ve diyet programı önerilir."
    emoji = "🚨"

print(f"Kategori: {emoji} {kategori_bmi}")
print(f"Tavsiye: {tavsiye}")
print()

# ========================================
# SORU 23: Mevsim Belirleme
# ========================================
print("=" * 70)
print("SORU 23: MEVSİM BELİRLEME")
print("=" * 70)

ay = int(input("Ay numarası girin (1-12): "))

print()
print("🌍 MEVSİM BİLGİSİ")
print("━" * 70)

if ay == 12 or ay == 1 or ay == 2:
    mevsim = "KIŞ ❄️"
elif ay == 3 or ay == 4 or ay == 5:
    mevsim = "İLKBAHAR 🌸"
elif ay == 6 or ay == 7 or ay == 8:
    mevsim = "YAZ ☀️"
elif ay == 9 or ay == 10 or ay == 11:
    mevsim = "SONBAHAR 🍂"
else:
    mevsim = "GEÇERSİZ AY!"

print(f"Ay: {ay}")
print(f"Mevsim: {mevsim}")
print()

# ========================================
# SORU 31: Hesap Makinesi (4 İşlem)
# ========================================
print("=" * 70)
print("SORU 31: HESAP MAKİNESİ")
print("=" * 70)

sayi1_hm = float(input("İlk sayı: "))
islem = input("İşlem (+, -, *, /): ")
sayi2_hm = float(input("İkinci sayı: "))

print()
print("🧮 HESAPLAMA SONUCU")
print("━" * 70)

if islem == "+":
    sonuc = sayi1_hm + sayi2_hm
    print(f"{sayi1_hm} + {sayi2_hm} = {sonuc}")
elif islem == "-":
    sonuc = sayi1_hm - sayi2_hm
    print(f"{sayi1_hm} - {sayi2_hm} = {sonuc}")
elif islem == "*":
    sonuc = sayi1_hm * sayi2_hm
    print(f"{sayi1_hm} × {sayi2_hm} = {sonuc}")
elif islem == "/":
    if sayi2_hm != 0:
        sonuc = sayi1_hm / sayi2_hm
        print(f"{sayi1_hm} ÷ {sayi2_hm} = {sonuc:.2f}")
    else:
        print("❌ HATA: Sıfıra bölme yapılamaz!")
else:
    print("❌ HATA: Geçersiz işlem!")

print()

# ========================================
# SORU 33: Üç Sayının En Büyüğü
# ========================================
print("=" * 70)
print("SORU 33: ÜÇ SAYININ EN BÜYÜĞÜ")
print("=" * 70)

s1 = float(input("1. sayı: "))
s2 = float(input("2. sayı: "))
s3 = float(input("3. sayı: "))

print()
print("📊 KARŞILAŞTIRMA")
print("━" * 70)

# Yöntem 1: if-elif ile
if s1 >= s2 and s1 >= s3:
    en_buyuk = s1
elif s2 >= s1 and s2 >= s3:
    en_buyuk = s2
else:
    en_buyuk = s3

print(f"Sayılar: {s1}, {s2}, {s3}")
print(f"En Büyük: {en_buyuk}")
print()

# ========================================
# SORU 34: Artık Yıl Kontrolü
# ========================================
print("=" * 70)
print("SORU 34: ARTIK YIL KONTROLÜ")
print("=" * 70)

yil = int(input("Yıl girin: "))

print()
print("📅 ARTIK YIL DEĞERLENDİRMESİ")
print("━" * 70)
print(f"Yıl: {yil}")
print()

# Artık yıl kuralı:
# 4'e bölünür VE (100'e bölünmez VEYA 400'e bölünür)
if yil % 4 == 0 and (yil % 100 != 0 or yil % 400 == 0):
    print("✅ Bu yıl ARTIK YILDIR (366 gün)")
    print("Şubat ayı 29 gündür.")
else:
    print("❌ Bu yıl ARTIK YIL DEĞİLDİR (365 gün)")
    print("Şubat ayı 28 gündür.")

print()
print("ℹ️  Artık Yıl Kuralı:")
print("  • 4'e tam bölünmeli")
print("  • 100'e bölünüyorsa, 400'e de bölünmeli")
print()

# ========================================
# SORU 37: Geometrik Şekil Alan Hesabı
# ========================================
print("=" * 70)
print("SORU 37: GEOMETRİK ŞEKİL ALAN HESABI")
print("=" * 70)

print("""
ŞEKİL MENÜSÜ:
1 - Kare
2 - Dikdörtgen
3 - Üçgen
4 - Daire
""")

secim = int(input("Şekil seçin (1-4): "))

print()
print("📐 ALAN HESAPLAMA")
print("━" * 70)

if secim == 1:
    kenar = float(input("Kenar uzunluğu (cm): "))
    alan = kenar ** 2
    print(f"Kare Alanı: {alan} cm²")
    
elif secim == 2:
    uzun = float(input("Uzun kenar (cm): "))
    kisa = float(input("Kısa kenar (cm): "))
    alan = uzun * kisa
    print(f"Dikdörtgen Alanı: {alan} cm²")
    
elif secim == 3:
    taban = float(input("Taban (cm): "))
    yukseklik = float(input("Yükseklik (cm): "))
    alan = (taban * yukseklik) / 2
    print(f"Üçgen Alanı: {alan} cm²")
    
elif secim == 4:
    yaricap = float(input("Yarıçap (cm): "))
    pi = 3.14159
    alan = pi * (yaricap ** 2)
    print(f"Daire Alanı: {alan:.2f} cm²")
    
else:
    print("❌ Geçersiz seçim!")

print()

# ========================================
# SORU 40: Oyun Kazanma Sistemi
# ========================================
print("=" * 70)
print("SORU 40: OYUN KAZANMA SİSTEMİ")
print("=" * 70)

puan = int(input("Puanınız: "))
can = int(input("Canınız: "))
sure = int(input("Kalan süre (saniye): "))

print()
print("🎮 OYUN SONUCU")
print("━" * 70)
print(f"Puan: {puan}")
print(f"Can: {can}")
print(f"Süre: {sure} saniye")
print("━" * 70)

# Tüm koşullar sağlanmalı
if puan >= 100 and can > 0 and sure > 0:
    print("🏆 KAZANDINIZ! TEBRİKLER! 🎉")
    print("Tüm görevleri başarıyla tamamladınız!")
else:
    print("💀 KAYBETTİNİZ!")
    print("\nKaybetme Nedenleri:")
    
    if puan < 100:
        print(f"  • Puan yetersiz (En az 100 gerekli, sizde {puan})")
    if can <= 0:
        print("  • Canınız bitti")
    if sure <= 0:
        print("  • Süreniz doldu")

print()

# ========================================
# BONUS: İÇ İÇE IF ÖRNEĞİ
# ========================================
print("=" * 70)
print("BONUS: İÇ İÇE IF - ARABA KİRALAMA")
print("=" * 70)

yas_araba = int(input("Yaşınız: "))
ehliyet_var = input("Ehliyetiniz var mı? (evet/hayır): ").lower()

print()
print("🚗 ARABA KİRALAMA DEĞERLENDİRMESİ")
print("━" * 70)

if yas_araba >= 18:
    print("✅ Yaş kontrolü: Uygun")
    
    if ehliyet_var == "evet":
        print("✅ Ehliyet kontrolü: Var")
        print("━" * 70)
        print("🎉 ARABA KİRALAYABİLİRSİNİZ!")
    else:
        print("❌ Ehliyet kontrolü: Yok")
        print("━" * 70)
        print("⚠️  Önce ehliyet almalısınız!")
else:
    print("❌ Yaş kontrolü: Uygun değil")
    print("━" * 70)
    print("⚠️  18 yaşından küçüksünüz!")

print()

# ========================================
# BİTİŞ MESAJI VE ÖNEMLİ NOTLAR
# ========================================
print("=" * 70)
print("✅ TÜM ÇÖZÜMLER TAMAMLANDI!")
print("=" * 70)
print()
print("💡 ÖNEMLİ HATIRLATMALAR:")
print()
print("1️⃣  KARŞILAŞTIRMA:")
print("   • Eşitlik kontrolü için == (çift eşittir)")
print("   • Atama için = (tek eşittir)")
print()
print("2️⃣  MANTIKSAL OPERATÖRLER:")
print("   • and → Her iki koşul da True olmalı")
print("   • or → En az bir koşul True olmalı")
print("   • not → Koşulu tersine çevirir")
print()
print("3️⃣  GİRİNTİ (INDENTATION):")
print("   • Python'da girintiler çok önemli!")
print("   • if/elif/else bloklarında 4 boşluk kullanın")
print()
print("4️⃣  İKİ NOKTA ÜST ÜSTE (:):")
print("   • if, elif, else'den sonra : koymayı unutmayın")
print()
print("5️⃣  elif KULLANIMI:")
print("   • İlk True koşul çalışır, diğerleri atlanır")
print("   • else koşul almaz, sadece else: şeklinde")
print()
print("6️⃣  BOOLEAN DEĞİŞKENLER:")
print("   • if yagmur == True yerine")
print("   • if yagmur yazın (daha kısa ve okunabilir)")
print()
print("=" * 70)
print("🎉 Koşullu ifadelerde ustalaşıyorsunuz! Başarılar!")
print("=" * 70)