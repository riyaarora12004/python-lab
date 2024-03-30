# Example 1: Using else with while and break
i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("While loop completed successfully")

# Example 2: Using else with while without break
i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("While loop completed successfully")
