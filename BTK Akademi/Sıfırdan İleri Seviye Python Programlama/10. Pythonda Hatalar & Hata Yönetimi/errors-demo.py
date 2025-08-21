liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

# for i in liste:
#     try:
#         print(int(i))
#     except ValueError:
#         continue


# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı 
# olduğundan emin olunuz aksi halde hata mesajı yazın.

# while True:
#     try:
#         x = input("Sayı: ")
#         if x == 'q':
#             break
#         print(f"{int(x)} bir sayıdır")
#     except ValueError:
#         print(f"{x} bir sayı değildir")


# 3: Girilen parola içinde türkçe karakter hatası veriniz.

# turkishChar = ['ü','ğ','ı','ş','ç','ö','İ','Ü','Ö','Ş','Ç','Ğ']
# try:
#     password = input("Password: ")
#     for i in password:
#         if i in turkishChar:
#             raise Exception
# except Exception:
#     print("Şifreniz Türkçe karakter içeremez")

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için
# hata mesajları verin.

def factorial(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x * factorial(x-1)

while True:
    try:
        number = int(input('Sayı: '))
        if number < 0:
            raise ValueError
        x = factorial(number)
        print(x)
    except ValueError:
        print("Lütfen bir doğal sayı giriniz!")   
    else:
        break     