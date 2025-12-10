# ========================================
# PYTHON 5. HAFTA - ÖRNEK ÇÖZÜMLER
# Döngüler - for Döngüsü
# ========================================

print("=" * 70)
print("PYTHON 5. HAFTA - FOR DÖNGÜSÜ ÖRNEK ÇÖZÜMLER")
print("=" * 70)
print()

# ========================================
# SORU 1: 1'den 10'a Kadar Sayılar
# ========================================
print("=" * 70)
print("SORU 1: 1'DEN 10'A KADAR SAYILAR")
print("=" * 70)

print("Sayılar:")
for i in range(1, 11):  # 11 dahil değil, bu yüzden 10'a kadar
    print(i)

print()

# ========================================
# SORU 4: 0-20 Arası Çift Sayılar
# ========================================
print("=" * 70)
print("SORU 4: 0-20 ARASI ÇİFT SAYILAR")
print("=" * 70)

print("Çift Sayılar:")

# Yöntem 1: if ile kontrol
for i in range(21):
    if i % 2 == 0:
        print(i, end=" ")
print()

# Yöntem 2: range adım ile (daha verimli)
print("\nAlternatif yöntem:")
for i in range(0, 21, 2):  # 2'şer atlayarak
    print(i, end=" ")

print("\n")

# ========================================
# SORU 5: Geri Sayım
# ========================================
print("=" * 70)
print("SORU 5: GERİ SAYIM")
print("=" * 70)

print("🚀 10'dan 1'e Geri Sayım:")
for i in range(10, 0, -1):  # -1 ile geriye doğru
    print(i)

print("🎉 Başla!")
print()

# ========================================
# SORU 6: Kelime Harflerini Tek Tek Yazdırma
# ========================================
print("=" * 70)
print("SORU 6: KELİME HARFLERİNİ TEK TEK YAZDIRMA")
print("=" * 70)

kelime = input("Bir kelime girin: ")

print("\nHarfler:")
for harf in kelime:
    print(f"→ {harf}")

print()

# ========================================
# SORU 7: 1-10 Arası Toplam
# ========================================
print("=" * 70)
print("SORU 7: 1-10 ARASI TOPLAM")
print("=" * 70)

toplam = 0
for i in range(1, 11):
    toplam += i  # toplam = toplam + i

print("➕ TOPLAMA İŞLEMİ")
print("━" * 70)
print(f"{sayi_fak}! = {faktoriyel}")

# Adım adım göster
carpim_str = " × ".join([str(i) for i in range(1, sayi_fak + 1)])
print(f"Hesaplama: {carpim_str} = {faktoriyel}")
print()

# ========================================
# SORU 18: Fibonacci Serisi
# ========================================
print("=" * 70)
print("SORU 18: FİBONACCI SERİSİ")
print("=" * 70)

print("🔢 İlk 10 Fibonacci Sayısı:")
print("━" * 70)

a, b = 0, 1
print(a, end=" ")
print(b, end=" ")

for i in range(8):  # 2 sayı zaten yazdırıldı, 8 tane daha
    c = a + b
    print(c, end=" ")
    a, b = b, c

print("\n")

# ========================================
# SORU 20: Basamak Toplamı
# ========================================
print("=" * 70)
print("SORU 20: BASAMAK TOPLAMI")
print("=" * 70)

sayi_basamak = int(input("Bir sayı girin: "))
toplam_basamak = 0
gecici = sayi_basamak

while gecici > 0:
    basamak = gecici % 10
    toplam_basamak += basamak
    gecici //= 10

print()
print("🔢 BASAMAK ANALİZİ")
print("━" * 70)
print(f"Sayı: {sayi_basamak}")
print(f"Basamaklar Toplamı: {toplam_basamak}")
print()

# ========================================
# SORU 21: Ters Çevrilmiş Üçgen
# ========================================
print("=" * 70)
print("SORU 21: TERS ÇEVRİLMİŞ ÜÇGEN")
print("=" * 70)

print("⭐ TERS ÜÇGEN:")
for i in range(5, 0, -1):  # 5'ten 1'e
    print("*" * i)

