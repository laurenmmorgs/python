from gettext import find


user = {
    'first_name': "Lauren",
    'last_name': "Morgan",
    'age': 23,
    'email': 'lm@email.com',
    'graduated' : False,
    'dogs_name': ['bandit','ginger']
}
other_user = {}
print(user['dogs_name'][0])
print(user.get('user_name'))
user['last_name']= 'C'
# other_user.update(
#     {
#     'first_name': "Parker",
#     'last_name': "C",
#     'age': 20,
#     'email': 'pc@email.com',
#     'graduated' : False,
#     'dogs_name': ['bandit','ginger']
#     })
# other_user.update(
#     {
#     'first_name': "Fran",
#     'last_name': "B",
#     })
# value = other_user.pop('age')
# print(value)


# for i in user:
#     print(user[i])

# for key in user.keys():
#     print(key)

# for values in user.values():
#     print(values)

# for key, val in user.items():
#     print(f"val: {val} key: {key}" ) # shows how to print out both 

# for items in user.items():
#     print(items) # Does the same thing but not so artsy 


users = []
def create(first_name, last_name,email, age, has_kids = False):
    user = {
    'first_name': first_name,
    'last_name': last_name,
    'email': email,
    'age': age,
    'has_kids': has_kids,
    'children': []
    }
    users.append(user)
    # print(users)
    return user

user1 = create('Cameron', 'Smith', 'cs@email.com', 34, True)
user2 = create('Test', 'McTest', 'Test@email.com', 35)
user3 = create('Timmy', 'Q', 'Q@email.com', 334, True)
user4= create('Orange', 'T', 'ot@email.com', 64, True)
user5 = create('clint', 'g', 'cg@email.com', 24, True)
# print(users)


# loop through a list

def find_one(first_name,child_name):
    # print(first_name,child_name)
    for user in users:
        # print(user)
        for val in user.values():
            # print(val)
            if val == first_name:
                if user['has_kids']:
                    # print(user)
                    # print(val)
                    user['children'].append(child_name)
                    # print(user['children'])
                else: 
                    print("They don't have kids")

def find_users(first_name, child_name):
    for user in users:
        if user['first_name'] == first_name:
            user['children'].append(child_name)
            print(user['children'])



find_users('Timmy','charles')
find_users('Timmy', 'Tommy')
find_users('Test', 'Bob')