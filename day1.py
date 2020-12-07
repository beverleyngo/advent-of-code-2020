# Import the list of numbers and add to expense_list:
expense_list = []
f=open('input.txt',"r")
for line in f:
    expense_list.append(int(line.strip('\n')))

# Loop through expense_list:
for i in range(len(expense_list)):
    # Create new list not containing current number:
    remaining_list = []
    remaining_list = expense_list.copy()
    remaining_list.pop(i)

    int1 = expense_list[i]
    int2 = 2020 - int1

    # Search remaining numbers in new list for 2020 - current number:
    for i in remaining_list:
        if i == int2:
            print(int1)
            print(int2)
            print(int1*int2)
            break