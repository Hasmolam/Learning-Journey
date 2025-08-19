# Bankamatik Uygulaması

SadikHesap = {
    'ad': 'Sadık Turan',
    'hesapNo': '13245678',
    'bakiye': 3000,
    'ekHesap': 2000
}

AliHesap = {
    'ad': 'Ali Turan',
    'hesapNo': '12345678',
    'bakiye': 2000,
    'ekHesap': 1000
}

def getMoney(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap['bakiye'] + hesap['ekHesap']) < miktar:
        print("Yeterli bakiyeniz bulunmamaktadır!")
    elif hesap['bakiye'] < miktar:
        pref = input(f"Ana bakiyeniz yetersiz. Ek hesap kullanılsın mı?(e/h)")
        if pref.lower() == "e":
            hesap['ekHesap'] = hesap['ekHesap'] - (miktar - hesap['bakiye'])
            hesap['bakiye'] = 0
            print(f"Kalan bakiyeniz: {hesap['bakiye']} Kalan Ek hesap bakiyeniz: {hesap['ekHesap']}")
        elif pref.lower() == "h":
            print("İşlem iptal edilmiştir. İyi günler dileriz.")
    else:
        hesap['bakiye'] -= miktar
        print(f"İşlem gerçekleştirilmiştir. Kalan bakiyeniz: {hesap['bakiye']}")

def displayMoney(hesap):
    print(f"\nMerhaba {hesap['ad']}\n{hesap['hesapNo']} hesap nolu hesabınızın bakiyesi: {hesap['bakiye']}\nEk hesap bakiyesi: {hesap['ekHesap']}")

getMoney(SadikHesap, 1000) 

displayMoney(SadikHesap)      

