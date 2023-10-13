import pandas as pd

# Read the data from the provided sheet
data = pd.read_csv("C:\\Users\\thema\\OneDrive\\Desktop\\Folder\\3179\\data\\Unique Athletes.csv")

# Pivot the DataFrame to have "Team" as columns and "NOC" as rows
pivot_df = pd.pivot_table(data, values='ID', index='NOC', columns='Team', aggfunc='count', fill_value=0)

# Calculate the total number of athletes for each NOC
total_athletes_by_noc = pivot_df.sum(axis=1)

data['Team'] = data['Team'].str.replace(r'[^a-zA-Z\s]', '')

unq = pd.DataFrame(data['Team'].unique())

unq.to_csv("countries.csv")



# Calculate the percentage of athletes representing each country
percentage_representing_country = pivot_df.div(total_athletes_by_noc, axis=0) * 100

# Calculate the percentage of athletes from one country to another (e.g., USA to Spain)
percentage_from_one_country_to_another = (pivot_df / total_athletes_by_noc).T * 100

# Print the resulting DataFrame with percentages
# percentage_representing_country.to_csv("Comparison.csv", index=True)