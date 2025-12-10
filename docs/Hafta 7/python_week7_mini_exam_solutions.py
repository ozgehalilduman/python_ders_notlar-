# =================================================================
# PYTHON 7. HAFTA MİNİ SINAV ÇÖZÜMLERİ
# KONU: LİSTELER (Try-Except blokları olmadan sadeleştirilmiş versiyon)
# =================================================================

# ========================================
# SORU 1 (8 Puan) - KOLAY
# Alışveriş Listesi Oluşturucu
# ========================================
print("=" * 70)
print("SORU 1 (8 Puan) - KOLAY: Alışveriş Listesi Oluşturucu")
print("=" * 70)

alisveris_listesi = []

# 5 ürünü listeye ekleme (3 Puan)
print("--- Ürün Girişi ---")
for i in range(5):
    urun = input(f"{i + 1}. ürün: ")
    alisveris_listesi.append(urun)

print("\n═══════════════════════════")
print("    ALIŞVERİŞ LİSTESİ")
print("═══════════════════════════")

# Numaralı listeleme (döngü ve enumerate) (2 Puan)
for index, urun in enumerate(alisveris_listesi):
    print(f"{index + 1}. {urun}")

# len() kullanımı (1 Puan)
toplam_urun = len(alisveris_listesi)
print(f"\nToplam ürün: {toplam_urun}")

# İlk ve son eleman erişimi (2 Puan)
if toplam_urun > 0:
    ilk_urun = alisveris_listesi[0]
    son_urun = alisveris_listesi[-1]
    print(f"İlk ürün: {ilk_urun}")
    print(f"Son ürün: {son_urun}")
    
print()
print(" PUANLAMA:")
print("  • 5 ürünü listeye ekleme: 3 puan")
print("  • Numaralı listeleme (döngü): 2 puan")
print("  • len() kullanımı: 1 puan")
print("  • İlk ve son eleman erişimi: 2 puan")
print("----------------------------------------------------------------------")


# ========================================
# SORU 2 (10 Puan) - KOLAY-ORTA
# Sayı Listesi Analizi
# ========================================
print("=" * 70)
print("SORU 2 (10 Puan) - KOLAY-ORTA: Sayı Listesi Analizi")
print("=" * 70)

sayilar = []
cift_sayilar = []

# 6 sayıyı listeye ekleme (2 Puan)
print("--- Sayı Girişi ---")
for i in range(6):
    # Hata kontrolsüz int() dönüşümü yapılmıştır
    sayi = int(input(f"{i + 1}. sayı: ")) 
    sayilar.append(sayi)
    
# Toplam ve Ortalama (3 Puan)
toplam = sum(sayilar)
ortalama = toplam / len(sayilar)

# Max ve min bulma (2 Puan)
en_buyuk = max(sayilar)
en_kucuk = min(sayilar)

# Çift sayıları filtreleme (3 Puan)
for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)

print("\n═══════════════════════════")
print("      ANALİZ SONUÇLARI")
print("═══════════════════════════")
print(f"Liste: {sayilar}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama:.2f}")
print(f"En Büyük: {en_buyuk}")
print(f"En Küçük: {en_kucuk}")
print(f"Çift Sayılar: {cift_sayilar}")
    
print()
print(" PUANLAMA:")
print("  • 6 sayıyı listeye ekleme: 2 puan")
print("  • Toplam hesaplama: 2 puan")
print("  • Ortalama hesaplama: 1 puan")
print("  • Max ve min bulma: 2 puan")
print("  • Çift sayıları filtreleme: 3 puan")
print("----------------------------------------------------------------------")


# ========================================
# SORU 3 (12 Puan) - ORTA
# Not Defteri Uygulaması (CRUD Menüsü)
# ========================================
print("=" * 70)
print("SORU 3 (12 Puan) - ORTA: Not Defteri Uygulaması")
print("=" * 70)

notlar = [] # Boş liste oluşturma (1 Puan)

while True: # while True döngüsü (2 Puan)
    print("\n═══════════════════════════")
    print("      NOT DEFTERİ")
    print("═══════════════════════════")
    print("1. Not ekle")
    print("2. Notları listele")
    print("3. Not sil")
    print("4. Çıkış")
    
    secim = input("Seçim: ")

    if secim == '1':
        # Not ekleme (append) (2 Puan)
        not_metni = input("Not: ")
        notlar.append(not_metni)
        print(" Not eklendi!")

    elif secim == '2':
        # Notları listeleme (for döngüsü) (2 Puan)
        if not notlar:
            print(" Not Defteri Boş.")
        else:
            print("\n NOTLARIM:")
            for index, not_m in enumerate(notlar): 
                print(f"{index + 1}. {not_m}")

    elif secim == '3':
        # Not silme (pop) (3 Puan)
        if not notlar:
            print("Silinecek not bulunmamaktadır.")
            continue
            
        print("\n📝 NOTLARIM:")
        for index, not_m in enumerate(notlar):
            print(f"{index + 1}. {not_m}")
            
        silinecek_no = int(input("Silmek istediğiniz notun sıra numarasını girin: ")) # Hata kontrolsüz

        if 1 <= silinecek_no <= len(notlar):
            silinen_not = notlar.pop(silinecek_no - 1) 
            print(f" '{silinen_not}' notu silindi!")
        else:
            print(" Geçersiz sıra numarası!")

    elif secim == '4':
        # Çıkış (break) (1 Puan)
        print("\n👋 Çıkış yapılıyor...")
        break # Döngüden çıkar

    else:
        # Formatlı çıktı (1 Puan)
        print(" Geçersiz seçim. Lütfen 1, 2, 3 veya 4 girin.")

