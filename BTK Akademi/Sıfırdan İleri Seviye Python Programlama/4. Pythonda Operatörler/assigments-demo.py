x, y, z = 2, 5, 10

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?

number1 = int(input("Sayı 1: "))
number2 = int(input("Sayı 2: "))
print(f"Cevap: {number1*number2 - (x+y+z)}")


# 2- y' nin  x' e kalansız bölümünü hesaplayınız.

div = y // x

# 3- (x,y,z) toplamının mod 3' ü nedir ?

mod3 = (x+y+z) % 3

# 4- y' nin x. kuvvetini hesaplayınız.

pows = y ** x

# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?

numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
z3 = z ** 3

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?

x, *y, z = numbers
sumy = sum(y)