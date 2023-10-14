import pandas as pd

data = pd.read_csv("C:\\Users\\thema\\OneDrive\\Desktop\\Folder\\3179\\data\\Unique Athletes.csv")

df = pd.DataFrame(data)

df = df[~df['Season'].str.contains('Winter')]

df = df.dropna(subset = ["Medal"])

medals = df.groupby(['Year', 'NOC'])['Medal'].count()

medals.to_csv("Medal Count Each Year.csv", index=True)