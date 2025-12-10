# ========================================
# PYTHON 2. HAFTA - ÖRNEK ÇÖZÜMLER
# Veri Tipleri ve Matematiksel İşlemler
# ========================================

print("=" * 60)
print("PYTHON 2. HAFTA - ÖRNEK ÇÖZÜMLER")
print("=" * 60)
print()

# ========================================
# SORU 1: Veri Tipi Belirleme
# ========================================
print("=" * 60)
print("SORU 1: VERİ TİPİ BELİRLEME")
print("=" * 60)

isim = "Python"
yas = 30
boy = 1.75
ogrenci_mi = True

print("VERİ TİPLERİ TABLOSU")
print("━" * 60)
print(f"Değişken: isim")
print(f"Değer: {isim}")
print(f"Tip: {type(isim)}")
print("━" * 60)
print(f"Değişken: yas")
print(f"Değer: {yas}")
print(f"Tip: {type(yas)}")
print("━" * 60)
print(f"Değişken: boy")
print(f"Değer: {boy}")
print(f"Tip: {type(boy)}")
print("━" * 60)
print(f"Değişken: ogrenci_mi")
print(f"Değer: {ogrenci_mi}")
print(f"Tip: {type(ogrenci_mi)}")
print("━" * 60)
print()

# ========================================
# SORU 2: Bölme İşlemleri Karşılaştırma
# ========================================
print("=" * 60)
print("SORU 2: BÖLME İŞLEMLERİ KARŞILAŞTIRMA")
print("=" * 60)

sayi = 100
bolen = 3

normal_bolme = sayi / bolen
tam_bolme = sayi // bolen
kalan = sayi % bolen

print("BÖLME İŞLEMLERİ")
print("━" * 60)
print(f"{sayi} / {bolen} = {normal_bolme:.3f} (float sonuç)")
print(f"{sayi} // {bolen} = {tam_bolme} (tam sayı kısmı)")
print(f"{sayi} % {bolen} = {kalan} (kalan)")
print("━" * 60)
print(f"Açıklama: {sayi} sayısı {bolen}'e {tam_bolme} kere tam bölünür,")
print(f"{kalan} kadar artar.")
print()

# ========================================
# SORU 3: Üs Alma İşlemleri
# ========================================
print("=" * 60)
print("SORU 3: ÜS ALMA İŞLEMLERİ")
print("=" * 60)

print("ÜS ALMA TABLOSU")
print("━" * 60)
print(f"2^1 = {2**1}")
print(f"2^2 = {2**2}")
print(f"2^3 = {2**3}")
print(f"2^4 = {2**4}")
print(f"2^5 = {2**5}")
print(f"2^6 = {2**6}")
print(f"2^7 = {2**7}")
print(f"2^8 = {2**8}")
print(f"2^9 = {2**9}")
print(f"2^10 = {2**10}")
print("━" * 60)
print()

# ========================================
# SORU 4: String'den Sayıya Dönüşüm
# ========================================
print("=" * 60)
print("SORU 4: STRING'DEN SAYIYA DÖNÜŞÜM")
print("=" * 60)

str_sayi1 = "123"
str_sayi2 = "45.6"

print(f"String 1: '{str_sayi1}' (tip: {type(str_sayi1)})")
print(f"String 2: '{str_sayi2}' (tip: {type(str_sayi2)})")
print()

# Dönüşüm
int_sayi1 = int(str_sayi1)
float_sayi2 = float(str_sayi2)

print(f"Dönüştürüldü: {int_sayi1} (tip: {type(int_sayi1)})")
print(f"Dönüştürüldü: {float_sayi2} (tip: {type(float_sayi2)})")
print()

toplam = int_sayi1 + float_sayi2
print(f"Toplam: {int_sayi1} + {float_sayi2} = {toplam}")
print(f"Sonuç tipi: {type(toplam)}")
print()

