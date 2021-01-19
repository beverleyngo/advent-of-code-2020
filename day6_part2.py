from collections import OrderedDict 

# function to import text file
def import_file(file):
    with open(file) as f:
        contents = f.read()

    groups = contents.split('\n\n')
    return groups

# function to find number of people per group, group answers and group unique answers
def group_analysis(list):
    people_count = []
    all_groups = []
    unique_letters = []
    for group in list:
        # count the number of people (rows) per group
        people = 1
        people += group.count('\n')
        people_count.append(people)

        # remove newline from each group so each group forms one string
        new_string = group.replace('\n', '')
        all_groups.append(new_string)

        # find the unique questions for each group
        unique_letters.append(''.join(set(new_string)))
    
    return people_count, all_groups, unique_letters

# function to find the number of unique answers answered by every person in each group
def count_groups(people_count, all_groups, unique_letters):
    answered_counts = []

    # find when occurences of unique letter in group == to no. people in group
    for group in range(len(all_groups)):
        yes_count = 0
        for letter in unique_letters[group]:
            if all_groups[group].count(letter) == people_count[group]:
                yes_count += 1
        answered_counts.append(yes_count)
    
    return answered_counts

# driver program
if __name__ == '__main__':  
    file = 'day6_input.txt'
    groups = import_file(file)
    people_count, all_groups, unique_letters = group_analysis(groups)
    counts = count_groups(people_count, all_groups, unique_letters)
    print('The sum of counts is: ' + str(sum(counts)))