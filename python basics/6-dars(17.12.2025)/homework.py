# 8-amaliyot. 77-bet




# avtolar = ['audi', 'bmw', 'volvo']

# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# # javob = float(input("12x6 nechiga teng?>>>"))

# if javob != 72:
#     print("Javob xato!")





# yosh = int(input("Yoshingiz nechida?>>>"))

# if yosh >= 18:
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas!')






# yil = int(input("Tug'ilgan yilingizni kiriting:"))

# if 2025 - yil < 18:
#     print(f"Yoshingiz {2025 - yil}da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")






# login = input("Yangi login tanlang:")

# if len(login) <= 5: 
#     print("Login 5 harfdan ko'proq bo'lishi shart!")








# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())









# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']

# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())





# ismlar = input("Login ismingizni kiriting: ")

# if ismlar.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {ismlar.title()}!")






# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))

# if son1 == son2:
#     print("Sonlar teng!")




    
# son = float(input("Istalgan sonni kiriting: "))

# if son > 0:
#     print("Musbat son")
# else:
#     print("Manfiy son")







# son = float(input("Son kiriting: "))

# if son > 0:
#     ildiz = son ** 0.5
#     print(ildiz)
# else:
#     print("Musbat son kiriting")






# son = int(input("Son kiriting: "))

# if son % 2 == 0:
#     print("Juft son")
# else:
#     print("Toq son")





# 9-amaliyot. 90-bet 




# son = int(input("Juft son kiriting: "))

# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas.")






# yosh = int(input("Yoshingizni kiriting: "))

# if yosh < 4 or yosh > 60:
#     narx = 0
# elif yosh < 18:
#     narx = 10000
# else:
#     narx = 20000

# print(f"Sizga chipta narxi: {narx} so'm")











# son1 = float(input("Birinchi sonni kiriting: "))
# son2 = float(input("Ikkinchi sonni kiriting: "))

# if son1 > son2:
#     print("Birinchi son katta")
# elif son1 < son2:
#     print("Ikkinchi son katta")
# else:
#     print("Sonlar teng")







# mahsulotlar = ['olma', 'banan', 'non', 'shakar', 'choy', 'sut', 'yog', 'tuxum', 'tuz', 'guruch']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot} do'konimizda bor")
#     else:
#         print(f"{mahsulot} do'konimizda yo'q")







# mahsulotlar = ['olma', 'banan', 'non', 'shakar', 'choy', 'sut', 'yog', 'tuxum', 'tuz', 'guruch']
# bor_mahsulotlar = []
# mavjud_emas = []

# for n in range(5):
#     savol = input(f"{n+1}-mahsulotni kiriting: ")
#     if savol in mahsulotlar:
#         bor_mahsulotlar.append(savol)
#     else:
#         mavjud_emas.append(savol)

# if not mavjud_emas:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")








# foydalanuvchilar = ['ali', 'vali', 'olim', 'anvar', 'nodir']
# yangi_login = input("Yangi login tanlang: ").lower()

# if yangi_login in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {yangi_login}!")








# son = int(input("Butun son kiriting: "))

# for n in range(2, 11):
#     if son % n == 0:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")





















# 12-amaliyot.109-bet












# ranglar = {'qizil', 'yashil', 'ko''k'}

# # Bitta rang qo'shish
# ranglar.add('sariq')

# # Bir nechta rang qo'shish
# yangi_ranglar = ['oq', 'qora', 'pushti']
# ranglar.update(yangi_ranglar)

# print(ranglar)




# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# # Umumiy elementlar (Intersection)
# umumiy = set1.intersection(set2)
# print(f"Ikkala to'plamda bor sonlar: {umumiy}")

# # Farqi (Difference)
# farq = set1.difference(set2)
# print(f"Faqat set1 da bor sonlar: {farq}")

# # Simmetrik farq (Symmetric Difference)
# simmetrik = set1.symmetric_difference(set2)
# print(f"Faqat bittasida bor sonlar (ikkalasida ham borlari olib tashlangan): {simmetrik}")



















# bozorlik = {'choy', 'non', 'kartoshka', 'tuxum', 'sut'}
# mahsulotlar = {'non', 'sut', 'tuxum', 'olma', 'un', 'tuz'}

# # 1. Do'konda bor bo'lgan bozorlik mahsulotlari
# bor = list(bozorlik.intersection(mahsulotlar))
# print(f"Do'konda bor narsalar: {bor}")

# # 2. Do'konda yo'q bo'lgan bozorlik mahsulotlari
# yoq = list(bozorlik.difference(mahsulotlar))
# print(f"Do'konda yo'q narsalar: {yoq}")

# # 3. Do'kon egasi yangi narsalar olib keldi
# yangi_narsalar = ['kartoshka', 'shakar', 'guruch']
# mahsulotlar.update(yangi_narsalar)
# print(f"Yangilangan do'kon mahsulotlari: {mahsulotlar}")


























# 13-amaliyot.116-bet








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
















# dostlar_kinolari = {
#     'Ali': ['Forsaj', 'O"rgimchak odam', 'Avatar'],
#     'Vali': ['Titanik', 'Uyda yolg"iz'],
#     'Olim': ['Interstellar', 'Inception', 'Tenet']
# }

# for ism, kinolar in dostlar_kinolari.items():
#     print(f"\n{ism}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino)






# davlatlar = {
#     "O'zbekiston": {
#         "poytaxt": "Toshkent",
#         "aholi": 36,
#         "pul": "So'm"
#     },
#     "AQSH": {
#         "poytaxt": "Vashington",
#         "aholi": 330,
#         "pul": "Dollar"
#     },
#     "Rossiya": {
#         "poytaxt": "Moskva",
#         "aholi": 144,
#         "pul": "Rubl"
#     }
# }

# davlat = input("Davlat nomini kiriting: ")

# if davlat in davlatlar:
#     malumot = davlatlar[davlat]
#     print(f"\n{davlat} haqida ma'lumot:")
#     print(f"Poytaxti: {malumot['poytaxt']}")
#     print(f"Aholisi: {malumot['aholi']} mln")
#     print(f"Pul birligi: {malumot['pul']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot yo'q")

























# 14-amaliyot.122-bet







# savol = "Yaxshi ko'rgan kitobingizni kiriting"
# savol = savol + "\n(To'xtash uchun 'stop' deb yozing): "

# kitob = ""
# while kitob != 'stop':
#     kitob = input(savol)
#     if kitob != 'stop':
#         print(f"{kitob.title()} - juda zo'r kitob!")















# savol = "Yoshingizni kiriting (chiqish uchun 'exit' yoki 'quit' deb yozing): "
# ishora = True

# while ishora:
#     qiymat = input(savol)
    
#     if qiymat == 'exit' or qiymat == 'quit':
#         ishora = False
#     else:
#         yosh = int(qiymat)
#         if yosh < 7:
#             print("Chipta: 2000 so'm")
#         elif yosh < 18:
#             print("Chipta: 3000 so'm")
#         elif yosh < 65:
#             print("Chipta: 10000 so'm")
#         else:
#             print("Chipta bepul!")















# while True:
#     qiymat = input("Yoshingizni kiriting: ")
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
    
#     yosh = int(qiymat)









# # XATO KOD!
# son = 1
# while son < 5:
#     print(son)
