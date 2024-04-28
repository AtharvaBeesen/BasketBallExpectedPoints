df = df.reset_index(drop=True)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import model_selection
from sklearn.model_selection import train_test_split

df2 = df[['PERIOD','MINUTES_REMAINING','SECONDS_REMAINING','ACTION_TYPE','SHOT_TYPE','SHOT_ZONE_AREA','LOC_X','LOC_Y','SHOT_DISTANCE','SEASON_TYPE','SHOT_MADE_FLAG']]

df2["SECONDS_REMAINING"] = df2["MINUTES_REMAINING"]*60 + df["SECONDS_REMAINING"]

df4 = df2[['PERIOD','SECONDS_REMAINING','ACTION_TYPE','SHOT_TYPE','SHOT_ZONE_AREA','SHOT_DISTANCE','SEASON_TYPE','SHOT_MADE_FLAG']]

df5 = df4.rename(columns={"ACTION_TYPE": "Shot_Action", "SHOT_TYPE": "Shot_Type", "SHOT_DISTANCE" : "Shot_Distance", "SEASON_TYPE":"Season_Type", "PERIOD":"Period","SECONDS_REMAINING":"Seconds_Remaining","SHOT_ZONE_AREA" : "Shot_Zone_Area", "SHOT_MADE_FLAG":"Output"})

df6 = df5.replace("Right Side(R)","Side")
df6 = df6.replace("Left Side(L)","Side")
df6 = df6.replace("Right Side Center(RC)","SideCenter")
df6 = df6.replace("Left Side Center(LC)","SideCenter")
df6 = df6.replace("Center(C)","Center")
df6 = df6.replace("Back Court(BC)","BackCourt")

from sklearn.preprocessing import OneHotEncoder

df6

#https://medium.com/analytics-vidhya/how-to-handle-categorical-features-ab65c3cf498e#:~:text=1)%20Using%20the%20categorical%20variable,category%20with%20a%20probability%20ratio.

#creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')
#one-hot-encoding on shot type
shot_type_df = pd.DataFrame(encoder.fit_transform(df6[['Shot_Type']]).toarray())

#one-hot-encoding on season type
season_type_df = pd.DataFrame(encoder.fit_transform(df6[['Season_Type']]).toarray())

#one-hot-encoding on season type
shot_zone_df = pd.DataFrame(encoder.fit_transform(df6[['Shot_Zone_Area']]).toarray())

shot_type_df.columns = ["2pt","3pt"]
season_type_df.columns = ["Playoffs","Regular"]
shot_zone_df.columns = ["BackCourt", "Center", "Side", "SideCenter"]

df7 = df6.join(shot_type_df)
df7 = df7.join(season_type_df)
df7 = df7.join(shot_zone_df)

df7

df7.drop("Shot_Type", axis=1, inplace=True)
df7.drop("Season_Type", axis=1, inplace=True)
df7.drop("Shot_Zone_Area", axis =1, inplace=True)

df_freq = df7.copy()
df_prob = df7.copy()

#testing multiple ways to handle categorical feature & nominal variable Shot_Action

#count/frequency encoding
country_map = df_freq['Shot_Action'].value_counts().to_dict()
#df_freq['Shot_Action']=df_freq['Shot_Action'].map(country_map)
#df_freq = df_freq

#probability ratio encoding
prob=df_prob.groupby(['Shot_Action'])['Output'].mean()
prob_df=pd.DataFrame(prob)
prob_df['Miss']=1-prob_df['Output']
prob_df['Probability Ratio']=prob_df['Output']/prob_df['Miss']
prob_encod_dictionary=prob_df['Probability Ratio'].to_dict()
df_prob['Shot_Action']=df_prob['Shot_Action'].map(prob_encod_dictionary)

feature_cols = ['Shot_Action','Shot_Distance','Seconds_Remaining','Period','2pt','3pt','Regular','Playoffs','BackCourt','Center','Side','SideCenter']
X = df_prob[feature_cols];
y = df_prob.Output;
indices = df_prob.index.values

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X_train, X_test,indices_train,indices_test = train_test_split(X,indices, test_size=0.33, random_state=42)

y_train, y_test = y[indices_train],  y[indices_test]

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression(random_state=42, max_iter=100000)

clf.fit(X_train, y_train)

prediction_of_probability = clf.predict_proba(X_test)

df_prob_new = df_prob.copy()

df_prob_new.loc[indices_test,'pred'] = prediction_of_probability[:,1]
df_prob_new.loc[indices_train,'pred'] = clf.predict_proba(X_train)[:,1]

y_pred_test = clf.predict(X_test)


from sklearn.metrics import accuracy_score
accuracy_score(y_test,y_pred_test)

df_prob_new['3pt'] = df_prob_new['3pt'] * 3
df_prob_new['2pt'] = df_prob_new['2pt'] * 2

df_prob_new['outputTrue'] = df_prob_new['Output'] * (df_prob_new['3pt'] + df_prob_new['2pt'])
df_prob_new['predTrue'] = df_prob_new['pred'] * (df_prob_new['3pt'] + df_prob_new['2pt'])

df0 = df_prob_new.sum(axis=0)
print(df0)

(df0.outputTrue/df0.predTrue)*100-100

extracted = df_prob_new[['outputTrue','predTrue']]
df = df.join(extracted)

dfTest = df.loc[df['PLAYER_NAME'] == 'Kevin Durant']
dfTest2 = dfTest.sum(axis=0)
((dfTest2.outputTrue/dfTest2.predTrue)-1)*100

df.tail(30)

df.to_csv('dfWithExpectedPtsModel2USINGAPI.csv', index = False)