# Function to import file.
def import_file(file):
    op = []
    ar = []
    # Split each line into two lists for operation and argument.
    with open(file) as f:
        for line in f:
            line_op, line_ar = line.split()
            op.append(line_op)
            ar.append(int(line_ar))
    return op, ar

# Function to find the accumulator value.
def find_value(op,ar):
    # Keep track of accumulator value using a counter.
    # Keep track of current row using executed_lines.
    count = 0
    executed_lines = [0]

    # Iterate starting from row 0.
    # The next row to be iterated is calculated in the for loop.
    for i in executed_lines:

        # If the operation is 'nop' and row i+1 hasn't already been visited, go to row i+1.
        if op[i] == 'nop':
            if i+1 not in executed_lines:
                executed_lines.append(i+1)
            # If we have already been to that row, stop the program and return the accumulator value.
            else:
                print(count)
                exit

        # If the operation is 'acc' and row i+1 hasn't already been visited, go to row i+1.
        elif op[i] == 'acc':
            if i+1 not in executed_lines:
                executed_lines.append(i+1)

                # Add the argument for current row to the count, to update the accumulator.
                count += ar[i]

            # If we have already been to that row, stop the program and return the accumulator value.
            else:
                print(count)
                exit

        # If the operation is 'jmp' and the row i+ar[i] (the jump step) hasn't been visited, go to that row.
        elif op[i] == 'jmp':
            if i+ar[i] not in executed_lines:
                executed_lines.append(i+ar[i])

            # If we have already been to that row, stop the program and return the accumulator value.
            else:
                print(count)
                exit

# Driver program.
if __name__ == '__main__':  
    op, ar = import_file('day8_input.txt')
    print("The accumulator value is:") 
    find_value(op,ar)