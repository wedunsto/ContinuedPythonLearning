import pandas as pd

test = dict()
value = []
color = []
df = pd.DataFrame()

test["1"] = [1,2,3,4,5,6]
test["2"] = [7,8,9,10,11,12]
for keys in test.keys():
    for val in test[keys]:
        value.append(val)
        color.append(keys)
df["Value"] = value
df["Color"] = color

df.to_csv("practicedictionary.csv")

print(df.columns)

#columns = ["Red","Green","Blue"]
#df = pd.DataFrame([[1,2,3],[4,5,6]],columns = columns)
#print(df,"\n\n")

#df['Yellow'] = [2,1]

#df.to_csv("testdf.csv")

#df = pd.DataFrame()
#df["Red"] = [1,2,3,4,5]
#df["Blue"] = []
#+print(df)