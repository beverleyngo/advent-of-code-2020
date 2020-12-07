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

    # Loop through remaining_list:
    for i in range(len(remaining_list)):
        # Only create int2 if the number is less than int2:
        if remaining_list[i] <= int2:
            int2 = remaining_list[i]
            # New variable to find third number if matches:
            int3 = 2020 - int1 - int2 

            # Create another list not containing int1 and int2:
            remaining_list_2 = []
            remaining_list_2 = remaining_list.copy()
            remaining_list_2.pop(i)

            # Loop through second list to find third matching number:
            for i in range(len(remaining_list_2)):
                if remaining_list_2[i] == int3:
                    print(int1*int2*int3)
                    break