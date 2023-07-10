x = [[5, 2, 3], [10, 8, 9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
]
sports_directory = {
    "basketball": ["Kobe", "Jordan", "James", "Curry"],
    "soccer": ["Messi", "Ronaldo", "Rooney"],
}
z = [{"x": 10, "y": 20}]

x[1][0] = 15
print(x)

students[0]['last_name'] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)

# ******************************
print("****************************")

students = [
    {'first_name': 'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for dictionaire in some_list:
        # print(dictionaire.items())
        for key,value in dictionaire.items():
            print(f"{key} - {value}")
    return None

iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# ************************************
print("****************************")
def iterateDictionary2(key_name, some_list):
    for dictionaire in some_list:
        # print(dictionaire.items())
        for key in dictionaire.keys():
            print(dictionaire[key])
    return None

iterateDictionary2('first_name', students)


# ************************************
print("****************************")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dictionary):
    for key in dictionary.keys():
        print(len(dictionary[key]),key)
        for i in dictionary[key]:
            print(i)
        print(' ')
    return None

printInfo(dojo)