#1 Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ]
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [
    {'x': 10, 'y': 20}
    ]


#1
x[1][0] = 15
print(x)
#2
students[0]['last_name'] = 'Bryant'
print(students)
# #3

sports_directory['soccer'][0] = 'Andres'
print(sports_directory['soccer'])

# #4

z[0]['y']= 30
print(z)


#2 Iterate through a list of Dictionaries

from optparse import Values
from re import I
from sqlite3 import connect
from tkinter import N
from tkinter.messagebox import RETRY
from turtle import st


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



def iterateDictionary(students):
    for users in students:
        # print(users)
        for val in users.values():
            print(val)



iterateDictionary(students) 


# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen


#3 Get values from a list of dictionaries 



def iterateDictionary2(key_name,students): 
        for names in students:
                print(names[key_name])


iterateDictionary2('first_name',students)
iterateDictionary2('last_name', students)


#4 Iterate through a dictionary with list values  (SOMEWHAT DONE)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}



def printInfo(dojo_dict):
        for i in dojo:
                print(len(dojo[i]))
                print(i)
                for x in dojo[i]:
                        print(x)
printInfo(dojo)




