import pandas as pd

df = pd.read_csv("C:\\Users\\thema\\OneDrive\\Desktop\\Folder\\3179\\data\\athlete_events.csv")

players_count = df.groupby(['Year', 'Season', 'Games', 'City']).size().reset_index(name='Player_Count')

winter_olympics = players_count[players_count['Season'] == 'Winter']
summer_olympics = players_count[players_count['Season'] == 'Summer']

# Calculate the number of repeats of cities hosting the Olympics
city_counts = players_count.groupby('City').size().reset_index(name='City_Repeats')

# Merge the city counts back to the original DataFrame
players_count = pd.merge(players_count, city_counts, on='City', how='left')

players_count.to_csv("Cities.csv", index = True)

# winter_olympics.to_csv("Winter Olympics sport.csv", index=True)
# summer_olympics.to_csv("Summer Olympics sport.csv", index=True)
