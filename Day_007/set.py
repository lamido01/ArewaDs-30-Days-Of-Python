# Q1
empty_tuple = ()
# Q2
brothers = ('usman', 'Auwal', 'sule', 'ibrahim')
sisters = ('Fatima', 'Aisha', 'zainab', 'hajara')
# Q3
siblings = brothers + sisters
# Q4
print('number of siblings is:',len(siblings))
# Q5
family_members = list(siblings)
family_members[6] = 'Habiba'
family_members[7] = 'Abubakar'
print(family_members)

# Exercise Leval 2
# Q1
family_members = ['usman', 'Auwal', 'sule', 'ibrahim', 'Fatima', 'Aisha', 'Habiba', 'Abubakar']
siblings, parents = family_members[:6], family_members[6:]
print('Siblings: ',siblings) 
print('Parents:', parents)
# Q2
fruits = ('Apple','Orange','Banana','Mango','Lemon')
vegetables = ('onion','Yam','maize','beans','carrots')
animals = ('camel','horse','Ram','Cow','Dog','pig')
food_stuff_tp = fruits + vegetables + animals
print(food_stuff_tp)
# Q3
food_stuff_lt = list(food_stuff_tp)
# Q4
print(len(food_stuff_lt))
middle1 = len(food_stuff_lt)//2 -1
middele2 = len(food_stuff_lt)//2 + 1
middle_stuff = food_stuff_lt[middle1:middele2]
print('Middle Stuff:',middle_stuff)

# Q5
first_three = food_stuff_lt[:3]
print('First three:', first_three)
# Q6
del food_stuff_tp

# Q7
print('Donkey is in food stuff:', 'Donkey' in food_stuff_lt)
# Q8
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia is a Nordic country:', 'Estonia' in nordic_countries)
print('Iceland is a Nordic country:', 'Iceland' in nordic_countries)