print()

# ========================================
# SORU 23: Armstrong Sayı Kontrolü
# ========================================
print("=" * 70)
print("SORU 23: ARMSTRONG SAYI KONTROLÜ")
print("=" * 70)

sayi_arm = int(input("3 basamaklı sayı girin: "))

# Basamakları ayır
yuzler = sayi_arm // 100
onlar = (sayi_arm % 100) // 10
birler = sayi_arm % 10

# Armstrong kontrolü (her basamağın küpü)
kup_toplami = (yuzler ** 3) + (onlar ** 3) + (birler ** 3)

print()
print("🔍 ARMSTRONG KONTROLÜ")
print("━" * 70)
print(f"Sayı: {sayi_arm}")
print(f"Basamaklar: {yuzler}, {onlar}, {birler}")
print(f"Hesaplama: {yuzler}³ + {onlar}³ + {birler}³ = {kup_toplami}")

if sayi_arm == kup_toplami:
    print("✅ Bu bir ARMSTRONG sayısıdır!")
else:
    print("❌ Bu bir Armstrong sayısı değildir.")

print()

# ========================================
# SORU 25: Piramit Şekli
# ========================================
print("=" * 70)
print("SORU 25: PİRAMİT ŞEKLİ")
print("=" * 70)

print("⭐ ORTALANMIŞ PİRAMİT:")
satirlar = 5

for i in range(1, satirlar + 1):
    bosluk = " " * (satirlar - i)
    yildiz = "*" * (2 * i - 1)
    print(bosluk + yildiz)

print()

# ========================================
# SORU 26: Palindrome Sayı Kontrolü
# ========================================
print("=" * 70)
print("SORU 26: PALINDROME SAYI KONTROLÜ")
print("=" * 70)

sayi_pal = input("Bir sayı girin: ")
ters_sayi = sayi_pal[::-1]

print()
print("🔄 PALINDROME KONTROLÜ")
print("━" * 70)
print(f"Sayı: {sayi_pal}")
print(f"Tersi: {ters_sayi}")

if sayi_pal == ters_sayi:
    print("✅ Bu bir PALINDROME sayısıdır!")
else:
    print("❌ Palindrome değildir.")

print()

# ========================================
# SORU 27: İç İçe Döngü - Çarpım Tablosu
# ========================================
print("=" * 70)
print("SORU 27: ÇARPIM TABLOSU (1-5)")
print("=" * 70)

print("📊 ÇARPIM TABLOSU")
print("━" * 70)

for i in range(1, 6):
    print(f"\n{i}'in Çarpım Tablosu:")
    for j in range(1, 11):
        print(f"{i} x {j:2} = {i*j:3}", end="  ")
    print()

print()

# ========================================
# SORU 28: Kuvvet Hesaplama (Döngü ile)
# ========================================
print("=" * 70)
print("SORU 28: KUVVET HESAPLAMA")
print("=" * 70)

taban = int(input("Taban sayı: "))
us = int(input("Üs sayı: "))

sonuc_kuvvet = 1
for i in range(us):
    sonuc_kuvvet *= taban

print()
print("🔢 ÜSLÜ SAYI HESABI")
print("━" * 70)
print(f"{taban}^{us} = {sonuc_kuvvet}")

# Doğrulama
print(f"Doğrulama: {taban ** us}")
print()

# ========================================
# SORU 31: Asal Sayı Listesi (1-50)
# ========================================
print("=" * 70)
print("SORU 31: ASAL SAYI LİSTESİ")
print("=" * 70)

print("🔢 1-50 ARASI ASAL SAYILAR:")
print("━" * 70)

asal_sayilar = []

for sayi in range(2, 51):  # 2'den başla (1 asal değil)
    asal_mi = True
    
    for bolen in range(2, sayi):
        if sayi % bolen == 0:
            asal_mi = False
            break
    
    if asal_mi:
        asal_sayilar.append(sayi)
        print(sayi, end=" ")

print(f"\n\nToplam {len(asal_sayilar)} adet asal sayı bulundu.")
print()

