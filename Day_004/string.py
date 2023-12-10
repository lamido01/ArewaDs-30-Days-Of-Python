import math
age = 25
height = 3.6
complex_num = 3 + 5j
# Araea of a triangle 

base_of_triangle = input('Enter  base of the triangle:')
height_of_triangle = input("Enter height of the triangle:")
area_of_triangle = 0.5 * float(base_of_triangle) * float(height_of_triangle)
print('The area of the triangle is', area_of_triangle)
# perimeter of a triagle 

side_a = int(input('Enter side a :'))
side_b = int(input('Enter side b :'))
side_c =int(input('Enter side c :'))
perimeter = side_a + side_b + side_c
print('The perimeter of the triangle is' , perimeter)
# Area and perimeter of a rectangle

length =float(input('Enter length :'))
width = float(input('Enter width :'))
area = (length * width)
perimeter = 2 * (length + width)
print('The area is ',  area)
print('The perimeter is ' , perimeter)

# Area and circumference of a circle
radius = float(input('Entar the radius :' ))
area = math.pi * radius * radius
circumference = 2 * math.pi * radius
print('The area is ' , area)
print('The circumference is ' , circumference)

# x and Y intercept of y = 2x - 2

slope_1 = 2
x_intercept = (1, 0)
y_intercept = (0, -2)
slope_2 = (10 - 2) / (6 - 2)

# comparing 2 slope
print('slope 1 is slope 2 :', slope_1 is slope_2)
# Lenth of python and dragon

print(len('python') != len('dragon'))
print('on in both python and dragon : ', 'on' in 'python' and 'on' in  'dragon')
print('jargon in i hope this course is not full of jargon : ', 'jargon' in 'i hope this course is not full of jargon' )
print('There is no {on} in both dragon and python : ', 'on' not in 'dragon' and 'on' not in 'python')
print(str(float(len('python'))))

# checking Even Number
number = int(input('Entaer a number : '))

if(number % 2) == 0: 
    print('{0} is even number'.format(number))
else :
    print('{0} is odd number'.format(number))
     
print('7 // 3 is int(2.7) :', 7 // 3 == int(2.7))

print('type(10) is type(10) :', type('10') == type(10))

print(' str(9.8) is equal to 10 :', '9.8' is 10)
# weekly earning
hours = int(input('Enter hours : '))
rate_per_hour = int(input('Enter rate per hour : '))
weekly_earning = rate_per_hour * hours
print('your weekly earning is is ', weekly_earning)

# Number of seconds a person lived
sec_year = 31536000
number_of_years = int(input('Enter number of years lived : '))
seconds_lived = number_of_years * sec_year
print('You lived for ', seconds_lived, ' ', 'seconds' )











 


















