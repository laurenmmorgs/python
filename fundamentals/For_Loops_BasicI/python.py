#1. Basic 
for i in range(0,151):
    print(i)

#2. Multiples of five
for i in range(5,1001,5):
    print(i)

#3. Counting the dojo way 
for i in range(1,101): 
    if i % 5 == 0:
        print("coding")
    if i % 10 == 0:
        print("Coding Dojo")
    else: 
        print(i)

#Whoa that sucker is hufe
sum = 0

for i in range(0, 500001):
    if i % 2 != 0:
        sum = sum + i 
print(sum)

#countdown by fours
for i in range(2018,0,-4):
    print(i)

#flexible counter 
lowNum = 3
highNum = 10
multiple = 3

for i in range(lowNum,highNum,multiple):
    print(i)