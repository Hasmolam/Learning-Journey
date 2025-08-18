# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme 
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu 
#    lise ya da üniversite olmalıdır. 


# name = input("İsim: ")
# age = int(input("Yaş: "))
# ed = input("Eğitim Durumu: ")

# if (age >= 18) and (ed.lower() == "lise" or ed.lower() == "üniversite"):
#     print(f"{name} ehliyet alabilirsin")
# else:
#     print(f"{name} ehliyet alamazsın")    


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# note1 = int(input("Yazılı 1: "))
# note2 = int(input("Yazılı 2: "))
# note3 = int(input("Sözlü 1: "))
# avg = (note1 + note2 + note3)/3

# if 0 <= avg <= 24:
#     print(f"Ortalaman: {avg} Notun: 0")
# elif 25 <= avg <= 44:
#     print(f"Ortalaman: {avg} Notun: 1")
# elif 25 <= avg <= 54:
#     print(f"Ortalaman: {avg} Notun: 2")
# elif 55 <= avg <= 69:
#     print(f"Ortalaman: {avg} Notun: 3")    
# elif 70 <= avg <= 84:
#     print(f"Ortalaman: {avg} Notun: 4") 
# elif 85 <= avg <= 100:
#     print(f"Ortalaman: {avg} Notun: 5")  
# else:
#     print("Yanlış bilgi girdiniz!")        


# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

date = input("Aracın trafiğe çıkma tarihi(yıl/ay/gün): ")
datelist = date.split("/")

d = datetime.date(int(datelist[0]),int(datelist[1]),int(datelist[2]))
today = datetime.date.today()

timeMaintanence = today - d

print(f"{(timeMaintanence.days//365)+1}. servis aralığı")