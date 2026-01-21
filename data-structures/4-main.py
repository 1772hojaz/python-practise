#!/usr/bin/python3
replace_in_list = __import__('replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
print(my_list)
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)
print(f"The new list shows {new_list}")
print(f"The my_list shows {my_list}")
x = 0
y = 20


other =  replace_in_list(my_list, x, y)

print(f"the other list {other}")
print(f"the my_list shows{my_list}")
