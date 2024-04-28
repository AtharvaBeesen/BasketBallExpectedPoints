
from nba_api.stats.endpoints import shotchartdetail
import json
import requests
import pandas as pd
df = pd.DataFrame()
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2000-01',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df1 = pd.DataFrame(rows)
df1.columns = headers
df1['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2001-02',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df2 = pd.DataFrame(rows)
df2.columns = headers
df2['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2002-03',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df3 = pd.DataFrame(rows)
df3.columns = headers
df3['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2003-04',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df4 = pd.DataFrame(rows)
df4.columns = headers
df4['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2004-05',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df5 = pd.DataFrame(rows)
df5.columns = headers
df5['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2005-06',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df6 = pd.DataFrame(rows)
df6.columns = headers
df6['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2006-07',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df7 = pd.DataFrame(rows)
df7.columns = headers
df7['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2007-08',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df8 = pd.DataFrame(rows)
df8.columns = headers
df8['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2008-09',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df9 = pd.DataFrame(rows)
df9.columns = headers
df9['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2009-10',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df10 = pd.DataFrame(rows)
df10.columns = headers
df10['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2010-11',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df11 = pd.DataFrame(rows)
df11.columns = headers
df11['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2011-12',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df12 = pd.DataFrame(rows)
df12.columns = headers
df12['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2012-13',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df13 = pd.DataFrame(rows)
df13.columns = headers
df13['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2013-14',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df14 = pd.DataFrame(rows)
df14.columns = headers
df14['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2014-15',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df15 = pd.DataFrame(rows)
df15.columns = headers
df15['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2015-16',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df16 = pd.DataFrame(rows)
df16.columns = headers
df16['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2016-17',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df17 = pd.DataFrame(rows)
df17.columns = headers
df17['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2017-18',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df18 = pd.DataFrame(rows)
df18.columns = headers
df18['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2018-19',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df19 = pd.DataFrame(rows)
df19.columns = headers
df19['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2019-20',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df20 = pd.DataFrame(rows)
df20.columns = headers
df20['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2020-21',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df21 = pd.DataFrame(rows)
df21.columns = headers
df21['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2021-22',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df22 = pd.DataFrame(rows)
df22.columns = headers
df22['SEASON_TYPE']='Regular'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2022-23',
    season_type_all_star = ['Regular Season', 'Playoffs'],
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
df23 = pd.DataFrame(rows)
df23.columns = headers
df23['SEASON_TYPE']='Regular'
###
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2000-01',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfa = pd.DataFrame(rows)
dfa.columns = headers
dfa['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2001-02',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfb = pd.DataFrame(rows)
dfb.columns = headers
dfb['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2002-03',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfc = pd.DataFrame(rows)
dfc.columns = headers
dfc['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2003-04',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfd = pd.DataFrame(rows)
dfd.columns = headers
dfd['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2004-05',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfe = pd.DataFrame(rows)
dfe.columns = headers
dfe['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2005-06',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dff = pd.DataFrame(rows)
dff.columns = headers
dff['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2006-07',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfg = pd.DataFrame(rows)
dfg.columns = headers
dfg['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2007-08',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfh = pd.DataFrame(rows)
dfh.columns = headers
dfh['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2008-09',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfi = pd.DataFrame(rows)
dfi.columns = headers
dfi['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2009-10',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfj = pd.DataFrame(rows)
dfj.columns = headers
dfj['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2010-11',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfk = pd.DataFrame(rows)
dfk.columns = headers
dfk['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2011-12',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfl = pd.DataFrame(rows)
dfl.columns = headers
dfl['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2012-13',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfm = pd.DataFrame(rows)
dfm.columns = headers
dfm['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2013-14',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfn = pd.DataFrame(rows)
dfn.columns = headers
dfn['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2014-15',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfo = pd.DataFrame(rows)
dfo.columns = headers
dfo['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2015-16',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfp = pd.DataFrame(rows)
dfp.columns = headers
dfp['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2016-17',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfq = pd.DataFrame(rows)
dfq.columns = headers
dfq['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2017-18',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfr = pd.DataFrame(rows)
dfr.columns = headers
dfr['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2018-19',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfs = pd.DataFrame(rows)
dfs.columns = headers
dfs['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2019-20',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dft = pd.DataFrame(rows)
dft.columns = headers
dft['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2020-21',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfu = pd.DataFrame(rows)
dfu.columns = headers
dfu['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2021-22',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfv = pd.DataFrame(rows)
dfv.columns = headers
dfv['SEASON_TYPE']='Playoffs'
response = shotchartdetail.ShotChartDetail(
    team_id = 0,
    player_id = 0,
    season_nullable = '2022-23',
    season_type_all_star = 'Playoffs',
    context_measure_simple = 'FGA'
)
content = json.loads(response.get_json())
# convert contents into dataframe
results = content['resultSets'][0]
headers = results['headers']
rows = results['rowSet']
dfw = pd.DataFrame(rows)
dfw.columns = headers
dfw['SEASON_TYPE']='Playoffs'
dfw
df = df1.append(dfa.append(df2.append(dfb).append(df3.append(dfc.append(df4.append(dfd.append(df5.append(dfe.append(df6.append(dff.append(df7.append(dfg.append(df8.append(dfh.append(df9.append(dfi.append(df10.append(dfj.append(df11.append(dfk.append(df12.append(dfl.append(df13.append(dfm.append(df14.append(dfn.append(df15.append(dfo.append(df16.append(dfp.append(df17.append(dfq.append(df18.append(dfr.append(df19.append(dfs.append(df20.append(dft.append(df21.append(dfu.append(df22.append(dfv.append(df23.append(dfw))))))))))))))))))))))))))))))))))))))))))))



