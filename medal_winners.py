import pandas as pd

df = pd.read_csv("C:\\Users\\thema\\OneDrive\\Desktop\\Folder\\3179\\data\\athlete_events.csv")

df = pd.DataFrame(df)

df.dropna(subset = ['Medal', 'Sport', 'Height', 'Age'], inplace = True)

df = df.drop_duplicates(subset="ID", keep="first")

print(pd.to_numeric(df['Age'], errors='coerce').isnull().sum())

#df.to_csv("Medal Winners.csv", index=False)