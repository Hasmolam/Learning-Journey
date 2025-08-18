names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.

names.append('Cenk')

# 2-  "Sena" değerini listenin başına ekleyiniz.

names.insert(0, "Sena")

# 3-  "Deniz" isminin indeksi nedir ?

names.index("Deniz")

# 4-  "Deniz" ismini listeden siliniz.

names.remove("Deniz")

# 5-  "Ali" listenin bir elemanı mıdır ?

isAli = "Ali" in names

# 6-  Liste elemanlarını ters çevirin.

names.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.

names.sort()

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.

years.sort()

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.

str = "Chevrolet,Dacia"
strlist = str.split(",")

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?

minyears = min(years)
maxyears = max(years)

# 11- years dizisinde kaç tane 1998 değeri vardır ?

years.count(1998)

# 12- years dizisinin tüm elemanlarını siliniz.

years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

userList = []

for i in range(3):
    x = input("Listeye eklenecek elemanı giriniz: ")
    userList.append(x)
