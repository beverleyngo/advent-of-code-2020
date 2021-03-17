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

# Function to find the encryption weakness.
def encryption_weakness(rows, target):
    # Loop through the values.
    for i in range(len(rows)):
        # Keep a count of the total and the values which will be summed.
        total = 0
        values = []
        j = i

        # Keep appending values whilst the total is less than the target.
        while total < target:
            total += rows[j]
            values.append(rows[j])
            j += 1

        # if the total is equal to the target, this means there is a match.
        if total == target:
            # Add the maximum and minimum of the values which were summed
            weakness = max(values) + min(values)
            # Return the value.
            return(weakness)


# Driver program.
if __name__ == '__main__':  
    rows = import_file('day9_input.txt')
    target = find_value(rows, 25)
    print(encryption_weakness(rows, target))