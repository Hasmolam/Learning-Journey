'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan 
   sayılara denir. 
'''

x = int(input("Sayı: "))
n = 0
for i in range(1,x+1):
    if x%i == 0:
        n += 1
if x == 1:
    print('Sayı asal değil')
elif n <= 2:
    print("Sayı Asal")
else:
    print('Sayı asal değil')    
