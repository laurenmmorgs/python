#1 Countdown --done
# from itertools import count


# def countdown(lists):
#         output = []
#         for i in range(lists, -1, -1):
#             output.append(i)
#         return output

# print(countdown(5))

#2 Print and return --done


# def print_and_return(my_list): 
#     print(my_list[0])
#     return(my_list[1])

# print(print_and_return([1,2]))



# 3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

#3 first plus length 

# def first_plus_length(inputs):
#     sum = 0
#     x = inputs[0]
#     y = len(inputs)
#     sum = x + y
#     return sum 

# print(first_plus_length([1,2,3,4,5]))



# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False
# def values_greater_than_second(lists):
#     output = []
#     x = 0 
#     for value in lists: 
#         if value > lists[1]:
#             output.append(value)
#             print(output)
#             x += 1 
#             print(x) 
#         elif value == lists[0]:
#             return False

    

# print(values_greater_than_second([5,2,3,2,1,4]))



# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

# def length_and_value(a,b):
#     output = []
#     for i in range(b):
#         output.append(b)
#         return(output*a)


# print(length_and_value(4,7))