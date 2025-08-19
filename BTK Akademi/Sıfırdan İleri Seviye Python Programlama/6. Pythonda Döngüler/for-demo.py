sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayilar listesindeki hangi sayılar 3'ün katıdır ?

# for i in sayilar:
#     if i % 3 == 0:
#         print(i)

# 2- Sayilar listesinde sayıların toplamı kaçtır ?

# summ = 0

# for i in sayilar:
#      summ += i
# print(summ)     

# 3- Sayilar listesindeki tek sayıların karesini alınız.

# for i in sayilar:
#     if i % 2 == 1:
#         print(i**2)


sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# 4- Şehirlerden hangileri en fazla 5 karakterlidir ?

# for i in sehirler:
#     if len(i) <= 5:
#         print(i)


urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

# 5- Ürünlerin fiyatları toplamı nedir ?

# summ = 0

# for d in urunler:
#     for key, value in d.items():
#         if key == 'price':
#             summ += int(value)
# print(summ)

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz ?

for d in urunler:
    if int(d['price']) <= 5000: 
        print(f"Ürün: {d['name']} Fiyatı: {d['price']}")