# ========================================
# PYTHON 6. HAFTA - ÖRNEK ÇÖZÜMLER
# Döngüler - while Döngüsü
# ========================================

print("=" * 70)
print("PYTHON 6. HAFTA - WHILE DÖNGÜSÜ ÖRNEK ÇÖZÜMLER")
print("=" * 70)
print()

# ========================================
# SORU 1: 1'den 10'a Sayma
# ========================================
print("=" * 70)
print("SORU 1: 1'DEN 10'A SAYMA (while ile)")
print("=" * 70)

sayac = 1

print("Sayılar:")
while sayac <= 10:
    print(sayac, end=" ")
    sayac += 1

print("\n")

# ========================================
# SORU 2: Şifre Kontrolü
# ========================================
print("=" * 70)
print("SORU 2: ŞİFRE KONTROLÜ")
print("=" * 70)

dogru_sifre = "1234"
girilen_sifre = ""

while girilen_sifre != dogru_sifre:
    girilen_sifre = input("Şifre girin: ")
    
    if girilen_sifre != dogru_sifre:
        print("❌ Yanlış şifre! Tekrar deneyin.")

print("✅ Giriş başarılı!")
print()

# ========================================
# SORU 4: Pozitif Sayı Alma
# ========================================
print("=" * 70)
print("SORU 4: POZİTİF SAYI ALMA")
print("=" * 70)

sayi = -1

while sayi <= 0:
    sayi = float(input("Pozitif bir sayı girin: "))
    
    if sayi <= 0:
        print("❌ Negatif veya sıfır! Pozitif sayı girin.")

print(f"✅ Girdiğiniz sayı: {sayi}")
print()

# ========================================
# SORU 5: Geri Sayım
# ========================================
print("=" * 70)
print("SORU 5: GERİ SAYIM")
print("=" * 70)

print("🚀 10'dan 1'e Geri Sayım:")
sayac_geri = 10

while sayac_geri >= 1:
    print(sayac_geri, end=" ")
    sayac_geri -= 1

print("\n🎉 Başla!\n")

# ========================================
# SORU 10: Sayı Toplama (Toplam 50'yi geçince dur)
# ========================================
print("=" * 70)
print("SORU 10: SAYI TOPLAMA (50'yi geçince dur)")
print("=" * 70)

toplam = 0
sayac_top = 0

while toplam < 50:
    sayi_girdi = int(input(f"Sayı girin (Toplam: {toplam}): "))
    toplam += sayi_girdi
    sayac_top += 1

print()
print("🎯 SONUÇ")
print("━" * 70)
print(f"Toplam 50'yi geçti: {toplam}")
print(f"Girilen sayı adedi: {sayac_top}")
print()

# ========================================
# SORU 11: Basit Menü
# ========================================
print("=" * 70)
print("SORU 11: BASİT MENÜ")
print("=" * 70)

while True:
    print("\n--- MENÜ ---")
    print("1. Merhaba")
    print("2. Hoşça kal")
    print("3. Çıkış")
    
    secim = input("Seçiminiz (1-3): ")
    
    if secim == "1":
        print("👋 Merhaba!")
    elif secim == "2":
        print("👋 Hoşça kalın!")
    elif secim == "3":
        print("❌ Çıkış yapılıyor...")
        break
    else:
        print("⚠️  Geçersiz seçim!")

print()

# ========================================
# SORU 16: Ortalama Hesaplama
# ========================================
print("=" * 70)
print("SORU 16: ORTALAMA HESAPLAMA")
print("=" * 70)

print("Sayılar girin (Bitirmek için 0):")
toplam_ort = 0
adet_ort = 0

while True:
    sayi_ort = float(input("Sayı: "))
    
    if sayi_ort == 0:
        break
    
    toplam_ort += sayi_ort
    adet_ort += 1

print()
if adet_ort > 0:
    ortalama = toplam_ort / adet_ort
    print(f"📊 Girilen {adet_ort} sayının ortalaması: {ortalama:.2f}")
else:
    print("Hiç sayı girilmedi!")

print()

# ========================================
# SORU 17: En Büyük Sayı Bulma
# ========================================
print("=" * 70)
print("SORU 17: EN BÜYÜK SAYI BULMA")
print("=" * 70)

print("Sayılar girin (Bitirmek için -1):")
en_buyuk = None

