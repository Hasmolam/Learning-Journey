# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın. 

# def displayWords(name, number):
#     for n in range(number):
#         print(name)

# displayWords('Allah', 5)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

# def creator(*parms):
#     return [x for x in parms]

# liste = creator(10, 151,552, "Kral")
# print(liste)

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.

# def isPrime(x):
#     k = 0
#     for n in range(x+1):
#         if n == 0:
#             continue
#         if x%n == 0:
#             k += 1
#     if x == 1:
#         return False
#     elif x == 0:
#         return False
#     elif k <= 2:
#         return True
#     else:
#         return False


# def primeNumbers(a,b):
#     x = 0
#     for n in range(a,b):
#         if isPrime(n):
#             print(n)

# a = int(input("Sayı 1: "))
# b = int(input("Sayı 2: "))
# primeNumbers(a, b)

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def perfectDivisor(a):
    tlist = []
    for n in range(1,a+1):
        if a % n == 0:
            tlist.append(n)
    return tlist        

a = int(input("Number: "))
answer = perfectDivisor(a)
print(answer)