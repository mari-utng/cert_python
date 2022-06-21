my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = my_list

for i in my_list:
    if i in new_list:
        del my_list[i]
        
print("La lista con elementos únicos:")
print(my_list)