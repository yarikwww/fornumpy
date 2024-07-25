
import pandas as pd
from io import StringIO
#task 2 a)
print('Task 2 a)')
data = """
Team,Goals,Shots on target,Shots off target,Shooting Accuracy,% Goals-to-shots,Total shots (inc. Blocked),Hit Woodwork,Penalty goals,Penalties not scored,Headed goals,Passes,Passes completed,Passing Accuracy,Touches,Crosses,Dribbles,Corners Taken,Tackles,Clearances,Interceptions,Clearances off line,Clean Sheets,Blocks,Goals conceded,Saves made,Saves-to-shots ratio,Fouls Won,Fouls Conceded,Offsides,Yellow Cards,Red Cards,Subs on,Subs off,Players Used
Croatia,4,13,12,51.9%,16.0%,32,0,0,0,2,1076,828,76.9%,1706,60,42,14,49,83,56,,0,10,3,13,81.3%,41,62,2,9,0,9,9,16
Czech Republic,4,13,18,41.9%,12.9%,39,0,0,0,0,1565,1223,78.1%,2358,46,68,21,62,98,37,2,1,10,6,9,60.1%,53,73,8,7,0,11,11,19
Denmark,4,10,10,50.0%,20.0%,27,1,0,0,3,1298,1082,83.3%,1873,43,32,16,40,61,59,0,1,10,5,10,66.7%,25,38,8,4,0,7,7,15
England,5,11,18,50.0%,17.2%,40,0,0,0,3,1488,1200,80.6%,2440,58,60,16,86,106,72,1,2,29,3,22,88.1%,43,45,6,5,0,11,11,16
France,3,22,24,37.9%,6.5%,65,1,0,0,0,2066,1803,87.2%,2909,55,76,28,71,76,58,0,1,7,5,6,54.6%,36,51,5,6,0,11,11,19
Germany,10,32,32,47.8%,15.6%,80,2,1,0,2,2774,2427,87.4%,3761,101,60,35,91,73,69,0,1,11,6,10,62.6%,63,49,12,4,0,15,15,17
Greece,5,8,18,30.7%,19.2%,32,1,1,1,0,1187,911,76.7%,2016,52,53,10,65,123,87,0,1,23,7,13,65.1%,67,48,12,9,1,12,12,20
Italy,6,34,45,43.0%,7.5%,110,2,0,0,2,3016,2531,83.9%,4363,75,75,30,98,137,136,1,2,18,7,20,74.1%,101,89,16,16,0,18,18,19
Netherlands,2,12,36,25.0%,4.1%,60,2,0,0,0,1556,1381,88.7%,2163,50,49,22,34,41,41,0,0,9,5,12,70.6%,35,30,3,5,0,7,7,15
Poland,2,15,23,39.4%,5.2%,48,0,0,0,1,1059,852,80.4%,1724,55,39,14,67,87,62,0,0,8,3,6,66.7%,48,56,3,7,1,7,7,17
Portugal,6,22,42,34.3%,9.3%,82,6,0,0,2,1891,1461,77.2%,2958,91,64,41,78,92,86,0,2,11,4,10,71.5%,73,90,10,12,0,14,14,16
Republic of Ireland,1,7,12,36.8%,5.2%,28,0,0,0,1,851,606,71.2%,1433,43,18,8,45,78,43,1,0,23,9,17,65.4%,43,51,11,6,1,10,10,17
Russia,5,9,31,22.5%,12.5%,59,2,0,0,1,1602,1345,83.9%,2278,40,40,21,65,74,58,0,0,8,3,10,77.0%,34,43,4,6,0,7,7,16
Spain,12,42,33,55.9%,16.0%,100,0,1,0,2,4317,3820,88.4%,5585,69,106,44,122,102,79,0,5,8,1,15,93.8%,102,83,19,11,0,17,17,18
Sweden,5,17,19,47.2%,13.8%,39,3,0,0,1,1192,965,80.9%,1806,44,29,7,56,54,45,0,1,12,5,8,61.6%,35,51,7,7,0,9,9,18
Ukraine,2,7,26,21.2%,6.0%,38,0,0,0,2,1276,1043,81.7%,1894,33,26,18,65,97,29,0,0,4,4,13,76.5%,48,31,4,5,0,9,9,18
"""

df = pd.read_csv(StringIO(data))
print(df)


print('Task 2 b)')

#task 2 b)
selected_columns = df[['Team', 'Yellow Cards', 'Red Cards']]
print(selected_columns)

#task 2 c)
print('Task 2 c)')
num_teams = df['Team'].nunique()
print(f"The number of teams that participated in Euro 2012 is: {num_teams}")

#task 2 d)
print('Task 2 d)')
teams_scored_more_than_6 = df[df['Goals'] > 6]
print(teams_scored_more_than_6[['Team', 'Goals']])

