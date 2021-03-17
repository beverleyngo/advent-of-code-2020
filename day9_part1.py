# Function to import text file
def import_file(file):
    rows = []
    with open(file) as f:
        for line in f:
            rows.append(int(line.strip('\n')))
    return rows

# Function to find first value that cannot be summed from two previous values.
def find_value(n, p): # Takes the list of values and the preamble length as parameters.
    for i in range(p, len(n)):
        # Define the target value and the preamble/previous numbers before target.
        target = n[i]
        previous = n[i-p:i]

        # loop through the preamble to find two matching values.
        for j in range(len(previous)):
            # There is a match if the complementary of a value exists.
            complementary = target - previous[j]
            remaining_4 = []
            remaining_4 = previous.copy()
            remaining_4.pop(j)
            if complementary in remaining_4:
                break
        # Return the target value if there are no matches.
        else:
            return target


# Driver program.
if __name__ == '__main__':  
    rows = import_file('day9_input.txt')
    print(find_value(rows,25))