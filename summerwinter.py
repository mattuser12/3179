import pandas as pd

df = pd.read_csv("C:\\Users\\thema\\OneDrive\\Desktop\\Folder\\3179\\data\\athlete_events.csv")

players_count = df.groupby(['Season', 'Sport']).size().reset_index(name='Player_Count')

winter_olympics = players_count[players_count['Season'] == 'Winter']
summer_olympics = players_count[players_count['Season'] == 'Summer']

print(winter_olympics.nlargest(10, 'Player_Count')[['Sport', 'Player_Count']])

# winter_olympics.to_csv("Winter Olympics sport.csv", index = True)
# summer_olympics.to_csv("Summer Olympics sport.csv", index = True)