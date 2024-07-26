import pandas as pd
#Task 2 a)
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
df = pd.read_csv(url)
print('Task 2 b)')

df_filtered = df.loc[:, ['Team', 'Yellow Cards', 'Red Cards']]
print(df_filtered)
print('Task 2 c)')


teams_participated_mask = df.loc[:, 'Team'].notna()
print(f"Команди на Євро 2012:\n{teams_participated_mask}")
num_teams = df.loc[:, 'Team'].nunique()
print(f"Кількість команд на Євро 2012: {num_teams}")
print('Task 2 d)')

teams_more_than_6_goals_mask = df.loc[:, 'Goals'] > 6
print(teams_more_than_6_goals_mask)