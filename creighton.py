import pandas as pd
import gspread

#from gspread_dataframe import get_as_dataframe, set_with_dataframe

#gc = gspread.service_account(filename='/Users/joshbucy/Desktop/creighton/service_account.json')

#sh = gc.open("Creighton Basketball Rankings")

teamname = pd.read_html('https://www.espn.com/mens-college-basketball/bpi')[0]
stats = pd.read_html('https://www.espn.com/mens-college-basketball/bpi')[1]
TTeam = pd.read_html('https://www.espn.com/mens-college-basketball/bpi/_/view/tournament')[0]
TStats = pd.read_html('https://www.espn.com/mens-college-basketball/bpi/_/view/tournament')[1]
NET = pd.read_html('https://www.ncaa.com/rankings/basketball-men/d1/ncaa-mens-basketball-net-rankings')[0]

frames = [teamname, stats]
join = pd.concat([teamname, stats], axis=1, join='outer')

frames = [TTeam, TStats]
join2 = pd.concat([TTeam, TStats], axis=1, join='outer')

locateCreighton = join[join['Team'].str.contains('Creighton')]
locateCreighton2 = join2[join2['Team'].str.contains('Creighton')]
locateCreighton3 = NET[NET['School'].str.contains('Creighton')]

#locateCreighton.dropna(inplace=True)

#join3 = pd.concat(
#    objs=(locateCreighton, locateCreighton2, locateCreighton3),
#    axis=1, 
#    join='outer'
#).reset_index()

result_df = pd.concat([locateCreighton.reset_index(drop=True), locateCreighton2.reset_index(drop=True), locateCreighton3.reset_index(drop=True)], axis=1)

#join3 = join3.astype(str)

#join3 = pd.concat([locateCreighton, locateCreighton2, locateCreighton3], axis=1, join='outer')

'''join3.set_axis(['Team1', 'Conference',
'Current Record', 'BPI', 'BPI Rank', 'BPI Trend',
'BPI Offense', 'BPI Defense', 'Projected Record',
'Projected Conference Record', 'Win Conference?',
'Remaining SOS', 'Team2', 'Conference2', 'Average Seed',
'Bracket Region', 'Title Win%', 'Championship Game',
'Final 4%', 'Elite 8%', 'Sweet 16%', 'Round of 32%'], axis='columns', inplace=True)'''

#locateCreighton = join3[join3['Team'].str.contains('Creighton')]

#print(locateCreighton)
#print(join3.dtypes)

print(result_df)

#result_df.to_csv('test.csv')
result_df.to_excel('/Users/joshbucy/Library/CloudStorage/OneDrive-Personal/Documents/2023/Creighton Stats/test.xlsx')
#print(sh.sheet1.get('A1'))
#worksheet = sh.get_worksheet(0)
#worksheet.update([result_df.columns.values.tolist()] + result_df.values.tolist())

#worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())