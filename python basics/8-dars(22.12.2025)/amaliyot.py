
# savol = "Yaxshi ko'rgan kitobingizni kiriting"
# savol = savol + "\n(To'xtash uchun 'stop' deb yozing): "

# kitob = ""
# while kitob != 'stop':
#     kitob = input(savol)
#     if kitob != 'stop':
#         print(f"{kitob.title()} - juda zo'r kitob!")












# # Har bir shaxs uchun alohida lug'at
# shaxs1 = {
#     'ism': 'Alisher Navoiy',
#     'soha': 'Adabiyot',
#     'asarlar': ['Xamsa', 'Lison ut-tayr']
# }
# shaxs2 = {
#     'ism': 'Stiv Jobs',
#     'soha': 'Texnologiya',
#     'asarlar': ['iPhone', 'Macintosh']
# }
# shaxs3 = {
#     'ism': 'Albert Eynshteyn',
#     'soha': 'Fizika',
#     'asarlar': ['Nisbiylik nazariyasi']
# }

# # Lug'atlarni bitta ro'yxatga joylaymiz
# shaxslar = [shaxs1, shaxs2, shaxs3]

# # Ma'lumotlarni konsolga chiqaramiz
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} quyidagi asarlarni yozgan:")
#     for asar in asarlar:
#         print(f"- {asar}")



























# savat = []

# while True:
#     mahsulot = input("Savatga mahsulot qo'shing (to'xtash uchun 'stop' deb yozing): ")
#     if mahsulot == 'stop':
#         break
#     savat.append(mahsulot)

# print(f"Sizning savatingiz: {savat}")



# bozor = {'olma': 10000, 'non': 4000, 'choy': 5000, 'sut': 8000}

# # Mijozning savati
# buyurtmalar = ['olma', 'non', 'baliq', 'choy']

# for buyurtma in buyurtmalar:
#     if buyurtma in bozor:
#         narx = bozor[buyurtma]
#         print(f"{buyurtma.title()}ning narxi - {narx} so'm")
#     else:
#         print(f"Kechirasiz, bizda {buyurtma} yo'q")







# akam = {
#     'ismi': 'Anvar',
#     'tugilgan_yili': 1995,
#     'shahar': 'Samarqand'
# }

# ismi = akam['ismi']
# yili = akam['tugilgan_yili']
# shahar = akam['shahar']

# print(f"Akamning ismi {ismi}, u {yili}-yilda, {shahar} shahrida tug'ilgan.")






# taomlar = {
#     'ali': 'osh',
#     'vali': 'shashlik',
#     'olim': 'manti',
#     'nodira': 'pitsa',
#     'anvar': 'somsa'
# }

# print(f"Alining sevimli taomi {taomlar['ali']}")
# print(f"Olimning sevimli taomi {taomlar['olim']}")
# print(f"Anvarning sevimli taomi {taomlar['anvar']}")







# python_lugat = {
#     'integer': 'butun son',
#     'float': 'unli son',
#     'string': 'matn',
#     'if': 'agar (shart tekshirish)',
#     'else': 'aks holda',
#     'for': 'takrorlash tsikli',
#     'list': 'royxat',
#     'dictionary': 'lugat',
#     'print': 'konsolga chiqarish',
#     'input': 'malumot kiritish'
# }

# soz = input("Python terminini kiriting: ").lower()

# if soz in python_lugat:
#     print(f"{soz.title()} so'zi '{python_lugat[soz]}' deb tarjima qilinadi.")
# else:
#     print("Bunday so'z mavjud emas.")










# 11-amaliyot.104-bet







# lugat = {
#     'integer': 'butun son',
#     'float': 'unli son',
#     'string': 'matn',
#     'if': 'shartni tekshirish',
#     'else': 'aks holda',
#     'for': 'takrorlash tsikli',
#     'list': 'royxat',
#     'dictionary': 'lugat',
#     'print': 'ekranga chiqarish',
#     'input': 'malumot kiritish'
# }

# for kalit in sorted(lugat.keys()):
#     print(f"{kalit.title()} - {lugat[kalit]}")






# davlatlar = {
#     'ozbekiston': 'toshkent',
#     'aqsh': 'vashington',
#     'italiya': 'rim',
#     'fransiya': 'parij',
#     'yaponiya': 'tokio'
# }

# print("Bizdagi davlatlar:")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat.upper())

# print("\nBizdagi poytaxtlar:")
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt.title())

# savol = input("\nQaysi davlatning poytaxtini bilishni istaysiz? ").lower()

# if savol in davlatlar:
#     print(f"{savol.upper()}ning poytaxti {davlatlar[savol].title()} shahri.")
# else:
#     print("Bizda bunday ma'lumot yo'q.")


#
# menyu = {
#     'osh': 20000,
#     'shashlik': 15000,
#     'manti': 18000,
#     'lagmon': 16000,
#     'somsa': 8000,
#     'non': 4000,
#     'choy': 3000,
#     'salat': 10000,
#     'pitsa': 50000,
#     'shurva': 15000
# }
#
# print("3 ta taom buyurtma bering:")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-taom: ").lower())
#
# for taom in buyurtmalar:
#     if taom in menyu:
#         print(f"{taom.title()} {menyu[taom]} so'm")
#     else:
#         print(f"Kechirasiz, bizda {taom} yo'q.")

# telefonlar  =   {
#     "ali"   :   "iphone x",
#     "vali"  :   "galaxy s9",
#     "olim"  :   "mi pro 10"
# }
# for k,v in telefonlar.items():
#     print(f"{k.title()}ning telefoni {v}")
# print(telefonlar.keys())
















# Har bir shaxs uchun alohida lug'at
# shaxs1 = {
#     'ism': 'Alisher Navoiy',
#     'soha': 'Adabiyot',
#     'asarlar': ['Xamsa', 'Lison ut-tayr']
# }
#
# shaxs2 = {
#     'ism': 'Stiv Jobs',
#     'soha': 'Texnologiya',
#     'asarlar': ['iPhone', 'Macintosh']
# }
# shaxs3 = {
#     'ism': 'Albert Eynshteyn',
#     'soha': 'Fizika',
#     'asarlar': ['Nisbiylik nazariyasi']
# }
#
# shaxslar = [shaxs1, shaxs2, shaxs3]
#
#
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} quyidagi asarlarni yozgan:")
#     for asar in asarlar:
#         print(f"- {asar}")
#
