# Q 1.
empty_lst = []
# Q 2
courses = ['Stat 202', 'cosc 102', 'math 102', 'biol 203','chem 106', 'zool 304']
# Q 3.
print('Number of courses : ', len(courses))
# Q4
First_course = courses[0]
print('firt course( in the list : ', First_course)
middle_index = len(courses) / 2 

last_index = len(courses) - 1
last_course = courses[last_index]
print('Last course in the list is :', last_course )

# Q5.
mixed_data_types = ['Aliyu', 23, 6.8, 'Single', 'Ajiya quaters']

# Q6.
it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Q7.
print(it_companies)

# Q8.
print('Number of  companies : ', len(it_companies))
# Q9.
first_company = it_companies[0]
middle_index = len(it_companies) / 2 - 1
Middle_company = it_companies[middle_index]
last_index = len(it_companies) - 1
last_comapany = it_companies[last_index]
print('First Company : ',first_company)
print('Middle company : ',Middle_company)
print('last Company : ' , last_comapany)

it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[0] = 'Coursera' 
print(it_companies)




