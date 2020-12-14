# Import the input text file:
with open('day4_input.txt') as f:
    contents = f.read()

# Each passport is a dictionary of key:value pairs. Create a list of dictionaries:
passports = contents.split('\n\n')
passports = [item.replace('\n', ' ') for item in passports]

passport_dicts = []
for i in range(len(passports)):
    d = dict(x.split(":") for x in passports[i].split(' '))
    passport_dicts.append(d)


# Loop through each passport and update count of valid passports:
valid = 0
for i in range(len(passport_dicts)):
    count = 0
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eye_colour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    hcl_allowed = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    if all([val in passport_dicts[i] for val in fields]):
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        if int(passport_dicts[i]['byr']) >= 1920 and int(passport_dicts[i]['byr']) <= 2002:
            count += 1

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        if int(passport_dicts[i]['iyr']) >= 2010 and int(passport_dicts[i]['iyr']) <= 2020:
            count += 1

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        if int(passport_dicts[i]['eyr']) >= 2020 and int(passport_dicts[i]['eyr']) <= 2030:
            count += 1

        # hgt (Height) - a number followed by either cm or in:
        # If cm, the number must be at least 150 and at most 193.
        if passport_dicts[i]['hgt'][-2:] == 'cm' and int(passport_dicts[i]['hgt'][:-2]) >= 150 and int(passport_dicts[i]['hgt'][:-2]) <= 193:
            count += 1
        # If in, the number must be at least 59 and at most 76.
        if passport_dicts[i]['hgt'][-2:] == 'in' and int(passport_dicts[i]['hgt'][:-2]) >= 59 and int(passport_dicts[i]['hgt'][:-2]) <= 76:
            count += 1

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        if passport_dicts[i]['hcl'][0] == '#' and len(passport_dicts[i]['hcl']) == 7 and (all([i for i in passport_dicts[i]['hcl'][1:]])):
            count += 1
        
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        if passport_dicts[i]['ecl'] in eye_colour:
            count += 1
        
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        if len(passport_dicts[i]['pid']) == 9 and passport_dicts[i]['pid'].isnumeric():
            count += 1

        # Update valid passports if it meets all 7 requirements:
        if count == 7:
            valid += 1
        
print('Number of valid passports: ' + str(valid))