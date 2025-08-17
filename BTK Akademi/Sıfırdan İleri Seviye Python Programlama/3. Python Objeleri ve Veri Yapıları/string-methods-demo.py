website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.

helloWorld = ' Hello World '.strip(" ")

# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.

sadikturan = 'www.sadikturan.com'
sadikturan2 = sadikturan[sadikturan.find("sadikturan"):sadikturan.find("sadikturan")+len("sadikturan")]

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.

courseLower = course.lower()

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))

websiteACount = website.count("a")

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?

isWww = website.startswith("www")
isCom = website.endswith("com")

# 6-  'website' içinde '.com' ifadesi var mı?

is_Com = bool(website.count('.com'))

# 7- 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)

isDigit = course.isdigit()
isAlpha = course.isalpha()

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.

contents = 'Contents'.center(50,"*")

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.

courseHyphen = course.replace(" ", "-")

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin

hello_world = 'Hello World'.replace("World", "There")

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.

courseNoSpace = course.split()
 