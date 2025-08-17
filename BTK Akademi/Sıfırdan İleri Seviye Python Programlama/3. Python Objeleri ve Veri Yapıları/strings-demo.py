website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

course_length = len(course)

# 2- 'website' içinden www karakterlerini alın.

website_www = website[7:10]

# 3- 'website' içinden com karakterlerini alın.

website_com = website[-3:]

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.

course_15 = f"{course[:15]}{course[-15:]}"

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

course_reverse = course[::-1]

# 6- Aşağıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.' 

name, surname, age, job = 'Bora','Yılmaz', 32, 'mühendis' 

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.

helloWorld = "Hello world"
helloWorld = f"{helloWorld[0:6]}W{helloWorld[7:]}"

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.

print(f"{'abc'*3}")