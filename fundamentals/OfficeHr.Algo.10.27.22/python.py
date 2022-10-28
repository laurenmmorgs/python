
# def helper(input):
#     if input > 0 and input < 10  or input < 0 and input >-10:
#         print("one digit")
#     elif input < 100 or input < -100:
#         print("two digit")
#     else:
#         print("I can't that high")

def helper(input):
    if input in range(9) or input in range(0,-9,-2):
        print("one digit")
    elif input in range(10, 99) or input in range(-10,-99, -1):
        print("two digits")
    else:
        print("too high")

def digits(num):
    if num > 0: 
        print("Positive")
        helper(num)
    elif num < 0:
        print("negative")
        helper(num)
    elif num == 0:
        print("zero")
    else:
        print("This is greater than 2 digits")

digits(-5555)

# from tkinter import Y


# def ArrayReverse(input):
#     output = []
#     for x in input:
#         output.append(x)
        

# print(ArrayReverse([3,1,6,4,2]))