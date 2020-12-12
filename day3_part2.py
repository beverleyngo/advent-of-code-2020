# Import each row of puzzle input into list:
rows = []
f=open('day3_input.txt',"r")
for line in f:
    rows.append(line.strip('\n'))

# Find the length of the list:
length = len(rows)

# Counters for number of trees encountered:
trees_a = 0
trees_b = 0
trees_c = 0
trees_d = 0
trees_e = 0

# Loop through first four conditions:
for i in range(1,length):
    space_a = rows[i][(i*1)%31]
    space_b = rows[i][(i*3)%31]
    space_c = rows[i][(i*5)%31]
    space_d = rows[i][(i*7)%31]
    if space_a == '#':
        trees_a += 1
    if space_b == '#':
        trees_b += 1
    if space_c == '#':
        trees_c += 1
    if space_d == '#':
        trees_d += 1

# Loop through final condition:
for i in range(0, length, 2):
    space_e =rows[i][int((i*0.5)%31)]
    if space_e == '#':
        trees_e += 1

# Find total:
print(trees_a * trees_b * trees_c * trees_d * trees_e)