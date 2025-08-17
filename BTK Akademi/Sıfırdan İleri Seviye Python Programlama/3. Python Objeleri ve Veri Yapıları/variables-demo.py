"""
    1- Bir müşterinin aşağıdaki bilgileri için değişken oluşturunuz.

    Müşteri adı
    Müşteri soyadı
    Müşteri ad + soyad
    Müşteri cinsiyet
    Müşteri tc kimlik
    Müşteri doğum yılı
    Müşteri adres bilgisi   
    Müşteri yaşı 
"""

customerName = "Burak"
customerSurname = "Yılmaz"
customerFullName = f"{customerName} {customerSurname}"
customerGender = "Erkek"
customerNo = "51426264670" #Rastgele bir sayı kullanılmıştır
customerBirthYear = 1985
customerAdress = 'Antalya Kaş' 
customerAge = 2025 - customerBirthYear

"""
    2- Aşağıdaki siparişlerin toplam bilgisini hesaplayınız.
    
    Sipariş 1 => 110    TL
    Sipariş 2 => 1100.5 TL
    Sipariş 3 => 356.95 TL

"""

order1 = 110
order2 = 1100.5
order3 = 356.95
print(f"Toplam: {order1+order2+order3}")