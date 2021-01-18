# import input file
all_seats = []
f=open('day5_input.txt',"r")
for line in f:
    all_seats.append(line.strip('\n'))

# function to find the seat row
def find_row(string, iteration, start, end):
    mid = (start + end) // 2

    if iteration == 6:
        if string[iteration] == 'F':
            return start
        if string[iteration] == 'B':
            return end

    if string[iteration] == 'F':
        return find_row(string, iteration + 1, start, mid)
    if string[iteration] == 'B':
        return find_row(string, iteration + 1, mid +1, end)

# function to find the seat column
def find_column(string, iteration, start, end):
    mid = (start + end) // 2
    
    if iteration == 9:
        if string[iteration] == 'L':
            return start
        if string[iteration] == 'R':
            return end

    if string[iteration] == 'L':
        return find_column(string, iteration + 1, start, mid)
    if string[iteration] == 'R':
        return find_column(string, iteration + 1, mid +1, end)

rows = []
columns = []
seat_ids = []
# function to find seat row, column and id for all seats 
for i in range(len(all_seats)):
    row = find_row(all_seats[i], 0, 0, 127)
    rows.append(row)

    column = find_column(all_seats[i], 7, 0, 7)
    columns.append(column)

    seat_id = (row * 8) + column
    seat_ids.append(seat_id)

# print the highest Seat ID
print('The highest Seat ID is: ' + str(max(seat_ids)))