# ========================================
# SORU 5: Yaş Hesaplama (INPUT)
# ========================================
print("=" * 60)
print("SORU 5: YAŞ HESAPLAMA")
print("=" * 60)

dogum_yili = input("Doğum yılınız: ")
dogum_yili_int = int(dogum_yili)  # String'i int'e çevir

su_anki_yil = 2025
yas_hesap = su_anki_yil - dogum_yili_int

print()
print("📅 YAŞ HESAPLAMA")
print(f"Doğum Yılı: {dogum_yili_int} (tip: {type(dogum_yili_int)})")
print(f"Şu Anki Yıl: {su_anki_yil}")
print(f"Yaşınız: {yas_hesap}")
print()

# ========================================
# SORU 11: String Birleştirme vs Sayı Toplama
# ========================================
print("=" * 60)
print("SORU 11: STRING VS SAYI TOPLAMA")
print("=" * 60)

# String toplama
str1 = "5"
str2 = "3"
str_sonuc = str1 + str2

# Sayı toplama
sayi1 = 5
sayi2 = 3
sayi_sonuc = sayi1 + sayi2

print("STRING TOPLAMA:")
print(f"'{str1}' + '{str2}' = '{str_sonuc}' (birleştirme)")
print(f"Tip: {type(str_sonuc)}")
print()

print("SAYI TOPLAMA:")
print(f"{sayi1} + {sayi2} = {sayi_sonuc} (matematiksel toplama)")
print(f"Tip: {type(sayi_sonuc)}")
print()

print("⚠️  DİKKAT: String toplama birleştirir, sayı toplama hesaplar!")
print()

# ========================================
# SORU 12: Tam Bölme Uygulaması
# ========================================
print("=" * 60)
print("SORU 12: TAM BÖLME UYGULAMASI")
print("=" * 60)

toplam_alisveris = 125
kisi_sayisi = 4

kisi_basi_ucret = toplam_alisveris // kisi_sayisi
artan_para = toplam_alisveris % kisi_sayisi

print("🛒 MARKET HESABI")
print(f"Toplam Alışveriş: {toplam_alisveris} TL")
print(f"Kişi Sayısı: {kisi_sayisi}")
print("━" * 60)
print(f"Kişi Başı: {kisi_basi_ucret} TL")
print(f"Artan Para: {artan_para} TL")
print()
print(f"Açıklama: Her kişi {kisi_basi_ucret} TL öder, {artan_para} TL artar.")
print()

# ========================================
# SORU 13: Kare ve Küp Hesaplama
# ========================================
print("=" * 60)
print("SORU 13: KARE VE KÜP HESAPLAMA")
print("=" * 60)

sayi_input = int(input("Bir sayı girin: "))

kare = sayi_input ** 2
kup = sayi_input ** 3

print()
print("📊 HESAPLAMA SONUÇLARI")
print(f"Sayı: {sayi_input}")
print(f"Karesi: {sayi_input}² = {kare}")
print(f"Küpü: {sayi_input}³ = {kup}")
print()

# ========================================
# SORU 16: KDV Hesaplama
# ========================================
print("=" * 60)
print("SORU 16: KDV HESAPLAMA")
print("=" * 60)

urun_fiyati_kdv = float(input("Ürün fiyatı (TL): "))

kdv_orani = 18  # Yüzde 18
kdv_tutari = urun_fiyati_kdv * kdv_orani / 100
toplam_fiyat_kdv = urun_fiyati_kdv + kdv_tutari

print()
print("💰 KDV HESAPLAMA")
print(f"Ürün Fiyatı: {urun_fiyati_kdv} TL")
print(f"KDV Oranı: %{kdv_orani}")
print(f"KDV Tutarı: {kdv_tutari:.2f} TL")
print("━" * 60)
print(f"TOPLAM: {toplam_fiyat_kdv:.2f} TL")
print()

