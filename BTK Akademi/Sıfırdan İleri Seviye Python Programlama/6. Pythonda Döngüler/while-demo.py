sayilar = [1,3,5,7,9,12,19,21]

# 1: sayilar listesini while ile ekrana yazdırın.

# i = 0
# while i < len(sayilar):
#     print(sayilar[i])
#     i +=1

# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm
#    tek sayıları ekrana yazdırın.

# begin = int(input("Başlangıç: "))
# end = int(input("Bitiş: "))
# while begin < end:
#     if begin % 2 == 1:
#         print(begin)
#     begin += 1

# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

# i = 100

# while i != 0:
#     print(i)
#     i -= 1

# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde
#    yazdırın.

# i = 1
# numbers = []
# while i != 6:
#     x = int(input(f"Sayı {i}: ")) 
#     numbers.append(x)
#     i += 1
# numbers.sort()
# print(f"{numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]}")

# 5: Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (name, price) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

urunler = []
i = int(input("Ürün Sayısı: "))
while i != 0:
    name = input("Ürün ismi: ")
    price = input("Ürün Fiyatı: ")
    urunler.append({"name":name, "price":price})
    i -= 1
n = 0
while n < len(urunler):
    print(f"Ürün ismi: {urunler[n]['name']}, Ürün Fiyatı: {urunler[n]["price"]}")
    n+=1        