
my_list = [1, 2, 3, 4, 5]

print("Elements of the list:")
for element in my_list:
    print(element)

my_list[2] = 10
print("Modified list:", my_list)

my_list.append(6)
print("After appending:", my_list)

my_list.remove(4)
print("After removing:", my_list)
