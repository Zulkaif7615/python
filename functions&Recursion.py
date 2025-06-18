# block of statement that perform a specific task
def sum(a,b):
    s = a+b
    return s

# print(sum(3,4))


def print_hello():
    print("hello world")
    
# out = print_hello()
# print(out) 
# None , If function nothing returns it output is none


# Lets practice 
cities = ["lahore","multan","khanewal","karachi","vehari"]

def print_len(list):
    print(len(list))

# print_len(cities)
# .............

def print_list(list):
    for item in list:
        print(item,end="")
        
# print_list(cities)

# ................

def factorial(n):
    fact = 1
    for i in range(1,n+1):
      fact *= i 
    print(fact)
# factorial(5)

# ................

def converter(usd_val):
    pak_val = usd_val * 83
    print(usd_val,"USD=",pak_val,"PAK")
# converter(50)

# ...............
# Recursion 
# when a function calls itself repeatedly 
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("end")
# show(7)

# ...........
def fact1(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact1(n-1)
# fact1(5)

# ...............
def calc_sum(n):
    if(n == 0):
        return
    return calc_sum(n-1) + n
# sum = calc_sum(5)
# print(sum)

# ............
def print_list(list,index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list,index+1)

fruits = ["manago","apple","banana","peach"]

print_list(fruits)

