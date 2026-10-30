"""
hata yönetimi:
    - hata (error) ve istisna (exception)
    - en sık karşılasılan hata tipleri

Neden önemli:
    - hata yönetimi programın çökmeden kontrollu bir şekilde çalışmasını sağlar
    
hata yönetimi = can dostumuz

yapay zekada nelerlerde kullanılır?
    - veri hazırlama
    - dosya okuma
    - model eğitim döngüsü
    - reg sistemleri

"""

# yazım hatası(syntax error)
if 5 > 3: # SyntaxError: expected ':'
    print("ok") # NameError: name 'ok' is not defined

# name error (tanımsız değişken)
# print(x) # NameError: name 'x' is not defined

# type error (tip uyuşmazlığı)
# print ("10" + 5) TypeError: can only concatenate str (not "int") to str

# value error (değer uygun değil)
# int("berat") ValueError: invalid literal for int() with base 10: 'berat'

# zero division error (sıfıra bölme hatası)
# print(10/0) ZeroDivisionError: division by zero

# index hatası
liste = [1, 2, 3, 4]
# print(liste[10]) IndexError: list index out of range

# key error (sözlükte anahtar hatası)
# ogrenci = {"isim": "berat"}
# print(ogrenci["yas"]) KeyError: 'yas'

# file not found hatası
# with open("berat.txt", "r") as f:
#     print(f.read()) FileNotFoundError: [Errno 2] No such file or directory: 'berat.txt'

# attribute hatasi (yanllıs metot özellik hatası)
sayi = 10
# sayi.append(5)  AttributeError: 'int' object has no attribute 'append'


# try - except - else - finally

"""
try- except
    - program hata verdiğinde durmasını istemeyiz
    - hata olursa yakalayıp kontrollu şekilde yönetmesi lazım
"""
# try:
#     sayi = int(input("sayı girin: "))
#     print(10/sayi)
# except:
#     print("bir hata oluştu")

# print("program başarılı bir şekilde çalışmaya devam ediyor. ")

# belirli bir hata yakalama yöntemi
try:
    sayi = int(input("sayı girin: "))
    print(10/sayi)
except ValueError:
    print("lütfen bir sayı girin: ")
except ZeroDivisionError:
    print("sıfıra bölme yapılamaz")

# else: hata yoksa çalışır
try:
    sayi = int(input("sayi girin: "))
    sonuc = 10/sayi
except (ValueError, ZeroDivisionError):
    print("hatalı giris")
else: # hata yoksa
    print(f"sonuc: {sonuc}")

# finally: her durumda çalışır

try:
    dosya = open("veri.txt", "r", encoding="utf-8")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("dosya buulunamadı")
finally:
    try:
        dosya.close()
    except:
        pass

# kendi hatamızı üretmek istersek ne yapalım
yas = int(input("yas: "))

if yas < 0:
    raise ValueError("yas negatif olamaz") # ValueError: yas negatif olamaz

# genel hata ayıklama mantığı
try:
    sayi = int(input("bir sayı girin: "))
    print(10/sayi)
except Exception as e:
    print(f"hata: {str(e)}")