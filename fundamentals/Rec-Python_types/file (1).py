num1 = 42 #data type is numbers and Primitive variable declaration 
num2 = 2.3 #data type is numbers and Primitive 
boolean = True #data type is boolean and Primitive 
string = 'Hello World' #data type is string and Primitive 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']  #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #tuples 
print(type(fruit)) #type check
print(pizza_toppings[1]) #accesses value from the list from index 1, sausage also is a composite data type
pizza_toppings.append('Mushrooms') #method to add in mushrooms into list
print(person['name']) #accesses the persons name which is john inside dictionary
person['name'] = 'George' #changes the name from john to George inside the dictionary
person['eye_color'] = 'blue' #tuple' object has no attribute 'append'
print(fruit[2]) #accesses the tuple at index 2

if num1 > 45:  #conditional if 
    print("It's greater") #- log statement
else: #conditional if 
    print("It's lower") #- log statement

if len(string) < 5: #conditional if 
    print("It's a short word!") #- log statement
elif len(string) > 15: #conditional elif 
    print("It's a long word!") #- log statement
else: #conditional else
    print("Just right!") #- log statement

for x in range(5): #for loop start 
    print(x) #for loop end 
for x in range(2,5):  #for loop start 
    print(x)#for loop end 
for x in range(2,10,3): #for loop start 
    print(x) #for loop end 
x = 0
while(x < 5): #while loop start
    print(x) #while loop stop
    x += 1 #while loop increment 

pizza_toppings.pop() #list delete value at end
pizza_toppings.pop(1) #list delete value at index 1 

print(person) #dictionary 
person.pop('eye_color') #removes the value
print(person) #dictionary prints

for topping in pizza_toppings: #for loop starts, start of function
    if topping == 'Pepperoni': #parameter  
        continue #continue 
    print('After 1st if statement') #argument 
    if topping == 'Olives': #parameter 
        break #stop

def print_hello_ten_times():  #function  
    for num in range(10): #parameter
        print('Hello') #return

print_hello_ten_times() #return 

def print_hello_x_times(x): #function and parameter
    for num in range(x): #parameter
        print('Hello') #return

print_hello_x_times(4) #argument

def print_hello_x_or_ten_times(x = 10): #function and argument 
    for num in range(x): #parameter
        print('Hello') #return 

print_hello_x_or_ten_times() #return 
print_hello_x_or_ten_times(4) #argument 


"""
Bonus section
"""

# print(num3) #NameError
# num3 = 72 # TypeError: 'tuple' object does not support item assignment
# fruit[0] = 'cranberry' #- AttributeError: 'tuple' object has no attribute 'append'
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) #- IndexError: list index out of range
#   print(boolean) #- IndentationError: unexpected indent
# fruit.append('raspberry') #tuples add value 
# fruit.pop(1) #tuples delete value 