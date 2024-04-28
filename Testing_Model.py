import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.model_selection import train_test_split

df = pd.read_csv("dfWithExpectedPtsModel2USINGAPI.csv")

df

dfTest = df.loc[df['PLAYER_NAME'] == 'Udonis Haslem']
dfTest2 = dfTest.sum(axis=0)
((dfTest2.outputTrue/dfTest2.predTrue)-1)*100

df2 = df[['PLAYER_NAME','GAME_ID','TEAM_NAME','outputTrue','predTrue','GAME_DATE']]
df2 = df2.rename(columns={'PLAYER_NAME':'Player_Name','GAME_ID':'Game_ID','TEAM_NAME':'Team_Name','GAME_DATE':'Game_Date'})

df2for2223 = df2[df2['Game_Date']>20221000]

df3 = df2for2223.groupby(['Player_Name','Game_ID'])[['outputTrue','predTrue']].sum()

dfK = df3.groupby('Player_Name').count()
dfK2 = dfK[dfK['outputTrue']>10]
dfK2 = dfK2.reset_index()

dfK2 = dfK2.drop('predTrue', axis = 1)
dfK2 = dfK2.drop('outputTrue', axis = 1)
dfK3 = dfK2['Player_Name'].to_numpy()

df3 = df3.reset_index()

df3a = df3.loc[df3['Player_Name'].isin(dfK3)]
df3b = df3a.set_index('Player_Name')

df4 = df3b.groupby(["Player_Name"])[['outputTrue','predTrue']].mean()

df5 = df4[df4["outputTrue"] > 10]

df5["xPtsPerformance"] = ((df5["outputTrue"]/df5["predTrue"])-1)*100

dfTop = df5.sort_values(by="xPtsPerformance", ascending = False)
dfBottom = df5.sort_values(by="xPtsPerformance")

dfTop.head(20)[["xPtsPerformance","outputTrue","predTrue"]]

dfBottom.head(20)[["xPtsPerformance","outputTrue","predTrue"]]

Player = "LaMelo Ball"
dfTop2 = dfTop.reset_index()
dfTop2[dfTop2['Player_Name']==Player]["xPtsPerformance"].item()

dfTopExpPts = df5.sort_values(by="predTrue", ascending = False)
dfTopExpPts.head(30)[["xPtsPerformance","outputTrue","predTrue"]]

dfTopPts = df5.sort_values(by="outputTrue", ascending = False)
dfTopPts.head(20)[["xPtsPerformance","outputTrue","predTrue"]]

dfNetTop = df5.copy()
dfNetTop["PtsAdded/Game"] = dfNetTop["outputTrue"] - dfNetTop["predTrue"]
dfNetTop = dfNetTop.sort_values(by="PtsAdded/Game", ascending = False)
dfNetTop.head(20)[["xPtsPerformance","outputTrue","predTrue","PtsAdded/Game"]]

dfNetTop = df5.copy()
dfNetTop["PtsAdded/Game"] = dfNetTop["outputTrue"] - dfNetTop["predTrue"]
dfNetTop = dfNetTop.sort_values(by="PtsAdded/Game", ascending = True)
dfNetTop.head(20)[["xPtsPerformance","outputTrue","predTrue","PtsAdded/Game"]]

dfGame1 = df2[df2['Game_ID']== 42200401]
dfGame1StatsTeam = dfGame1.groupby(["Team_Name"])[['outputTrue','predTrue']].sum()
dfGame1StatsTeam

dfGame2 = df2[df2['Game_ID']== 42200402]
dfGame2StatsTeam = dfGame2.groupby(["Team_Name"])[['outputTrue','predTrue']].sum()
dfGame2StatsTeam

dfGame3 = df2[df2['Game_ID']== 42200403]
dfGame3StatsTeam = dfGame3.groupby(["Team_Name"])[['outputTrue','predTrue']].sum()
dfGame3StatsTeam

dfGame4 = df2[df2['Game_ID']== 42200404]
dfGame4StatsTeam = dfGame4.groupby(["Team_Name"])[['outputTrue','predTrue']].sum()
dfGame4StatsTeam

# NBA LG Avg FT% Since 2000-01 is 76.0%