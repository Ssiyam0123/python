import pandas as pd
si  = pd.read_csv("data.csv")

# print(spinal_injury)
# print(spinal_injury.head(10))

ages = pd.Series(si['Age'])

# print(ages)

# print(si.loc[si['Age']==32])

print(si.shape)


