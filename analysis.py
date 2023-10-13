import pandas as pd


data = pd.read_csv("C:\\Users\\thema\\OneDrive\\Desktop\\Folder\\3179\\data\\athlete_events.csv")

df = pd.DataFrame(data)

df = df.dropna(subset=["Team", "NOC"])

unique_rows = df.drop_duplicates(subset="ID", keep="first")

unique_rows.to_csv("Unique Athletes.csv", index = False)