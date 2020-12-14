# Import the input text file with each passport as a string in a list:
with open('day4_input.txt') as f:
    contents = f.read()

passports = contents.split('\n\n')

# List of the fields required to be a valid passport:
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Count the number of passports which contain all required fields:
count = 0
for i in passports:
    if all([val in i for val in fields]):
        count += 1

print('The number of valid passports is: ' + str(count))
        