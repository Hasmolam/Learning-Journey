# 1- Girilen 2 sayıdan hangisi büyüktür ?

# n1 = int(input("Sayı 1: "))
# n2 = int(input("Sayı 2: "))

# if n1 > n2:
#     print(f"{n1} {n2}'den büyüktür")
# elif n2 > n1:
#     print(f"{n2} {n1}'den büyüktür")   
# elif n2 == n1:
#     print(f"{n1} ve {n2} eşittir")      

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

# vize1 = float(input("Vize 1: "))
# vize2 = float(input("Vize 2: "))
# final = float(input("Final: "))

# avg = (vize1*(3/10))+(vize2*(3/10))+(final*(2/5))
# if avg >= 50:
#     print(f"Ortalmanız: {avg} Sonuç: Geçtiniz")
# elif avg < 50:
#     print(f"Ortalmanız: {avg} Sonuç: Kaldınız")    


# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

# number = int(input("Sayı: "))
# if number % 2 == 0:
#     print("Çift")
# elif number % 2 == 1:
#     print("Tek")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

# sayi = int(input("Sayı: "))
# if sayi > 0:
#     print("Pozitif")
# elif sayi < 0:
#     print("Negatif")
# elif sayi == 0:
#     print("Nötr")        

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

email = "e" 
parola = "a"

mail = input("Mail: ")
password = input("Parola: ")

if mail == email:
    if password == parola:
        print("Giriş Başarılı")
    else:
        print("Yanlış Şifre!")    
else:
    print("Kullanıcı Adı veya Şifre Yanlış")        
