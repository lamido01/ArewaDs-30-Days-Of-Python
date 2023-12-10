# Q 1.
empty_lst = []
# Q 2
courses = ['Stat 202', 'cosc 102', 'math 102', 'biol 203','chem 106', 'zool 304']
# Q 3.
print('Number of courses : ', len(courses))
# Q4
First_course = courses[0]

print('firt course( in the list : ', First_course)

middle_course = courses[2]
print('Middle course : ', middle_course )

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
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index]
print('middle item : ', middle_company)


last_index = len(it_companies) - 1
last_comapany = it_companies[last_index]
print('First Company : ',first_company)

print('last Company : ' , last_comapany)

it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies[0] = 'Coursera' 
print(it_companies)

# Q 11
it_companies.append('Instagram')

# Q 12 
middle = len(it_companies) // 2
it_companies.insert(middle, 'DataCamp')
print('Middle index is :', middle)
print(it_companies)

# Q 13
it_companies[4].capitalize()
print(it_companies)

# Q14
non_it_companies = ['Maclean', 'Indomie', 'Dangote']
it_and_non_it_companies = it_companies + non_it_companies
print(it_and_non_it_companies)

# Q15
does_exist = 'Datacamp' in it_companies
print("'Datacamp' in it_comapnies :",  does_exist)

# Q16
it_companies.sort()
print("It companies sorted :", it_companies)

# Q 17 
it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies = it_companies.reverse()
print(it_companies)

# Q18
it_companies  = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
First_three = it_companies[0:3]
print(First_three)

# Q19
Ibm_index = it_companies.index('IBM')
last_three = it_companies[Ibm_index :]
print(last_three)

# Q20
del it_companies[0]
print(it_companies)

# Q21
del it_companies[it_companies.index('Apple')]
print(it_companies)

#  Q22
del it_companies[len(it_companies)- 1]
print(it_companies)
# Q23
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.clear()
print(it_companies)

# Q25
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
print('front end and backend : ', joined)

# 26
Full_stack = joined.copy()
Full_stack.insert(Full_stack.index('Redux')+1, 'Python')
Full_stack.insert(Full_stack.index('Python')+1, "SQL")
print("Full Stack : ", Full_stack) 
 
 # Exercise LEvel 2
 # Q1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()

Average = sum(ages) / len(ages)
print('Average Age : ', Average)
Min_age = min(ages)
Max_age = max(ages)
print('max age :', Max_age )
print('minimum age : ', Min_age)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
n = len(ages)
if n % 2 == 0 :
    median1 = ages[n // 2]
    median2 = ages[n //2 - 1]
    median = (median1 + median2) / 2
else :
    median = ages[n // 2]
    print('Median is: ', median ) 
print('Range is: ', Max_age + Min_age)

Average = sum(ages) / len(ages)
print(abs(Min_age - Average))
print(abs(Max_age - Average))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(len(countries))
middle_country = countries[len(countries)//2]
print(middle_country) 

first_half = countries[0:countries.index('Lesotho')+2]
Second_half = countries[countries.index('Lesotho')+2:]
print('Fisrt Half is: ', first_half)
print('second Half is: ', Second_half)

print(len(countries)/2)
first_half = countries[0:countries.index('Lesotho')+1]
Second_half = countries[countries.index('Lesotho')+1:]
print('length first half:', len(first_half))
print('Length Second Half:', len(Second_half))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
fisrt_counrty, second_counrty,third_countrty, *scandic_countries = countries
print('Scandic countries: ',scandic_countries)




























