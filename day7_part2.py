# this was completed with help from 'Dylan Codes' on Youtube

# function to import text file
def import_file(file):
    with open(file) as f:
        contents = f.read()

    # each bag  is a string in a list
    bags = contents.split('\n')

    return bags

# recursive function to count the number of bags a colour contains
def count_contents(colour):
    contents = ''
    for bag in bags:
        if bag[:bag.index(' bags')] == colour:
            contents = bag
    
    if 'no' in contents:
        return 1

    contents = contents[contents.index('contain')+8:].split()

    bag_count = 0
    i = 0
    while i < len(contents):
        count = int(contents[i])
        colour = contents[i+1] + ' ' + contents[i+2]

        bag_count += count * count_contents(colour)
        i += 4
    
    return bag_count + 1

# driver program
if __name__ == '__main__':  
    bags = import_file('day7_input.txt')
    colour = 'shiny gold'
    print(colour + ' bags contain ' + str(count_contents('shiny gold') - 1) + ' bags.')