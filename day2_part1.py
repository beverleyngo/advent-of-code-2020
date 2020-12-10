import pandas as pd

#my_cols = ['int1', 'int2', 'letter', 'password']
passwordDf = pd.read_csv('day2_1_input.csv', sep=' ', header=None, engine="python")

passwordDf[['int1', 'int2']] = passwordDf[0].str.split('-', expand=True)
passwordDf[['letter', 'colon']] = passwordDf[1].str.split(':', expand=True)
passwordDf.rename(columns = {2: 'Password'}, inplace = True)
passwordDf = passwordDf.drop(columns=[0,1,'colon'])

valid = 0
for row in passwordDf.itertuples():
    occurences = row.Password.count(row.letter)
    if occurences >= int(row.int1) and occurences <= int(row.int2):
        valid += 1

print(valid)