# name=input('Isming nima ')
# birth_year=input('nechanchi yilsan')
# current_year= int(2025)-int(birth_year)
# print(f'Demak sen {current_year} yoshdasan')

                 


# number= int(input('raqam kiriting'))
           
#     3-1. Names: Store the names of a few of your friends in a list called names. Print 
# each person’s name by accessing each element in the list, one at a time.
# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
# printing each person’s name, print a message to them. The text of each mes
# sage should be the same, but each message should be personalized with the 
# person’s name.
# 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
# motorcycle or a car, and make a list that stores several examples. Use your list 
# to print a series of statements about these items, such as “I would like to own a 
# Honda motorcycle.”


#3.1
# names=['Sardor','Salbar','Dilshod']
# print(names[0])
# print(names[1])
# print(names[2])


# 3.2
# print(f'Hi my friend {names[0]}')
# print(f'Hi how are you doing ? {names[2]}')


# 3.3
# cars=['Honda Civic','Toyota Camry','Ford F-150','Toyota RAV4','Jeep Wrangler']
# print(f'Hey I would love to have {cars[0].title()}')
# print(f'I wanna buy {cars[2].title()} for my parents')

# cars[0]='damas'.title()
# print(cars)
# cars=['Honda Civic','Toyota Camry','Ford F-150','Toyota RAV4','Jeep Wrangler']
# print(cars)
# cars[1]='tico'.title()
# print(cars)
# cars[3]='malibu'.title()
# print(cars)





# append
# cars=[]
# cars.append('damas')
# # print(cars)
# cars.append('tico')
# cars.append('labo')
# print(cars)



# cars_list=[]
# wish_list=input('what cars do you want to have ? ')
# cars_list.append(wish_list)
# print(f'So you want to buy {cars_list}'.upper())


# food_list=[]
# recept_wish=input('What do you want to eat? ')
# food_list.append(recept_wish)
# print(f'Ok I am redy to give your {food_list}')


# cars=['malibu','damas','tico',]
# cars.insert(0, 'spark')
# print(cars)
# del cars[1]
# print(cars)








# # 1. Define the list of guests
# # I'm inviting three people I find inspiring or interesting!
# guests = ['Marie Curie', 'Albert Einstein', 'Malala Yousafzai']

# # 2. Use the list to print a personalized message to each person

# # Invitation 1 (index 0)
# print(f"Dear {guests[0]}, I would be honored if you could join me for a dinner of scientific discussion this weekend.")

# # Invitation 2 (index 1)
# print(f"Dear {guests[1]}, I am hosting a dinner and would love to hear your thoughts on the universe. Please join me!")

# # Invitation 3 (index 2)
# print(f"Dear {guests[2]}, Your bravery inspires millions. I would be thrilled if you could join me for dinner on Saturday.")




# # Starting list from Exercise 3-4
# guests = ['Marie Curie', 'Albert Einstein', 'Malala Yousafzai']

# # 1. Announce the change
# guest_who_cant_come = guests[0] 
# print(f"I just heard sad news: {guest_who_cant_come} can't make it to the dinner.")

# # 2. Replace the guest at the same index (0) with a new person
# guests[0] = 'Leonardo da Vinci'

# # 3. Print the new invitations!
# print(f"Dear {guests[0]}, I would be thrilled to welcome you to dinner. (New Guest!)")
# print(f"Dear {guests[1]}, I am hosting a dinner and would love to hear your thoughts on the universe. Please join me!")
# print(f"Dear {guests[2]}, Your bravery inspires millions. I would be thrilled if you could join me for dinner on Saturday.")






# 3-5.
# 
#  Changing Guest List: You just heard that one of your guests can’t make the 
# dinner, so you need to send out a new set of invitations. You’ll have to think of 
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print() call at the end of 
# your program, stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the 
# name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in 
# your list.
# 3-6. More Guests: You just found a bigger dinner table, so now more space is 
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or 3-5. Add a print() call to the 
# end of your program, informing people that you found a bigger table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
# arrive in time for the dinner, and now you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a 
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two 
# names remain in your list. Each time you pop a name from your list, print a 
# message to that person letting them know you’re sorry you can’t invite them 
# to dinner.
# • Print a message to each of the two people still on your list, letting them 
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure you actually have an empty list at the end of 
# your program.




# guests=['Nodir','Dilshod','Mirshod','Abror','Alisher','Navoiy']
# kelolmaydigan_shaxs=guests[0]
# print(f'Afsuski bu mehmon kel olmas ekan {guests[0].title()}')
# guests[0]='Ali'
# taklif=('Sizni taklif qilaman {guests}')
# print(guests)





























