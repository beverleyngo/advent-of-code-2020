# Function to import file
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
    # Same as day8_part1.py but stops the program if the next index
    # to be iterated is not within the range of the length of 'op'.
    for i in executed_lines:

        # If the operation is 'nop':
        if op[i] == 'nop':
            if i+1 not in executed_lines and i+1 < len(op):
                executed_lines.append(i+1)
            elif i+1 not in executed_lines and i+1 >= len(op):
                print("Success! " + str(count))
                exit
            else:
                exit

        # If the operation is 'acc':
        elif op[i] == 'acc':
            if i+1 not in executed_lines and i+1 < len(op):
                executed_lines.append(i+1)
                count += ar[i]
            elif i+1 not in executed_lines and i+1 >= len(op):
                count += ar[i]
                print("Success! " + str(count))
                exit
            else:
                exit

        # If the operation is 'jmp':
        elif op[i] == 'jmp':
            if i+ar[i] not in executed_lines and i+1 < len(op):
                executed_lines.append(i+ar[i])
            elif i+1 not in executed_lines and i+1 >= len(op):
                print("Success! " + str(count))
                exit
            else:
                exit

# Function to find the value of the accumulator after the program terminates
def after_termination(op,ar):
    for i in range(len(op)):
        temp_op = list(op)
        if temp_op[i] == 'jmp':
            temp_op[i] = 'nop'
        elif temp_op[i] == 'nop':
            temp_op[i] = 'jmp'

        find_value(temp_op,ar)

# Driver program.
if __name__ == '__main__':  
    op,ar = import_file('day8_input.txt')
    after_termination(op,ar)