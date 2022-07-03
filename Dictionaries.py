# Dictionary--- key-value pairs, unordered, muttable
mydict = {'name':'Kriston','age':20,'gpa':5.0}
mydict2 = dict(name='Kriston', age = 20, gpa = 5.0)  #notice here we will not use "" for keys
print(mydict)
print(mydict2)

value = mydict['name']  # Here we need to use [] to call the dict
print(value)

hisDict = {'gpa':5.0, 'grade':11,'major_num':13}
print(max(hisDict.values()))

'''change a dict'''
mydict['email'] = 'max@xyz.com'
print(mydict)

'''the way to delete elements from a dict'''
del mydict['name']
print(mydict)

mydict.pop('gpa')   #differ from LIST, pop in dictionary would not remove the last element, you need to assign a argument
print(mydict)

mydict.popitem()   # popitem() will remove the last element
print(mydict)

if 'age' in mydict:
    print(mydict['age'])
if 'you' in mydict:
    print(mydict['you'])  # nothing will be printed here cuz 'you' is not in mydict

try:
    print(mydict['name'])
except:
    print('error')

# for key in mydict2:
#     print(key)
#
# for value in mydict2.values():
#     print(value)

for key,value in mydict2.items():
    print(key,value)

# mydict2_copy = mydict2     # when you modify one of the two, the other will also be modified
# mydict2_copy['lover'] = 'wy'
# print(mydict2)
# print(mydict2_copy)

# if you only want to change one of the two(original and copy) use the code below
mydict2_copy = mydict2.copy()    # or mydict2_copy = dict(mydict2)
mydict2_copy['lover'] = 'wy'
print(mydict2)
print(mydict2_copy)

mydict3 = {'name':'Kriston','age':20,'gpa':5.0}
mydict4 = dict(name = 'kriston',age = 23, city = 'Toronto')
mydict3.update(mydict4)
print(mydict3)

my_tuple = (8,3)
mydict5 = {my_tuple: 11}   # we could only assign a key which is an immutable type like tuple, we cannot use a list
print(mydict5)

dict_1 = {"name": 'Chris', 'age': 13, 'address': 'stupid palace'}
dict_1.setdefault('name', 'hello')
print(dict_1.keys())
print(dict_1.items())