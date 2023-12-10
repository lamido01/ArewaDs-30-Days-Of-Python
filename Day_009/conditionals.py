# Q1
dog = {}
# Q2
dog = {'name' : 'Wiz','color' : 'brown', 'breed' : 'bulldog', 'legs' : 2 , 'age' : 2}
print(dog)
# Q3
Student = {'first_name' : 'Aliyu',
 'last_name' : 'Lamido',
  'gender' : 'male',
   'age' : 23, 
   'marrital_status' : 'single',
    'skills' : ['programming','data cleaning','Data Analysis','visualization'],
    'country' : 'Nigeria',
    'city' : 'Bauchi',
    'address': 'Ajiya Quaters '
    }

    # Q4
print(len(Student))
# Q5
skills =  Student['skills']
Skilks_data_type = type(skills)
print(skills)
print(Skilks_data_type)

# Q6
skills.append('Mining')
print(Student)
# Q7
dct_keys =  Student.keys()
print(dct_keys)
# Q8 
dct_values = Student.values()
print(dct_values)

# Q9
Student_tpl = Student.items()
print(Student_tpl)

# Q10
Student.popitem()
 
 # Q11
del Student





