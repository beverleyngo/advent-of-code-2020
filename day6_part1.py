from collections import OrderedDict 

# function to import text file
def import_file(file):
    with open(file) as f:
        contents = f.read()

    # each group is a string in a list
    groups = contents.split('\n\n')
    all_groups = []
    for group in groups:
        all_groups.append(group.replace('\n', ''))

    return all_groups

# function to remove duplicate letters from each string
def remove_dup(list):  
    new_list = []
    for group in list:
        new_list.append(''.join(set(group)))
    return new_list

# function to find the length of each string
def count_groups(list):
    counts = []
    for group in list:
        counts.append(len(group))
    return counts

# function to find the total counts
def find_counts(file):
    all_groups = import_file(file)
    all_groups_unduplicated = remove_dup(all_groups)
    counts = count_groups(all_groups_unduplicated)
    return sum(counts)

# driver program
if __name__ == '__main__':  
    file = 'day6_input.txt'
    print('The sum of counts for all groups = ' + str(find_counts(file)))