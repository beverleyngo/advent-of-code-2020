# function to import text file
def import_file(file):
    with open(file) as f:
        contents = f.read()

    # each bagvis a string in a list
    bags = contents.split('\n')

    return bags

# recursive function to count the number of bags
def count_bags_containing(colour):
    # find the bags which directly contain shiny gold
    directly_contains = [bag[:bag.index(' bags')] for bag in bags if colour in bag and bag.index(colour) != 0]
    
    # list of bags which either directly or indirectly contain shiny gold
    contains = []
    
    if len(directly_contains) == 0:
        return []

    else:
        # find the bags which contain the colours in directly_contains (i.e. bags which indirectly contain shiny gold)
        try_these_colours = [colour for colour in directly_contains if colour not in contains]
        
        for colour in try_these_colours:
            contains.append(colour)
            indirectly_contains = count_bags_containing(colour)
            contains += indirectly_contains

    # find the distinct colours
    unique = []
    for colour in contains:
        if colour not in unique:
            unique.append(colour)
    
    return unique

# driver program
if __name__ == '__main__':  
    bags = import_file('day7_input.txt')
    test = count_bags_containing('shiny gold')
    print('The number of bags which contain shiny gold is: ' + str(len(test)))