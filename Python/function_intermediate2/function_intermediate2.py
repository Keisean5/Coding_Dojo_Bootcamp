# x = [ [5,2,3], [10,8,9] ] 

# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }

# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15
# print(x)

# students[0]['last_name'] = 'Bryant'
# print(students)


# sports_directory ['soccer'][0] = 'Andres'
# print(sports_directory)

# z[0]['y'] = 30
# print(z)


# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30



students = [
    {'first_name' :  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# def iterateDictionary(some_list):
#     for some_item in some_list:
        
#         print(f'first_name - {some_item["first_name"]}, last_name - {some_item["last_name"]}')

# iterateDictionary(students)


# def iterateDictionary2(key_name, some_list):
#     for some_item in some_list:
#         print(some_item[key_name])

# iterateDictionary2('first_name', students)
# print("*******")
# iterateDictionary2('last_name', students)



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dojo_dict):
    for titles in dojo_dict:
        print(titles)
        for names in dojo_dict[titles]:
            print(names)

printInfo(dojo)