# ========================================
# SORU 22: İki Sayı Arasındaki İşlemler
# ========================================
print("=" * 60)
print("SORU 22: İKİ SAYI ARASINDAKİ TÜM İŞLEMLER")
print("=" * 60)

sayi_a = float(input("İlk sayı: "))
sayi_b = float(input("İkinci sayı: "))

print()
print("🔢 MATEMATIKSEL İŞLEMLER")
print("━" * 60)
print(f"{sayi_a} + {sayi_b} = {sayi_a + sayi_b}")
print(f"{sayi_a} - {sayi_b} = {sayi_a - sayi_b}")
print(f"{sayi_a} × {sayi_b} = {sayi_a * sayi_b}")
print(f"{sayi_a} ÷ {sayi_b} = {sayi_a / sayi_b:.2f}")
print(f"{sayi_a} // {sayi_b} = {sayi_a // sayi_b} (tam bölme)")
print(f"{sayi_a} % {sayi_b} = {sayi_a % sayi_b} (kalan)")
print(f"{sayi_a} ** {sayi_b} = {sayi_a ** sayi_b} (üs)")
print()

# ========================================
# SORU 32: Sayı Basamak Ayırma
# ========================================
print("=" * 60)
print("SORU 32: SAYI BASAMAK AYIRMA")
print("=" * 60)

uc_basamakli = int(input("3 basamaklı sayı girin (örn: 456): "))

yuzler = uc_basamakli // 100
onlar = (uc_basamakli % 100) // 10
birler = uc_basamakli % 10

print()
print("🔢 BASAMAK AYIRMA")
print(f"Sayı: {uc_basamakli}")
print("━" * 60)
print(f"Yüzler Basamağı: {yuzler}")
print(f"Onlar Basamağı: {onlar}")
print(f"Birler Basamağı: {birler}")
print()
print(f"Kontrol: {yuzler}×100 + {onlar}×10 + {birler}×1 = {yuzler*100 + onlar*10 + birler}")
print()

# ========================================
# SORU 35: Mini Hesap Makinesi
# ========================================
print("=" * 60)
print("SORU 35: MİNİ HESAP MAKİNESİ")
print("=" * 60)

sayi1_hm = float(input("İlk sayı: "))
operator = input("İşlem (+, -, *, /): ")
sayi2_hm = float(input("İkinci sayı: "))

print()
print("🧮 HESAP MAKİNESİ")
print("━" * 60)

if operator == "+":
    sonuc_hm = sayi1_hm + sayi2_hm
    print(f"{sayi1_hm} + {sayi2_hm} = {sonuc_hm}")
elif operator == "-":
    sonuc_hm = sayi1_hm - sayi2_hm
    print(f"{sayi1_hm} - {sayi2_hm} = {sonuc_hm}")
elif operator == "*":
    sonuc_hm = sayi1_hm * sayi2_hm
    print(f"{sayi1_hm} × {sayi2_hm} = {sonuc_hm}")
elif operator == "/":
    if sayi2_hm != 0:
        sonuc_hm = sayi1_hm / sayi2_hm
        print(f"{sayi1_hm} ÷ {sayi2_hm} = {sonuc_hm:.2f}")
    else:
        print("HATA: Sıfıra bölme yapılamaz!")
else:
    print("HATA: Geçersiz işlem!")

print()

# ========================================
# BONUS 1: Hatalı Kod Düzeltme
# ========================================
print("=" * 60)
print("BONUS 1: HATALI KOD DÜZELTİLMESİ")
print("=" * 60)

print("❌ HATALI KOD:")
print("yas = input('Yaşınız: ')")
print("gelecek_yas = yas + 10")
print()
print("Hata: input() string döndürür, string ile sayı toplanamaz!")
print()
print("✅ DOĞRU KOD:")
print("yas = int(input('Yaşınız: '))")
print("gelecek_yas = yas + 10")
print()

