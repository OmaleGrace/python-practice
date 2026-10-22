# #PRINTING

# ## print is used to display things to the console i.e terminal
# ## it is written with the key word print with everything lowercased
# print("Hello, Omahlay")


# #VARIABLES

# ## a variable is a name attatched to a value more like a storage
# ## variables can't start with a number and contain spaces
# ## a single equality sign is used to assign variables

# name = "Grace"
# print(name)
# food = "Swallow"
# print(food)

# ## reassigning varaibles
# x = "init"
# x = "NO"
# print(x)

# num = 10
# num = num + 5
# print(num)


# #DATA TYPES

# ## 1. string(str): text written in quotes
# ## 2. integer(int): a number written written without quotes
# ## 3. float: a number with a decimal  point
# ## 4. boolean(bool): only two possible values, True and False with it's first letter capitalized and no quotes

# ## type tells you the type of anything, it's keyword in python is 'type'

# print(type(42))
# print(type("42"))
# print(type(4.2))
# print(type(num))
# print(type(True))

# print("5" + "5")
# print(5 + 5)


# #CONVERTING TYPES

# ## int(..) converts to an integer
# ## str(..) converts to a string
# ## float(..) converts to a float

# num = num + int(-4.9)
# print(num)
# print(str(num) + "5")
# #print(int("Hello"))


# # GETTING INPUT FROM USER

# ## we use the word input  to get input from the user

# G = input("What is your name? ")
# print(G)

# B = input("How old are you? ")
# try:
#     print(int(B) + 1)
# except ValueError:
#     print("Cannot accept string!!")

# name = input("What is your name? ")
# price = input("What is the price of rice? ")
# quantity = input("How many items do you want? ")
# total = float(price) * int(quantity)
# print(f"{name}, your total is {total}")

print(5 > 3)
print(5 == 5)
print(5 == "5")
print(10 != 10)