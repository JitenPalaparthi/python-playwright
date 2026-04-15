# list is orderd, mutable collection
# index based
# mutable
# allow duplicates
# heterogeneous values inside the list
# think it as a dynamic array

import random
my_list = [32,3,345,46,5,565,56,454.223,True, "Hello Wrold"]

sum = 0
for i  in my_list:
    try:
        sum=sum+i
    except TypeError:
        None
        # sum=sum+0

print(sum)
print(len(my_list))

my_list=[]

#len(my_list)
print(len(my_list))


for _ in range(10):
    my_list.append(random.randint(1,10))

print(my_list)

try:
    my_list.remove(my_list[len(my_list)-1])
except ValueError:
    None
print(my_list)


my_tuple_list = [("JP","43"),("Jyothi,35"),("Swetha","36")]


def remove_last_value(lst):
      if len(lst)>0:
        lst.remove(lst[len(lst)-1])

remove_last_value(my_tuple_list)

print(my_tuple_list)

my_tuple_list=[]

remove_last_value(my_tuple_list)

print(my_tuple_list)