# ========================================
# SORU 32: Elmas Şekli
# ========================================
print("=" * 70)
print("SORU 32: ELMAS ŞEKLİ")
print("=" * 70)

print("💎 ELMAS:")
n = 5

# Üst kısım (genişleyen)
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Alt kısım (daralan)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print()

# ========================================
# SORU 33: Collatz Sanısı
# ========================================
print("=" * 70)
print("SORU 33: COLLATZ SANISI")
print("=" * 70)

sayi_collatz = int(input("Başlangıç sayısı: "))

print()
print("🔢 COLLATZ DİZİSİ:")
print("━" * 70)

adim = 0
print(sayi_collatz, end=" → ")

while sayi_collatz != 1:
    if sayi_collatz % 2 == 0:
        sayi_collatz = sayi_collatz // 2
    else:
        sayi_collatz = sayi_collatz * 3 + 1
    
    print(sayi_collatz, end=" → " if sayi_collatz != 1 else "")
    adim += 1

print(f"\n\nToplam {adim} adımda 1'e ulaşıldı.")
print()

# ========================================
# SORU 38: Sayı Desenli Piramit
# ========================================
print("=" * 70)
print("SORU 38: SAYI DESENLİ PİRAMİT")
print("=" * 70)

print("🔢 SAYI PİRAMİDİ:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print()

# ========================================
# SORU 40: Mini Hesap Makinesi (Döngülü)
# ========================================
print("=" * 70)
print("SORU 40: MİNİ HESAP MAKİNESİ (DÖNGÜLÜ)")
print("=" * 70)

print("🧮 HESAP MAKİNESİ")
print("━" * 70)
print("İşlemler: +, -, *, /")
print("Çıkmak için 'q' yazın")
print("━" * 70)

while True:
    islem = input("\nİşlem seçin (+, -, *, / veya q): ")
    
    if islem.lower() == 'q':
        print("👋 Hesap makinesi kapatılıyor...")
        break
    
    if islem not in ['+', '-', '*', '/']:
        print("❌ Geçersiz işlem!")
        continue
    
    try:
        sayi1 = float(input("1. sayı: "))
        sayi2 = float(input("2. sayı: "))
        
        if islem == '+':
            sonuc_hm = sayi1 + sayi2
        elif islem == '-':
            sonuc_hm = sayi1 - sayi2
        elif islem == '*':
            sonuc_hm = sayi1 * sayi2
        elif islem == '/':
            if sayi2 != 0:
                sonuc_hm = sayi1 / sayi2
            else:
                print("❌ Sıfıra bölme hatası!")
                continue
        
        print(f"✅ Sonuç: {sayi1} {islem} {sayi2} = {sonuc_hm}")
        
    except ValueError:
        print("❌ Lütfen geçerli bir sayı girin!")

print()

# ========================================
# BİTİŞ MESAJI VE ÖNEMLİ NOTLAR
# ========================================
print("=" * 70)
print("✅ TÜM FOR DÖNGÜSÜ ÇÖZÜMLER TAMAMLANDI!")
print("=" * 70)
print()
print("💡 FOR DÖNGÜSÜ ÖNEMLİ NOTLAR:")
print()
print("1️⃣  RANGE() KULLANIMI:")
print("   • range(5) → 0, 1, 2, 3, 4 (5 dahil değil!)")
print("   • range(1, 6) → 1, 2, 3, 4, 5")
print("   • range(0, 10, 2) → 0, 2, 4, 6, 8 (çift sayılar)")
print("   • range(10, 0, -1) → 10, 9, 8, ..., 1 (geriye)")
print()
print("2️⃣  GİRİNTİ (INDENTATION):")
print("   • Döngü içindeki kodlar 4 boşluk girintili olmalı")
print("   • Hata: IndentationError")
print()
print("3️⃣  İKİ NOKTA ÜST ÜSTE:")
print("   • for i in range(5): (: unutmayın!)")
print()
print("4️⃣  BREAK ve CONTINUE:")
print("   • break → Döngüyü tamamen sonlandırır")
print("   • continue → O adımı atlar, devam eder")
print()
print("5️⃣  STRING İLE DÖNGÜ:")
print("   • for harf in 'Python': → Her karakter")
print()
print("6️⃣  LİSTE İLE DÖNGÜ:")
print("   • for eleman in liste: → Her eleman")
print()
print("7️⃣  İÇ İÇE DÖNGÜLER:")
print("   • for i in range(3):")
print("       for j in range(3):")
print("           print(i, j)")
print()
print("8️⃣  ENUMERATE:")
print("   • for index, eleman in enumerate(liste):")
print("     → Hem index hem eleman")
print()
print("=" * 70)
print("🎉 For döngülerinde ustalaştınız! Tebrikler!")
print("=" * 70))
print("1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10")
print(f"Toplam = {toplam}")
print()

