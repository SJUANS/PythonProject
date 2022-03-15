"""
As you can see, the code is broken.
Create the missing functions, use default arguments.
Sometimes you have to use 'return' and sometimes you dont.
Start by creating the functions
"""
def is_on_list(list,item):
    existence = f"{item}" in list
    #https://pythonia.tistory.com/14 참조
    #list는 {}안에 넣지 않는다!
    return existence

def get_x(list,order):
    x = list[int(order)]
    return x

def add_x(list,item):
    return list.append(item)

def remove_x(list,item):
    return list.remove(item)

# \/\/\/\/\/\/\  DO NOT TOUCH AREA  \/\/\/\/\/\/\ #

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Is Wed on 'days' list?", is_on_list(days, "Wed"))

print("The fourth item in 'days' is:", get_x(days, 3))

add_x(days, "Sat")
print(days)

remove_x(days, "Mon")
print(days)

# /\/\/\/\/\/\/\ END DO NOT TOUCH AREA /\/\/\/\/\/\/\ #

