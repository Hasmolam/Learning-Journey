'''
    ogrenciler = {
        '120': {
            'ad': 'Ali',
            'soyad': 'Yılmaz',
            'telefon': '532 000 00 01'
        },
        '125': {
            'ad': 'Can',
            'soyad': 'Korkmaz',
            'telefon': '532 000 00 02'
        },
        '128': {
            'ad': 'Volkan',
            'soyad': 'Yükselen',
            'telefon': '532 000 00 03'
        },
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.

    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

students = {}

for i in range(3):
    print(f"{i+1}. öğrenci")
    studentsNo = input("Öğrenci Numarası: ")
    studentName = input("Öğrencinin Adı: ")
    studenSurname = input("Öğrencinin Soyadı: ")
    studentPhone = input("Öğrencinin Telefon Numarası: ")
    students.update({studentsNo : {"name" : studentName, "surname": studenSurname, "phone number": studentPhone}})

request = input("Görmek istediğiniz Öğrencini numarasını giriniz: ")
print(f"Öğrencinin Adı: {students[request]["name"]}\nÖğrencinin Soyadı: {students[request]["surname"]}\nÖğrencinin Telefon Numarası: {students[request]["phone number"]}")
    