import pandas as pd

freq = ''
range1 = [i for i in range(1,9)]

df = pd.read_csv('input06.csv', header=None, usecols=range1)

for col in df:
    freq += df[col].value_counts().idxmax()

print(freq)

# part two!
freq = ''

for col in df:
    freq += df[col].value_counts().idxmin()

print(freq)
