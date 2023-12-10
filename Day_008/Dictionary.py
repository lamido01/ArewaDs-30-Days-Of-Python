# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Q1
print('number of IT companies:', len(it_companies))
# Q2
it_companies.add('Twitter')
# Q3
it_companies.update('Facebook', 'Datacamp','Telegram')
# Q4
it_companies.pop()
print(it_companies)
# Q5
# Remove() return error when the elements is not in the set while discard() does not

# Level 2

print('A and B:',A.union(B))
print('A intersection B:', A.intersection(B))
print('A is subset of B: ', A.issubset(B))
print('A and B are disjoint:', A.isdisjoint(B))
print('symetric difference between A and B:', A.symmetric_difference(B))
del A,B,it_companies

# Level 3
# Q1
age_set = set(age)
if len(age) > len(age_set) :
    print('list is bigger')
else :
    print('Set is bigger')
# Q2

# Q3
string = "I am a teacher and I love to inspire and teach people"
splited_str = string.split()
print(splited_str)
converted_string = set(splited_str)
print(converted_string)
print('Number of unique words used in the sentence is ', len(converted_string))


 