# ========================================
# SORU 8: Çarpım Tablosu (Tek Sayı)
# ========================================
print("=" * 70)
print("SORU 8: ÇARPIM TABLOSU")
print("=" * 70)

sayi = int(input("Bir sayı girin: "))

print()
print(f"📊 {sayi} ÇARPIM TABLOSU")
print("━" * 70)

for i in range(1, 11):
    sonuc = sayi * i
    print(f"{sayi} x {i:2} = {sonuc:3}")

print()

# ========================================
# SORU 10: Tek Sayıları Toplama
# ========================================
print("=" * 70)
print("SORU 10: TEK SAYILARI TOPLAMA")
print("=" * 70)

tek_toplam = 0
print("1'den 50'ye kadar tek sayılar:")

for i in range(1, 51):
    if i % 2 != 0:  # Tek sayı kontrolü
        print(i, end=" ")
        tek_toplam += i

print(f"\n\nTek sayıların toplamı: {tek_toplam}")
print()

# ========================================
# SORU 11: Liste Elemanlarını Yazdırma
# ========================================
print("=" * 70)
print("SORU 11: LİSTE ELEMANLARINI YAZDIRMA")
print("=" * 70)

diller = ["Python", "Java", "C++", "JavaScript"]

print("💻 PROGRAMLAMA DİLLERİ")
print("━" * 70)

# Yöntem 1: enumerate kullanarak
for index, dil in enumerate(diller, 1):  # 1'den başlat
    print(f"{index}. {dil}")

print()

# ========================================
# SORU 12: Yıldız Üçgeni
# ========================================
print("=" * 70)
print("SORU 12: YILDIZ ÜÇGENİ")
print("=" * 70)

print("⭐ ÜÇGEN ŞEKLİ:")
for i in range(1, 6):
    print("*" * i)

print()

# ========================================
# SORU 13: Sayıların Karesi
# ========================================
print("=" * 70)
print("SORU 13: SAYILARIN KARESİ")
print("=" * 70)

print("🔢 KARE TABLOSU")
print("━" * 70)

for i in range(1, 11):
    kare = i ** 2
    print(f"{i:2}² = {kare:3}")

print()

# ========================================
# SORU 14: Sesli Harf Sayma (Döngü ile)
# ========================================
print("=" * 70)
print("SORU 14: SESLİ HARF SAYMA")
print("=" * 70)

cumle = input("Bir cümle girin: ")
sesli_harfler = "aeıioöuüAEIİOÖUÜ"
sesli_sayisi = 0

for harf in cumle:
    if harf in sesli_harfler:
        sesli_sayisi += 1

print()
print("🔤 ANALİZ SONUCU")
print("━" * 70)
print(f"Cümle: {cumle}")
print(f"Toplam Karakter: {len(cumle)}")
print(f"Sesli Harf Sayısı: {sesli_sayisi}")
print()

# ========================================
# SORU 16: Faktöriyel Hesaplama
# ========================================
print("=" * 70)
print("SORU 16: FAKTÖRİYEL HESAPLAMA")
print("=" * 70)

sayi_fak = int(input("Bir sayı girin: "))
faktoriyel = 1

# Hesaplama
for i in range(1, sayi_fak + 1):
    faktoriyel *= i  # faktoriyel = faktoriyel * i

print()
print("🔢 FAKTÖRİYEL HESABI")
print("━" * 70