# Doğru uygulama
yas_bonus = int(input("Yaşınızı girin (test için): "))
gelecek_yas_bonus = yas_bonus + 10
print(f"Şu anki yaşınız: {yas_bonus}")
print(f"10 yıl sonra: {gelecek_yas_bonus}")
print()

# ========================================
# BONUS 2: Yüzde Hesabı Hatası
# ========================================
print("=" * 60)
print("BONUS 2: YÜZDE HESABI HATASI")
print("=" * 60)

print("❌ HATALI KOD:")
print("fiyat = 100")
print("indirim = fiyat * 20%")
print()
print("Hata: Python'da % mod operatörüdür, yüzde hesabı yapmaz!")
print()
print("✅ DOĞRU KOD:")
print("fiyat = 100")
print("indirim = fiyat * 20 / 100")
print()

# Doğru uygulama
fiyat_bonus = 100
indirim_bonus = fiyat_bonus * 20 / 100
print(f"Fiyat: {fiyat_bonus} TL")
print(f"%20 İndirim: {indirim_bonus} TL")
print(f"İndirimli Fiyat: {fiyat_bonus - indirim_bonus} TL")
print()

# ========================================
# EK BİLGİLENDİRME: Tip Dönüşüm Örnekleri
# ========================================
print("=" * 60)
print("EK: TİP DÖNÜŞÜM ÖRNEKLERİ")
print("=" * 60)

print("1️⃣ STRING → INT:")
str_val = "42"
int_val = int(str_val)
print(f"   '{str_val}' → {int_val} (tip: {type(int_val)})")
print()

print("2️⃣ STRING → FLOAT:")
str_val2 = "3.14"
float_val = float(str_val2)
print(f"   '{str_val2}' → {float_val} (tip: {type(float_val)})")
print()

print("3️⃣ INT → FLOAT:")
int_val2 = 10
float_val2 = float(int_val2)
print(f"   {int_val2} → {float_val2} (tip: {type(float_val2)})")
print()

print("4️⃣ FLOAT → INT (ondalık kısmı atar):")
float_val3 = 3.99
int_val3 = int(float_val3)
print(f"   {float_val3} → {int_val3} (tip: {type(int_val3)})")
print()

print("5️⃣ INT/FLOAT → STRING:")
num_val = 42
str_val3 = str(num_val)
print(f"   {num_val} → '{str_val3}' (tip: {type(str_val3)})")
print()

# ========================================
# İŞLEM ÖNCELİĞİ ÖRNEĞİ
# ========================================
print("=" * 60)
print("İŞLEM ÖNCELİĞİ ÖRNEKLERİ")
print("=" * 60)

print("Parantez olmadan:")
sonuc1 = 5 + 3 * 2
print(f"5 + 3 * 2 = {sonuc1} (önce çarpma)")
print()

print("Parantez ile:")
sonuc2 = (5 + 3) * 2
print(f"(5 + 3) * 2 = {sonuc2} (önce parantez içi)")
print()

print("Karmaşık örnek:")
sonuc3 = 10 + 5 * 2 ** 3 / 4 - 2
print(f"10 + 5 * 2³ / 4 - 2 = {sonuc3}")
print("Sıra: 2³=8 → 5*8=40 → 40/4=10 → 10+10=20 → 20-2=18")
print()

# ========================================
# BİTİŞ MESAJI
# ========================================
print("=" * 60)
print("✅ TÜM ÇÖZÜMLER TAMAMLANDI!")
print("=" * 60)
print()
print("💡 ÖNEMLİ HATIRLATMALAR:")
print("1. input() her zaman STRING döndürür!")
print("2. Sayısal işlem yapacaksanız int() veya float() kullanın")
print("3. / operatörü FLOAT, // operatörü INT döndürür")
print("4. % operatörü KALAN bulur, yüzde hesaplamaz")
print("5. ** operatörü üs alma içindir")
print()
print("🎉 Başarılar!")
print("=" * 60)