print()
print(" PUANLAMA:")
print("  • Boş liste oluşturma: 1 puan")
print("  • while True döngüsü ve menü: 2 puan")
print("  • Not ekleme (append): 2 puan")
print("  • Notları listeleme (for döngüsü): 2 puan")
print("  • Not silme (pop veya remove): 3 puan")
print("  • Çıkış (break): 1 puan")
print("  • Formatlı çıktı: 1 puan")
print("----------------------------------------------------------------------")


# ========================================
# SORU 4 (10 Puan) - ORTA
# Kelime Oyunu - Palindrome Listesi
# ========================================
print("=" * 70)
print("SORU 4 (10 Puan) - ORTA: Kelime Oyunu - Palindrome Listesi")
print("=" * 70)

girilen_kelimeler = []
palindrome_kelimeler = [] # Palindrome listesi oluşturma (2 Puan)

# 5 kelimeyi listeye ekleme (2 Puan)
print("--- Kelime Girişi ---")
for i in range(5):
    kelime = input(f"{i + 1}. kelime: ").lower()
    girilen_kelimeler.append(kelime)
    
    # Kelime ters çevirme ([::-1] slicing) (2 Puan)
    ters_kelime = kelime[::-1] 
    
    # Palindrome kontrolü (if karşılaştırma) (2 Puan)
    if kelime == ters_kelime:
        print(f'"{kelime}" tersi "{ters_kelime}" - PALİNDROME ✓')
        palindrome_kelimeler.append(kelime)
    else:
        print(f'"{kelime}" tersi "{ters_kelime}" - Palindrome değil')

print("\n═══════════════════════════")
print("      SONUÇLAR")
print("═══════════════════════════")
print(f"Girilen Kelimeler: {girilen_kelimeler}")
print(f"Palindrome Kelimeler: {palindrome_kelimeler}")

# Formatlı çıktı ve sayma (2 Puan)
print(f"Toplam Palindrome: {len(palindrome_kelimeler)}")

print()
print(" PUANLAMA:")
print("  • 5 kelimeyi listeye ekleme: 2 puan")
print("  • Kelime ters çevirme ([::-1]): 2 puan")
print("  • Palindrome kontrolü (if karşılaştırma): 2 puan")
print("  • Palindrome listesi oluşturma: 2 puan")
print("  • Formatlı çıktı ve sayma: 2 puan")
print("----------------------------------------------------------------------")


# ========================================
# SORU 5 (10 Puan) - ORTA-ZOR
# Öğrenci Not Sistemi
# ========================================
print("=" * 70)
print("SORU 5 (10 Puan) - ORTA-ZOR: Öğrenci Not Sistemi")
print("=" * 70)

isimler = []    # İki paralel liste oluşturma (2 Puan)
notlar = []

# Harf notu hesaplama fonksiyonu
def harf_notu_hesapla(not_degeri):
    # Harf notu hesaplama (if-elif-else) (3 Puan)
    if not_degeri >= 85:
        return 'A'
    elif not_degeri >= 70:
        return 'B'
    elif not_degeri >= 50:
        return 'C'
    else:
        return 'F'

# 3 öğrenci bilgisi alma (1 Puan)
for i in range(3):
    print(f"\n{i + 1}. öğrenci:")
    isim = input("İsim: ")
    not_degeri = int(input("Not: ")) # Hata kontrolsüz
            
    isimler.append(isim)
    notlar.append(not_degeri)

# Öğrenci bilgilerini birleştirme
ogrenci_bilgileri = []
for isim, not_degeri in zip(isimler, notlar):
    harf = harf_notu_hesapla(not_degeri)
    ogrenci_bilgileri.append((isim, not_degeri, harf))

# Sıralama (sorted) (2 Puan)
sirali_ogrenci_bilgileri = sorted(ogrenci_bilgileri, key=lambda x: x[1], reverse=True)

# Sınıf ortalaması (1 Puan)
sinif_ortalamasi = sum(notlar) / len(notlar)

print("\n═══════════════════════════")
print("    SINIF NOT TABLOSU")
print("═══════════════════════════")

# Formatlı tablo çıktısı (1 Puan)
for i, (isim, not_degeri, harf) in enumerate(sirali_ogrenci_bilgileri):
    print(f"{i + 1}. {isim.ljust(8)}: {not_degeri} ({harf})") 

print("═══════════════════════════")
print(f"Sınıf Ortalaması: {sinif_ortalamasi:.1f}")

print()
print(" PUANLAMA:")
print("  • İki liste oluşturma (isim, not): 2 puan")
print("  • 3 öğrenci bilgisi alma: 1 puan")
print("  • Harf notu hesaplama (if-elif-else): 3 puan")
print("  • Sıralama (sorted veya sort kullanarak): 2 puan")
print("  • Sınıf ortalaması: 1 puan")
print("  • Formatlı tablo çıktısı: 1 puan")
print("----------------------------------------------------------------------")