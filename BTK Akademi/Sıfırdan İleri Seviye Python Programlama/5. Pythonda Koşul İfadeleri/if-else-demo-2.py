# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

# number1 = int(input("Sayı: "))
# is0100 = 0 <= number1 <= 100

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.

# number2 = int(input("Sayı: "))
# isPosEven = number2 % 2 == 0 and number2 > 0

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız. 
# email = 'email@sadikturan.com'
# password = 'abc123'

# email = 'email@sadikturan.com'
# password = 'abc123'

# inEmail = input("Email: ")
# inPassword = input("Parola: ")

# if email == inEmail:
#     if inPassword == password:
#         print("Giriş Başarılı")
#     else:
#         print("Geçersiz Şifre!")
# else:
#     print("Geçersiz kullanıcı!")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# list1 = []

# for i in range(3):
#     x = int(input(f"Sayı {i+1}: "))
#     list1.append(x)
# list1.sort()
# print(f"{list1[0]} < {list1[1]} < {list1[2]}")    


# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.


# vize1 = float(input("Vize 1: "))
# vize2 = float(input("Vize 2: "))
# final = float(input("Final: "))

# avg = (vize1*0.3) + (vize2*0.3) + (final*0.4)

# if final > 70:
#     print("Geçti")
# elif (avg > 50) and final > 50:
#     print("Geçti")
# else:
#     print("Kaldı")


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name = input("İsim: ")
kg = float(input("Kilo: "))
size = float(input("Boy: "))

index = (kg/(size*size))

if 30 < index < 34.9:
    print("Obez")
elif 25 < index < 29.9:
    print("Fazla Kilolu")
elif 18.5 < index < 24.9:
    print("Normal")
elif 0 < index < 18.4:
    print("Şişman")
else:
    print("Bilinemeyen veri")