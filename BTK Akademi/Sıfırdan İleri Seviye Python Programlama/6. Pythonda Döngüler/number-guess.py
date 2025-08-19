'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı 
      üzerinden hesaplansın.
'''

from random import randint

x = randint(0,100)
tahmin = -5
hak = int(input("Hak sayısı: "))
score = 100
can = hak
while tahmin != x and hak > 0:

    tahmin = int(input("Tahmin: "))

    if x < tahmin:
        print("Aşağı")
    elif x > tahmin:
        print("Yukarı")
    hak -= 1 
    
    if tahmin == x:
        print(f"Doğru tahmin! Puanın: {score}")
        break
    score = score - 100/can
    print(f"Kalan hak: {hak}")
else:
    print(f"Canın bitti! Cevap: {x} Puanın: 0") 
 