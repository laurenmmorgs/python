#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#output will be 5 


# #2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#output will be 5 if we dont print and throw an error if we do print 

# #3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#output will be 5 

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#output will be 5 

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#output will be 5 and null 

#6
def add(b,c):
    print(b+c)

print(add(1,2) + add(2,3))
#output will be 3, 5, 8  (WRONG AS IT THREW AN ERROR)

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#output will be 25 because it made it strings 

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#output will be 100 then 10

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#output will be 7, 14, 14 (WRONG BECAUSE IT RETURNS 7 AND 14 7+14=21)

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#output will be 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#output will be 500, 300, 500, none, 500. (WRONG IT WILL BE 500, 500, 300, 500 because it prints b then goes to the next print after the function and continues)

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#output will be 500 500 300 500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#output will be 500 500 300 300 


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#output will be 1 3 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#output will be 1 3 5 10 