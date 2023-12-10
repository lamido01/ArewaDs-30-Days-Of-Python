# concatenating string
print('Thirty' + ' ' 'Days' + ' ' 'of' + ' ' 'python')
print('Coding' + ' ' 'For' + ' ' 'All')

# Declaring a variable
company = "Coding For All "
print(company)
company_length = len(company)
print( 'The length of the string {} is {}.'.format(company, company_length) )

# change lower case to upper case
print('lower case to upper case : ' ,company.upper())
# upper to lower
print('upper to lower : ' ,company.lower())
 
# capitalize()
print('first word capitalize : ' ,company.capitalize())
# title
print('Title case : ' ,company.title())
# swapcase()
print(company.swapcase())
# slicing first word out of Coding For All
company = "Coding For All "
first_word = company[0 : len('coding')]
print('fisrt word out of coding for all : ' ,first_word)

cod = 'coding for all'
sub_cod = 'coding'
print(cod.rindex(sub_cod))

 # Ex 11
company = 'coding for all'
print(company.replace('coding', 'python'))

# Ex 12 python for every one to python for all
challenge = 'python for Every one'
print(challenge.replace('Every one', 'all'))

# Ex 13 
challenge = 'Coding For All'
print(challenge.split(' '))

# Ex 14
challenge = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(challenge.split(','))

 # Ex 15
coding = 'Coding For all'
first_character = coding[0]
print('The FIrst character in the string {} is {}'.format(coding, first_character))

# Ex 16
last_character = coding[-1]
print('The last character in the string {} is {}'.format(coding, last_character))

# Ex 17
character = coding[10: 0]
print('The chatracter at index 10 in the string {} is {}'.format(coding, character))


# Ex 18

# Ex 19

# Ex 20
coding = 'Coding For all'
sub_coding = 'C'
print(coding.index(sub_coding))

# Ex 21
coding = 'Coding For all'
sub_coding = 'F'
print(coding.index(sub_coding))

# Ex 22
coding_for = 'Coding For All People'
sub_challenge = 'l'
print(coding_for.rfind(sub_challenge))

# Ex 23
Sentence = 'You cannot end a sentence with because because because is a conjunction'
sub_sentence = 'because'
print(Sentence.rfind(sub_sentence))

# Ex 24
Sentence = 'You cannot end a sentence with because because because is a conjunction'
sub_sentence = 'because'
print(Sentence.rindex(sub_sentence))
# Ex 25
sentence = 'You cannot end a sentence with because because because is a conjunction'
sub_sentence = 'because'
start = sentence.find(sub_sentence)
end = sentence.rfind(sub_sentence)
phrase = sentence[start:]
print(phrase)
# Ex 26
string = 'Coding for all'
sub_string = 'Coding'
print("'Coding for all start with' start with 'Coding' : ", string.startswith('Coding') )
 # Ex 27
string = 'Coding for all'
sub_string = 'Coding'
print("'Coding for all ' ends with 'Coding' : ", string.endswith('Coding') )
# Ex 30
identifier_1 = '30DaysOfPython'
identifier_2 = 'thirty_days_of_python'
print("{} is a valid Identifier :".format(identifier_1), identifier_1.isidentifier())
print("{} is a valid Identifier :".format(identifier_2), identifier_2.isidentifier())

# EX 32
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
join_python_libraries = '-'.join(python_libraries)
print(python_libraries)









