my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print("After appending:", my_list)

my_list.insert(2, 10)
print("After inserting:", my_list)

popped_element = my_list.pop()
print("Popped element:", popped_element)
print("After popping:", my_list)

my_list.extend([7, 8, 9])
print("After extending:", my_list)
