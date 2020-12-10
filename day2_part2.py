# Import pandas library:
import pandas as pd

# Create dataframe with input file:
passwordDf = pd.read_csv('day2_1_input.csv', sep=' ', header=None, engine="python")

# Format the dataframe to contain four columns:
passwordDf[['int1', 'int2']] = passwordDf[0].str.split('-', expand=True)
passwordDf[['letter', 'colon']] = passwordDf[1].str.split(':', expand=True)
passwordDf.rename(columns = {2: 'Password'}, inplace = True)
passwordDf = passwordDf.drop(columns=[0,1,'colon'])

# Counter for valid passwords:
valid = 0

# Iterate through dataframe rows:
for row in passwordDf.itertuples():
    count = 0
    # Add to count if first position contains letter:
    if (row.Password[(int(row.int1)) -1]) == row.letter:
        count += 1
    # Add to count if second position contains letter:
    if (row.Password[(int(row.int2)) -1]) == row.letter:
        count += 1
    # Update valid passwords if exactly one of the positions contains letter:
    if count == 1:
        valid += 1

print(valid)