while True:
    sayi_eb = float(input("Sayı: "))
    
    if sayi_eb == -1:
        break
    
    if en_buyuk is None or sayi_eb > en_buyuk:
        en_buyuk = sayi_eb

print()
if en_buyuk is not None:
    print(f"🏆 En büyük sayı: {en_buyuk}")
else:
    print("Hiç sayı girilmedi!")

print()

# ========================================
# SORU 19: Faktöriyel (while ile)
# ========================================
print("=" * 70)
print("SORU 19: FAKTÖRİYEL (while ile)")
print("=" * 70)

n = int(input("Bir sayı girin: "))
faktoriyel = 1
sayac_fak = 1

while sayac_fak <= n:
    faktoriyel *= sayac_fak
    sayac_fak += 1

print()
print(f"🔢 {n}! = {faktoriyel}")
print()

# ========================================
# SORU 20: Fibonacci (while ile)
# ========================================
print("=" * 70)
print("SORU 20: FİBONACCI (while ile)")
print("=" * 70)

print("🔢 İlk 10 Fibonacci Sayısı:")
a, b = 0, 1
sayac_fib = 0

while sayac_fib < 10:
    print(a, end=" ")
    a, b = b, a + b
    sayac_fib += 1

print("\n")

# ========================================
# SORU 22: Sayı Tahmin Oyunu
# ========================================
print("=" * 70)
print("SORU 22: SAYI TAHMİN OYUNU")
print("=" * 70)

import random

gizli_sayi = random.randint(1, 100)
tahmin_sayisi = 0

print("🎲 1-100 arası bir sayı tuttum!")
print("Tahmin edin:")

while True:
    tahmin = int(input("\nTahminiz: "))
    tahmin_sayisi += 1
    
    if tahmin == gizli_sayi:
        print(f"🎉 Tebrikler! {tahmin_sayisi} tahminde buldunuz!")
        break
    elif tahmin < gizli_sayi:
        print("⬆️  Daha büyük bir sayı")
    else:
        print("⬇️  Daha küçük bir sayı")

print()

# ========================================
# SORU 23: Kullanıcı Girişi (3 Deneme)
# ========================================
print("=" * 70)
print("SORU 23: KULLANICI GİRİŞİ (3 Deneme)")
print("=" * 70)

dogru_sifre_3 = "python123"
deneme_hakki = 3
giris_basarili = False

while deneme_hakki > 0:
    sifre_3 = input(f"Şifre (Kalan hak: {deneme_hakki}): ")
    
    if sifre_3 == dogru_sifre_3:
        print("✅ Giriş başarılı!")
        giris_basarili = True
        break
    else:
        deneme_hakki -= 1
        if deneme_hakki > 0:
            print(f"❌ Yanlış şifre! {deneme_hakki} hakkınız kaldı.")

if not giris_basarili:
    print("🔒 Hesap kilitlendi!")

print()

# ========================================
# SORU 26: Basamak Sayma
# ========================================
print("=" * 70)
print("SORU 26: BASAMAK SAYMA")
print("=" * 70)

sayi_basamak = int(input("Bir sayı girin: "))
basamak_sayisi = 0
gecici = abs(sayi_basamak)  # Mutlak değer (negatif için)

if gecici == 0:
    basamak_sayisi = 1
else:
    while gecici > 0:
        basamak_sayisi += 1
        gecici //= 10

print()
print(f"🔢 {sayi_basamak} sayısı {basamak_sayisi} basamaklıdır.")
print()

# ========================================
# SORU 31: Hesap Makinesi (Sürekli)
# ========================================
print("=" * 70)
print("SORU 31: HESAP MAKİNESİ (Sürekli)")
print("=" * 70)

print("🧮 HESAP MAKİNESİ")
print("İşlemler: +, -, *, /")
print("Çıkmak için 'q' yazın")
print("━" * 70)

while True:
    islem = input("\nİşlem seçin (+,-,*,/ veya q): ")
    
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
            sonuc = sayi1 + sayi2
        elif islem == '-':
            sonuc = sayi1 - sayi2
        elif islem == '*':
            sonuc = sayi1 * sayi2
        elif islem == '/':
            if sayi2 != 0:
                sonuc = sayi1 / sayi2
            else:
                print("❌ Sıfıra bölme hatası!")
                continue
        
        print(f"✅ Sonuç: {sayi1} {islem} {sayi2} = {sonuc}")
        
    except ValueError:
        print("❌ Geçersiz sayı girdiniz!")

print()

