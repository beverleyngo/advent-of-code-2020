# Import each row of puzzle input into list:
rows = []
f=open('day3_input.txt',"r")
for line in f:
    rows.append(line.strip('\n'))

# Find the length of the list:
length = len(rows)

# Counter for number of trees encountered:
trees = 0

# Loop throw each row and find if it lands on a tree for that row:
for i in range(1,length):
    space =rows[i][(i*3)%31]
    if space == '#':
        trees += 1

print(trees)