import pandas as pd

df = pd.read_csv("C:\\Users\\thema\\OneDrive\\Desktop\\Folder\\3179\\data\\Unique Athletes.csv")

df = df.groupby(['Year', 'Season', 'Sex']).size().reset_index(name='Count')

df = df.drop(df.index[0])

df_pivot = df.pivot_table(index=['Year', 'Season'], columns='Sex', values='Count').reset_index()

df_pivot['MaleRatio'] = df_pivot['M'] / (df_pivot['M'] + df_pivot['F'])
df_pivot['FemaleRatio'] = df_pivot['F'] / (df_pivot['M'] + df_pivot['F'])

summer_df = df_pivot[df_pivot['Season'] == 'Summer']
winter_df = df_pivot[df_pivot['Season'] == 'Winter']

summer_df.to_csv("Summer Ratio.csv", index = True)
winter_df.to_csv("Winter Ratio.csv", index = True)