# ========================================
# SORU 32: Collatz Sanısı (while ile)
# ========================================
print("=" * 70)
print("SORU 32: COLLATZ SANISI")
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
# SORU 33: EBOB Bulma (Öklid Algoritması)
# ========================================
print("=" * 70)
print("SORU 33: EBOB BULMA (Öklid Algoritması)")
print("=" * 70)

a = int(input("1. sayı: "))
b = int(input("2. sayı: "))

a_orijinal = a
b_orijinal = b

while b != 0:
    kalan = a % b
    a = b
    b = kalan

print()
print(f"🔢 EBOB({a_orijinal}, {b_orijinal}) = {a}")
print()

# ========================================
# SORU 35: To-Do List Uygulaması
# ========================================
print("=" * 70)
print("SORU 35: TO-DO LIST UYGULAMASI")
print("=" * 70)

gorevler = []

while True:
    print("\n📝 YAPILACAKLAR LİSTESİ")
    print("━" * 70)
    print("1. Görev ekle")
    print("2. Görevleri listele")
    print("3. Görev sil")
    print("4. Çıkış")
    print("━" * 70)
    
    secim_todo = input("Seçiminiz: ")
    
    if secim_todo == "1":
        gorev = input("Görev: ")
        gorevler.append(gorev)
        print("✅ Görev eklendi!")
        
    elif secim_todo == "2":
        if len(gorevler) == 0:
            print("📭 Liste boş!")
        else:
            print("\n📋 GÖREVLER:")
            for i, gorev in enumerate(gorevler, 1):
                print(f"{i}. {gorev}")
                
    elif secim_todo == "3":
        if len(gorevler) == 0:
            print("❌ Silinecek görev yok!")
        else:
            print("\n📋 GÖREVLER:")
            for i, gorev in enumerate(gorevler, 1):
                print(f"{i}. {gorev}")
            
            try:
                sira = int(input("Silinecek görev numarası: "))
                if 1 <= sira <= len(gorevler):
                    silinen = gorevler.pop(sira - 1)
                    print(f"🗑️  '{silinen}' silindi!")
                else:
                    print("❌ Geçersiz numara!")
            except ValueError:
                print("❌ Geçersiz giriş!")
                
    elif secim_todo == "4":
        print("👋 Çıkış yapılıyor...")
        break
    else:
        print("❌ Geçersiz seçim!")

print()

# ========================================
# BİTİŞ MESAJI VE ÖNEMLİ NOTLAR
# ========================================
print("=" * 70)
print("✅ TÜM WHILE DÖNGÜSÜ ÇÖZÜMLER TAMAMLANDI!")
print("=" * 70)
print()
print("💡 WHILE DÖNGÜSÜ ÖNEMLİ NOTLAR:")
print()
print("1️⃣  TEMEL YAPI:")
print("   while koşul:")
print("       # Kod")
print("       # Sayacı güncelle!")
print()
print("2️⃣  SONSUZ DÖNGÜDEN KAÇININ:")
print("   • Mutlaka bir çıkış koşulu olmalı")
print("   • Sayaç varsa mutlaka güncelleyin")
print("   • break ile çıkış yolu bırakın")
print()
print("3️⃣  WHILE TRUE KULLANIMI:")
print("   while True:")
print("       if cikis_kosulu:")
print("           break")
print()
print("4️⃣  BREAK ve CONTINUE:")
print("   • break → Döngüyü tamamen bitirir")
print("   • continue → O adımı atlar, devam eder")
print()
print("5️⃣  NE ZAMAN WHILE KULLANMALI:")
print("   • Kaç kere döneceği belirsiz")
print("   • Kullanıcı 'dur' diyene kadar")
print("   • Oyun döngüleri")
print("   • Menü sistemleri")
print()
print("6️⃣  FOR vs WHILE:")
print("   • for → Belirli tekrar sayısı")
print("   • while → Belirsiz tekrar sayısı")
print()
print("7️⃣  VERI DOĞRULAMA:")
print("   while girdi_gecersiz:")
print("       girdi = input('Tekrar girin: ')")
print()
print("8️⃣  SAYAÇ KULLANIMI:")
print("   sayac = 0")
print("   while sayac < 10:")
print("       print(sayac)")
print("       sayac += 1  # UNUTMAYIN!")
print()
print("=" * 70)
print("🎉 while döngülerinde ustalaştınız! Tebrikler!")
print("=" * 70)