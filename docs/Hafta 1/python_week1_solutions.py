# ========================================
# PYTHON 1. HAFTA - ÖRNEK ÇÖZÜMLER
# ========================================

print("=" * 50)
print("PYTHON 1. HAFTA ÖRNEK ÇÖZÜMLER")
print("=" * 50)
print()

# ========================================
# SORU 1: Market Alışverişi Hesaplama
# ========================================
print("=" * 50)
print("SORU 1: MARKET ALIŞVERİŞİ")
print("=" * 50)

urun_fiyati = 12.5
adet = 4
toplam = urun_fiyati * adet

print("=== MARKET FİŞİ ===")
print(f"Ürün Fiyatı: {urun_fiyati} TL")
print(f"Adet: {adet}")
print("------------------")
print(f"Toplam Tutar: {toplam} TL")
print()

# ========================================
# SORU 4: Sinema Bileti Fiyatı Hesaplama
# ========================================
print("=" * 50)
print("SORU 4: SİNEMA BİLETİ")
print("=" * 50)

ogrenci_fiyat = 20
yetiskin_fiyat = 35
ogrenci_adet = 3
yetiskin_adet = 2

ogrenci_toplam = ogrenci_fiyat * ogrenci_adet
yetiskin_toplam = yetiskin_fiyat * yetiskin_adet
genel_toplam = ogrenci_toplam + yetiskin_toplam

print("🎬 SİNEMA BİLET HESABI")
print(f"Öğrenci Biletleri: {ogrenci_adet} x {ogrenci_fiyat} TL = {ogrenci_toplam} TL")
print(f"Yetişkin Biletleri: {yetiskin_adet} x {yetiskin_fiyat} TL = {yetiskin_toplam} TL")
print("─" * 30)
print(f"TOPLAM: {genel_toplam} TL")
print()

# ========================================
# SORU 10: Bir Ürünün İndirimli Fiyatı
# ========================================
print("=" * 50)
print("SORU 10: İNDİRİMLİ FİYAT")
print("=" * 50)

orijinal_fiyat = 250
indirim_orani = 15  # Yüzde olarak

indirim_tutari = orijinal_fiyat * indirim_orani / 100
indirimli_fiyat = orijinal_fiyat - indirim_tutari

print("🏷️  İNDİRİM HESAPLAMA")
print(f"Orijinal Fiyat: {orijinal_fiyat} TL")
print(f"İndirim Oranı: %{indirim_orani}")
print(f"İndirim Tutarı: {indirim_tutari} TL")
print("─" * 25)
print(f"İndirimli Fiyat: {indirimli_fiyat} TL")
print()

# ========================================
# SORU 20: Diyet Kalori Hesaplama
# ========================================
print("=" * 50)
print("SORU 20: GÜNLÜK KALORİ")
print("=" * 50)

kahvalti = 350
ogle = 650
aksam = 550
atistirmalik = 200

toplam_kalori = kahvalti + ogle + aksam + atistirmalik

print("🍎 GÜNLÜK KALORİ TAKIBI")
print(f"Kahvaltı:      {kahvalti} kcal")
print(f"Öğle Yemeği:   {ogle} kcal")
print(f"Akşam Yemeği:  {aksam} kcal")
print(f"Atıştırmalık:  {atistirmalik} kcal")
print("─" * 25)
print(f"TOPLAM:       {toplam_kalori} kcal")
print()

# ========================================
# SORU 26: Kullanıcıdan İsim ve Yaş Alma (INPUT)
# ========================================
print("=" * 50)
print("SORU 26: İSİM VE YAŞ ALMA")
print("=" * 50)

isim = input("İsminiz: ")
yas = input("Yaşınız: ")

print()
print("╔════════════════════════╗")
print("║  HOŞ GELDİNİZ!        ║")
print(f"║  Ad: {isim:<16} ║")
print(f"║  Yaş: {yas:<15} ║")
print("╚════════════════════════╝")
print()

# ========================================
# SORU 27: Dikdörtgen Alan Hesaplama (INPUT)
# ========================================
print("=" * 50)
print("SORU 27: DİKDÖRTGEN ALAN")
print("=" * 50)

uzun_kenar = float(input("Uzun kenar (cm): "))
kisa_kenar = float(input("Kısa kenar (cm): "))

alan = uzun_kenar * kisa_kenar

print()
print("📐 DİKDÖRTGEN ALAN HESABI")
print(f"Uzun Kenar: {uzun_kenar} cm")
print(f"Kısa Kenar: {kisa_kenar} cm")
print(f"ALAN: {alan} cm²")
print()

# ========================================
# SORU 35: Kafe Hesabı (INPUT + COWSAY)
# ========================================
print("=" * 50)
print("SORU 35: KAFE HESABI (COWSAY)")
print("=" * 50)

import cowsay

kahve_adet = int(input("Kaç kahve: "))
kek_adet = int(input("Kaç kek: "))

kahve_fiyat = 35
kek_fiyat = 25

toplam_hesap = (kahve_adet * kahve_fiyat) + (kek_adet * kek_fiyat)

print()
cowsay.cow(f"Toplam: {toplam_hesap} TL")
print()

# ========================================
# EK ÖRNEK: Tüm Print Formatları
# ========================================
print("=" * 50)
print("BONUS: PRİNT FORMATLARI")
print("=" * 50)

print("1. Basit print:")
print("Merhaba Dünya!")
print()

print("2. F-string ile print:")
sayi = 42
print(f"Sayı: {sayi}")
print()

print("3. Çizgi çekmek:")
print("═" * 30)
print("─" * 30)
print("━" * 30)
print()

print("4. Emoji kullanımı:")
print("🎉 Başarılı!")
print("⚠️  Dikkat!")
print("✅ Tamamlandı!")
print()

print("5. Çoklu satır düzenleme:")
print("""
╔════════════════╗
║  PYTHON 2025  ║
║  1. HAFTA     ║
╚════════════════╝
""")

print("=" * 50)
print("ÇÖZÜMLER TAMAMLANDI! 🎉")
print("=" * 50)