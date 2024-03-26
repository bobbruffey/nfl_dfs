import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time
import warnings
warnings.filterwarnings('ignore')
from datetime import date
from datetime import datetime


def get_current_year():
    curr_date = date.today().isoformat()
    curr_year = 0
    if (curr_date >= '01/11/2024'):
        curr_year = 2024
    else:
        curr_year = 2023
    return curr_year


def get_current_week():
    curr_date = date.today().isoformat()
    curr_week = 0
    if (curr_date < '09/07/2023'):
        curr_week = 0
    elif ((curr_date >= '09/07/2023') &
         (curr_date <= '09/12/2023')):
        curr_week = 1
    elif ((curr_date >= '09/13/2023') &
         (curr_date <= '09/19/2023')):
        curr_week = 2
    elif ((curr_date >= '09/20/2023') &
         (curr_date <= '09/26/2023')):
        curr_week = 3
    elif ((curr_date >= '09/27/2023') &
         (curr_date <= '10/03/2023')):
        curr_week = 4
    elif ((curr_date >= '10/04/2023') &
         (curr_date <= '10/10/2023')):
        curr_week = 5
    elif ((curr_date >= '10/11/2023') &
         (curr_date <= '10/17/2023')):
        curr_week = 6
    elif ((curr_date >= '10/18/2023') &
         (curr_date <= '10/24/2023')):
        curr_week = 7
    elif ((curr_date >= '10/25/2023') &
         (curr_date <= '10/31/2023')):
        curr_week = 8
    elif ((curr_date >= '11/01/2023') &
         (curr_date <= '11/07/2023')):
        curr_week = 9
    elif ((curr_date >= '11/08/2023') &
         (curr_date <= '11/14/2023')):
        curr_week = 10
    elif ((curr_date >= '11/15/2023') &
         (curr_date <= '11/21/2023')):
        curr_week = 11
    elif ((curr_date >= '11/22/2023') &
         (curr_date <= '11/28/2023')):
        curr_week = 12
    elif ((curr_date >= '11/29/2023') &
         (curr_date <= '12/05/2023')):
        curr_week = 13
    elif ((curr_date >= '12/06/2023') &
         (curr_date <= '12/12/2023')):
        curr_week = 14
    elif ((curr_date >= '12/13/2023') &
         (curr_date <= '12/19/2023')):
        curr_week = 15
    elif ((curr_date >= '12/20/2023') &
         (curr_date <= '12/26/2023')):
        curr_week = 16
    elif ((curr_date >= '12/27/2023') &
         (curr_date <= '01/02/2024')):
        curr_week = 17
    elif ((curr_date >= '01/03/2024') &
         (curr_date <= '01/10/2024')) :
        curr_week = 18
    else:
        curr_week = 1 #if date is after week 18, then will be week 1 of next season, until sched comes out
    return curr_week
    

def update_player_weekly_stats():
    
    urls = ['https://www.pro-football-reference.com/players/A/',
       'https://www.pro-football-reference.com/players/B/',
       'https://www.pro-football-reference.com/players/C/',
       'https://www.pro-football-reference.com/players/D/',
       'https://www.pro-football-reference.com/players/E/',
       'https://www.pro-football-reference.com/players/F/',
       'https://www.pro-football-reference.com/players/G/',
       'https://www.pro-football-reference.com/players/H/',
       'https://www.pro-football-reference.com/players/I/',
       'https://www.pro-football-reference.com/players/J/',
       'https://www.pro-football-reference.com/players/K/',
       'https://www.pro-football-reference.com/players/L/',
       'https://www.pro-football-reference.com/players/M/',
       'https://www.pro-football-reference.com/players/N/',
       'https://www.pro-football-reference.com/players/O/',
       'https://www.pro-football-reference.com/players/P/',
       'https://www.pro-football-reference.com/players/Q/',
       'https://www.pro-football-reference.com/players/R/',
       'https://www.pro-football-reference.com/players/S/',
       'https://www.pro-football-reference.com/players/T/',
       'https://www.pro-football-reference.com/players/U/',
       'https://www.pro-football-reference.com/players/V/',
       'https://www.pro-football-reference.com/players/W/',
       'https://www.pro-football-reference.com/players/X/',
       'https://www.pro-football-reference.com/players/Y/',
       'https://www.pro-football-reference.com/players/Z/']
    
    
    l = []
    for i in range(len(urls)):
        time.sleep(5)

        url = urls[i]
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'lxml')
        tags = soup.find_all('p')
        tags = tags[:-12]
       # df_dropped_last_n = df.iloc[:-n]
       # tags = tags.astype(str)
        [l.append(x) for x in tags] 
       # l.append(tags)
    
    tags_df = pd.DataFrame(l, columns = ['Player','Position'])

    test = tags_df
    #test.head()
    test = pd.DataFrame(test)
    #test.columns
    test['colB'] = test['Player'].replace('[', '')
    
    
    test['Player'] = test['Player'].astype(str)
    test['Position'] = test['Position'].astype(str)
    #test.head()
    new = test['Player'].str.split('"', expand=True)
    
    
    new = new.drop(columns = [0])
    new[1] = new[1].str.replace('.htm',"")

    new['Gamelog'] = 'https://www.pro-football-reference.com' + new[1] + '/gamelog/'
    #new2 = new[2].str.split()
    new['Player'] = new[2].str.replace('</a>',"")
    new['Player'] = new['Player'].str.replace('</b>',"")
    new['Player'] = new['Player'].str.replace('>',"")

    new2 = new['Player'].str.split(' ', expand=True)
    
    pos_list = ['(WR)', '(LB)', '(RB)', '(DE)', '(S)', '(OT)', '(DB)', '(OLB)', '(OL)',
           '(QB)', '(P)', '(G)', '(CB)', '(DL)', '(FS)', '(K)', '(OG)',
           '(EDGE)', '(DT)', '(TE)', '(T)', '(NT)', '(FB)', '(SS)', '(LS)',
           '(ILB)', '(OG)', '(C)', '(DT)', '(DL)']

    new2['position'] = np.where(new2[2].isin(pos_list), new2[2], 
                           np.where(new2[3].isin(pos_list), new2[3], ""))
    new2['player'] = np.where(((~new2[3].isin(pos_list)) & (new2[3].notnull())), new2[0] + " " + new2[1] + " " + new2[2] + " " + new2[3],
                         np.where(((~new2[2].isin(pos_list)) & (new2[2].notnull())), new2[0] + " " + new2[1] + " " + new2[2],
                                 new2[0] + " " + new2[1]))
    
    
    new['Player'] = new2['player']
    
    test['Gamelog'] = new['Gamelog']
    test['Player'] = new['Player']
    test['Position_2'] = new2['position']
    
    pos = test['Position'].str.split(' ', expand=True)
    
    pos['position'] = np.where((pos[1].str.contains('19')) | (pos[1].str.contains('20')),"",
                           pos[1])

    pos['playing_period'] = np.where((pos[1].str.contains('19')) | (pos[1].str.contains('20')), pos[1],
                                pos[2])
    
    test['Position_1'] = pos['position']
    test['Playing_Prd'] = pos['playing_period']
    test['Position'] = np.where(test['Position_1'] != "", test['Position_1'],
                           test['Position_2'])
    test['Position'] = test['Position'].str[1:]
    test['Position'] = test['Position'].str[:-1]
    
    play_prd = test['Playing_Prd'].str.split('-', expand=True)
    
    test['Playing_Prd_Strt'] = play_prd[0]
    test['Playing_Prd_End'] = play_prd[1]
    
    players = test[['Gamelog', 'Player','Position',
                'Playing_Prd_Strt','Playing_Prd_End']]

    
    
    players['Playing_Prd_End'] = players['Playing_Prd_End'].astype(int)
    players['Playing_Prd_Strt'] = players['Playing_Prd_Strt'].astype(int)

    players_curr = players[players['Playing_Prd_End'] >= 2015]
    players_curr['Playing_Prd_Strt'] = np.where(players_curr['Playing_Prd_Strt'] <= 2015, 2015,
                                               players_curr['Playing_Prd_Strt'])
    
    players_curr = players_curr[players_curr['Position'] != 'TE-C']
    players_curr = players_curr[players_curr['Position'] != 'DE-C']

    players_curr['Position'] = players_curr['Position'].map({'SAF':'S','LT':'T','QB/TE':'TE','G,C':'G',
                                                        'WR-PR':'WR','RG':'G','RB-WR':'RB','FB-LB':'FB',
                                                        'LB-DE':'LB','RT':'T','DE-LB':'DE','DT-DE':'DT',
                                                        'NT-DE':'DT','C-G':'C','HB':'RB','LG':'G',
                                                        'T-G':'T','DE-DT':'DE','G-T':'G','G-C':'G',
                                                        'NT':'DT', 'EDGE':'DE', 'OG':'G',
                                                        'WR':'WR','LB':'LB','RB':'RB','DB':'DB','CB':'CB',
                                                        'DE':'DE','TE':'TE','DT':'DT','T':'T','QB':'QB',
                                                        'OLB':'OLB','G':'G','S':'S','C':'C','OT':'OT',
                                                        'DL':'DL','OL':'OL','K':'K','P':'P','ILB':'ILB',
                                                        'FS':'FS','SS':'SS','FB':'FB','LS':'LS'})
    
    
    players_curr = players_curr[players_curr['Playing_Prd_End']>=2015]
    
    #player clean up
    players_curr = players_curr.replace({'Player':{' III':'',
                                                   ' II':'',
                                                   ' Jr.':'',
                                                   'AJ Dillon':'A.J. Dillon',
                                                  "De'Von Achane":'Devon Achane',
                                                  'DJ Chark':'D.J. Chark',
                                                   'D.K. Metcalf':'DK Metcalf',
                                                   'Gabriel Davis':'Gabe Davis',
                                                   'JJ Arcega-Whiteside':'J.J. Arcega-Whiteside',
                                                   'KaVontae Turpin':'Kavontae Turpin',
                                                   'Matthew Slater':'Matt Slater',
                                                   
                                                  }},
                                       regex=True)
    players_curr.Player = players_curr.Player.str.replace(r'\(.*\)', '')
    players_curr['Player'] = players_curr['Player'].apply(lambda x: x.strip())
    
    players_curr.loc[players_curr.Player == 'Cordarrelle Patterson', 'Position'] = 'RB'
    players_curr.loc[players_curr.Player == 'Logan Thomas', 'Position'] = 'TE'
    players_curr.loc[players_curr.Player == 'Ty Montgomery', 'Position'] = 'RB'
    players_curr.loc[players_curr.Player == 'Jamal Agnew', 'Position'] = 'WR'
    players_curr.loc[players_curr.Player == 'Elijah Higgins', 'Position'] = 'TE'
    players_curr.loc[players_curr.Player == 'Juwan Johnson', 'Position'] = 'TE'
    players_curr.loc[players_curr.Player == 'Lawrence Cager', 'Position'] = 'TE'
    players_curr.loc[players_curr.Player == 'Taysom Hill', 'Position'] = 'TE'
    
    
    return players_curr
    

def get_nfl_sched():
    #this will need to be a file on s3 to pull from there
    #temp this goes to a local file
    nfl_sched = pd.read_csv('C:/Users/bobbr/OneDrive/Documents/The Plan/NFL/NFL Schedule.csv')
    return nfl_sched

#function to scrape/update defense weekly stats
def def_weekly_stats_scrape(first_yr, last_yr, nfl_sched):
    
    first_wk = 1
    num_years = last_yr - first_yr
    temp_df = pd.DataFrame()
    curr_yr = first_yr
    for i in range(0,num_years+1):
        if(curr_yr < 2021):
            weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
            year = [curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,
                   curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,
                   curr_yr,curr_yr,curr_yr,curr_yr,curr_yr]
        else:
            weeks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            year = [curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,
                   curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,curr_yr,
                   curr_yr,curr_yr,curr_yr,curr_yr,curr_yr, curr_yr]
        

        curr_yr = curr_yr+1
        
        temp2 = pd.DataFrame(data = {'week':weeks,
                            'year':year})
        
    
        temp_df = temp_df.append(temp2)
    
    temp_df['page'] = 'https://fftoday.com/stats/playerstats.php?Season=' + temp_df['year'].astype(str) + '&GameWeek=' + temp_df['week'].astype(str) + '&PosID=99&LeagueID=26955'
    temp_df['page'] = temp_df['page'].astype(str)
    temp_df = temp_df.reset_index()
    temp_df = temp_df.drop(columns = ['index'])
    df2 = pd.DataFrame()

    for j in range(len(temp_df)):
        url = temp_df['page'][j]
        data = requests.get(url).text
        soup = BeautifulSoup(data, 'html.parser')
        dfs = pd.read_html(data)
        df = dfs[7]
        df = df.drop(labels = [0,1], axis = 0)
        df.columns = ['Team','G','Sack','FR', 'INT',
                   'DefTD','PA','PaYd/G','RuYd/G',
                 'Safety','KickTD','FPts','FPts/G']
        df['week_num'] = temp_df['week'][j]
        df['year'] = temp_df['year'][j]
        df2 = df2.append(df)
    
    new = df2['Team'].str.split(" ", expand = True)
    df2['Team'] = new[1]
    
    df2['abbr'] = df2['Team']
    df2['abbr'] = df2['abbr'].map({'Cardinals':'ARI','49ers':'SF','Saints':'NO',
                                   'Panthers':'CAR','Cowboys':'DAL','Texans':'HOU',
                                   'Raiders':'LV','Rams':'LAR','Lions':'DET',
                                   'Chiefs':'KC','Commanders':'WSH','Ravens':'BAL',
                                   'Colts':'IND','Steelers':'PIT','Bengals':'CIN',
                                   'Seahawks':'SEA','Dolphins':'MIA','Vikings':'MIN',
                                   'Patriots':'NE','Giants':'NYG','Titans':'TEN',
                                   'Broncos':'DEN', 'Jets':'NYJ','Eagles':'PHI',
                                   'Chargers':'LAC','Buccaneers':'TB','Bills':'BUF',
                                   'Browns':'CLE','Falcons':'ATL','Jaguars':'JAX',
                                   'Bears':'CHI','Packers':'GB'})
    
    df2 = df2.rename(columns = {'abbr':'CITY',
                               'PaYd/G':'PaYD',
                               'RuYd/G':'RuYd'})
    df2['Week'] = df2['week_num']
    df2['team_wk_year'] = df2['CITY'] + " " + df2['week_num'].astype(str) + " " + df2['year'].astype(str)
    nfl_sched['team_wk_year'] = nfl_sched['TEAM'] + " " + nfl_sched['Week'].astype(str) + " " + nfl_sched['Year'].astype(str)
    nfl_sched = nfl_sched.rename(columns = {'Opponent':'Opp'})
    nfl_sched = nfl_sched[['team_wk_year', 'Opp']]
    nfl_sched['away flag'] = np.where(nfl_sched['Opp'].astype(str).str[0] == '@', 1, 0)
    
    df2 = pd.merge(df2, nfl_sched, how = 'inner', on = 'team_wk_year', 
                  suffixes = (None, None))
    df2['PA'] = df2['PA'].astype(int)
    df2['PA_pts'] = np.where(df2['PA']==0, 10,
                            np.where((df2['PA']>0) & (df2['PA']<=6),7,
                                    np.where((df2['PA']>6) & (df2['PA']<=13),4,
                                            np.where((df2['PA']>13) & (df2['PA']<=20),1,
                                                    np.where((df2['PA']>20) & (df2['PA']<=27),0,
                                                            np.where((df2['PA']>28) & (df2['PA']<=34),-1,-4))))))
    df2['FPts'] = (df2['Sack'].astype(int)*1 + df2['FR'].astype(int)*2 +
                   df2['INT'].astype(int)*2 + df2['DefTD'].astype(int)*6 
                   + df2['Safety'].astype(int)*2 + df2['KickTD'].astype(int)*6 
                   + df2['PA_pts'].astype(int))    
    df2 = df2[['Team','CITY','Week','Sack','FR','INT','DefTD',
                'PA','PaYD','RuYd','Safety',
                'KickTD','FPts','week_num','year',
                'Opp','away flag','team_wk_year']]

    
    return df2
    
def def_curr_wk_for_positions(def_df,
                    nfl_sched,
                    curr_wk,
                    curr_yr):
    nfl_sched = nfl_sched[(nfl_sched['Year'] == curr_yr) & 
                         (nfl_sched['Week'] == curr_wk)]
    
    nfl_sched = nfl_sched.rename(columns = {'Year':'year',
                                           'TEAM':'CITY',
                                           'Opponent':'Opp'})
    nfl_sched['week_num'] = nfl_sched['Week']
    nfl_sched['Opp'] = nfl_sched["Opp"].str.replace("@","")
    nfl_sched['opp_wk_year'] = nfl_sched['Opp'] + " " + nfl_sched['week_num'].astype(str) + " " + nfl_sched['year'].astype(str)    
   

    nfl_sched['Team'] = nfl_sched['CITY'].map({'ARI':'Cardinals','SF':'49ers','NO':'Saints',
                                   'CAR':'Panthers','DAL':'Cowboys','HOU':'Texans',
                                   'LV':'Raiders','LAR':'Rams','DET':'Lions',
                                   'KC':'Chiefs','WSH':'Commanders','BAL':'Ravens',
                                   'IND':'Colts','PIT':'Steelers','CIN':'Bengals',
                                   'SEA':'Seahawks','MIA':'Dolphins','MIN':'Vikings',
                                   'NE':'Patriots','NYG':'Giants','TEN':'Titans',
                                   'DEN':'Broncos', 'NYJ':'Jets','PHI':'Eagles',
                                   'LAC':'Chargers','TB':'Buccaneers','BUF':'Bills',
                                   'CLE':'Browns','ATL':'Falcons','JAX':'Jaguars',
                                   'CHI':'Bears','GB':'Packers'})
    
    nfl_sched['Sack'] = None
    nfl_sched['FR'] = None
    nfl_sched['INT'] = None
    nfl_sched['DefTD'] = None
    nfl_sched['PA'] = None
    nfl_sched['PaYD'] = None
    nfl_sched['RuYd'] = None
    nfl_sched['Safety'] = None
    nfl_sched['KickTD'] = None
    nfl_sched['FPts'] = None
    nfl_sched['away flag'] = None

    def_df['Opp'] = def_df['Opp'].str.replace('@','')
    def_df['opp_wk_year'] = def_df['Opp'] + " " + def_df['week_num'].astype(str) + " " + def_df['year'].astype(str)
    def_df = def_df.append(nfl_sched)

#    filt_wk = str(curr_wk) + " " + str(curr_yr)
    
#    def_df_wk = def_df_wk[def_df_wk['team_wk_year'].str.contains(filt_wk)]
    
    return def_df

def pull_all_player_data(player_df, def_df, position):
        
    #if (position == 'QB'):
        qb = player_df[player_df['Position'] == position]
        qb = qb[qb['Player'] != 'Zach Miller']
        qb = qb.reset_index()
        qb = qb.drop(columns = ['index'])
        
        df_qb = pd.DataFrame()
        print('test')

        for i in range(0,len(qb)):
        #for i in range(len(qb)):
            try:
                time.sleep(3.1)
                print(i)
                player = qb['Player'][i]
                print(qb['Player'][i])
                url = qb['Gamelog'][i]
                #print(qb['Player'][i])
                data = requests.get(url).text
                #print(data)
                soup = BeautifulSoup(data, 'html.parser')
                #print(soup)
                dfs = pd.read_html(data)
                df = dfs[0]
                df['Player'] = player
                #print(df.head())    
                #print(df.columns)
                df_qb = pd.concat([df_qb, df], axis=0, ignore_index=True)
            except:
                print("No tables found exception")
                i = i - 1
                continue
        
        df_qb.columns = df_qb.columns.get_level_values(0) + '' +  df_qb.columns.get_level_values(1)
        if (position == 'QB'):
            print(df_qb.columns)
            
            df_qb = df_qb[['FumblesFF', 'FumblesFL',
                                'FumblesFR', 'FumblesFmb',
                                'FumblesTD', 'FumblesYds', 'Off. SnapsNum',
                                'Off. SnapsPct', 'PassingAY/A','PassingAtt',
                                'PassingCmp', 'PassingCmp%', 'PassingInt', 'PassingRate',
                                'PassingSk', 'PassingTD', 'PassingY/A', 'PassingYds',
                                'PassingYds.1', 'Player', 'RushingAtt',
                                'RushingTD', 'RushingY/A', 'RushingYds',
                            #   'ST SnapsNum', 'ST SnapsPct',
                                'Scoring2PM', 'ScoringPts', 'ScoringTD',
                                'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                                'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                                'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                                'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                                'Unnamed: 7_level_0Unnamed: 7_level_1',
                                'Unnamed: 8_level_0Opp', 'Unnamed: 9_level_0Result']]
        
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                                'FumblesFL':'Fumbles FL', 'FumblesFR':'Fumbles FR',
                                'FumblesFmb':'Fumbles Fmb', 'FumblesTD':'Fumbles TD',
                                'FumblesYds':'Fumbles Yds', 'Off. SnapsNum':'Off. Snaps Num',
                                'Off. SnapsPct':'Off. Snaps Pct',
                                'PassingAY/A':'Passing AY/A','PassingAtt':'Passing Att',
                                'PassingCmp':'Passing Cmp', 'PassingCmp%':'Passing Cmp%',
                                'PassingInt':'Passing Int', 'PassingRate':'Passing Rate',
                                'PassingSk':'Passing Sk', 'PassingTD': 'Passing TD',
                                'PassingY/A':'Passing Y/A', 'PassingYds':'Passing Yds',
                                'PassingYds.1':'Passing Sack Yds Lost',
                                'Player':'Player ', 'RushingAtt':'Rushing Att',
                                'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                'RushingYds':'Rushing Yds',
#                               'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                'ScoringTD':'Scoring TD',
                                'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                'Unnamed: 8_level_0Opp':'Opp',
                                'Unnamed: 9_level_0Result':'Result'})
            print(df_qb.columns)

        elif (position == 'RB'):
            
            df_qb = df_qb[['FumblesFF', 'FumblesFL', 'FumblesFR',
                        'FumblesFmb', 'FumblesTD', 'FumblesYds',
                        'Kick ReturnsRt','Kick ReturnsTD', 'Kick ReturnsY/Rt',
                        'Kick ReturnsYds','Off. SnapsNum', 'Off. SnapsPct',
                        'Player', 'Punt ReturnsRet', 'Punt ReturnsTD',
                        'Punt ReturnsY/R', 'Punt ReturnsYds', 'ReceivingCtch%',
                        'ReceivingRec', 'ReceivingTD','ReceivingTgt',
                        'ReceivingY/R', 'ReceivingY/Tgt', 'ReceivingYds',                                            
                        'RushingAtt', 'RushingTD', 'RushingY/A', 'RushingYds',
                        'ST SnapsNum', 'ST SnapsPct', 'Scoring2PM', 'ScoringPts',
                        'ScoringTD', 'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                        'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                        'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                        'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                        'Unnamed: 7_level_0Unnamed: 7_level_1',
                        'Unnamed: 8_level_0Opp', 'Unnamed: 9_level_0Result']]

            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                        'FumblesFL':'Fumbles FL', 'FumblesFR':'Fumbles FR',
                        'FumblesFmb':'Fumbles Fmb', 'FumblesTD':'Fumbles TD',
                        'FumblesYds':'Fumbles Yds','Kick ReturnsRt':'Kick Returns Rt',
                        'Kick ReturnsTD':'Kick Returns TD', 'Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                        'Kick ReturnsYds':'Kick Returns Yds', 'Off. SnapsNum':'Off. Snaps Num',
                        'Off. SnapsPct':'Off. Snaps Pct', 'Player':'Player ', 
                        'Punt ReturnsRet':'Punt Returns Ret','Punt ReturnsTD':'Punt Returns TD',
                        'Punt ReturnsY/R':'Punt Returns Y/R','Punt ReturnsYds':'Punt Returns Yds',
                        'ReceivingCtch%':'Receiving Ctch%', 'ReceivingRec':'Receiving Rec',
                        'ReceivingTD':'Receiving TD','ReceivingTgt':'Receiving Tgt',
                        'ReceivingY/R':'Receiving Y/R', 'ReceivingY/Tgt':'Receiving Y/Tgt',
                        'ReceivingYds':'Receiving Yds', 'RushingAtt':'Rushing Att',
                        'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                        'RushingYds':'Rushing Yds',
                        'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                        'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                        'ScoringTD':'Scoring TD', 'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                        'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                        'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                        'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                        'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                        'Unnamed: 8_level_0Opp':'Opp', 'Unnamed: 9_level_0Result':'Result'})
        
        elif (position == 'WR'):
            
            df_qb = df_qb[[
                'FumblesFF','FumblesFL','FumblesFR',
                'FumblesFmb','FumblesTD','FumblesYds',
                'Kick ReturnsRt','Kick ReturnsTD','Kick ReturnsY/Rt',
                'Kick ReturnsYds','Off. SnapsNum','Off. SnapsPct',
                'Player','Punt ReturnsRet','Punt ReturnsTD',
                'Punt ReturnsY/R','Punt ReturnsYds','ReceivingCtch%',
                'ReceivingRec','ReceivingTD', 'ReceivingTgt',
                'ReceivingY/R','ReceivingY/Tgt','ReceivingYds',
                'RushingAtt','RushingTD', 'RushingY/A',
               'RushingYds','ST SnapsNum', 'ST SnapsPct',
                'Scoring2PM', 'ScoringPts','ScoringTD', 
                'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                'Unnamed: 7_level_0Unnamed: 7_level_1',
                'Unnamed: 8_level_0Opp','Unnamed: 9_level_0Result'
                
            ]]
                    
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                        'FumblesFL':'Fumbles FL', 'FumblesFR':'Fumbles FR',
                        'FumblesFmb':'Fumbles Fmb','FumblesTD':'Fumbles TD',
                        'FumblesYds':'Fumbles Yds','Kick ReturnsRt':'Kick Returns Rt',
                        'Kick ReturnsTD':'Kick Returns TD','Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                        'Kick ReturnsYds':'Kick Returns Yds','Off. SnapsNum':'Off. Snaps Num',
                        'Off. SnapsPct':'Off. Snaps Pct', 'Player':'Player ', 
                        'Punt ReturnsRet':'Punt Returns Ret','Punt ReturnsTD':'Punt Returns TD',
                        'Punt ReturnsY/R':'Punt Returns Y/R','Punt ReturnsYds':'Punt Returns Yds',
                        'ReceivingCtch%':'Receiving Ctch%','ReceivingRec':'Receiving Rec',
                        'ReceivingTD':'Receiving TD', 'ReceivingTgt':'Receiving Tgt',
                        'ReceivingY/R':'Receiving Y/R', 'ReceivingY/Tgt':'Receiving Y/Tgt',
                        'ReceivingYds':'Receiving Yds','RushingAtt':'Rushing Att',
                        'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                        'RushingYds':'Rushing Yds',
                        'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                        'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                        'ScoringTD':'Scoring TD',
                        'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                        'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                        'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                        'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                        'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                        'Unnamed: 8_level_0Opp':'Opp',
                        'Unnamed: 9_level_0Result':'Result'})
         
        elif (position == 'TE'):
            
            df_qb = df_qb[[ 'FumblesFF', 'FumblesFL','FumblesFR','FumblesFmb',
                            'FumblesTD', 'FumblesYds', 'Off. SnapsNum',
                            'Off. SnapsPct', 'Player',#'Punt ReturnsRet',
                            #'Punt ReturnsTD', 'Punt ReturnsY/R','Punt ReturnsYds',
                            'ReceivingCtch%', 'ReceivingRec', 'ReceivingTD',
                            'ReceivingTgt','ReceivingY/R', 'ReceivingY/Tgt',
                            'ReceivingYds', 'RushingAtt', 'RushingTD', 'RushingY/A',
                            'RushingYds', 'ST SnapsNum', 'ST SnapsPct', 'Scoring2PM', 'ScoringPts',
                            'ScoringTD', 'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                             'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                            'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                            'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                            'Unnamed: 7_level_0Unnamed: 7_level_1', 'Unnamed: 8_level_0Opp',
                            'Unnamed: 9_level_0Result'
            ]]
                    
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                            'FumblesFL':'Fumbles FL', 'FumblesFR':'Fumbles FR',
                            'FumblesFmb':'Fumbles Fmb','FumblesTD':'Fumbles TD',
                            'FumblesYds':'Fumbles Yds','Kick ReturnsRt':'Kick Returns Rt',
                            'Kick ReturnsTD':'Kick Returns TD','Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                            'Kick ReturnsYds':'Kick Returns Yds', 'Off. SnapsNum':'Off. Snaps Num',
                            'Off. SnapsPct':'Off. Snaps Pct', 'Player':'Player ', 
                            'Punt ReturnsRet':'Punt Returns Ret', 'Punt ReturnsTD':'Punt Returns TD',
                            'Punt ReturnsY/R':'Punt Returns Y/R','Punt ReturnsYds':'Punt Returns Yds',
                            'ReceivingCtch%':'Receiving Ctch%', 'ReceivingRec':'Receiving Rec',
                            'ReceivingTD':'Receiving TD','ReceivingTgt':'Receiving Tgt',
                            'ReceivingY/R':'Receiving Y/R', 'ReceivingY/Tgt':'Receiving Y/Tgt',
                            'ReceivingYds':'Receiving Yds', 'RushingAtt':'Rushing Att',
                            'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                            'RushingYds':'Rushing Yds', 'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                            'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                            'ScoringTD':'Scoring TD', 'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                            'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                            'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                            'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                            'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                            'Unnamed: 8_level_0Opp':'Opp', 'Unnamed: 9_level_0Result':'Result'})
                 
        elif (position == 'K'):
            
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                    'FumblesFL':'Fumbles FL','FumblesFR':'Fumbles FR',
                    'FumblesFmb':'Fumbles Fmb', 'FumblesTD':'Fumbles TD',
                    'FumblesYds':'Fumbles Yds','Kick ReturnsRt':'Kick Returns Rt',
                    'Kick ReturnsTD':'Kick Returns TD','Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                    'Kick ReturnsYds':'Kick Returns Yds', 'Off. SnapsNum':'Off. Snaps Num',
                    'Off. SnapsPct':'Off. Snaps Pct', 'Player':'Player ', 
                    'Punt ReturnsRet':'Punt Returns Ret','Punt ReturnsTD':'Punt Returns TD',
                    'Punt ReturnsY/R':'Punt Returns Y/R', 'Punt ReturnsYds':'Punt Returns Yds',
                    'ReceivingCtch%':'Receiving Ctch%', 'ReceivingRec':'Receiving Rec',
                    'ReceivingTD':'Receiving TD', 'ReceivingTgt':'Receiving Tgt',
                    'ReceivingY/R':'Receiving Y/R', 'ReceivingY/Tgt':'Receiving Y/Tgt',
                    'ReceivingYds':'Receiving Yds', 'RushingAtt':'Rushing Att',
                    'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                    'RushingYds':'Rushing Yds',
                    'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                    'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                    'ScoringTD':'Scoring TD',
                    'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                    'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                    'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                    'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                    'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                    'Unnamed: 8_level_0Opp':'Opp', 'Unnamed: 9_level_0Result':'Result'})
            
            df_qb = df_qb[['Player ','ST Snaps Num', 'ST Snaps Pct', 'Scoring Pts',
                           'ScoringXPM','ScoringXPA','ScoringXP%','ScoringFGM','ScoringFGA',
                           'ScoringFG%',#'ScoringTD',
                          'Rk', 'GS', 'Year', 'Date', 'G#', 'Week', 'Age', 'Tm',
                          'home_away', 'Opp','Result']]
          
        
        print(df_qb.shape)
        df_qb2 = df_qb[df_qb['G#'] != '']
        df_qb2 = df_qb2[df_qb2['G#'] != 'G#']
        df_qb2 = df_qb2[~df_qb2['Date'].str.contains("Game")]
   #     df_qb2 = df_qb2[df_qb2['GS'] != 'Did Not Play']
        
        df_qb2 = df_qb2[~df_qb2['GS'].isin(['Did Not Play', 'Inactive',
                                           'Injured Reserve','Non-Football Injury',
                                           'Suspended','Returned from Injured Reserve',
                                           'COVID-19 List','Exempt List',
                                           'Physically Unable to Perform'])]

        df_qb2['Week'] = df_qb2['Week'].astype(int)
        df_qb2['Year'] = df_qb2['Year'].astype(int)
        df_qb2['player_wk_year'] = df_qb2['Player '] + " " + df_qb2['Week'].astype(str) + " " + df_qb2['Year'].astype(str)
        #mean_age = df_qb2['Age'].mean()
        df_qb2['Age'] = df_qb2['Age'].fillna(value = 26, inplace=True)
        df_qb2['Age'] = df_qb2['Age'].astype(float, errors='ignore').astype(int,errors='ignore')
        print('yay')
        
        return df_qb2

def position_feat_eng_df_creation_new(df_qb2,
                                  def_df,
                                  position#,
                                 #file_save
                                 ):
    
        
        test_df = df_qb2[['Player ','Week', 'Year', 'player_wk_year']]
        test_df['Week'] = test_df['Week'].astype(int)
        test_df['Year'] = test_df['Year'].astype(int)     
        
        print(test_df.shape)
        a = list(test_df['Player '].unique())
        test_df2 = pd.DataFrame()
        for p in a:
            player_name_df = test_df[test_df['Player ']==p]
                
            for i in range(1,7):
               # print(i)
                wks_ago = i
                week_num_wks_ago = "week num " + str(i) + " wks ago"
                year_wks_ago = "year " + str(i) + " wks ago"
                player_wks_ago = "player " + str(i) + " wks ago"                
                
#                 prev_games_played_ago = i
#                 week_num_prev_game_played = 'week num ' + str(i) + " games played ago" 
#                 year_prev_game_played = 'year ' + str(i) + " games played ago"
#                 player_prev_game_player = 'player ' + str(i) + " games played ago"
#                 player_wk_year_prev_game_player = 'player_wk_year ' + str(i) + " games played ago"
                if (i == 1):
                    player_name_df[player_wks_ago] = [np.nan]+list(player_name_df["player_wk_year"])[:-1]
                    #player_name_df[player_prev_game_player] = [np.nan]+list(player_name_df["Player "])[:-1]
                    player_name_df[week_num_wks_ago] = [np.nan]+list(player_name_df["Week"])[:-1]
                    player_name_df[year_wks_ago] = [np.nan]+list(player_name_df["Year"])[:-1]

                elif ( i > 1):
                   # player_name_df[player_wks_ago] = [np.nan]+list(player_name_df[prior_player_wk_year_prev_game_player])[:-1]
                    player_name_df[player_wks_ago] = [np.nan]+list(player_name_df[prior_player_prev_game_player])[:-1]
                    player_name_df[week_num_wks_ago] = [np.nan]+list(player_name_df[prior_week_num_prev_game_played])[:-1]
                    player_name_df[year_wks_ago] = [np.nan]+list(player_name_df[prior_year_prev_game_played])[:-1]

                prior_prev_games_played_ago = i
                prior_week_num_prev_game_played = "week num " + str(i) + " wks ago"
                prior_year_prev_game_played =  "year " + str(i) + " wks ago"
                prior_player_prev_game_player = "player " + str(i) + " wks ago" 
                #prior_player_wk_year_prev_game_player = 'player_wk_year ' + str(i) + " games played ago"

            test_df2 = test_df2.append(player_name_df)

        test_df = test_df2    
        print(test_df.shape)
        new_df = pd.DataFrame()
        for i in range(0,7):
            print(i)
            if (i == 0):
                #new_df = df_qb2
                test_df2 = test_df.drop(columns = ['Player ', 'Week', 'Year'])
                new_df = pd.merge(test_df2, df_qb2, how = 'left', on = ['player_wk_year'], suffixes = (None, None))
                print(new_df.head())
            else:
                temp_df = df_qb2.drop(columns = ['Rk','GS','Year','G#'])
                for col in temp_df.columns:
                    new_col = col + " " + str(i) + " wks ago"
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                merge_column = "player " + str(i) + " wks ago"
                temp_df[merge_column] = df_qb2['player_wk_year']
                new_df = pd.merge(new_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
        
        qb_df = new_df
        print(qb_df.shape)
        tms = ['Tm','Tm 1 wks ago', 'Tm 2 wks ago',
              'Tm 3 wks ago','Tm 4 wks ago','Tm 5 wks ago','Tm 6 wks ago'#,
              ]

        opp = ['Opp','Opp 1 wks ago', 'Opp 2 wks ago',
              'Opp 3 wks ago','Opp 4 wks ago','Opp 5 wks ago','Opp 6 wks ago'#,
              ]
        
        for i in tms:
            #print(i)
            qb_df[i] = qb_df[i].map({'NWE': 'NE',
                               'NOR': 'NO', 'SFO': 'SF', 'SDG':'LAC',
                              'GNB':'GB','TAM':'TB','WAS':'WSH',
                              'KAN':'KC', 'OAK':'LV', 'STL':'LAR',
                              'LVR':'LV', 'IND':'IND', 'SEA':'SEA',
                             'HOU':'HOU', 'ATL':'ATL', 'CIN':'CIN',
                             'PIT':'PIT','NYG':'NYG', 'DET':'DET',
                             'CLE':'CLE','DEN':'DEN','DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI',
                             'BAL':'BAL','JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA',
                             'CAR':'CAR','PHI':'PHI','MIN':'MIN',
                             'TEN':'TEN', 'LAR':'LAR', 'LAC':'LAC'})
        for i in opp:
            #print(i)
            qb_df[i] = qb_df[i].map({'NWE': 'NE', 'NOR': 'NO',
                              'SFO': 'SF', 'SDG':'LAC', 'GNB':'GB','TAM':'TB',
                              'WAS':'WSH','KAN':'KC', 'OAK':'LV', 'STL':'LAR',
                              'LVR':'LV','IND':'IND', 'SEA':'SEA', 'HOU':'HOU',
                             'ATL':'ATL','CIN':'CIN', 'PIT':'PIT', 'NYG':'NYG',
                             'DET':'DET','CLE':'CLE', 'DEN':'DEN', 'DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI','BAL':'BAL',
                             'JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA', 'CAR':'CAR',
                             'PHI':'PHI', 'MIN':'MIN', 'TEN':'TEN', 'LAR':'LAR',
                             'LAC':'LAC'})    
            
        #opp
        opp_wk_year = ['opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago', 'opp 3 wk year ago',
              'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago'
                      ]

        wk = ['Week', 'Week 1 wks ago', 'Week 2 wks ago', 'Week 3 wks ago', 'Week 4 wks ago', 'Week 5 wks ago',
              'Week 6 wks ago'
             ]

        year = ['Year', 'year 1 wks ago', 'year 2 wks ago', 'year 3 wks ago', 'year 4 wks ago', 'year 5 wks ago',
               'year 6 wks ago'
               ]
        
        
        for i in range(0,7):
            #print(i)
            #print(opp[i])
            #print(wk[i])
            #print(year[i])
            opp_colname = opp[i]
            wk_colname = wk[i]
            year_colname = year[i]#.astype(int)
            qb_df[wk_colname] = qb_df[wk_colname].astype(str).str.replace('.0', '',regex=False)
            
            qb_df[year_colname] = qb_df[year_colname].astype(str).str.replace('.0', '',regex=False)
            opp_wk_year_colname = opp_wk_year[i]
            if (i== 0):
                qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str) + " " + qb_df[year_colname].astype(str)#.str.replace('.0', '',regex=False)
            else:
                #qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str).str[:-2] + " " + qb_df[year_colname].astype(str)
                qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str) + " " + qb_df[year_colname].astype(str)#.str.replace('.0','', regex=False)
        
        #if (i == 0):

        test_df = qb_df[['player_wk_year','opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago', 'opp 3 wk year ago',
              'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago'#, 'opp 7 wk year ago',
                        ]]
        print(test_df.shape)
        new_df = pd.DataFrame()

        for i in range(0,7):
            #print(i)
            if (i == 0):
                #new_df = df_qb2
                #test_df2 = test_df.drop(columns = [])
                new_df = pd.merge(test_df, def_df, how = 'left', left_on = ['opp wk year'], right_on = ['team_wk_year'], suffixes = (None, None))
                new_df = new_df.drop(columns = ['team_wk_year'])
                #print(new_df.head())
            else:
                temp_df = def_df.drop(columns = ['Week','week_num','year','Opp','team_wk_year'])
              #  temp_df2 = temp_df
                for col in temp_df.columns:
                    new_col = 'opp' + " " + col + " " + str(i) + 'wks ago'
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                #merge_column = "player " + str(i) + " wks ago"
                #merge_column = 
                temp_df['team_wk_year'] = def_df['team_wk_year']
               # print(temp_df2.head())
                qb_no_null = test_df[[opp_wk_year[i]]]
               # print(qb_no_null.head())
                qb_no_null = qb_no_null[qb_no_null.notnull()]
              #  print(qb_no_null.head())
                qb_no_null = pd.merge(qb_no_null, temp_df, how = 'inner', left_on = [opp_wk_year[i]], right_on = ['team_wk_year'], suffixes = (None,None))
                #print(qb_no_null.head())
                qb_no_null = qb_no_null.drop_duplicates()
        
                qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
                new_df = pd.merge(new_df, qb_no_null, how = 'left', left_on = [opp_wk_year[i]], right_on = ['team_wk_year'], suffixes = (None, None))
                new_df = new_df.drop(columns = ['team_wk_year'])
        
        new_df = new_df.drop_duplicates()
        
        qb_df2 = qb_df.drop(columns = ['Week', 'Opp', 'opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago',
           'opp 3 wk year ago', 'opp 4 wk year ago', 'opp 5 wk year ago',
           'opp 6 wk year ago'#, 'opp 7 wk year ago', 'opp 8 wk year ago',
                                      ])
        

        new_df2 = pd.merge(qb_df2,new_df, how = 'left', on = 'player_wk_year', suffixes = (None,None))
        print(new_df2.shape)
        test_df = def_df[['CITY','week_num', 'year', 'team_wk_year']]
        for i in range(1,7):
            #print(i)
            wks_ago = i
            week_num_wks_ago = "week num " + str(i) + " wks ago"
            year_wks_ago = "year " + str(i) + " wks ago"
            #player_wks_ago = "player " + str(i) + " wks ago"
            team_wk_year = 'team_wk_year ' + str(i) + " wks ago"
            if(i == 1):
                curr_wk = "week_num"
                curr_yr = "year"
                test_df[curr_wk] = test_df['week_num']
                test_df[curr_yr] = test_df['year']
                test_df[week_num_wks_ago] = np.where(test_df[curr_wk] == 1, 17, test_df[curr_wk] - 1)
                test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
            else:
                curr_wk = "week num " + str(i-1) + " wks ago"
                curr_yr = "year " + str(i-1) + " wks ago"
                test_df[week_num_wks_ago] = np.where(test_df[curr_wk] == 1, 17, test_df[curr_wk]-1)
                test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr] -1, test_df[curr_yr])

            test_df[team_wk_year] = test_df['CITY'] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)
        
        return new_df2
            
def position_feat_eng_df_creation(player_df,
                                  def_df,
                                  position#,
                                 #file_save
                                 ):
    
    #if (position == 'QB'):
        qb = player_df[player_df['Position'] == position]
        qb = qb[qb['Player'] != 'Zach Miller']
        qb = qb.reset_index()
        qb = qb.drop(columns = ['index'])
        
        df_qb = pd.DataFrame()
        print('test')

        for i in range(0,len(qb)):
        #for i in range(len(qb)):
            try:
                time.sleep(3.1)
                print(i)
                player = qb['Player'][i]
                print(qb['Player'][i])
                url = qb['Gamelog'][i]
                #print(qb['Player'][i])
                data = requests.get(url).text
                #print(data)
                soup = BeautifulSoup(data, 'html.parser')
                #print(soup)
                dfs = pd.read_html(data)
                df = dfs[0]
                df['Player'] = player
                #print(df.head())    
                #print(df.columns)
                df_qb = pd.concat([df_qb, df], axis=0, ignore_index=True)
            except:
                print("No tables found exception")
                i = i - 1
                continue
        
        df_qb.columns = df_qb.columns.get_level_values(0) + '' +  df_qb.columns.get_level_values(1)
        if (position == 'QB'):
            print(df_qb.columns)
            
            df_qb = df_qb[['FumblesFF',
                                  'FumblesFL',
                                  'FumblesFR',
                                  'FumblesFmb',
                                  'FumblesTD',
                                        'FumblesYds', 'Off. SnapsNum',
                                        'Off. SnapsPct',
                                        'PassingAY/A','PassingAtt',
                                        'PassingCmp', 'PassingCmp%',
                                        'PassingInt', 'PassingRate',
                                        'PassingSk', 'PassingTD',
                                        'PassingY/A', 'PassingYds',
                                        'PassingYds.1',
                                        'Player', 'RushingAtt',
                                        'RushingTD', 'RushingY/A',
                                        'RushingYds',
                                     #   'ST SnapsNum', 'ST SnapsPct',
                                        'Scoring2PM', 'ScoringPts',
                                        'ScoringTD',
                                        'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                                        'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                                        'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                                        'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                                        'Unnamed: 7_level_0Unnamed: 7_level_1',
                                  'Unnamed: 8_level_0Opp',
                                        'Unnamed: 9_level_0Result']]

            print(df_qb.columns)
        
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                                  'FumblesFL':'Fumbles FL',
                                  'FumblesFR':'Fumbles FR',
                                  'FumblesFmb':'Fumbles Fmb',
                                  'FumblesTD':'Fumbles TD',
                                        'FumblesYds':'Fumbles Yds', 'Off. SnapsNum':'Off. Snaps Num',
                                        'Off. SnapsPct':'Off. Snaps Pct',
                                        'PassingAY/A':'Passing AY/A','PassingAtt':'Passing Att',
                                        'PassingCmp':'Passing Cmp', 'PassingCmp%':'Passing Cmp%',
                                        'PassingInt':'Passing Int', 'PassingRate':'Passing Rate',
                                        'PassingSk':'Passing Sk', 'PassingTD': 'Passing TD',
                                        'PassingY/A':'Passing Y/A', 'PassingYds':'Passing Yds',
                                        'PassingYds.1':'Passing Sack Yds Lost',
                                        'Player':'Player ', 'RushingAtt':'Rushing Att',
                                        'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                        'RushingYds':'Rushing Yds',
#                                        'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                        'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                        'ScoringTD':'Scoring TD',
                                        'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                        'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                        'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                        'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                        'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                  'Unnamed: 8_level_0Opp':'Opp',
                                        'Unnamed: 9_level_0Result':'Result'})
            print(df_qb.columns)

        elif (position == 'RB'):
            
            df_qb = df_qb[['FumblesFF',
                                  'FumblesFL',
                                  'FumblesFR',
                                  'FumblesFmb',
                                  'FumblesTD',
                                        'FumblesYds',
                                               'Kick ReturnsRt',
                                            'Kick ReturnsTD',
                                       'Kick ReturnsY/Rt',
                                            'Kick ReturnsYds',
                                            'Off. SnapsNum',
                                        'Off. SnapsPct',
                                        'Player', 
                                            'Punt ReturnsRet',
                                            'Punt ReturnsTD',
                                       'Punt ReturnsY/R',
                                            'Punt ReturnsYds',
                                               
                                            'ReceivingCtch%',
                                            'ReceivingRec',
                                            'ReceivingTD',
                                       'ReceivingTgt',
                                            'ReceivingY/R',
                                            'ReceivingY/Tgt',
                                            'ReceivingYds',
                                            
                                            'RushingAtt',
                                        'RushingTD', 'RushingY/A',
                                        'RushingYds',
                                        'ST SnapsNum', 'ST SnapsPct',
                                        'Scoring2PM', 'ScoringPts',
                                        'ScoringTD',
                                        'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                                        'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                                        'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                                        'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                                        'Unnamed: 7_level_0Unnamed: 7_level_1',
                                  'Unnamed: 8_level_0Opp',
                                        'Unnamed: 9_level_0Result']]

            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                                  'FumblesFL':'Fumbles FL',
                                  'FumblesFR':'Fumbles FR',
                                  'FumblesFmb':'Fumbles Fmb',
                                  'FumblesTD':'Fumbles TD',
                                        'FumblesYds':'Fumbles Yds',
                                               'Kick ReturnsRt':'Kick Returns Rt',
                                            'Kick ReturnsTD':'Kick Returns TD',
                                       'Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                                            'Kick ReturnsYds':'Kick Returns Yds',
                                            'Off. SnapsNum':'Off. Snaps Num',
                                        'Off. SnapsPct':'Off. Snaps Pct',
                                        'Player':'Player ', 
                                            'Punt ReturnsRet':'Punt Returns Ret',
                                            'Punt ReturnsTD':'Punt Returns TD',
                                       'Punt ReturnsY/R':'Punt Returns Y/R',
                                            'Punt ReturnsYds':'Punt Returns Yds',
                                               
                                            'ReceivingCtch%':'Receiving Ctch%',
                                            'ReceivingRec':'Receiving Rec',
                                            'ReceivingTD':'Receiving TD',
                                       'ReceivingTgt':'Receiving Tgt',
                                            'ReceivingY/R':'Receiving Y/R',
                                            'ReceivingY/Tgt':'Receiving Y/Tgt',
                                            'ReceivingYds':'Receiving Yds',
                                            
                                            'RushingAtt':'Rushing Att',
                                        'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                        'RushingYds':'Rushing Yds',
                                        'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                        'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                        'ScoringTD':'Scoring TD',
                                                                                        
                                        'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                        'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                        'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                        'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                        'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                  'Unnamed: 8_level_0Opp':'Opp',
                                        'Unnamed: 9_level_0Result':'Result'})
            print(df_qb.columns)
        
        elif (position == 'WR'):
            print(df_qb.columns)
            
            df_qb = df_qb[[
                'FumblesFF','FumblesFL','FumblesFR',
                'FumblesFmb','FumblesTD','FumblesYds',
                'Kick ReturnsRt','Kick ReturnsTD','Kick ReturnsY/Rt',
                'Kick ReturnsYds','Off. SnapsNum','Off. SnapsPct',
                'Player','Punt ReturnsRet','Punt ReturnsTD',
                'Punt ReturnsY/R','Punt ReturnsYds','ReceivingCtch%',
                'ReceivingRec','ReceivingTD', 'ReceivingTgt',
                'ReceivingY/R','ReceivingY/Tgt','ReceivingYds',
                'RushingAtt','RushingTD', 'RushingY/A',
               'RushingYds','ST SnapsNum', 'ST SnapsPct',
                'Scoring2PM', 'ScoringPts','ScoringTD', 
                'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                'Unnamed: 7_level_0Unnamed: 7_level_1',
                'Unnamed: 8_level_0Opp','Unnamed: 9_level_0Result'
                
            ]]
            

            print(df_qb.columns)
        
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                                  'FumblesFL':'Fumbles FL',
                                  'FumblesFR':'Fumbles FR',
                                  'FumblesFmb':'Fumbles Fmb',
                                  'FumblesTD':'Fumbles TD',
                                        'FumblesYds':'Fumbles Yds',
                                               'Kick ReturnsRt':'Kick Returns Rt',
                                            'Kick ReturnsTD':'Kick Returns TD',
                                       'Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                                            'Kick ReturnsYds':'Kick Returns Yds',
                                            'Off. SnapsNum':'Off. Snaps Num',
                                        'Off. SnapsPct':'Off. Snaps Pct',
                                        'Player':'Player ', 
                                            'Punt ReturnsRet':'Punt Returns Ret',
                                            'Punt ReturnsTD':'Punt Returns TD',
                                       'Punt ReturnsY/R':'Punt Returns Y/R',
                                            'Punt ReturnsYds':'Punt Returns Yds',
                                               
                                            'ReceivingCtch%':'Receiving Ctch%',
                                            'ReceivingRec':'Receiving Rec',
                                            'ReceivingTD':'Receiving TD',
                                       'ReceivingTgt':'Receiving Tgt',
                                            'ReceivingY/R':'Receiving Y/R',
                                            'ReceivingY/Tgt':'Receiving Y/Tgt',
                                            'ReceivingYds':'Receiving Yds',
                                            
                                            'RushingAtt':'Rushing Att',
                                        'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                        'RushingYds':'Rushing Yds',
                                        'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                        'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                        'ScoringTD':'Scoring TD',
                                        'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                        'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                        'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                        'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                        'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                  'Unnamed: 8_level_0Opp':'Opp',
                                        'Unnamed: 9_level_0Result':'Result'})
            print(df_qb.columns)
         
        elif (position == 'TE'):
            print(df_qb.columns)
            
            df_qb = df_qb[[ 'FumblesFF', 'FumblesFL','FumblesFR','FumblesFmb',
                            'FumblesTD', 'FumblesYds', #'Kick ReturnsRt',
                            #'Kick ReturnsTD', 'Kick ReturnsY/Rt',
                            #'Kick ReturnsYds', 
                           'Off. SnapsNum',
                            'Off. SnapsPct', 'Player',#'Punt ReturnsRet',
                            #'Punt ReturnsTD', 'Punt ReturnsY/R','Punt ReturnsYds',
                            'ReceivingCtch%', 'ReceivingRec', 'ReceivingTD',
                            'ReceivingTgt','ReceivingY/R', 'ReceivingY/Tgt',
                            'ReceivingYds', 'RushingAtt', 'RushingTD', 'RushingY/A',
                            'RushingYds', 'ST SnapsNum', 'ST SnapsPct', 'Scoring2PM', 'ScoringPts',
                            'ScoringTD', 'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                             'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                            'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                            'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                            'Unnamed: 7_level_0Unnamed: 7_level_1', 'Unnamed: 8_level_0Opp',
                            'Unnamed: 9_level_0Result'
            ]]
            
            print(df_qb.columns)
        
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                                  'FumblesFL':'Fumbles FL',
                                  'FumblesFR':'Fumbles FR',
                                  'FumblesFmb':'Fumbles Fmb',
                                  'FumblesTD':'Fumbles TD',
                                        'FumblesYds':'Fumbles Yds',
                                               'Kick ReturnsRt':'Kick Returns Rt',
                                            'Kick ReturnsTD':'Kick Returns TD',
                                       'Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                                            'Kick ReturnsYds':'Kick Returns Yds',
                                            'Off. SnapsNum':'Off. Snaps Num',
                                        'Off. SnapsPct':'Off. Snaps Pct',
                                        'Player':'Player ', 
                                            'Punt ReturnsRet':'Punt Returns Ret',
                                            'Punt ReturnsTD':'Punt Returns TD',
                                       'Punt ReturnsY/R':'Punt Returns Y/R',
                                            'Punt ReturnsYds':'Punt Returns Yds',
                                               
                                            'ReceivingCtch%':'Receiving Ctch%',
                                            'ReceivingRec':'Receiving Rec',
                                            'ReceivingTD':'Receiving TD',
                                       'ReceivingTgt':'Receiving Tgt',
                                            'ReceivingY/R':'Receiving Y/R',
                                            'ReceivingY/Tgt':'Receiving Y/Tgt',
                                            'ReceivingYds':'Receiving Yds',
                                            
                                            'RushingAtt':'Rushing Att',
                                        'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                        'RushingYds':'Rushing Yds',
                                        'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                        'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                        'ScoringTD':'Scoring TD',
                                        'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                        'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                        'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                        'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                        'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                  'Unnamed: 8_level_0Opp':'Opp',
                                        'Unnamed: 9_level_0Result':'Result'})
         
            print(df_qb.columns)
        
        elif (position == 'K'):
            print(df_qb.columns)
            
            df_qb = df_qb.rename(columns = {'FumblesFF':'Fumbles FF',
                      'FumblesFL':'Fumbles FL',
                      'FumblesFR':'Fumbles FR',
                      'FumblesFmb':'Fumbles Fmb',
                      'FumblesTD':'Fumbles TD',
                            'FumblesYds':'Fumbles Yds',
                                   'Kick ReturnsRt':'Kick Returns Rt',
                                'Kick ReturnsTD':'Kick Returns TD',
                           'Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                                'Kick ReturnsYds':'Kick Returns Yds',
                                'Off. SnapsNum':'Off. Snaps Num',
                            'Off. SnapsPct':'Off. Snaps Pct',
                            'Player':'Player ', 
                                'Punt ReturnsRet':'Punt Returns Ret',
                                'Punt ReturnsTD':'Punt Returns TD',
                           'Punt ReturnsY/R':'Punt Returns Y/R',
                                'Punt ReturnsYds':'Punt Returns Yds',
                                'ReceivingCtch%':'Receiving Ctch%',
                                'ReceivingRec':'Receiving Rec',
                                'ReceivingTD':'Receiving TD',
                           'ReceivingTgt':'Receiving Tgt',
                                'ReceivingY/R':'Receiving Y/R',
                                'ReceivingY/Tgt':'Receiving Y/Tgt',
                                'ReceivingYds':'Receiving Yds',
                                'RushingAtt':'Rushing Att',
                            'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                            'RushingYds':'Rushing Yds',
                            'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                            'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                            'ScoringTD':'Scoring TD',
                            'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                            'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                            'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                            'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                            'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                      'Unnamed: 8_level_0Opp':'Opp',
                            'Unnamed: 9_level_0Result':'Result'})
            
            df_qb = df_qb[['Player ','ST Snaps Num', 'ST Snaps Pct', 'Scoring Pts',
                           'ScoringXPM','ScoringXPA','ScoringXP%','ScoringFGM','ScoringFGA',
                           'ScoringFG%',#'ScoringTD',
                          'Rk', 'GS', 'Year', 'Date', 'G#', 'Week', 'Age', 'Tm',
                          'home_away', 'Opp','Result']]
          
        
        print(df_qb.shape)
        df_qb2 = df_qb[df_qb['G#'] != '']
        df_qb2 = df_qb2[df_qb2['G#'] != 'G#']
        df_qb2 = df_qb2[~df_qb2['Date'].str.contains("Game")]
   #     df_qb2 = df_qb2[df_qb2['GS'] != 'Did Not Play']
        
        df_qb2 = df_qb2[~df_qb2['GS'].isin(['Did Not Play', 'Inactive',
                                           'Injured Reserve','Non-Football Injury',
                                           'Suspended','Returned from Injured Reserve',
                                           'COVID-19 List','Exempt List',
                                           'Physically Unable to Perform'])]

        df_qb2['Week'] = df_qb2['Week'].astype(int)
        df_qb2['Year'] = df_qb2['Year'].astype(int)
        df_qb2['player_wk_year'] = df_qb2['Player '] + " " + df_qb2['Week'].astype(str) + " " + df_qb2['Year'].astype(str)
        #mean_age = df_qb2['Age'].mean()
        df_qb2['Age'] = df_qb2['Age'].fillna(value = 26, inplace=True)
        df_qb2['Age'] = df_qb2['Age'].astype(float, errors='ignore').astype(int,errors='ignore')
        print('yay')
        
       #return df_qb2
        
        test_df = df_qb2[['Player ','Week', 'Year', 'player_wk_year']]
        test_df['Week'] = test_df['Week'].astype(int)
        test_df['Year'] = test_df['Year'].astype(int)     
        
        print(test_df.shape)
        a = list(test_df['Player '].unique())
        test_df2 = pd.DataFrame()
        for p in a:
            player_name_df = test_df[test_df['Player ']==p]
                
            for i in range(1,7):
               # print(i)
                wks_ago = i
                week_num_wks_ago = "week num " + str(i) + " wks ago"
                year_wks_ago = "year " + str(i) + " wks ago"
                player_wks_ago = "player " + str(i) + " wks ago"                
                
#                 prev_games_played_ago = i
#                 week_num_prev_game_played = 'week num ' + str(i) + " games played ago" 
#                 year_prev_game_played = 'year ' + str(i) + " games played ago"
#                 player_prev_game_player = 'player ' + str(i) + " games played ago"
#                 player_wk_year_prev_game_player = 'player_wk_year ' + str(i) + " games played ago"
                if (i == 1):
                    player_name_df[player_wks_ago] = [np.nan]+list(player_name_df["player_wk_year"])[:-1]
                    #player_name_df[player_prev_game_player] = [np.nan]+list(player_name_df["Player "])[:-1]
                    player_name_df[week_num_wks_ago] = [np.nan]+list(player_name_df["Week"])[:-1]
                    player_name_df[year_wks_ago] = [np.nan]+list(player_name_df["Year"])[:-1]

                elif ( i > 1):
                   # player_name_df[player_wks_ago] = [np.nan]+list(player_name_df[prior_player_wk_year_prev_game_player])[:-1]
                    player_name_df[player_wks_ago] = [np.nan]+list(player_name_df[prior_player_prev_game_player])[:-1]
                    player_name_df[week_num_wks_ago] = [np.nan]+list(player_name_df[prior_week_num_prev_game_played])[:-1]
                    player_name_df[year_wks_ago] = [np.nan]+list(player_name_df[prior_year_prev_game_played])[:-1]

                prior_prev_games_played_ago = i
                prior_week_num_prev_game_played = "week num " + str(i) + " wks ago"
                prior_year_prev_game_played =  "year " + str(i) + " wks ago"
                prior_player_prev_game_player = "player " + str(i) + " wks ago" 
                #prior_player_wk_year_prev_game_player = 'player_wk_year ' + str(i) + " games played ago"

            test_df2 = test_df2.append(player_name_df)

        test_df = test_df2    
        print(test_df.shape)
        new_df = pd.DataFrame()
        for i in range(0,7):
            print(i)
            if (i == 0):
                #new_df = df_qb2
                test_df2 = test_df.drop(columns = ['Player ', 'Week', 'Year'])
                new_df = pd.merge(test_df2, df_qb2, how = 'left', on = ['player_wk_year'], suffixes = (None, None))
                print(new_df.head())
            else:
                temp_df = df_qb2.drop(columns = ['Rk','GS','Year','G#'])
                for col in temp_df.columns:
                    new_col = col + " " + str(i) + " wks ago"
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                merge_column = "player " + str(i) + " wks ago"
                temp_df[merge_column] = df_qb2['player_wk_year']
                new_df = pd.merge(new_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
        
        qb_df = new_df
        print(qb_df.shape)
        tms = ['Tm','Tm 1 wks ago', 'Tm 2 wks ago',
              'Tm 3 wks ago','Tm 4 wks ago','Tm 5 wks ago','Tm 6 wks ago'#,
              ]

        opp = ['Opp','Opp 1 wks ago', 'Opp 2 wks ago',
              'Opp 3 wks ago','Opp 4 wks ago','Opp 5 wks ago','Opp 6 wks ago'#,
              ]
        
        for i in tms:
            #print(i)
            qb_df[i] = qb_df[i].map({'NWE': 'NE',
                               'NOR': 'NO', 'SFO': 'SF', 'SDG':'LAC',
                              'GNB':'GB','TAM':'TB','WAS':'WSH',
                              'KAN':'KC', 'OAK':'LV', 'STL':'LAR',
                              'LVR':'LV', 'IND':'IND', 'SEA':'SEA',
                             'HOU':'HOU', 'ATL':'ATL', 'CIN':'CIN',
                             'PIT':'PIT','NYG':'NYG', 'DET':'DET',
                             'CLE':'CLE','DEN':'DEN','DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI',
                             'BAL':'BAL','JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA',
                             'CAR':'CAR','PHI':'PHI','MIN':'MIN',
                             'TEN':'TEN', 'LAR':'LAR', 'LAC':'LAC'})
        for i in opp:
            #print(i)
            qb_df[i] = qb_df[i].map({'NWE': 'NE', 'NOR': 'NO',
                              'SFO': 'SF', 'SDG':'LAC', 'GNB':'GB','TAM':'TB',
                              'WAS':'WSH','KAN':'KC', 'OAK':'LV', 'STL':'LAR',
                              'LVR':'LV','IND':'IND', 'SEA':'SEA', 'HOU':'HOU',
                             'ATL':'ATL','CIN':'CIN', 'PIT':'PIT', 'NYG':'NYG',
                             'DET':'DET','CLE':'CLE', 'DEN':'DEN', 'DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI','BAL':'BAL',
                             'JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA', 'CAR':'CAR',
                             'PHI':'PHI', 'MIN':'MIN', 'TEN':'TEN', 'LAR':'LAR',
                             'LAC':'LAC'})    
            
        #opp
        opp_wk_year = ['opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago', 'opp 3 wk year ago',
              'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago'#, 'opp 7 wk year ago',
                      ]

        wk = ['Week', 'Week 1 wks ago', 'Week 2 wks ago', 'Week 3 wks ago', 'Week 4 wks ago', 'Week 5 wks ago',
              'Week 6 wks ago'#, 'Week 7 wks ago', 'Week 8 wks ago', 'Week 9 wks ago', 'Week 10 wks ago',
             ]

        year = ['Year', 'year 1 wks ago', 'year 2 wks ago', 'year 3 wks ago', 'year 4 wks ago', 'year 5 wks ago',
               'year 6 wks ago'#, 'year 7 wks ago', 'year 8 wks ago', 'year 9 wks ago', 'year 10 wks ago',
               ]
        
        
        for i in range(0,7):
            opp_colname = opp[i]
            wk_colname = wk[i]
            year_colname = year[i]#.astype(int)
            qb_df[wk_colname] = qb_df[wk_colname].astype(str).str.replace('.0', '',regex=False)
            
            qb_df[year_colname] = qb_df[year_colname].astype(str).str.replace('.0', '',regex=False)
            opp_wk_year_colname = opp_wk_year[i]
            if (i== 0):
                qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str) + " " + qb_df[year_colname].astype(str)#.str.replace('.0', '',regex=False)
            else:
                #qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str).str[:-2] + " " + qb_df[year_colname].astype(str)
                qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str) + " " + qb_df[year_colname].astype(str)#.str.replace('.0','', regex=False)
        
        #if (i == 0):

        test_df = qb_df[['player_wk_year','opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago', 'opp 3 wk year ago',
              'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago'#, 'opp 7 wk year ago',
                        ]]
        print(test_df.shape)
        new_df = pd.DataFrame()

        for i in range(0,7):
            #print(i)
            if (i == 0):
                #new_df = df_qb2
                #test_df2 = test_df.drop(columns = [])
                new_df = pd.merge(test_df, def_df, how = 'left', left_on = ['opp wk year'], right_on = ['team_wk_year'], suffixes = (None, None))
                new_df = new_df.drop(columns = ['team_wk_year'])
                #print(new_df.head())
            else:
                temp_df = def_df.drop(columns = ['Week','week_num','year','Opp','team_wk_year'])
              #  temp_df2 = temp_df
                for col in temp_df.columns:
                    new_col = 'opp' + " " + col + " " + str(i) + 'wks ago'
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                #merge_column = "player " + str(i) + " wks ago"
                #merge_column = 
                temp_df['team_wk_year'] = def_df['team_wk_year']
               # print(temp_df2.head())
                qb_no_null = test_df[[opp_wk_year[i]]]
               # print(qb_no_null.head())
                qb_no_null = qb_no_null[qb_no_null.notnull()]
              #  print(qb_no_null.head())
                qb_no_null = pd.merge(qb_no_null, temp_df, how = 'inner', left_on = [opp_wk_year[i]], right_on = ['team_wk_year'], suffixes = (None,None))
                #print(qb_no_null.head())
                qb_no_null = qb_no_null.drop_duplicates()
        
                qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
                new_df = pd.merge(new_df, qb_no_null, how = 'left', left_on = [opp_wk_year[i]], right_on = ['team_wk_year'], suffixes = (None, None))
                new_df = new_df.drop(columns = ['team_wk_year'])
        
        new_df = new_df.drop_duplicates()
        
        qb_df2 = qb_df.drop(columns = ['Week', 'Opp', 'opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago',
           'opp 3 wk year ago', 'opp 4 wk year ago', 'opp 5 wk year ago',
           'opp 6 wk year ago'#, 'opp 7 wk year ago', 'opp 8 wk year ago',
                                      ])
        

        new_df2 = pd.merge(qb_df2,new_df, how = 'left', on = 'player_wk_year', suffixes = (None,None))
        print(new_df2.shape)
        test_df = def_df[['CITY','week_num', 'year', 'team_wk_year']]
        for i in range(1,7):
            #print(i)
            wks_ago = i
            week_num_wks_ago = "week num " + str(i) + " wks ago"
            year_wks_ago = "year " + str(i) + " wks ago"
            #player_wks_ago = "player " + str(i) + " wks ago"
            team_wk_year = 'team_wk_year ' + str(i) + " wks ago"
            if(i == 1):
                curr_wk = "week_num"
                curr_yr = "year"
                test_df[curr_wk] = test_df['week_num']
                test_df[curr_yr] = test_df['year']
                test_df[week_num_wks_ago] = np.where(test_df[curr_wk] == 1, 17, test_df[curr_wk] - 1)
                test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
            else:
                curr_wk = "week num " + str(i-1) + " wks ago"
                curr_yr = "year " + str(i-1) + " wks ago"
                test_df[week_num_wks_ago] = np.where(test_df[curr_wk] == 1, 17, test_df[curr_wk]-1)
                test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr] -1, test_df[curr_yr])

            test_df[team_wk_year] = test_df['CITY'] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)
        
        return new_df2



def position_feat_eng_df_creation2(new_df2, def_df, position,
                                  #file_save
                                  ):
        nfl_sched = get_nfl_sched()#pd.read_csv('C:/Users/bobbr/OneDrive/Documents/The Plan/NFL/NFL Schedule.csv')
        a = list(nfl_sched['TEAM'].unique())
        test_df2 = pd.DataFrame()
        for p in a:
           # print(p)
            team_name_df = nfl_sched[(nfl_sched['TEAM']==p) &
                                    (nfl_sched['Opponent'] != 'BYE')]
            team_name_df=team_name_df.sort_values(by = ['Year','Week'],
                                                 ascending = [True, True])
            team_name_df['team_wk_year'] = team_name_df['TEAM'] + " " + team_name_df['Week'].astype(str) + " " + team_name_df['Year'].astype(str)

            for i in range(1,7):
          #      print(i)
                wks_ago = i
                week_num_wks_ago = 'week num ' + str(i) + " wks ago"
                year_wks_ago = "year " + str(i) + " wks ago"
                team_wks_ago = "team_wk_year " + str(i) + " wks ago"

                if (i == 1):
                    team_name_df[team_wks_ago] = [np.nan] + list(team_name_df['team_wk_year'])[:-1]
                   # team_name_df[week_num_wks_ago] = [np.nan] + list(team_name_df['Week'])[:-1]
                   # team_name_df[year_wks_ago] = [np.nan] + list(team_name_df["Year"])[:-1]

                elif ( i > 1):
                    team_name_df[team_wks_ago] = [np.nan]+list(team_name_df[prior_team_prev_game_player])[:-1]
                   # team_name_df[week_num_wks_ago] = [np.nan]+list(team_name_df[prior_week_num_prev_game_played])[:-1]
                   # team_name_df[year_wks_ago] = [np.nan]+list(team_name_df[prior_year_prev_game_played])[:-1]

                prior_prev_games_played_ago = i
                #prior_week_num_prev_game_played = "week num " + str(i) + " wks ago"
                #prior_year_prev_game_played =  "year " + str(i) + " wks ago"
                prior_team_prev_game_player = "team_wk_year " + str(i) + " wks ago" 

            test_df2 = test_df2.append(team_name_df)
    
            
        test_df=test_df2
        new_def_df = pd.DataFrame()
      #  return test_df
        for i in range(0,7):
            #print(i)
            if (i == 0):
                #new_df = df_qb2
                #test_df = test_df.drop(columns = ['CITY','week_num','year'])
                test_df = test_df.drop(columns = ['TEAM','Week','Year','Opponent'])

                new_def_df = pd.merge(def_df, test_df, how = 'left', on = ['team_wk_year'], suffixes = (None, None))
              #  new_def_df = new_def_df.drop(columns = ['team_wk_year'])
                new_def_df = new_def_df.drop_duplicates(subset=['team_wk_year'], keep='last')
                
                print(new_def_df.head())
            else:
                #temp_df = def_df.drop(columns = ['Team','CITY','Week','week_num','year'])
                temp_df = def_df.drop(columns = ['Team','CITY','Week','week_num','year'])

              #  temp_df2 = temp_df
                for col in temp_df.columns:
                    new_col = 'def matchup' + " " + col + " " + str(i) + 'wks ago'
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                #merge_column = "player " + str(i) + " wks ago"
                #merge_column = 
                merge_column = "team_wk_year " + str(i) + " wks ago"
                temp_df[merge_column] = def_df['team_wk_year']
                #temp_df['team_wk_year'] = def_df['team_wk_year']
               # qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
                temp_df = temp_df.drop_duplicates(subset=[merge_column], keep='last')
                temp_df = temp_df.drop_duplicates()
                new_def_df = pd.merge(new_def_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
               # new_def_df = new_def_df.drop(columns = ['team_wk_year'])

        
        new_def_df2 = new_def_df.drop(columns = [#'week num 1 wks ago', 'year 1 wks ago', 'week num 2 wks ago',
                    'Team', 'CITY', 'Week', 'Sack', 'FR', 'INT', 'DefTD',
               'PA', 'PaYD', 'RuYd', 'Safety', 'KickTD', 'FPts', 'week_num',
               'year', 'Opp', 'away flag', 'opp_wk_year'
                                                ])
        
        new_df3 = pd.merge(new_df2,new_def_df2,how = 'left', left_on = ['opp wk year'], right_on = ['team_wk_year'], suffixes = (None,None))
        print(new_df3.shape)
        #new_df3.to_csv(file_save)
        return new_df3

def create_qb_trend_var(qb_df, position#, file_save
                       ):
    qb_df = qb_df.drop(columns = [#'Unnamed: 0',
                                  'week num 1 wks ago',
        'year 1 wks ago','player 1 wks ago','week num 2 wks ago','year 2 wks ago',
        'player 2 wks ago','week num 3 wks ago','year 3 wks ago','player 3 wks ago',
        'week num 4 wks ago','year 4 wks ago','player 4 wks ago','week num 5 wks ago',
         'year 5 wks ago','player 5 wks ago','week num 6 wks ago','year 6 wks ago',
         'player 6 wks ago',#'week num 7 wks ago','year 7 wks ago','player 7 wks ago',
        'opp 1 wk year ago','opp 2 wk year ago',
        'opp 3 wk year ago','opp 4 wk year ago','opp 5 wk year ago','opp 6 wk year ago'#,
        ])
    qb_df = qb_df.drop_duplicates()
    print(qb_df.shape)
    
    print('trend 1 creation')
    trend = [2,3,4,5,6]#,9,12,15,18,24,30]
    temp_df = qb_df[['player_wk_year']]    
    temp_df2 = pd.DataFrame()     
    features = ['opp Sack', 'opp FR', 'opp INT', 'opp DefTD', 'opp PA', 'opp PaYD', 'opp RuYd',
       'opp Safety', 'opp KickTD', 'opp FPts']#, 'opp away flag']

    
    for feat in features:
        for i in range(1,7):
            fillna_col = feat + " " + str(i) + "wks ago"
            qb_df[fillna_col] = qb_df[fillna_col].fillna(0)
            qb_df[fillna_col] = qb_df[fillna_col].astype('float')#*100
            newcol_i = "new col " + str(i)
            temp_df2[newcol_i] = qb_df[fillna_col]#*100
        for t in trend:
        
            newcol_sum = "sum " + feat + " " + str(t) + "wk trend"
            newcol_avg = "avg " + feat + " " + str(t) + "wk trend"
            newcol_min = "min " + feat + " " + str(t) + "wk trend"
            newcol_max = "max " + feat + " " + str(t) + "wk trend"
            if (t == 2):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2']].sum(skipna= False, axis = 1) #* 100
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2']].mean(skipna= False, axis = 1) #* 100
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2']].max(skipna= False, axis = 1) #* 100 
            if (t == 3):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3']].max(skipna= False, axis = 1) #* 100
            if (t == 4):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].max(skipna= False, axis = 1) #* 100     
            if (t == 5):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].max(skipna= False, axis = 1) #* 100     
            if (t == 6):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].max(skipna= False, axis = 1) #* 100     

    qb_df = pd.merge(qb_df, temp_df, how = 'inner', on= 'player_wk_year', suffixes = (None,None))
    qb_df = qb_df.drop_duplicates()
    print(qb_df.shape)
    
    print('trend 2 creation')

    trend = [2,3,4,5,6]#,9,12,15,18,24,30]
    temp_df = qb_df[['player_wk_year']]    
    temp_df2 = pd.DataFrame()     
    if (position == 'QB'):
        
        features = ['Fumbles FF','Fumbles FL','Fumbles FR','Fumbles Fmb',
        'Fumbles TD','Fumbles Yds','Off. Snaps Num','Off. Snaps Pct','Passing AY/A',
        'Passing Att','Passing Cmp','Passing Cmp%','Passing Int','Passing Rate',
        'Passing Sk','Passing TD','Passing Y/A','Passing Yds',
        'Rushing Att','Rushing TD','Rushing Y/A','Rushing Yds',#'ST Snaps Num',
        #'ST Snaps Pct',
                    'Scoring 2PM','Scoring Pts','Scoring TD'#,
        #'Age'
                   ]
    elif(position == 'RB' or position == 'WR'):
        
        features = ['Fumbles FF','Fumbles FL','Fumbles FR','Fumbles Fmb',
        'Fumbles TD','Fumbles Yds','Kick Returns Rt','Kick Returns TD',
        'Kick Returns Y/Rt','Kick Returns Yds','Off. Snaps Num','Off. Snaps Pct',
        'Punt Returns Ret','Punt Returns TD','Punt Returns Y/R','Punt Returns Yds',
        'Receiving Ctch%','Receiving Rec','Receiving TD','Receiving Tgt',
        'Receiving Y/R','Receiving Y/Tgt','Receiving Yds','Rushing Att',
        'Rushing TD','Rushing Y/A','Rushing Yds','ST Snaps Num',
        'ST Snaps Pct','Scoring 2PM','Scoring Pts',#'Scoring Sfty',
        'Scoring TD','Age']
    
    elif(position == 'TE'):
        
        features = ['Fumbles FF','Fumbles FL','Fumbles FR','Fumbles Fmb',
        'Fumbles TD','Fumbles Yds','Off. Snaps Num','Off. Snaps Pct',
        'Receiving Ctch%','Receiving Rec','Receiving TD','Receiving Tgt',
        'Receiving Y/R','Receiving Y/Tgt','Receiving Yds','Rushing Att',
        'Rushing TD','Rushing Y/A','Rushing Yds','ST Snaps Num',
        'ST Snaps Pct','Scoring 2PM','Scoring Pts',#'Scoring Sfty',
        'Scoring TD','Age']    
    elif(position == 'K'):
        features = ['ScoringXPM', 'ScoringXPA', 'ScoringXP%',
                    'ScoringFGM', 'ScoringFGA', 'ScoringFG%', 'Scoring Pts','Age']        
        


        
    #for feat in features:
    #    qb_df[feat] = qb_df[feat].astype('float')

    for feat in features:
        for i in range(1,7):
            fillna_col = feat + " " + str(i) + " wks ago"
            qb_df[fillna_col] = qb_df[fillna_col].fillna(0)
            if (feat == 'Off. Snaps Pct' or feat == 'Receiving Ctch%' or
               feat == 'ST Snaps Pct' or 'Passing Cmp%'):
                qb_df[fillna_col] = qb_df[fillna_col].astype(str)
                qb_df[fillna_col] = qb_df[fillna_col].str.rstrip('%').astype('float')#/100.0
            else:   
                #print('not feat')
                qb_df[fillna_col] = qb_df[fillna_col].astype('float')
            newcol_i = "new col " + str(i)
            temp_df2[newcol_i] = qb_df[fillna_col]#*100
        for t in trend:
        
            newcol_sum = "sum " + feat + " " + str(t) + "wk trend"
            newcol_avg = "avg " + feat + " " + str(t) + "wk trend"
            newcol_min = "min " + feat + " " + str(t) + "wk trend"
            newcol_max = "max " + feat + " " + str(t) + "wk trend"
            if (t == 2):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2']].sum(skipna= False, axis = 1)  #* 100
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2']].mean(skipna= False, axis = 1)  #* 100
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2']].max(skipna= False, axis = 1) #* 100 
            if (t == 3):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3']].max(skipna= False, axis = 1) #* 100
            if (t == 4):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].max(skipna= False, axis = 1) #* 100     
            if (t == 5):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].max(skipna= False, axis = 1)# * 100     
            if (t == 6):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].max(skipna= False, axis = 1) #* 100     

    print('merge 2')
    qb_df = pd.merge(qb_df, temp_df, how = 'inner', on= 'player_wk_year', suffixes = (None,None))
    qb_df = qb_df.drop_duplicates()

    print(qb_df.shape)

    print('trend 3 creation')
    
    trend = [2,3,4,5,6]#,9,12,15,18,24,30]
    temp_df = qb_df[['player_wk_year']]    
    temp_df2 = pd.DataFrame()     
    features = ['def matchup Sack','def matchup FR',
    'def matchup INT','def matchup DefTD',
    'def matchup PA','def matchup PaYD',
    'def matchup RuYd','def matchup Safety',
    'def matchup KickTD','def matchup FPts']#,
    #'def matchup Opp',
                #'def matchup away flag']
    
   # for feat in features:
   #     qb_df[feat] = qb_df[feat].astype('float')

    for feat in features:
        for i in range(1,7):
            fillna_col = feat + " " + str(i) + "wks ago"
            qb_df[fillna_col] = qb_df[fillna_col].fillna(0)
            qb_df[fillna_col] = qb_df[fillna_col].astype('float')
            newcol_i = "new col " + str(i)
            temp_df2[newcol_i] = qb_df[fillna_col]
        for t in trend:
        
            newcol_sum = "sum " + feat + " " + str(t) + "wk trend"
            newcol_avg = "avg " + feat + " " + str(t) + "wk trend"
            newcol_min = "min " + feat + " " + str(t) + "wk trend"
            newcol_max = "max " + feat + " " + str(t) + "wk trend"
            if (t == 2):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2']].sum(skipna= False, axis = 1)  #* 100
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2']].mean(skipna= False, axis = 1)  #* 100
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2']].max(skipna= False, axis = 1) #* 100 
            if (t == 3):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3']].max(skipna= False, axis = 1) #* 100
            if (t == 4):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].max(skipna= False, axis = 1) #* 100     
            if (t == 5):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].max(skipna= False, axis = 1) #* 100     
            if (t == 6):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].sum(skipna= False, axis = 1) #* 100 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].mean(skipna= False, axis = 1) #* 100 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].min(skipna= False, axis = 1) #* 100 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].max(skipna= False, axis = 1) #* 100     

    print('merge 3')
    qb_df = pd.merge(qb_df, temp_df, how = 'inner', on= 'player_wk_year', suffixes = (None,None))
    qb_df = qb_df.drop_duplicates()

    print(qb_df.shape)

    #qb_df.to_csv(file_save)
    return qb_df

def def_feat_eng_df_creation(def_df,
                                # file_save
                            ):
                
    def_df['Opp'] = def_df["Opp"].str.replace("@","")
    def_df['opp_wk_year'] = def_df['Opp'] + " " + def_df['week_num'].astype(str) + " " + def_df['year'].astype(str)    

    tms = ['Tm','Tm 1 wks ago', 'Tm 2 wks ago',
              'Tm 3 wks ago','Tm 4 wks ago','Tm 5 wks ago','Tm 6 wks ago'
          ]

    opp = ['Opp','Opp 1 wks ago', 'Opp 2 wks ago',
              'Opp 3 wks ago','Opp 4 wks ago','Opp 5 wks ago','Opp 6 wks ago'
          ]

        #opp
    opp_wk_year = ['opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago', 'opp 3 wk year ago',
              'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago']

    wk = ['Week', 'Week 1 wks ago', 'Week 2 wks ago', 'Week 3 wks ago', 'Week 4 wks ago', 'Week 5 wks ago',
              'Week 6 wks ago'
         ]

    year = ['Year', 'year 1 wks ago', 'year 2 wks ago', 'year 3 wks ago', 'year 4 wks ago', 'year 5 wks ago',
               'year 6 wks ago'
           ]
        
    test_df = def_df[['CITY','week_num', 'year', 'team_wk_year']]
    for i in range(1,7):
        print(i)
        wks_ago = i
        week_num_wks_ago = "week num " + str(i) + " wks ago"
        year_wks_ago = "year " + str(i) + " wks ago"
        player_wks_ago = "team_wk_year " + str(i) + " wks ago"
        if(i == 1):
            curr_wk = "week_num"
            curr_yr = "year"
            test_df[curr_wk] = test_df['week_num']
            test_df[curr_yr] = test_df['year']
            test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
                                             np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
            test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
        else:
            curr_wk = "week num " + str(i-1) + " wks ago"
            curr_yr = "year " + str(i-1) + " wks ago"
            test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
                                             np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
            test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
        test_df[player_wks_ago] = test_df['CITY'] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)

            
    new_def_df = pd.DataFrame()

    for i in range(0,7):
        print(i)
        if (i == 0):
            #new_df = df_qb2
            test_df = test_df.drop(columns = ['CITY','week_num','year'])
            new_def_df = pd.merge(def_df, test_df, how = 'left', on = ['team_wk_year'], suffixes = (None, None))
          #  new_def_df = new_def_df.drop(columns = ['team_wk_year'])
            print(new_def_df.head())
        else:
            temp_df = def_df.drop(columns = ['Team','CITY','Week','week_num','year'])
      #  temp_df2 = temp_df
            for col in temp_df.columns:
                new_col = 'def matchup' + " " + col + " " + str(i) + 'wks ago'
                temp_df[new_col] = temp_df[col]
                temp_df = temp_df.drop(columns = [col])
        #merge_column = "player " + str(i) + " wks ago"
        #merge_column = 
            merge_column = "team_wk_year " + str(i) + " wks ago"
            temp_df[merge_column] = def_df['team_wk_year']
        #temp_df['team_wk_year'] = def_df['team_wk_year']
       # qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
            new_def_df = pd.merge(new_def_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
        #new_def_df = new_def_df.drop(columns = ['team_wk_year'])

        
    new_def_df2 = new_def_df.drop(columns = ['week num 1 wks ago', 'year 1 wks ago', 'week num 2 wks ago',
           'year 2 wks ago', 'week num 3 wks ago', 'year 3 wks ago',
           'week num 4 wks ago', 'year 4 wks ago', 'week num 5 wks ago',
           'year 5 wks ago', 'week num 6 wks ago', 'year 6 wks ago',
            'Sack', 'FR', 'INT', 'DefTD',
           'PA', 'PaYD', 'RuYd', 'Safety', 'KickTD',
          'PA', 'away flag'
                                 ]) 
            
    test_df = def_df[['Opp','week_num', 'year', 'opp_wk_year']]
    for i in range(1,7):
        print(i)
        wks_ago = i
        week_num_wks_ago = "week num " + str(i) + " wks ago"
        year_wks_ago = "year " + str(i) + " wks ago"
        #player_wks_ago = "player " + str(i) + " wks ago"
        team_wk_year = 'opp_wk_year ' + str(i) + " wks ago"
        if(i == 1):
            curr_wk = "week_num"
            curr_yr = "year"
            test_df[curr_wk] = test_df['week_num']
            test_df[curr_yr] = test_df['year']
            test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
                                             np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
            test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
        else:
            curr_wk = "week num " + str(i-1) + " wks ago"
            curr_yr = "year " + str(i-1) + " wks ago"
            test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
                                             np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
            test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])

        test_df[team_wk_year] = test_df['Opp'] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)

    test_df.head()
    test_df = test_df.drop_duplicates()    
        
    new_def_df = pd.DataFrame()
    print("test")
    for i in range(0,7):
        print(i)
        if (i == 0):
        #new_df = df_qb2
            test_df = test_df.drop(columns = ['Opp','week_num','year'])
            new_def_df = pd.merge(def_df, test_df, how = 'left', on = ['opp_wk_year'], suffixes = (None, None))
      #  new_def_df = new_def_df.drop(columns = ['team_wk_year'])
            print(new_def_df.head())
        else:
            temp_df = def_df.drop(columns = ['Team','Opp','Week','week_num','year'])
      #  temp_df2 = temp_df
            for col in temp_df.columns:
                new_col = 'opp matchup' + " " + col + " " + str(i) + 'wks ago'
                temp_df[new_col] = temp_df[col]
                temp_df = temp_df.drop(columns = [col])
        #merge_column = "player " + str(i) + " wks ago"
        #merge_column = 
            merge_column = "opp_wk_year " + str(i) + " wks ago"
            temp_df[merge_column] = def_df['opp_wk_year']
        #temp_df['team_wk_year'] = def_df['team_wk_year']
       # qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
            new_def_df = pd.merge(new_def_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
            new_def_df = new_def_df.drop_duplicates(subset=merge_column, keep = 'first')
            print(new_def_df.shape)
        #new_def_df = new_def_df.drop(columns = ['team_wk_year'])

        
    new_def_df3 = new_def_df.drop(columns = ['week num 1 wks ago', 'year 1 wks ago', 'week num 2 wks ago',
       'year 2 wks ago', 'week num 3 wks ago', 'year 3 wks ago',
       'week num 4 wks ago', 'year 4 wks ago', 'week num 5 wks ago',
       'year 5 wks ago', 'week num 6 wks ago', 'year 6 wks ago',
        'Team', 'CITY', 'Week', 'Sack', 'FR', 'INT', 'DefTD',
       'PA', 'PaYD', 'RuYd', 'Safety', 'KickTD',
        'FPts', 'team_wk_year', 'PA', 'week_num',
       'year', 'Opp', 'away flag'])
       
        
    new_def_df4 = pd.merge(new_def_df2, new_def_df3, how = 'inner', on = 'opp_wk_year', suffixes = (None,None))

   
    trend = [2,3,4,5,6]
    temp_df = new_def_df4[['team_wk_year']]    
    temp_df2 = pd.DataFrame()     
    features = ['opp matchup Sack', 'opp matchup FR', 'opp matchup INT', 'opp matchup DefTD', 'opp matchup PA',
            'opp matchup PaYD', 'opp matchup RuYd',
       'opp matchup Safety', 'opp matchup KickTD', 'opp matchup FPts'#, #'opp matchup away flag',
           #'opp matchup PA'
               ]

    for feat in features:
        for i in range(1,7):
            fillna_col = feat + " " + str(i) + "wks ago"
            new_def_df4[fillna_col] = new_def_df4[fillna_col].fillna(0)
            new_def_df4[fillna_col] = new_def_df4[fillna_col].astype('float')
            newcol_i = "new col " + str(i)
            temp_df2[newcol_i] = new_def_df4[fillna_col]
        for t in trend:
        
            newcol_sum = "sum " + feat + " " + str(t) + "wk trend"
            newcol_avg = "avg " + feat + " " + str(t) + "wk trend"
            newcol_min = "min " + feat + " " + str(t) + "wk trend"
            newcol_max = "max " + feat + " " + str(t) + "wk trend"
            if (t == 2):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2']].max(skipna= False, axis = 1) 
            if (t == 3):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3']].max(skipna= False, axis = 1)
            if (t == 4):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].max(skipna= False, axis = 1)     
            if (t == 5):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].max(skipna= False, axis = 1)     
            if (t == 6):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].max(skipna= False, axis = 1)     

        
    new_def_df4 = pd.merge(new_def_df4, temp_df, how = 'inner', on= 'team_wk_year', suffixes = (None,None))        
    
    
    trend = [2,3,4,5,6]
    temp_df = new_def_df4[['team_wk_year']]    
    temp_df2 = pd.DataFrame()     
    features = ['def matchup Sack',
    'def matchup FR',
    'def matchup INT',
    'def matchup DefTD',
    'def matchup PA',
    'def matchup PaYD',
    'def matchup RuYd',
    'def matchup Safety',
    'def matchup KickTD',
    'def matchup FPts'#,
    #'def matchup Opp',
    #'def matchup away flag',
     #      'def matchup PA'
               ]

    for feat in features:
        for i in range(1,7):
            fillna_col = feat + " " + str(i) + "wks ago"
            new_def_df4[fillna_col] = new_def_df4[fillna_col].fillna(0)
            new_def_df4[fillna_col] = new_def_df4[fillna_col].astype('float')
            newcol_i = "new col " + str(i)
            temp_df2[newcol_i] = new_def_df4[fillna_col]
        for t in trend:
        
            newcol_sum = "sum " + feat + " " + str(t) + "wk trend"
            newcol_avg = "avg " + feat + " " + str(t) + "wk trend"
            newcol_min = "min " + feat + " " + str(t) + "wk trend"
            newcol_max = "max " + feat + " " + str(t) + "wk trend"
            if (t == 2):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2']].max(skipna= False, axis = 1) 
            if (t == 3):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3']].max(skipna= False, axis = 1)
            if (t == 4):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].max(skipna= False, axis = 1)     
            if (t == 5):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].max(skipna= False, axis = 1)     
            if (t == 6):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].max(skipna= False, axis = 1)     


    new_def_df4 = pd.merge(new_def_df4, temp_df, how = 'inner', on= 'team_wk_year', suffixes = (None,None))
    new_def_df4 = new_def_df4.drop_duplicates()
    #new_def_df4.to_csv(file_save)
    
    return new_def_df4

def def_feat_eng_df_creation_v2(def_df,
                                # file_save
                            ):
                
    def_df['Opp'] = def_df["Opp"].str.replace("@","")
    def_df['opp_wk_year'] = def_df['Opp'] + " " + def_df['week_num'].astype(str) + " " + def_df['year'].astype(str)    

    tms = ['Tm','Tm 1 wks ago', 'Tm 2 wks ago',
              'Tm 3 wks ago','Tm 4 wks ago','Tm 5 wks ago','Tm 6 wks ago'
          ]

    opp = ['Opp','Opp 1 wks ago', 'Opp 2 wks ago',
              'Opp 3 wks ago','Opp 4 wks ago','Opp 5 wks ago','Opp 6 wks ago'
          ]

        #opp
    opp_wk_year = ['opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago', 'opp 3 wk year ago',
              'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago']

    wk = ['Week', 'Week 1 wks ago', 'Week 2 wks ago', 'Week 3 wks ago', 'Week 4 wks ago', 'Week 5 wks ago',
              'Week 6 wks ago'
         ]

    year = ['Year', 'year 1 wks ago', 'year 2 wks ago', 'year 3 wks ago', 'year 4 wks ago', 'year 5 wks ago',
               'year 6 wks ago'
           ]
        
    test_df = def_df[['CITY','week_num', 'year', 'team_wk_year']]
        
    nfl_sched = get_nfl_sched()
    a = list(nfl_sched['TEAM'].unique())
    test_df2 = pd.DataFrame()
    
    for p in a:
        team_name_df = nfl_sched[(nfl_sched['TEAM']==p) & 
                                (nfl_sched['Opponent'] != 'BYE')]
        team_name_df = team_name_df.sort_values(by = ['Year','Week'],
                                               ascending = [True, True])
        team_name_df['team_wk_year'] = team_name_df['TEAM'] + " " + team_name_df['Week'].astype(str) + " " + team_name_df['Year'].astype(str)

        for i in range(1,7):

            wks_ago = i
            week_num_wks_ago = 'week num ' + str(i) + " wks ago"
            year_wks_ago = 'year ' + str(i) + " wks ago"
            team_wks_ago = 'team_wk_year ' + str(i) + " wks ago"

            if (i == 1):
                team_name_df[team_wks_ago] = [np.nan] + list(team_name_df['team_wk_year'])[:-1]

            elif (i > 1):

                team_name_df[team_wks_ago] = [np.nan]+list(team_name_df[prior_team_prev_game_player])[:-1]

            prior_prev_games_played_ago = i
            prior_team_prev_game_player = "team_wk_year " + str(i) + " wks ago"

        test_df2 = test_df2.append(team_name_df)

    test_df = test_df2
    
    
#     for i in range(1,7):
#         print(i)
#         wks_ago = i
#         week_num_wks_ago = "week num " + str(i) + " wks ago"
#         year_wks_ago = "year " + str(i) + " wks ago"
#         player_wks_ago = "team_wk_year " + str(i) + " wks ago"
#         if(i == 1):
#             curr_wk = "week_num"
#             curr_yr = "year"
#             test_df[curr_wk] = test_df['week_num']
#             test_df[curr_yr] = test_df['year']
#             test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
#                                              np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
#             test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
#         else:
#             curr_wk = "week num " + str(i-1) + " wks ago"
#             curr_yr = "year " + str(i-1) + " wks ago"
#             test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
#                                              np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
#             test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
#         test_df[player_wks_ago] = test_df['CITY'] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)

    #return test_df
            
    new_def_df = pd.DataFrame()

    for i in range(0,7):
    #    print(i)
        if (i == 0):
            #new_df = df_qb2
            test_df = test_df.drop(columns = ['Week'])#,'CITY','week_num','year'])
            new_def_df = pd.merge(def_df, test_df, how = 'left', on = ['team_wk_year'], suffixes = (None, None))
          #  new_def_df = new_def_df.drop(columns = ['team_wk_year'])
    #        print(new_def_df.head())
        else:
            temp_df = def_df.drop(columns = ['Team','CITY','Week','week_num','year'])
      #  temp_df2 = temp_df
            for col in temp_df.columns:
                new_col = 'def matchup' + " " + col + " " + str(i) + 'wks ago'
                temp_df[new_col] = temp_df[col]
                temp_df = temp_df.drop(columns = [col])
        #merge_column = "player " + str(i) + " wks ago"
        #merge_column = 
            merge_column = "team_wk_year " + str(i) + " wks ago"
            temp_df[merge_column] = def_df['team_wk_year']
        #temp_df['team_wk_year'] = def_df['team_wk_year']
       # qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
            new_def_df = pd.merge(new_def_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
        #new_def_df = new_def_df.drop(columns = ['team_wk_year'])

    #return new_def_df    
    new_def_df2 = new_def_df.drop(columns = [#'week num 1 wks ago', 'year 1 wks ago', 'week num 2 wks ago',
#            'year 2 wks ago', 'week num 3 wks ago', 'year 3 wks ago',
#            'week num 4 wks ago', 'year 4 wks ago', 'week num 5 wks ago',
#            'year 5 wks ago', 'week num 6 wks ago', 'year 6 wks ago',
            'Sack', 'FR', 'INT', 'DefTD',
           'PA', 'PaYD', 'RuYd', 'Safety', 'KickTD',
          'PA', 'away flag'
                                 ]) 
    
#    return new_def_df2

            
    test_df = def_df[['Opp','week_num', 'year', 'opp_wk_year']]
    
    nfl_sched = get_nfl_sched()
    nfl_sched['Opponent'] = nfl_sched["Opponent"].str.replace("@","")
    nfl_sched['opp_wk_year'] = nfl_sched['Opponent'] + " " + nfl_sched['Week'].astype(str) + " " + nfl_sched['Year'].astype(str)
    a = list(nfl_sched['Opponent'].unique())
    test_df2 = pd.DataFrame()
    
    for p in a:
        team_name_df = nfl_sched[(nfl_sched['Opponent']==p) & 
                                (nfl_sched['Opponent'] != 'BYE')]
        team_name_df = team_name_df.sort_values(by = ['Year','Week'],
                                               ascending = [True, True])
        #team_name_df['team_wk_year'] = team_name_df['TEAM'] + " " + team_name_df['Week'].astype(str) + " " + team_name_df['Year'].astype(str)
        for i in range(1,7):

            wks_ago = i
            week_num_wks_ago = 'week num ' + str(i) + " wks ago"
            year_wks_ago = 'year ' + str(i) + " wks ago"
            opp_wks_ago = 'opp_wk_year ' + str(i) + " wks ago"

            if (i == 1):
                team_name_df[opp_wks_ago] = [np.nan] + list(team_name_df['opp_wk_year'])[:-1]

            elif (i > 1):

                team_name_df[opp_wks_ago] = [np.nan]+list(team_name_df[prior_team_prev_game_player])[:-1]

            prior_prev_games_played_ago = i
            prior_team_prev_game_player = "opp_wk_year " + str(i) + " wks ago"

        test_df2 = test_df2.append(team_name_df)

    test_df = test_df2
    
    #return test_df
    
#     for i in range(1,7):
#         print(i)
#         wks_ago = i
#         week_num_wks_ago = "week num " + str(i) + " wks ago"
#         year_wks_ago = "year " + str(i) + " wks ago"
#         #player_wks_ago = "player " + str(i) + " wks ago"
#         team_wk_year = 'opp_wk_year ' + str(i) + " wks ago"
#         if(i == 1):
#             curr_wk = "week_num"
#             curr_yr = "year"
#             test_df[curr_wk] = test_df['week_num']
#             test_df[curr_yr] = test_df['year']
#             test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
#                                              np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
#             test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
#         else:
#             curr_wk = "week num " + str(i-1) + " wks ago"
#             curr_yr = "year " + str(i-1) + " wks ago"
#             test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
#                                              np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
#             test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])

#         test_df[team_wk_year] = test_df['Opp'] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)

#     test_df.head()
#     test_df = test_df.drop_duplicates()    
        
    new_def_df = pd.DataFrame()
   # print("test")
    for i in range(0,7):
   #     print(i)
        if (i == 0):
        #new_df = df_qb2
            test_df = test_df.drop(columns = ['Week'])#'Opp','week_num','year'])
            new_def_df = pd.merge(def_df, test_df, how = 'left', on = ['opp_wk_year'], suffixes = (None, None))
      #  new_def_df = new_def_df.drop(columns = ['team_wk_year'])
   #         print(new_def_df.head())
        else:
            temp_df = def_df.drop(columns = ['Team','Opp','Week','week_num','year'])
      #  temp_df2 = temp_df
            for col in temp_df.columns:
                new_col = 'opp matchup' + " " + col + " " + str(i) + 'wks ago'
                temp_df[new_col] = temp_df[col]
                temp_df = temp_df.drop(columns = [col])
        #merge_column = "player " + str(i) + " wks ago"
        #merge_column = 
            merge_column = "opp_wk_year " + str(i) + " wks ago"
            temp_df[merge_column] = def_df['opp_wk_year']
        #temp_df['team_wk_year'] = def_df['team_wk_year']
       # qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
            new_def_df = pd.merge(new_def_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
            new_def_df = new_def_df.drop_duplicates(subset=merge_column, keep = 'first')
      #      print(new_def_df.shape)
        #new_def_df = new_def_df.drop(columns = ['team_wk_year'])

        
    new_def_df3 = new_def_df.drop(columns = [#'week num 1 wks ago', 'year 1 wks ago', 'week num 2 wks ago',
       #'year 2 wks ago', 'week num 3 wks ago', 'year 3 wks ago',
       #'week num 4 wks ago', 'year 4 wks ago', 'week num 5 wks ago',
       #'year 5 wks ago', 'week num 6 wks ago', 'year 6 wks ago',
        'Team', 'CITY', 'Week', 'Sack', 'FR', 'INT', 'DefTD',
       'PA', 'PaYD', 'RuYd', 'Safety', 'KickTD',
        'FPts', 'team_wk_year', 'PA', 'week_num',
       'year', 'Opp', 'away flag',#'opp wk year',
    'Year','TEAM','Opponent'
    ])
    
    #return new_def_df3
       
        
    new_def_df4 = pd.merge(new_def_df2, new_def_df3, how = 'inner', on = 'opp_wk_year', suffixes = (None,None))
    #return new_def_df4
   
    trend = [2,3,4,5,6]
    temp_df = new_def_df4[['team_wk_year']]    
    temp_df2 = pd.DataFrame()     
    features = ['opp matchup Sack', 'opp matchup FR', 'opp matchup INT', 'opp matchup DefTD', 'opp matchup PA',
            'opp matchup PaYD', 'opp matchup RuYd',
       'opp matchup Safety', 'opp matchup KickTD', 'opp matchup FPts'#, #'opp matchup away flag',
           #'opp matchup PA'
               ]

    for feat in features:
        for i in range(1,7):
            fillna_col = feat + " " + str(i) + "wks ago"
            new_def_df4[fillna_col] = new_def_df4[fillna_col].fillna(0)
            new_def_df4[fillna_col] = new_def_df4[fillna_col].astype('float')
            newcol_i = "new col " + str(i)
            temp_df2[newcol_i] = new_def_df4[fillna_col]
        for t in trend:
        
            newcol_sum = "sum " + feat + " " + str(t) + "wk trend"
            newcol_avg = "avg " + feat + " " + str(t) + "wk trend"
            newcol_min = "min " + feat + " " + str(t) + "wk trend"
            newcol_max = "max " + feat + " " + str(t) + "wk trend"
            if (t == 2):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2']].max(skipna= False, axis = 1) 
            if (t == 3):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3']].max(skipna= False, axis = 1)
            if (t == 4):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].max(skipna= False, axis = 1)     
            if (t == 5):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].max(skipna= False, axis = 1)     
            if (t == 6):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].max(skipna= False, axis = 1)     

        
    new_def_df4 = pd.merge(new_def_df4, temp_df, how = 'inner', on= 'team_wk_year', suffixes = (None,None))        
    
    
    trend = [2,3,4,5,6]
    temp_df = new_def_df4[['team_wk_year']]    
    temp_df2 = pd.DataFrame()     
    features = ['def matchup Sack',
    'def matchup FR',
    'def matchup INT',
    'def matchup DefTD',
    'def matchup PA',
    'def matchup PaYD',
    'def matchup RuYd',
    'def matchup Safety',
    'def matchup KickTD',
    'def matchup FPts'#,
    #'def matchup Opp',
    #'def matchup away flag',
     #      'def matchup PA'
               ]

    for feat in features:
        for i in range(1,7):
            fillna_col = feat + " " + str(i) + "wks ago"
            new_def_df4[fillna_col] = new_def_df4[fillna_col].fillna(0)
            new_def_df4[fillna_col] = new_def_df4[fillna_col].astype('float')
            newcol_i = "new col " + str(i)
            temp_df2[newcol_i] = new_def_df4[fillna_col]
        for t in trend:
        
            newcol_sum = "sum " + feat + " " + str(t) + "wk trend"
            newcol_avg = "avg " + feat + " " + str(t) + "wk trend"
            newcol_min = "min " + feat + " " + str(t) + "wk trend"
            newcol_max = "max " + feat + " " + str(t) + "wk trend"
            if (t == 2):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2']].max(skipna= False, axis = 1) 
            if (t == 3):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3']].max(skipna= False, axis = 1)
            if (t == 4):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2', 'new col 3','new col 4']].max(skipna= False, axis = 1)     
            if (t == 5):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3','new col 4', 'new col 5']].max(skipna= False, axis = 1)     
            if (t == 6):
                temp_df[newcol_sum] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].sum(skipna= False, axis = 1) 
                temp_df[newcol_avg] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].mean(skipna= False, axis = 1) 
                temp_df[newcol_min] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].min(skipna= False, axis = 1) 
                temp_df[newcol_max] = temp_df2[['new col 1', 'new col 2','new col 3',
                                         'new col 4', 'new col 5','new col 6']].max(skipna= False, axis = 1)     


    new_def_df4 = pd.merge(new_def_df4, temp_df, how = 'inner', on= 'team_wk_year', suffixes = (None,None))
    new_def_df4 = new_def_df4.drop_duplicates()
    #new_def_df4.to_csv(file_save)
    
    return new_def_df4

def cleanup_final_df(df, position):
    if (position == 'QB'):
        df = df[df['GS']=='*']
        df = df.drop(columns = [
           #'Player ',
            'Rk','GS',#'Date','G#','Tm',
            #'home_away','Result',
            'Player  1 wks ago','Date 1 wks ago',
            'Week 1 wks ago','Tm 1 wks ago','home_away 1 wks ago','Opp 1 wks ago',
            'Result 1 wks ago', 'player_wk_year 1 wks ago', 
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago','Opp 2 wks ago',
            'Result 2 wks ago', 'player_wk_year 2 wks ago', 
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago','Opp 3 wks ago',
            'Result 3 wks ago', 'player_wk_year 3 wks ago', 
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago','Opp 4 wks ago',
            'Result 4 wks ago', 'player_wk_year 4 wks ago', 
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago','Opp 5 wks ago',
            'Result 5 wks ago', 'player_wk_year 5 wks ago', 
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago','Opp 6 wks ago',
            'Result 6 wks ago', 'player_wk_year 6 wks ago', 
            'opp wk year',#'Team','CITY',
            'week_num', 'year','Opp',
            'away flag','opp_wk_year','opp Team 1wks ago',
            'opp CITY 1wks ago','opp away flag 1wks ago',
            'opp opp_wk_year 1wks ago','opp Team 2wks ago','opp CITY 2wks ago',
            'opp CITY 2wks ago', 'opp away flag 2wks ago','opp opp_wk_year 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago',
            'opp CITY 3wks ago', 'opp away flag 3wks ago','opp opp_wk_year 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago',
            'opp CITY 4wks ago', 'opp away flag 4wks ago','opp opp_wk_year 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago',
            'opp CITY 5wks ago', 'opp away flag 5wks ago','opp opp_wk_year 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago',
            'opp CITY 6wks ago', 'opp away flag 6wks ago','opp opp_wk_year 6wks ago',
            'team_wk_year', 'team_wk_year 1 wks ago','team_wk_year 2 wks ago',
            'team_wk_year 3 wks ago', 'team_wk_year 4 wks ago','team_wk_year 5 wks ago',
            'team_wk_year 6 wks ago','def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago','def matchup opp_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago','def matchup opp_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago','def matchup opp_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago','def matchup opp_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago','def matchup opp_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','def matchup opp_wk_year 6wks ago',
            'sum Passing AY/A 2wk trend', 'sum Passing AY/A 3wk trend',
            'sum Passing AY/A 4wk trend', 'sum Passing AY/A 5wk trend',
            'sum Passing AY/A 6wk trend', 'sum Passing Cmp% 2wk trend',
            'sum Passing Cmp% 3wk trend','sum Passing Cmp% 4wk trend',
            'sum Passing Cmp% 5wk trend','sum Passing Cmp% 6wk trend',
            'sum Passing Rate 2wk trend','sum Passing Rate 3wk trend',
            'sum Passing Rate 4wk trend','sum Passing Rate 5wk trend',
            'sum Passing Rate 6wk trend','sum Passing Y/A 2wk trend',
            'sum Passing Y/A 3wk trend','sum Passing Y/A 4wk trend',
            'sum Passing Y/A 5wk trend','sum Passing Y/A 6wk trend',
            'sum Rushing Y/A 2wk trend','sum Rushing Y/A 3wk trend',
            'sum Rushing Y/A 4wk trend','sum Rushing Y/A 5wk trend',
            'sum Rushing Y/A 6wk trend'
        ])
    elif ((position == 'RB') | 
          (position == 'WR')):
        df['Year'] = df['Year'].astype(int)
        df = df[df['Year']>=2015]
        df = df.drop(columns = [
            #'Player ',
            'Rk','GS',#'Date','G#','Tm',
            #'home_away','Result',
            'Player  1 wks ago','Date 1 wks ago',
            'Week 1 wks ago','Tm 1 wks ago','home_away 1 wks ago','Opp 1 wks ago',
            'Result 1 wks ago', 'player_wk_year 1 wks ago', 
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago','Opp 2 wks ago',
            'Result 2 wks ago', 'player_wk_year 2 wks ago', 
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago','Opp 3 wks ago',
            'Result 3 wks ago', 'player_wk_year 3 wks ago', 
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago','Opp 4 wks ago',
            'Result 4 wks ago', 'player_wk_year 4 wks ago', 
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago','Opp 5 wks ago',
            'Result 5 wks ago', 'player_wk_year 5 wks ago', 
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago','Opp 6 wks ago',
            'Result 6 wks ago', 'player_wk_year 6 wks ago', 
            'opp wk year',#'Team','CITY',
            'week_num', 'year','Opp',
            'away flag','opp_wk_year','opp Team 1wks ago',
            'opp CITY 1wks ago','opp away flag 1wks ago',
            'opp opp_wk_year 1wks ago','opp Team 2wks ago','opp CITY 2wks ago',
            'opp CITY 2wks ago', 'opp away flag 2wks ago','opp opp_wk_year 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago',
            'opp CITY 3wks ago', 'opp away flag 3wks ago','opp opp_wk_year 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago',
            'opp CITY 4wks ago', 'opp away flag 4wks ago','opp opp_wk_year 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago',
            'opp CITY 5wks ago', 'opp away flag 5wks ago','opp opp_wk_year 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago',
            'opp CITY 6wks ago', 'opp away flag 6wks ago','opp opp_wk_year 6wks ago',
            'team_wk_year', 'team_wk_year 1 wks ago','team_wk_year 2 wks ago',
            'team_wk_year 3 wks ago', 'team_wk_year 4 wks ago','team_wk_year 5 wks ago',
            'team_wk_year 6 wks ago','def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago','def matchup opp_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago','def matchup opp_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago','def matchup opp_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago','def matchup opp_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago','def matchup opp_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','def matchup opp_wk_year 6wks ago',
            'sum Kick Returns Y/Rt 2wk trend', 'sum Kick Returns Y/Rt 3wk trend',
            'sum Kick Returns Y/Rt 4wk trend', 'sum Kick Returns Y/Rt 5wk trend', 
            'sum Kick Returns Y/Rt 6wk trend', 'sum Off. Snaps Pct 2wk trend',
            'sum Off. Snaps Pct 3wk trend', 'sum Off. Snaps Pct 4wk trend',
            'sum Off. Snaps Pct 5wk trend', 'sum Off. Snaps Pct 6wk trend',
            'sum Punt Returns Y/R 2wk trend','sum Punt Returns Y/R 3wk trend',
            'sum Punt Returns Y/R 4wk trend','sum Punt Returns Y/R 5wk trend',
            'sum Punt Returns Y/R 6wk trend', 'sum Receiving Ctch% 2wk trend',
            'sum Receiving Ctch% 3wk trend','sum Receiving Ctch% 4wk trend',
            'sum Receiving Ctch% 5wk trend','sum Receiving Ctch% 6wk trend',
            'sum Receiving Y/R 2wk trend','sum Receiving Y/R 3wk trend',
            'sum Receiving Y/R 4wk trend','sum Receiving Y/R 5wk trend',
            'sum Receiving Y/R 6wk trend', 'sum Receiving Y/Tgt 2wk trend',
            'sum Receiving Y/Tgt 3wk trend','sum Receiving Y/Tgt 4wk trend',
            'sum Receiving Y/Tgt 5wk trend','sum Receiving Y/Tgt 6wk trend',
            'sum Rushing Y/A 2wk trend','sum Rushing Y/A 3wk trend',
            'sum Rushing Y/A 4wk trend','sum Rushing Y/A 5wk trend',
            'sum Rushing Y/A 6wk trend', 'sum ST Snaps Pct 2wk trend',
            'sum ST Snaps Pct 3wk trend','sum ST Snaps Pct 4wk trend',
            'sum ST Snaps Pct 5wk trend','sum ST Snaps Pct 6wk trend'
        ])
    elif(position == 'TE'):
        df['Year'] = df['Year'].astype(int)
        df = df[df['Year']>=2015]
        df = df.drop(columns = [#'Player ',
            'Rk','GS',#'Date','G#','Tm',
            #'home_away','Result',
            'Player  1 wks ago','Date 1 wks ago',
            'Week 1 wks ago','Tm 1 wks ago','home_away 1 wks ago','Opp 1 wks ago',
            'Result 1 wks ago', 'player_wk_year 1 wks ago', 
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago','Opp 2 wks ago',
            'Result 2 wks ago', 'player_wk_year 2 wks ago', 
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago','Opp 3 wks ago',
            'Result 3 wks ago', 'player_wk_year 3 wks ago', 
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago','Opp 4 wks ago',
            'Result 4 wks ago', 'player_wk_year 4 wks ago', 
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago','Opp 5 wks ago',
            'Result 5 wks ago', 'player_wk_year 5 wks ago', 
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago','Opp 6 wks ago',
            'Result 6 wks ago', 'player_wk_year 6 wks ago', 
            'opp wk year',#'Team','CITY',
            'week_num', 'year','Opp',
            'away flag','opp_wk_year','opp Team 1wks ago',
            'opp CITY 1wks ago','opp away flag 1wks ago',
            'opp opp_wk_year 1wks ago','opp Team 2wks ago','opp CITY 2wks ago',
            'opp CITY 2wks ago', 'opp away flag 2wks ago','opp opp_wk_year 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago',
            'opp CITY 3wks ago', 'opp away flag 3wks ago','opp opp_wk_year 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago',
            'opp CITY 4wks ago', 'opp away flag 4wks ago','opp opp_wk_year 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago',
            'opp CITY 5wks ago', 'opp away flag 5wks ago','opp opp_wk_year 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago',
            'opp CITY 6wks ago', 'opp away flag 6wks ago','opp opp_wk_year 6wks ago',
            'team_wk_year', 'team_wk_year 1 wks ago','team_wk_year 2 wks ago',
            'team_wk_year 3 wks ago', 'team_wk_year 4 wks ago','team_wk_year 5 wks ago',
            'team_wk_year 6 wks ago','def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago','def matchup opp_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago','def matchup opp_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago','def matchup opp_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago','def matchup opp_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago','def matchup opp_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','def matchup opp_wk_year 6wks ago',
            'sum Off. Snaps Pct 2wk trend',
            'sum Off. Snaps Pct 3wk trend', 'sum Off. Snaps Pct 4wk trend',
            'sum Off. Snaps Pct 5wk trend', 'sum Off. Snaps Pct 6wk trend',
            'sum Receiving Ctch% 2wk trend',
            'sum Receiving Ctch% 3wk trend','sum Receiving Ctch% 4wk trend',
            'sum Receiving Ctch% 5wk trend','sum Receiving Ctch% 6wk trend',
            'sum Receiving Y/R 2wk trend','sum Receiving Y/R 3wk trend',
            'sum Receiving Y/R 4wk trend','sum Receiving Y/R 5wk trend',
            'sum Receiving Y/R 6wk trend', 'sum Receiving Y/Tgt 2wk trend',
            'sum Receiving Y/Tgt 3wk trend','sum Receiving Y/Tgt 4wk trend',
            'sum Receiving Y/Tgt 5wk trend','sum Receiving Y/Tgt 6wk trend',
            'sum Rushing Y/A 2wk trend','sum Rushing Y/A 3wk trend',
            'sum Rushing Y/A 4wk trend','sum Rushing Y/A 5wk trend',
            'sum Rushing Y/A 6wk trend', 'sum ST Snaps Pct 2wk trend',
            'sum ST Snaps Pct 3wk trend','sum ST Snaps Pct 4wk trend',
            'sum ST Snaps Pct 5wk trend','sum ST Snaps Pct 6wk trend'
        ])
    elif(position == 'K'):
        df['Year'] = df['Year'].astype(int)
        df = df[df['Year']>=2015]
        df = df.drop(columns = [#'Player ',
            'Rk','GS',#'Date','G#','Tm',
            #'home_away','Result',
            'Player  1 wks ago','Date 1 wks ago',
            'Week 1 wks ago','Tm 1 wks ago','home_away 1 wks ago','Opp 1 wks ago',
            'Result 1 wks ago', 'player_wk_year 1 wks ago', 
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago','Opp 2 wks ago',
            'Result 2 wks ago', 'player_wk_year 2 wks ago', 
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago','Opp 3 wks ago',
            'Result 3 wks ago', 'player_wk_year 3 wks ago', 
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago','Opp 4 wks ago',
            'Result 4 wks ago', 'player_wk_year 4 wks ago', 
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago','Opp 5 wks ago',
            'Result 5 wks ago', 'player_wk_year 5 wks ago', 
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago','Opp 6 wks ago',
            'Result 6 wks ago', 'player_wk_year 6 wks ago', 
            'opp wk year',#'Team','CITY',
            'week_num', 'year','Opp',
            'away flag','opp_wk_year','opp Team 1wks ago',
            'opp CITY 1wks ago','opp away flag 1wks ago',
            'opp opp_wk_year 1wks ago','opp Team 2wks ago','opp CITY 2wks ago',
            'opp CITY 2wks ago', 'opp away flag 2wks ago','opp opp_wk_year 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago',
            'opp CITY 3wks ago', 'opp away flag 3wks ago','opp opp_wk_year 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago',
            'opp CITY 4wks ago', 'opp away flag 4wks ago','opp opp_wk_year 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago',
            'opp CITY 5wks ago', 'opp away flag 5wks ago','opp opp_wk_year 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago',
            'opp CITY 6wks ago', 'opp away flag 6wks ago','opp opp_wk_year 6wks ago',
            'team_wk_year', 'team_wk_year 1 wks ago','team_wk_year 2 wks ago',
            'team_wk_year 3 wks ago', 'team_wk_year 4 wks ago','team_wk_year 5 wks ago',
            'team_wk_year 6 wks ago','def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago','def matchup opp_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago','def matchup opp_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago','def matchup opp_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago','def matchup opp_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago','def matchup opp_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','def matchup opp_wk_year 6wks ago',
            'sum ScoringXP% 2wk trend','sum ScoringXP% 3wk trend',
            'sum ScoringXP% 4wk trend','sum ScoringXP% 5wk trend',
            'sum ScoringXP% 6wk trend', 'sum ScoringFG% 2wk trend',
            'sum ScoringFG% 3wk trend', 'sum ScoringFG% 4wk trend',
            'sum ScoringFG% 5wk trend', 'sum ScoringFG% 6wk trend'
        ])
    elif(position=='D'):
        df['year'] = df['year'].astype(int)
        df = df[df['year']>2016]
        df = df.drop(columns = [
            'Team','CITY','Week',#'week_num','year','Opp',
            'opp_wk_year',
            'team_wk_year 1 wks ago', 'team_wk_year 2 wks ago',
            'team_wk_year 3 wks ago', 'team_wk_year 4 wks ago',
            'team_wk_year 5 wks ago', 'team_wk_year 6 wks ago',
            'def matchup Opp 1wks ago','def matchup Opp 2wks ago',
            'def matchup Opp 3wks ago','def matchup Opp 4wks ago',
            'def matchup Opp 5wks ago','def matchup Opp 6wks ago',
            'def matchup away flag 1wks ago', 'def matchup away flag 2wks ago',
            'def matchup away flag 3wks ago', 'def matchup away flag 4wks ago',
            'def matchup away flag 5wks ago', 'def matchup away flag 6wks ago',
            'def matchup team_wk_year 1wks ago', 'def matchup team_wk_year 2wks ago',
            'def matchup team_wk_year 3wks ago', 'def matchup team_wk_year 4wks ago',
            'def matchup team_wk_year 5wks ago', 'def matchup team_wk_year 6wks ago',
            'def matchup opp_wk_year 1wks ago', 'def matchup opp_wk_year 2wks ago',
            'def matchup opp_wk_year 3wks ago', 'def matchup opp_wk_year 4wks ago',
            'def matchup opp_wk_year 5wks ago', 'def matchup opp_wk_year 6wks ago',
            'opp_wk_year 1 wks ago', 'opp_wk_year 2 wks ago', 'opp_wk_year 3 wks ago',
            'opp_wk_year 4 wks ago', 'opp_wk_year 5 wks ago', 'opp_wk_year 6 wks ago',
            'opp matchup CITY 1wks ago', 'opp matchup CITY 2wks ago', 'opp matchup CITY 3wks ago',
            'opp matchup CITY 4wks ago', 'opp matchup CITY 5wks ago', 'opp matchup CITY 6wks ago',
            'opp matchup team_wk_year 1wks ago','opp matchup team_wk_year 2wks ago',
            'opp matchup team_wk_year 3wks ago','opp matchup team_wk_year 4wks ago',
            'opp matchup team_wk_year 5wks ago','opp matchup team_wk_year 6wks ago',
            'opp matchup opp_wk_year 1wks ago', 'opp matchup opp_wk_year 2wks ago',
            'opp matchup opp_wk_year 3wks ago', 'opp matchup opp_wk_year 4wks ago',
            'opp matchup opp_wk_year 5wks ago', 'opp matchup opp_wk_year 6wks ago',
            'opp matchup away flag 1wks ago', 'opp matchup away flag 2wks ago',
            'opp matchup away flag 3wks ago','opp matchup away flag 4wks ago',
            'opp matchup away flag 5wks ago','opp matchup away flag 6wks ago'#,
            #'opp wk year',
         #   'Year','TEAM','Opponent'#,
#             'def matchup opp wk year 1wks ago','def matchup opp wk year 2wks ago',
#             'def matchup opp wk year 3wks ago','def matchup opp wk year 4wks ago',
#             'def matchup opp wk year 5wks ago','def matchup opp wk year 6wks ago',
#             'opp matchup opp wk year 1wks ago','opp matchup opp wk year 2wks ago',
#             'opp matchup opp wk year 3wks ago','opp matchup opp wk year 4wks ago',
#             'opp matchup opp wk year 5wks ago','opp matchup opp wk year 6wks ago'
        ])
        
            
        
    return df

def data_prep_for_player_pull():
    year = get_current_year()
    week = get_current_week()
    test_fun = update_player_weekly_stats()
    nfl_sched = get_nfl_sched()#pd.read_csv('C:/Users/bobbr/OneDrive/Documents/The Plan/NFL/NFL Schedule.csv')

    test = def_weekly_stats_scrape(first_yr = 2015, last_yr = year, nfl_sched = nfl_sched)
    
    def_weekly = def_curr_wk_for_positions(def_df = test,
                    nfl_sched = nfl_sched,
                    curr_wk = week,
                    curr_yr = year)
    
    return year, week, test_fun, nfl_sched, test, def_weekly

    
def qb_all_data_pull(year, week, test_fun, nfl_sched,
                    test, def_weekly):
    
    df_qb = position_feat_eng_df_creation(player_df = test_fun,
                              def_df = test,
                              position = 'QB')
    df_qb2 = position_feat_eng_df_creation2(new_df2 = df_qb, 
                                        def_df = test,
                                        position = 'QB')
    test_final = create_qb_trend_var(qb_df=df_qb2,
                                 position = 'QB'#,
                                #file_save = 'qb_player_data_final.csv'
                                    )
    test_final2 = cleanup_final_df(df=test_final, position='QB')
    test_final2.to_csv('qb_player_data_final.csv')
    
    return test_final2


def rb_all_data_pull(year, week, test_fun, nfl_sched,
                    test, def_weekly):
    
    df_rb = position_feat_eng_df_creation(player_df = test_fun,
                              def_df = test,
                              position = 'RB')
    df_rb2 = position_feat_eng_df_creation2(new_df2 = df_rb, 
                                        def_df = test,
                                        position = 'RB')
    test_final = create_qb_trend_var(qb_df=df_rb2,
                                 position = 'RB'#,
                                #file_save = 'rb_player_data_final.csv'
                                    )
    test_final2 = cleanup_final_df(df=test_final, position='RB')
    test_final2.to_csv('rb_player_data_final.csv')
    
    return test_final2

def wr_all_data_pull(year, week, test_fun, nfl_sched,
                    test, def_weekly):
    
    df_wr = position_feat_eng_df_creation(player_df = test_fun,
                              def_df = test,
                              position = 'WR')
    df_wr2 = position_feat_eng_df_creation2(new_df2 = df_wr, 
                                        def_df = test,
                                        position = 'WR')
    test_final = create_qb_trend_var(qb_df=df_wr2,
                                 position = 'WR'#,
                                #file_save = 'wr_player_data_final.csv'
                                    )
    test_final2 = cleanup_final_df(df=test_final, position='WR')
    test_final2.to_csv('wr_player_data_final.csv')
    return test_final2

def te_all_data_pull(year, week, test_fun, nfl_sched,
                    test, def_weekly):
    
    df_te = position_feat_eng_df_creation(player_df = test_fun,
                              def_df = test,
                              position = 'TE')
    df_te2 = position_feat_eng_df_creation2(new_df2 = df_te, 
                                        def_df = test,
                                        position = 'TE')
    test_final = create_qb_trend_var(qb_df=df_te2,
                                 position = 'TE'#,
                               # file_save = 'te_player_data_final.csv'
                                    )
    test_final2 = cleanup_final_df(df=test_final, position='TE')
    test_final2.to_csv('te_player_data_final.csv')

    return test_final2

def k_all_data_pull(year, week, test_fun, nfl_sched,
                    test, def_weekly):
    
    df_k = position_feat_eng_df_creation(player_df = test_fun,
                              def_df = test,
                              position = 'K')
    df_k2 = position_feat_eng_df_creation2(new_df2 = df_k, 
                                        def_df = test,
                                        position = 'K')
    test_final = create_qb_trend_var(qb_df=df_k2,
                                 position = 'K'#,
                                #file_save = 'k_player_data_final.csv'
                                    )
    test_final2 = cleanup_final_df(df=test_final, position='K')
    test_final2.to_csv('k_player_data_final.csv')

    return test_final2

def def_all_data_pull(year, week, test_fun, nfl_sched,
                    test, def_weekly):
    
    def_temp = def_feat_eng_df_creation(def_df = test#,
                                       #file_save = 'def_team_data.csv'
                                       )
    test_final2 = cleanup_final_df(df=def_temp, position='D')
    test_final2.to_csv('def_team_data.csv')

    return test_final2

def run_update_weekly_player_stats():
    
    year, week, test_fun, nfl_sched, test, def_weekly = data_prep_for_player_pull()
    print("QB Data Pull Start")
    test_final_qb = qb_all_data_pull(year, week, test_fun, 
                                   nfl_sched, test, def_weekly)
    print("RB Data Pull Start")
    test_final_rb = rb_all_data_pull(year, week, test_fun, 
                                   nfl_sched, test, def_weekly) 
    print("WR Data Pull Start")
    test_final_wr = wr_all_data_pull(year, week, test_fun, 
                                   nfl_sched, test, def_weekly)   
    print("TE Data Pull Start")
    test_final_te = te_all_data_pull(year, week, test_fun, 
                                   nfl_sched, test, def_weekly)
    print("K Data Pull Start")
    test_final_k = k_all_data_pull(year, week, test_fun,
                                  nfl_sched, test, def_weekly)
    print("D Data Pull Start")
    test_final_d = def_all_data_pull(year, week, test_fun,
                                    nfl_sched, test, def_weekly)
    
    return test_final_qb, test_final_rb, test_final_wr, test_final_te, test_final_k, test_final_d
    
def get_nfl_depth_chart(year, position):
    import nfl_data_py as nfl
#     depth_chart=nfl.import_depth_charts(years=[year])
#     depth_chart = depth_chart[['season','club_code','week',
#                           'game_type','depth_team',
#                           'position','full_name']]
#     depth_chart=depth_chart[depth_chart['position']==position]

    depth_chart=nfl.import_weekly_rosters(years=[year])
    depth_chart=depth_chart[['season','team','position',
                             'depth_chart_position',
                            'player_name','week',
                            'status_description_abbr','game_type']]
    depth_chart.loc[depth_chart.player_name == 'Taysom Hill', 'position'] = 'TE'

    
    depth_chart = depth_chart[depth_chart['position']==position]
    depth_chart = depth_chart[depth_chart['status_description_abbr']=='A01']
    depth_chart = depth_chart.replace({'player_name':{'Nathaniel Dell':'Tank Dell',
                                                      'Jeffrey Wilson':'Jeff Wilson'
                                              }},
                                      regex = True)
    
    return depth_chart
    
def get_current_wk_depth_chart(depth_chart, week):
    
    depth_chart['week']=depth_chart['week'].astype(int)
    depth_chart=depth_chart[depth_chart['week']==week]
    
    return depth_chart


#### now we need to get our current week players and get an oot df
#for the week we care about
def create_curr_wk_oot_qb(nfl_sched,
                          year,
                          week,
                          player_df,
                          position,
                          def_df#,
                         # depth_chart
                        # save_file
                         ):
    
        nfl_sched = nfl_sched[(nfl_sched['Year'] == year) &
                             (nfl_sched['Week'] == week)]
        nfl_sched = nfl_sched.reset_index()
        nfl_sched = nfl_sched.drop(columns = ['index'])
        
        depth_chart = get_nfl_depth_chart(year=year,position=position)
        depth_chart=get_current_wk_depth_chart(depth_chart,week=week)

        

        qb = pd.merge(player_df, depth_chart, left_on ='Player',
                     right_on='player_name',how='inner')
        qb=qb[qb['Position']==position]
        qb=qb[['Gamelog','Player','Position','Playing_Prd_Strt',
              'Playing_Prd_End']]
        qb=qb.reset_index()
        qb=qb.drop(columns=['index'])
        
        df_qb = pd.DataFrame()
        #for i in range(0,20):
        for i in range(len(qb)):
            try: 
                time.sleep(3.1)
            #    print(i)
                player = qb['Player'][i]
                print(qb['Player'][i])
                url = qb['Gamelog'][i]
                #print(qb['Player'][i])
                data = requests.get(url).text
                #print(data)
                soup = BeautifulSoup(data, 'html.parser')
                #print(soup)
                dfs = pd.read_html(data)
                df = dfs[0]
                df['Player'] = player
                #print(df.head())    
                #print(df.columns)
                df_qb = pd.concat([df_qb, df], axis=0, ignore_index=True)
            except:
                print("No tables found exception")
                i = i-1
                continue
                
        
        df_qb.columns = df_qb.columns.get_level_values(0) + '' +  df_qb.columns.get_level_values(1)
        df_qb = df_qb[['Player','Unnamed: 6_level_0Tm']]
        df_qb = df_qb.rename(columns = {'Unnamed: 6_level_0Tm':'TEAM'})
        df_qb = df_qb.drop_duplicates()
        df_qb['TEAM'] = df_qb['TEAM'].map({'NWE': 'NE',
                               'NOR': 'NO', 'SFO': 'SF', 'SDG':'LAC',
                              'GNB':'GB','TAM':'TB','WAS':'WSH',
                              'KAN':'KC', 'OAK':'LV', 'STL':'LAR',
                              'LVR':'LV', 'IND':'IND', 'SEA':'SEA',
                             'HOU':'HOU', 'ATL':'ATL', 'CIN':'CIN',
                             'PIT':'PIT','NYG':'NYG', 'DET':'DET',
                             'CLE':'CLE','DEN':'DEN','DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI',
                             'BAL':'BAL','JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA',
                             'CAR':'CAR','PHI':'PHI','MIN':'MIN',
                             'TEN':'TEN', 'LAR':'LAR', 'LAC':'LAC'})
        
        df_qb = pd.merge(df_qb, nfl_sched, how = 'inner', on = 'TEAM', 
                        suffixes = (None, None))
        df_qb = df_qb.rename(columns = {'TEAM':'team',
                                       'Player':'Player ',
                                       'Opponent':'opp'})
        df_qb['opp'] = df_qb['opp'].str.replace('@',"")

        df_qb['player_wk_year'] = df_qb['Player '] + " " + df_qb['Week'].astype(str) + " " + df_qb['Year'].astype(str)
        df_qb['opp wk year'] = df_qb['opp'] + " " + df_qb['Week'].astype(str) + " " + df_qb['Year'].astype(str)
        
        df = df_qb[['Week','Year','Player ','team',
                      'opp','player_wk_year','opp wk year']]
        
        
        qb = pd.merge(player_df, depth_chart, left_on ='Player',
                     right_on='player_name',how='inner')
        qb=qb[qb['Position']==position]
        qb=qb[['Gamelog','Player','Position','Playing_Prd_Strt',
              'Playing_Prd_End']]
        qb=qb.reset_index()
        qb=qb.drop(columns=['index'])
        
        df_qb2 = pd.DataFrame()
        #for i in range(0,20):
        for i in range(len(qb)):
            try:              
                time.sleep(3.1)

            #    print(i)
                player = qb['Player'][i]
                print(qb['Player'][i])
                url = qb['Gamelog'][i]
                #print(qb['Player'][i])
                data = requests.get(url).text
                #print(data)
                soup = BeautifulSoup(data, 'html.parser')
                #print(soup)
                dfs = pd.read_html(data)
                df2 = dfs[0]
                df2['Player'] = player
                #print(df.head())    
                #print(df.columns)
                df_qb2 = pd.concat([df_qb2, df2], axis=0, ignore_index=True)
            except:
                print("No tables found exception")
                i = i-1
                continue

        df_qb2.columns = df_qb2.columns.get_level_values(0) + '' +  df_qb2.columns.get_level_values(1)
        if (position == 'QB'):
            df_qb2 = df_qb2[['FumblesFF', 'FumblesFL','FumblesFR',
                            'FumblesFmb','FumblesTD','FumblesYds', 'Off. SnapsNum',
                            'Off. SnapsPct', 'PassingAY/A','PassingAtt',
                            'PassingCmp', 'PassingCmp%', 'PassingInt', 'PassingRate',
                            'PassingSk', 'PassingTD', 'PassingY/A', 'PassingYds',
                            'PassingYds.1', 'Player', 'RushingAtt',
                            'RushingTD', 'RushingY/A', 'RushingYds',
                            'Scoring2PM', 'ScoringPts', 'ScoringTD',
                            'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                            'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                            'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                            'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                            'Unnamed: 7_level_0Unnamed: 7_level_1',
                            'Unnamed: 8_level_0Opp', 'Unnamed: 9_level_0Result']]

        #    print(df_qb2.columns)
        
            df_qb2 = df_qb2.rename(columns = {'FumblesFF':'Fumbles FF', 'FumblesFL':'Fumbles FL',
                                'FumblesFR':'Fumbles FR', 'FumblesFmb':'Fumbles Fmb',
                                'FumblesTD':'Fumbles TD',
                                'FumblesYds':'Fumbles Yds', 'Off. SnapsNum':'Off. Snaps Num',
                                'Off. SnapsPct':'Off. Snaps Pct',
                                'PassingAY/A':'Passing AY/A','PassingAtt':'Passing Att',
                                'PassingCmp':'Passing Cmp', 'PassingCmp%':'Passing Cmp%',
                                'PassingInt':'Passing Int', 'PassingRate':'Passing Rate',
                                'PassingSk':'Passing Sk', 'PassingTD': 'Passing TD',
                                'PassingY/A':'Passing Y/A', 'PassingYds':'Passing Yds',
                                'PassingYds.1':'Passing Sack Yds Lost',
                                'Player':'Player ', 'RushingAtt':'Rushing Att',
                                'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                'RushingYds':'Rushing Yds',                             
                                'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                'ScoringTD':'Scoring TD',
                                'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                'Unnamed: 8_level_0Opp':'Opp',
                                'Unnamed: 9_level_0Result':'Result'})            

        elif (position == 'WR'):
            
            df_qb2 = df_qb2[[
                'FumblesFF','FumblesFL','FumblesFR',
                'FumblesFmb','FumblesTD','FumblesYds',
                'Kick ReturnsRt','Kick ReturnsTD','Kick ReturnsY/Rt',
                'Kick ReturnsYds','Off. SnapsNum','Off. SnapsPct',
                'Player','Punt ReturnsRet','Punt ReturnsTD',
                'Punt ReturnsY/R','Punt ReturnsYds','ReceivingCtch%',
                'ReceivingRec','ReceivingTD', 'ReceivingTgt',
                'ReceivingY/R','ReceivingY/Tgt','ReceivingYds',
                'RushingAtt','RushingTD', 'RushingY/A',
               'RushingYds','ST SnapsNum', 'ST SnapsPct',
                'Scoring2PM', 'ScoringPts','ScoringTD', 
                'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                'Unnamed: 7_level_0Unnamed: 7_level_1',
                'Unnamed: 8_level_0Opp','Unnamed: 9_level_0Result']]
            
            df_qb2 = df_qb2.rename(columns = {'FumblesFF':'Fumbles FF',
                                'FumblesFL':'Fumbles FL','FumblesFR':'Fumbles FR',
                                'FumblesFmb':'Fumbles Fmb','FumblesTD':'Fumbles TD',
                                'FumblesYds':'Fumbles Yds','Kick ReturnsRt':'Kick Returns Rt',
                                'Kick ReturnsTD':'Kick Returns TD','Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                                'Kick ReturnsYds':'Kick Returns Yds','Off. SnapsNum':'Off. Snaps Num',
                                'Off. SnapsPct':'Off. Snaps Pct','Player':'Player ', 
                                'Punt ReturnsRet':'Punt Returns Ret','Punt ReturnsTD':'Punt Returns TD',
                                'Punt ReturnsY/R':'Punt Returns Y/R','Punt ReturnsYds':'Punt Returns Yds',      
                                'ReceivingCtch%':'Receiving Ctch%', 'ReceivingRec':'Receiving Rec',
                                'ReceivingTD':'Receiving TD', 'ReceivingTgt':'Receiving Tgt',
                                'ReceivingY/R':'Receiving Y/R','ReceivingY/Tgt':'Receiving Y/Tgt',
                                'ReceivingYds':'Receiving Yds','RushingAtt':'Rushing Att',
                                'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                'RushingYds':'Rushing Yds','ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                'ScoringTD':'Scoring TD','Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                'Unnamed: 8_level_0Opp':'Opp',
                                'Unnamed: 9_level_0Result':'Result'})
                   
        elif (position == 'TE'):
            
            df_qb2 = df_qb2[[ 'FumblesFF', 'FumblesFL','FumblesFR','FumblesFmb',
                            'FumblesTD', 'FumblesYds', 'Off. SnapsNum',
                            'Off. SnapsPct', 'Player',
                            'ReceivingCtch%', 'ReceivingRec', 'ReceivingTD',
                            'ReceivingTgt','ReceivingY/R', 'ReceivingY/Tgt',
                            'ReceivingYds', 'RushingAtt', 'RushingTD', 'RushingY/A',
                            'RushingYds', 'ST SnapsNum', 'ST SnapsPct', 'Scoring2PM', 'ScoringPts',
                            'ScoringTD', 'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                             'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                            'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                            'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                            'Unnamed: 7_level_0Unnamed: 7_level_1', 'Unnamed: 8_level_0Opp',
                            'Unnamed: 9_level_0Result'
            ]]
        
            df_qb2 = df_qb2.rename(columns = {'FumblesFF':'Fumbles FF', 'FumblesFL':'Fumbles FL',
                                  'FumblesFR':'Fumbles FR', 'FumblesFmb':'Fumbles Fmb',
                                  'FumblesTD':'Fumbles TD', 'FumblesYds':'Fumbles Yds',
                                  'Kick ReturnsRt':'Kick Returns Rt', 'Kick ReturnsTD':'Kick Returns TD',
                                  'Kick ReturnsY/Rt':'Kick Returns Y/Rt', 'Kick ReturnsYds':'Kick Returns Yds',
                                  'Off. SnapsNum':'Off. Snaps Num', 'Off. SnapsPct':'Off. Snaps Pct',
                                  'Player':'Player ', 'Punt ReturnsRet':'Punt Returns Ret',
                                  'Punt ReturnsTD':'Punt Returns TD', 'Punt ReturnsY/R':'Punt Returns Y/R',
                                  'Punt ReturnsYds':'Punt Returns Yds', 'ReceivingCtch%':'Receiving Ctch%',
                                  'ReceivingRec':'Receiving Rec', 'ReceivingTD':'Receiving TD',
                                  'ReceivingTgt':'Receiving Tgt', 'ReceivingY/R':'Receiving Y/R',
                                  'ReceivingY/Tgt':'Receiving Y/Tgt', 'ReceivingYds':'Receiving Yds',          
                                  'RushingAtt':'Rushing Att', 'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                  'RushingYds':'Rushing Yds', 'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                  'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                  'ScoringTD':'Scoring TD', 'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                  'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                  'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                  'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                  'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                  'Unnamed: 8_level_0Opp':'Opp', 'Unnamed: 9_level_0Result':'Result'})
                
        
        elif (position == 'RB'):
            
            df_qb2 = df_qb2[['FumblesFF', 'FumblesFL', 'FumblesFR', 'FumblesFmb',
                            'FumblesTD', 'FumblesYds', 'Kick ReturnsRt', 'Kick ReturnsTD',
                            'Kick ReturnsY/Rt','Kick ReturnsYds', 'Off. SnapsNum', 'Off. SnapsPct',
                            'Player', 'Punt ReturnsRet', 'Punt ReturnsTD','Punt ReturnsY/R',
                            'Punt ReturnsYds', 'ReceivingCtch%', 'ReceivingRec', 'ReceivingTD',
                            'ReceivingTgt', 'ReceivingY/R', 'ReceivingY/Tgt', 'ReceivingYds',
                            'RushingAtt', 'RushingTD', 'RushingY/A',
                            'RushingYds', 'ST SnapsNum', 'ST SnapsPct',
                            'Scoring2PM', 'ScoringPts',
                            'ScoringTD', 'Unnamed: 0_level_0Rk', 'Unnamed: 10_level_0GS',
                            'Unnamed: 1_level_0Year', 'Unnamed: 2_level_0Date',
                            'Unnamed: 3_level_0G#', 'Unnamed: 4_level_0Week',
                            'Unnamed: 5_level_0Age', 'Unnamed: 6_level_0Tm',
                            'Unnamed: 7_level_0Unnamed: 7_level_1',
                            'Unnamed: 8_level_0Opp', 'Unnamed: 9_level_0Result']]

            df_qb2 = df_qb2.rename(columns = {'FumblesFF':'Fumbles FF',
                                  'FumblesFL':'Fumbles FL', 'FumblesFR':'Fumbles FR',
                                  'FumblesFmb':'Fumbles Fmb', 'FumblesTD':'Fumbles TD',
                                'FumblesYds':'Fumbles Yds', 'Kick ReturnsRt':'Kick Returns Rt',
                                'Kick ReturnsTD':'Kick Returns TD', 'Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                                'Kick ReturnsYds':'Kick Returns Yds', 'Off. SnapsNum':'Off. Snaps Num',
                                'Off. SnapsPct':'Off. Snaps Pct', 'Player':'Player ', 'Punt ReturnsRet':'Punt Returns Ret',
                                'Punt ReturnsTD':'Punt Returns TD', 'Punt ReturnsY/R':'Punt Returns Y/R',
                                'Punt ReturnsYds':'Punt Returns Yds', 'ReceivingCtch%':'Receiving Ctch%',
                                'ReceivingRec':'Receiving Rec', 'ReceivingTD':'Receiving TD',
                                'ReceivingTgt':'Receiving Tgt', 'ReceivingY/R':'Receiving Y/R',
                                'ReceivingY/Tgt':'Receiving Y/Tgt',
                                'ReceivingYds':'Receiving Yds', 'RushingAtt':'Rushing Att',
                                'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                                'RushingYds':'Rushing Yds', 'ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                                'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                                'ScoringTD':'Scoring TD', 'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                                'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                                'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                                'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                                'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                                'Unnamed: 8_level_0Opp':'Opp','Unnamed: 9_level_0Result':'Result'})

        elif (position == 'K'):
              
            df_qb2 = df_qb2.rename(columns = {'FumblesFF':'Fumbles FF',
                    'FumblesFL':'Fumbles FL', 'FumblesFR':'Fumbles FR',
                    'FumblesFmb':'Fumbles Fmb', 'FumblesTD':'Fumbles TD',
                    'FumblesYds':'Fumbles Yds','Kick ReturnsRt':'Kick Returns Rt',
                    'Kick ReturnsTD':'Kick Returns TD','Kick ReturnsY/Rt':'Kick Returns Y/Rt',
                    'Kick ReturnsYds':'Kick Returns Yds','Off. SnapsNum':'Off. Snaps Num',
                    'Off. SnapsPct':'Off. Snaps Pct', 'Player':'Player ', 
                    'Punt ReturnsRet':'Punt Returns Ret', 'Punt ReturnsTD':'Punt Returns TD',
                    'Punt ReturnsY/R':'Punt Returns Y/R', 'Punt ReturnsYds':'Punt Returns Yds',
                    'ReceivingCtch%':'Receiving Ctch%', 'ReceivingRec':'Receiving Rec',
                    'ReceivingTD':'Receiving TD', 'ReceivingTgt':'Receiving Tgt',
                    'ReceivingY/R':'Receiving Y/R','ReceivingY/Tgt':'Receiving Y/Tgt',
                    'ReceivingYds':'Receiving Yds', 'RushingAtt':'Rushing Att',
                    'RushingTD':'Rushing TD', 'RushingY/A':'Rushing Y/A',
                    'RushingYds':'Rushing Yds','ST SnapsNum':'ST Snaps Num', 'ST SnapsPct':'ST Snaps Pct',
                    'Scoring2PM':'Scoring 2PM', 'ScoringPts':'Scoring Pts',
                    'ScoringTD':'Scoring TD', 'Unnamed: 0_level_0Rk':'Rk', 'Unnamed: 10_level_0GS':'GS',
                    'Unnamed: 1_level_0Year':'Year', 'Unnamed: 2_level_0Date':'Date',
                    'Unnamed: 3_level_0G#':'G#', 'Unnamed: 4_level_0Week':'Week',
                    'Unnamed: 5_level_0Age':'Age', 'Unnamed: 6_level_0Tm':'Tm',
                    'Unnamed: 7_level_0Unnamed: 7_level_1':'home_away',
                    'Unnamed: 8_level_0Opp':'Opp', 'Unnamed: 9_level_0Result':'Result'})
            
            df_qb2 = df_qb2[['Player ','ST Snaps Num', 'ST Snaps Pct', 'Scoring Pts',
                    'ScoringXPM','ScoringXPA','ScoringXP%','ScoringFGM','ScoringFGA',
                    'ScoringFG%',#'ScoringTD',
                    'Rk', 'GS', 'Year', 'Date', 'G#', 'Week', 'Age', 'Tm',
                    'home_away', 'Opp','Result']]
          
        
        
        df_qb2 = df_qb2[df_qb2['G#'] != '']
        df_qb2 = df_qb2[df_qb2['G#'] != 'G#']
        df_qb2 = df_qb2[~df_qb2['Date'].str.contains("Game")]
        df_qb2 = df_qb2[~df_qb2['GS'].isin(['Did Not Play', 'Inactive',
                                           'Injured Reserve','Non-Football Injury',
                                           'Suspended','Returned from Injured Reserve',
                                           'COVID-19 List','Exempt List',
                                           'Physically Unable to Perform'])]
        
        
        df_qb2['Week'] = df_qb2['Week'].astype(int)
        df_qb2['Year'] = df_qb2['Year'].astype(int)  
        min_date = df_qb2['Date'][(df_qb2['Year'] == year) &
                                 (df_qb2['Week'] == week)].min()
        
        df_qb2['player_wk_year'] = df_qb2['Player '] + " " + df_qb2['Week'].astype(str) + " " + df_qb2['Year'].astype(str)
   #     print('yay')
   #     print(df_qb2.shape)        
#         df_qb2 = df_qb2[(df_qb2['Year'] <= year) &
#                        (df_qb2['Week'] < week)]
        df_qb2 = df_qb2[df_qb2['Date']< min_date]
                         
    #    print(df_qb2.shape)
    #    print(depth_chart['club_code'].value_counts())
        depth_chart['team'] = depth_chart['team'].map({'NE': 'NE',
                               'NO': 'NO', 'SF': 'SF', 'LAC':'LAC',
                              'GB':'GB','TB':'TB','WAS':'WSH',
                              'KC':'KC', 'LV':'LV', 'LA':'LAR',
                              'IND':'IND', 'SEA':'SEA',
                             'HOU':'HOU', 'ATL':'ATL', 'CIN':'CIN',
                             'PIT':'PIT','NYG':'NYG', 'DET':'DET',
                             'CLE':'CLE','DEN':'DEN','DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI',
                             'BAL':'BAL','JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA',
                             'CAR':'CAR','PHI':'PHI','MIN':'MIN',
                             'TEN':'TEN'})
    #    print(depth_chart['club_code'].value_counts())
        depth_chart2 = depth_chart[['team','player_name']]
        depth_chart2 = depth_chart2.rename(columns = {#'season':'Year',
                                                     'team':'TEAM',
                                                     #'week':'Week',
                                                     'player_name':'Player '})
        depth_chart2 = pd.merge(depth_chart2, nfl_sched, how = 'inner', on = 'TEAM', 
                        suffixes = (None, None))
        depth_chart2['player_wk_year'] = depth_chart2['Player '] + " " + depth_chart2['Week'].astype(str) + " " + depth_chart2['Year'].astype(str)

        depth_chart2 = depth_chart2.rename(columns = {'TEAM':'Tm',
                                       'Opponent':'Opp'})
        depth_chart2['Opp'] = depth_chart2['Opp'].str.replace('@',"")
        
        df_qb2 = pd.merge(df_qb2, depth_chart2, how = 'outer',
                          on = ['player_wk_year', 'Opp','Tm','Week','Year', 'Player '])
      #  return df_qb2
        
        test_df = df_qb2[['Player ','Week', 'Year', 'player_wk_year']]
        test_df['Week'] = test_df['Week'].astype(int)
        test_df['Year'] = test_df['Year'].astype(int)
        
        a = list(test_df['Player '].unique())
        test_df2 = pd.DataFrame()
        for p in a:
            player_name_df = test_df[test_df['Player ']==p]
            
            for i in range(1,7):
            #print(i)
                wks_ago = i
                week_num_wks_ago = "week num " + str(i) + " wks ago"
                year_wks_ago = "year " + str(i) + " wks ago"
                player_wks_ago = "player " + str(i) + " wks ago"
            
                if(i == 1):
                    player_name_df[player_wks_ago] = [np.nan]+list(player_name_df["player_wk_year"])[:-1]
                    #player_name_df[player_prev_game_player] = [np.nan]+list(player_name_df["Player "])[:-1]
                    player_name_df[week_num_wks_ago] = [np.nan]+list(player_name_df["Week"])[:-1]
                    player_name_df[year_wks_ago] = [np.nan]+list(player_name_df["Year"])[:-1]                    
                
                elif (i > 1):
                    # player_name_df[player_wks_ago] = [np.nan]+list(player_name_df[prior_player_wk_year_prev_game_player])[:-1]
                    player_name_df[player_wks_ago] = [np.nan]+list(player_name_df[prior_player_prev_game_player])[:-1]
                    player_name_df[week_num_wks_ago] = [np.nan]+list(player_name_df[prior_week_num_prev_game_played])[:-1]
                    player_name_df[year_wks_ago] = [np.nan]+list(player_name_df[prior_year_prev_game_played])[:-1]
               
                prior_prev_games_played_ago = i
                prior_week_num_prev_game_played = "week num " + str(i) + " wks ago"
                prior_year_prev_game_played =  "year " + str(i) + " wks ago"
                prior_player_prev_game_player = "player " + str(i) + " wks ago" 
                #prior_player_wk_year_prev_game_player = 'player_wk_year ' + str(i) + " games played ago"

            test_df2 = test_df2.append(player_name_df)

        test_df = test_df2                    
                
#                 curr_wk = "Week"
#                 curr_yr = "Year"
#                 test_df[curr_wk] = test_df['Week']
#                 test_df[curr_yr] = test_df['Year']
#                 test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
#                                              np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
#                 test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
#             else:
#                 curr_wk = "week num " + str(i-1) + " wks ago"
#                 curr_yr = "year " + str(i-1) + " wks ago"
#                 test_df[week_num_wks_ago] = np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] >= 2022), 18,
#                                              np.where((test_df[curr_wk] == 1) & (test_df[curr_yr] < 2022), 17, test_df[curr_wk] - 1))
#                 test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
#             test_df[player_wks_ago] = test_df['Player '] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)
    
        new_df = pd.DataFrame()
        for i in range(0,7):
      #      print(i)
            if (i == 0):
                #new_df = df_qb2
                test_df2 = test_df.drop(columns = ['Player ', 'Week', 'Year'])
                new_df = pd.merge(test_df2, df_qb2, how = 'left', on = ['player_wk_year'], suffixes = (None, None))
              #  print(new_df.head())
            else:
                temp_df = df_qb2.drop(columns = ['Rk','GS','Year','G#'])
                for col in temp_df.columns:
                    new_col = col + " " + str(i) + " wks ago"
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                merge_column = "player " + str(i) + " wks ago"
                temp_df[merge_column] = df_qb2['player_wk_year']
                new_df = pd.merge(new_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
                new_df = new_df.drop_duplicates()
        
        tms = ['Tm','Tm 1 wks ago', 'Tm 2 wks ago',
          'Tm 3 wks ago','Tm 4 wks ago','Tm 5 wks ago','Tm 6 wks ago'#,
              ]

        opp = ['Opp','Opp 1 wks ago', 'Opp 2 wks ago',
          'Opp 3 wks ago','Opp 4 wks ago','Opp 5 wks ago','Opp 6 wks ago'#,
              ]
        
        qb_df = new_df
        
        for i in tms:
            #print(i)
            qb_df[i] = qb_df[i].map({'NWE': 'NE',
                               'NOR': 'NO', 'SFO': 'SF', 'SDG':'LAC',
                              'GNB':'GB','TAM':'TB','WAS':'WSH',
                              'KAN':'KC', 'OAK':'LV', 'STL':'LAR',
                              'LVR':'LV', 'IND':'IND', 'SEA':'SEA',
                             'HOU':'HOU', 'ATL':'ATL', 'CIN':'CIN',
                             'PIT':'PIT','NYG':'NYG', 'DET':'DET',
                             'CLE':'CLE','DEN':'DEN','DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI',
                             'BAL':'BAL','JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA',
                             'CAR':'CAR','PHI':'PHI','MIN':'MIN',
                             'TEN':'TEN', 'LAR':'LAR', 'LAC':'LAC'})
        for i in opp:
            #print(i)
            qb_df[i] = qb_df[i].map({'NWE': 'NE', 'NOR': 'NO',
                              'SFO': 'SF', 'SDG':'LAC', 'GNB':'GB','TAM':'TB',
                              'WAS':'WSH','KAN':'KC', 'OAK':'LV', 'STL':'LAR',
                              'LVR':'LV','IND':'IND', 'SEA':'SEA', 'HOU':'HOU',
                             'ATL':'ATL','CIN':'CIN', 'PIT':'PIT', 'NYG':'NYG',
                             'DET':'DET','CLE':'CLE', 'DEN':'DEN', 'DAL':'DAL',
                             'CHI':'CHI','BUF':'BUF','ARI':'ARI','BAL':'BAL',
                             'JAX':'JAX', 'NYJ':'NYJ','MIA':'MIA', 'CAR':'CAR',
                             'PHI':'PHI', 'MIN':'MIN', 'TEN':'TEN', 'LAR':'LAR',
                             'LAC':'LAC'})    
            
        #opp
        opp_wk_year = ['opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago', 'opp 3 wk year ago',
               'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago'
                      ]

        wk = ['Week', 'Week 1 wks ago', 'Week 2 wks ago', 'Week 3 wks ago', 'Week 4 wks ago', 'Week 5 wks ago',
               'Week 6 wks ago'
             ]

        year = ['Year', 'year 1 wks ago', 'year 2 wks ago', 'year 3 wks ago', 'year 4 wks ago', 'year 5 wks ago',
               'year 6 wks ago'
               ]
        
        
        for i in range(0,7):
     #       print(i)
            #print(opp[i])
            #print(wk[i])
            #print(year[i])
            opp_colname = opp[i]
            wk_colname = wk[i]
            year_colname = year[i]
            qb_df[wk_colname] = qb_df[wk_colname].astype(str).str.replace('.0', '',regex=False)
            
            qb_df[year_colname] = qb_df[year_colname].astype(str).str.replace('.0', '',regex=False)    
            opp_wk_year_colname = opp_wk_year[i]
            if (i== 0):
                qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str) + " " + qb_df[year_colname].astype(str)
            else:
               # qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str).str[:-2] + " " + qb_df[year_colname].astype(str)
                qb_df[opp_wk_year_colname] = qb_df[opp_colname] + " " + qb_df[wk_colname].astype(str) + " " + qb_df[year_colname].astype(str)

                #if (i == 0):
#        return qb_df
    
        test_df = qb_df[['player_wk_year','opp wk year', 'opp 1 wk year ago',
                         'opp 2 wk year ago', 'opp 3 wk year ago',
              'opp 4 wk year ago', 'opp 5 wk year ago', 'opp 6 wk year ago' ]]

        new_df = pd.DataFrame()

        for i in range(0,7):
     #       print(i)
            if (i == 0):
                #new_df = df_qb2
                #test_df2 = test_df.drop(columns = [])
                new_df = pd.merge(test_df, def_df, how = 'left', left_on = ['opp wk year'], right_on = ['team_wk_year'], suffixes = (None, None))
                new_df = new_df.drop(columns = ['team_wk_year'])
                #print(new_df.head())
            else:
                temp_df = def_df.drop(columns = ['Week','week_num','year','Opp','team_wk_year'])
              #  temp_df2 = temp_df
                for col in temp_df.columns:
                    new_col = 'opp' + " " + col + " " + str(i) + 'wks ago'
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                #merge_column = "player " + str(i) + " wks ago"
                #merge_column = 
                temp_df['team_wk_year'] = def_df['team_wk_year']
               # print(temp_df2.head())
                qb_no_null = test_df[[opp_wk_year[i]]]
               # print(qb_no_null.head())
                qb_no_null = qb_no_null[qb_no_null.notnull()]
                qb_no_null = qb_no_null.drop_duplicates()
              #  print(qb_no_null.head())
                qb_no_null = pd.merge(qb_no_null, temp_df, how = 'inner', left_on = [opp_wk_year[i]], right_on = ['team_wk_year'], suffixes = (None,None))
                #print(qb_no_null.head())
        
                qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
                qb_no_null = qb_no_null.drop_duplicates()
                new_df = pd.merge(new_df, qb_no_null, how = 'left', left_on = [opp_wk_year[i]], right_on = ['team_wk_year'], suffixes = (None, None))
                new_df = new_df.drop(columns = ['team_wk_year'])
                new_df = new_df.drop_duplicates()
        
        new_df = new_df.drop_duplicates()
        
        qb_df2 = qb_df.drop(columns = ['Week', 'Opp', 'opp wk year', 'opp 1 wk year ago', 'opp 2 wk year ago',
           'opp 3 wk year ago', 'opp 4 wk year ago', 'opp 5 wk year ago',
           'opp 6 wk year ago' ])
        

        new_df2 = pd.merge(qb_df2,new_df, how = 'left', on = 'player_wk_year', suffixes = (None,None))
        
#         test_df = def_df[['CITY','week_num', 'year', 'team_wk_year']]
#         for i in range(1,7):
#             #print(i)
#             wks_ago = i
#             week_num_wks_ago = "week num " + str(i) + " wks ago"
#             year_wks_ago = "year " + str(i) + " wks ago"
#             #player_wks_ago = "player " + str(i) + " wks ago"
#             team_wk_year = 'team_wk_year ' + str(i) + " wks ago"
#             if(i == 1):
#                 curr_wk = "week_num"
#                 curr_yr = "year"
#                 test_df[curr_wk] = test_df['week_num']
#                 test_df[curr_yr] = test_df['year']
#                 test_df[week_num_wks_ago] = np.where(test_df[curr_wk] == 1, 17, test_df[curr_wk] - 1)
#                 test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr]-1, test_df[curr_yr])
#             else:
#                 curr_wk = "week num " + str(i-1) + " wks ago"
#                 curr_yr = "year " + str(i-1) + " wks ago"
#                 test_df[week_num_wks_ago] = np.where(test_df[curr_wk] == 1, 17, test_df[curr_wk]-1)
#                 test_df[year_wks_ago] = np.where(test_df[curr_wk] == 1, test_df[curr_yr] -1, test_df[curr_yr])

#             test_df[team_wk_year] = test_df['CITY'] + " " + test_df[week_num_wks_ago].astype(str) + " " + test_df[year_wks_ago].astype(str)
#        return new_df2
        #test_df.head()

        new_def_df = pd.DataFrame()
        
        nfl_sched = get_nfl_sched()
        a = list(nfl_sched['TEAM'].unique())
        test_df2 = pd.DataFrame()
        
        for p in a:
            team_name_df = nfl_sched[(nfl_sched['TEAM']==p) & 
                                    (nfl_sched['Opponent'] != 'BYE')]
            team_name_df = team_name_df.sort_values(by = ['Year','Week'],
                                                   ascending = [True, True])
            team_name_df['team_wk_year'] = team_name_df['TEAM'] + " " + team_name_df['Week'].astype(str) + " " + team_name_df['Year'].astype(str)
            
            for i in range(1,7):
                
                wks_ago = i
                week_num_wks_ago = 'week num ' + str(i) + " wks ago"
                year_wks_ago = 'year ' + str(i) + " wks ago"
                team_wks_ago = 'team_wk_year ' + str(i) + " wks ago"
                
                if (i == 1):
                    team_name_df[team_wks_ago] = [np.nan] + list(team_name_df['team_wk_year'])[:-1]
                    
                elif (i > 1):
                    
                    team_name_df[team_wks_ago] = [np.nan]+list(team_name_df[prior_team_prev_game_player])[:-1]

                prior_prev_games_played_ago = i
                prior_team_prev_game_player = "team_wk_year " + str(i) + " wks ago"
            
            test_df2 = test_df2.append(team_name_df)
            
        test_df = test_df2
        new_def_df = pd.DataFrame()
        for i in range(0,7):
            #print(i)
            if (i == 0):
                #new_df = df_qb2
                #test_df = test_df.drop(columns = ['CITY','week_num','year'])
                test_df = test_df.drop(columns = ['TEAM','Week','Year','Opponent'])
                new_def_df = pd.merge(def_df, test_df, how = 'left', on = ['team_wk_year'], suffixes = (None, None))
                
                new_def_df = new_def_df.drop_duplicates(subset=['team_wk_year'], keep = 'last')
              #  new_def_df = new_def_df.drop(columns = ['team_wk_year'])
              #  print(new_def_df.head())
            else:
                temp_df = def_df.drop(columns = ['Team','CITY','Week','week_num','year'])
              #  temp_df2 = temp_df
                for col in temp_df.columns:
                    new_col = 'def matchup' + " " + col + " " + str(i) + 'wks ago'
                    temp_df[new_col] = temp_df[col]
                    temp_df = temp_df.drop(columns = [col])
                #merge_column = "player " + str(i) + " wks ago"
                #merge_column = 
                merge_column = "team_wk_year " + str(i) + " wks ago"
                temp_df[merge_column] = def_df['team_wk_year']
                #temp_df['team_wk_year'] = def_df['team_wk_year']
               # qb_no_null = qb_no_null.drop(columns = [opp_wk_year[i]])
                temp_df = temp_df.drop_duplicates(subset=[merge_column], keep='last')
                temp_df = temp_df.drop_duplicates()
                new_def_df = pd.merge(new_def_df, temp_df, how = 'left', on = [merge_column], suffixes = (None, None))
                #new_def_df = new_def_df.drop(columns = ['team_wk_year'])

        
        new_def_df2 = new_def_df.drop(columns = [#'team_wk_year',
                                                 'team_wk_year 1 wks ago', 
                                                 'team_wk_year 2 wks ago',
       'team_wk_year 3 wks ago', 'team_wk_year 4 wks ago',
       'team_wk_year 5 wks ago', 'team_wk_year 6 wks ago',
                                                 'Team', #'CITY',
                                                 'Week', 'Sack', 'FR', 'INT', 'DefTD',
               'PA', 'PaYD', 'RuYd', 'Safety', 'KickTD', 'FPts', 'week_num',
               'year', #'Opp',
                                                 'away flag','opp_wk_year'
                                                ])
        
        
     #   print(df['opp wk year'])
     #   print(df.shape)
     #   print(new_df2.shape)
        temp = df[['opp wk year','player_wk_year']]
        new_df2 = new_df2.drop(columns = ['opp wk year'])
        new_df2 = pd.merge(new_df2, temp, how = 'left', on = 'player_wk_year', suffixes = (None,None))
        new_df2 = new_df2.drop(columns = ['CITY', 'Opp'])
       # new_df2['opp wk year'] = df['opp wk year']
        new_df2 = new_df2.drop_duplicates()
        new_df2=new_df2.drop(columns=['team_wk_year'])

        new_df3 = pd.merge(new_df2,new_def_df2,how = 'left', left_on = ['opp wk year'], right_on = ['team_wk_year'], suffixes = (None,None))
        
        new_df3 = new_df3.drop(columns = ['def matchup opp_wk_year 1wks ago',# 'def matchup opp_wk_year 20wks ago',
            'def matchup opp_wk_year 2wks ago',
             'def matchup opp_wk_year 3wks ago', 'def matchup opp_wk_year 4wks ago',
             'def matchup opp_wk_year 5wks ago', 'def matchup opp_wk_year 6wks ago',
            'opp opp_wk_year 1wks ago',
             'opp opp_wk_year 2wks ago',
            'opp opp_wk_year 3wks ago',
             'opp opp_wk_year 4wks ago', 'opp opp_wk_year 5wks ago',
             'opp opp_wk_year 6wks ago' , 'opp_wk_year'])
        
        #new_df3['week_match'] = new_df3['CITY'] + " " + new_df3['Opp']
       # return new_df3
       # nfl_sched = nfl_sched[(nfl_sched['Year'] == year) & (nfl_sched['Week'] == week)]
        nfl_sched['Opponent'] = nfl_sched["Opponent"].str.replace("@","")
        nfl_sched['week_match'] = nfl_sched['TEAM'] + " " + nfl_sched['Opponent']
        nfl_sched = nfl_sched[['week_match']]
        
        #new_df4 = pd.merge(new_df3,nfl_sched,how = 'inner', on = ['week_match'], suffixes = (None,None))
        #new_df4 = new_df4.drop(columns = ['week_match'])
        
        
        #new_df3.to_csv(save_file)

        depth_chart['player_wk_year_team'] = depth_chart['player_name'] + " " + depth_chart['week'].astype(str) + " " + depth_chart['season'].astype(str) + " " + depth_chart['team']
        new_df3['player_wk_year_team'] = new_df3['player_wk_year'] + " " + new_df3['Opp']
#        return new_df3

        new_df4 = pd.merge(new_df3, depth_chart, how = 'inner',
                           left_on = 'player_wk_year_team', right_on = 'player_wk_year_team')
        
        new_df4 = new_df4.drop_duplicates('player_wk_year_team',
                                           keep='first')
        return new_df4


def def_curr_wk_oot(def_df,
                   # nfl_sched,
                    curr_wk,
                    curr_yr#,
                   # file_save
                   ):
    nfl_sched = get_nfl_sched()
    nfl_sched = nfl_sched[(nfl_sched['Year'] == curr_yr) & 
                         (nfl_sched['Week'] == curr_wk)]
    
    nfl_sched = nfl_sched.rename(columns = {'Year':'year',
                                           'TEAM':'CITY',
                                           'Opponent':'Opp'})
    
    nfl_sched['Team'] = nfl_sched['CITY'].map({'ARI':'Cardinals','SF':'49ers','NO':'Saints',
                                   'CAR':'Panthers','DAL':'Cowboys','HOU':'Texans',
                                   'LV':'Raiders','LAR':'Rams','DET':'Lions',
                                   'KC':'Chiefs','WSH':'Commanders','BAL':'Ravens',
                                   'IND':'Colts','PIT':'Steelers','CIN':'Bengals',
                                   'SEA':'Seahawks','MIA':'Dolphins','MIN':'Vikings',
                                   'NE':'Patriots','NYG':'Giants','TEN':'Titans',
                                   'DEN':'Broncos', 'NYJ':'Jets','PHI':'Eagles',
                                   'LAC':'Chargers','TB':'Buccaneers','BUF':'Bills',
                                   'CLE':'Browns','ATL':'Falcons','JAX':'Jaguars',
                                   'CHI':'Bears','GB':'Packers'})
    
    nfl_sched['week_num'] = nfl_sched['Week']
    nfl_sched['Opp'] = nfl_sched["Opp"].str.replace("@","")
    nfl_sched['opp wk year'] = nfl_sched['Opp'] + " " + nfl_sched['week_num'].astype(str) + " " + nfl_sched['year'].astype(str)    

    nfl_sched['team_wk_year'] = nfl_sched['CITY'] + " " + nfl_sched['week_num'].astype(str) + " " + nfl_sched['year'].astype(str)    
   
    nfl_sched['opp_wk_year'] = nfl_sched['Opp'] + " " + nfl_sched['week_num'].astype(str) + " " + nfl_sched['year'].astype(str)    

    
    nfl_sched['Sack'] = None
    nfl_sched['FR'] = None
    nfl_sched['INT'] = None
    nfl_sched['DefTD'] = None
    nfl_sched['PA'] = None
    nfl_sched['PaYD'] = None
    nfl_sched['RuYd'] = None
    nfl_sched['Safety'] = None
    nfl_sched['KickTD'] = None
    nfl_sched['FPts'] = None
    nfl_sched['away flag'] = None

    def_df['Opp'] = def_df['Opp'].str.replace('@','')
    def_df['opp wk year'] = def_df['Opp'] + " " + def_df['week_num'].astype(str) + " " + def_df['year'].astype(str)
    #def_df = def_df.append(nfl_sched)
    
    def_df = def_df.append(nfl_sched)
    def_df = def_df.drop(columns = ['opp wk year'])
    
    def_df_wk = def_feat_eng_df_creation_v2(def_df = def_df#,
                                 #file_save = file_save
                                        )
    
    filt_wk = " " + str(curr_wk) + " " + str(curr_yr)
    
    def_df_wk = def_df_wk[def_df_wk['team_wk_year'].str.contains(filt_wk)]
    
    #def_df_wk.to_cvs(file_save)
    
    return def_df_wk

def curr_wk_cleanup_final_df(df, position):
    if (position == 'QB'):
        df = df.drop(columns = [
            'Fumbles FF','Fumbles FL','Fumbles FR','Fumbles Fmb',
            'Fumbles TD','Fumbles Yds','Off. Snaps Num','Off. Snaps Pct',
            'Passing AY/A','Passing Att','Passing Cmp','Passing Cmp%',
            'Passing Int','Passing Int', 'Passing Rate', 'Passing Sk',
            'Passing TD','Passing Y/A','Passing Yds','Passing Sack Yds Lost',
            #'Player ',
            'Rushing Att','Rushing TD','Rushing Y/A',
            'Rushing Yds','Scoring 2PM','Scoring Pts','Scoring TD',
            'Rk','GS',#'Year','Date','G#',
            'Age',#'Tm','home_away',
            #'Result','Player  1 wks ago',
            'Date 1 wks ago',
            'Week 1 wks ago',#'Tm 1 wks ago',
            'home_away 1 wks ago',
            'Opp 1 wks ago','Result 1 wks ago','player_wk_year 1 wks ago',
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago',
            'Opp 2 wks ago','Result 2 wks ago','player_wk_year 2 wks ago',
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago',
            'Opp 3 wks ago','Result 3 wks ago','player_wk_year 3 wks ago',
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago',
            'Opp 4 wks ago','Result 4 wks ago','player_wk_year 4 wks ago',
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago',
            'Opp 5 wks ago','Result 5 wks ago','player_wk_year 5 wks ago',
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago',
            'Opp 6 wks ago','Result 6 wks ago','player_wk_year 6 wks ago',
            #'Team',
            'Week','FR','INT','DefTD','PA','PaYD','RuYd',
            'Safety','KickTD','FPts','week_num','year','away flag',
            'opp Team 1wks ago','opp CITY 1wks ago','opp away flag 1wks ago',
            'opp Team 2wks ago','opp CITY 2wks ago','opp away flag 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago','opp away flag 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago','opp away flag 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago','opp away flag 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago','opp away flag 6wks ago',
            'opp wk year','CITY','Opp','team_wk_year',#'team_wk_year 1 wks ago',
            #'team_wk_year 2 wks ago','team_wk_year 3 wks ago','team_wk_year 4 wks ago',
            #'team_wk_year 5 wks ago','team_wk_year 6 wks ago',
            'def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','player_wk_year_team',
            'season',#'club_code',
            'week','game_type',#'depth_team',
            'position',
            #'full_name',
            'player_name','team','depth_chart_position',
            'status_description_abbr','game_type',
            'sum Off. Snaps Pct 2wk trend','sum Off. Snaps Pct 3wk trend',
            'sum Off. Snaps Pct 4wk trend','sum Off. Snaps Pct 5wk trend',
            'sum Off. Snaps Pct 6wk trend', 'sum Passing AY/A 2wk trend',
            'sum Passing AY/A 3wk trend','sum Passing AY/A 4wk trend',
            'sum Passing AY/A 5wk trend','sum Passing AY/A 6wk trend',
            'sum Passing Cmp% 2wk trend','sum Passing Cmp% 3wk trend',
            'sum Passing Cmp% 4wk trend','sum Passing Cmp% 5wk trend',
            'sum Passing Cmp% 6wk trend','sum Passing Rate 2wk trend',
            'sum Passing Rate 3wk trend','sum Passing Rate 4wk trend',
            'sum Passing Rate 5wk trend','sum Passing Rate 6wk trend',
            'sum Passing Y/A 2wk trend','sum Passing Y/A 3wk trend',
            'sum Passing Y/A 4wk trend','sum Passing Y/A 5wk trend',
            'sum Passing Y/A 6wk trend','sum Rushing Y/A 2wk trend',
            'sum Rushing Y/A 3wk trend','sum Rushing Y/A 4wk trend',
            'sum Rushing Y/A 5wk trend','sum Rushing Y/A 6wk trend'
        ])
    elif ((position == 'RB') | 
          (position == 'WR')):
        df = df.drop(columns = [
         'Fumbles FF','Fumbles FL','Fumbles FR','Fumbles Fmb',
            'Fumbles TD','Fumbles Yds','Kick Returns Rt','Kick Returns TD',
            'Kick Returns Y/Rt','Kick Returns Yds',
            'Off. Snaps Num','Off. Snaps Pct',
            #'Player ',
            'Punt Returns Ret','Punt Returns TD',
            'Punt Returns Y/R','Punt Returns Yds','Receiving Ctch%',
            'Receiving Rec','Receiving TD','Receiving Tgt','Receiving Y/R',
            'Receiving Y/Tgt','Receiving Yds',
            'Rushing Att','Rushing TD','Rushing Y/A',
            'Rushing Yds','ST Snaps Num','ST Snaps Pct',
            'Scoring 2PM','Scoring Pts','Scoring TD',
            'Rk','GS',#'Year','Date','G#',
            'Age',#'Tm','home_away',
            #'Result','Player  1 wks ago',
            'Date 1 wks ago',
            'Week 1 wks ago',#'Tm 1 wks ago',
            'home_away 1 wks ago',
            'Opp 1 wks ago','Result 1 wks ago','player_wk_year 1 wks ago',
           # 'team_wk_year 1 wks ago',
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago',
            'Opp 2 wks ago','Result 2 wks ago','player_wk_year 2 wks ago',
           # 'team_wk_year 2 wks ago',
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago',
            'Opp 3 wks ago','Result 3 wks ago','player_wk_year 3 wks ago',
           # 'team_wk_year 3 wks ago',
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago',
            'Opp 4 wks ago','Result 4 wks ago','player_wk_year 4 wks ago',
           # 'team_wk_year 4 wks ago',
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago',
            'Opp 5 wks ago','Result 5 wks ago','player_wk_year 5 wks ago',
           # 'team_wk_year 5 wks ago',
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago',
            'Opp 6 wks ago','Result 6 wks ago','player_wk_year 6 wks ago',
           # 'team_wk_year 6 wks ago',
            #'Team',
            'Week','Sack','FR','INT','DefTD','PA','PaYD','RuYd',
            'Safety','KickTD','FPts','week_num','year','away flag',
            'opp Team 1wks ago','opp CITY 1wks ago','opp away flag 1wks ago',
            'opp Team 2wks ago','opp CITY 2wks ago','opp away flag 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago','opp away flag 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago','opp away flag 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago','opp away flag 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago','opp away flag 6wks ago',
            'opp wk year','CITY','Opp','team_wk_year',#'team_wk_year 1 wks ago',
            #'team_wk_year 2 wks ago','team_wk_year 3 wks ago','team_wk_year 4 wks ago',
            #'team_wk_year 5 wks ago','team_wk_year 6 wks ago',
            'def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','player_wk_year_team',
            'season',#'club_code',
            'week','game_type',#'depth_team',
            'position',
            #'full_name',
            'player_name','team','depth_chart_position',
            'status_description_abbr','game_type',
            'sum Kick Returns Y/Rt 2wk trend',
            'sum Kick Returns Y/Rt 3wk trend','sum Kick Returns Y/Rt 4wk trend',
            'sum Kick Returns Y/Rt 5wk trend','sum Kick Returns Y/Rt 6wk trend',
            'sum Off. Snaps Pct 2wk trend','sum Off. Snaps Pct 3wk trend',
            'sum Off. Snaps Pct 4wk trend','sum Off. Snaps Pct 5wk trend',
            'sum Off. Snaps Pct 6wk trend', 'sum Punt Returns Y/R 2wk trend',
            'sum Punt Returns Y/R 3wk trend','sum Punt Returns Y/R 4wk trend',
            'sum Punt Returns Y/R 5wk trend','sum Punt Returns Y/R 6wk trend',
            'sum Receiving Ctch% 2wk trend','sum Receiving Ctch% 3wk trend',
            'sum Receiving Ctch% 4wk trend','sum Receiving Ctch% 5wk trend',
            'sum Receiving Ctch% 6wk trend','sum Receiving Y/R 2wk trend',
            'sum Receiving Y/R 3wk trend','sum Receiving Y/R 4wk trend',
            'sum Receiving Y/R 5wk trend','sum Receiving Y/R 6wk trend',
            'sum Receiving Y/Tgt 2wk trend','sum Receiving Y/Tgt 3wk trend',
            'sum Receiving Y/Tgt 4wk trend','sum Receiving Y/Tgt 5wk trend',
            'sum Receiving Y/Tgt 6wk trend',
            'sum Rushing Y/A 2wk trend',
            'sum Rushing Y/A 3wk trend','sum Rushing Y/A 4wk trend',
            'sum Rushing Y/A 5wk trend','sum Rushing Y/A 6wk trend',
            'sum ST Snaps Pct 2wk trend','sum ST Snaps Pct 3wk trend',
            'sum ST Snaps Pct 4wk trend','sum ST Snaps Pct 5wk trend',
            'sum ST Snaps Pct 6wk trend'
        ])
    elif(position == 'TE'):
        df = df.drop(columns = [
         'Fumbles FF','Fumbles FL','Fumbles FR','Fumbles Fmb',
            'Fumbles TD','Fumbles Yds',
            'Off. Snaps Num','Off. Snaps Pct',
            #'Player ',
            'Receiving Ctch%',
            'Receiving Rec','Receiving TD','Receiving Tgt','Receiving Y/R',
            'Receiving Y/Tgt','Receiving Yds',
            'Rushing Att','Rushing TD','Rushing Y/A',
            'Rushing Yds','ST Snaps Num','ST Snaps Pct',
            'Scoring 2PM','Scoring Pts','Scoring TD',
            'Rk','GS',#'Year','Date','G#',
            'Age',#'Tm','home_away',
            #'Result','Player  1 wks ago',
            'Date 1 wks ago',
            'Week 1 wks ago',#'Tm 1 wks ago',
            'home_away 1 wks ago',
            'Opp 1 wks ago','Result 1 wks ago','player_wk_year 1 wks ago',
            #'team_wk_year 1 wks ago',
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago',
            'Opp 2 wks ago','Result 2 wks ago','player_wk_year 2 wks ago',
            #'team_wk_year 2 wks ago',
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago',
            'Opp 3 wks ago','Result 3 wks ago','player_wk_year 3 wks ago',
            #'team_wk_year 3 wks ago',
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago',
            'Opp 4 wks ago','Result 4 wks ago','player_wk_year 4 wks ago',
            #'team_wk_year 4 wks ago',
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago',
            'Opp 5 wks ago','Result 5 wks ago','player_wk_year 5 wks ago',
            #'team_wk_year 5 wks ago',
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago',
            'Opp 6 wks ago','Result 6 wks ago','player_wk_year 6 wks ago',
            #'team_wk_year 6 wks ago',
            #'Team',
            'Week','Sack','FR','INT','DefTD','PA','PaYD','RuYd',
            'Safety','KickTD','FPts','week_num','year','away flag',
            'opp Team 1wks ago','opp CITY 1wks ago','opp away flag 1wks ago',
            'opp Team 2wks ago','opp CITY 2wks ago','opp away flag 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago','opp away flag 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago','opp away flag 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago','opp away flag 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago','opp away flag 6wks ago',
            'opp wk year','CITY','Opp','team_wk_year',#'team_wk_year 1 wks ago',
            #'team_wk_year 2 wks ago','team_wk_year 3 wks ago','team_wk_year 4 wks ago',
            #'team_wk_year 5 wks ago','team_wk_year 6 wks ago',
            'def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','player_wk_year_team',
            'season',#'club_code',
            'week','game_type',#'depth_team',
            'position',
            #'full_name',
            'player_name','team','depth_chart_position',
            'status_description_abbr','game_type',
            'sum Off. Snaps Pct 2wk trend','sum Off. Snaps Pct 3wk trend',
            'sum Off. Snaps Pct 4wk trend','sum Off. Snaps Pct 5wk trend',
            'sum Off. Snaps Pct 6wk trend','sum Receiving Ctch% 2wk trend','sum Receiving Ctch% 3wk trend',
            'sum Receiving Ctch% 4wk trend','sum Receiving Ctch% 5wk trend',
            'sum Receiving Ctch% 6wk trend','sum Receiving Y/R 2wk trend',
            'sum Receiving Y/R 3wk trend','sum Receiving Y/R 4wk trend',
            'sum Receiving Y/R 5wk trend','sum Receiving Y/R 6wk trend',
            'sum Receiving Y/Tgt 2wk trend','sum Receiving Y/Tgt 3wk trend',
            'sum Receiving Y/Tgt 4wk trend','sum Receiving Y/Tgt 5wk trend',
            'sum Receiving Y/Tgt 6wk trend',
            'sum Rushing Y/A 2wk trend',
            'sum Rushing Y/A 3wk trend','sum Rushing Y/A 4wk trend',
            'sum Rushing Y/A 5wk trend','sum Rushing Y/A 6wk trend',
            'sum ST Snaps Pct 2wk trend','sum ST Snaps Pct 3wk trend',
            'sum ST Snaps Pct 4wk trend','sum ST Snaps Pct 5wk trend',
            'sum ST Snaps Pct 6wk trend'
        ])
    elif(position == 'K'):
        df = df.drop(columns = [
            #'Player ',
            'ST Snaps Num','ST Snaps Pct',
            'Scoring Pts','ScoringXPM','ScoringXPA','ScoringXP%',
            'ScoringFGM','ScoringFGA','ScoringFG%',
            'Rk','GS',#'Year','Date','G#',
            'Age',#'Tm','home_away',
            #'Result','Player  1 wks ago',
            'Date 1 wks ago',
            'Week 1 wks ago',#'Tm 1 wks ago',
            'home_away 1 wks ago',
            'Opp 1 wks ago','Result 1 wks ago','player_wk_year 1 wks ago',
            #'team_wk_year 1 wks ago',
            'Player  2 wks ago','Date 2 wks ago',
            'Week 2 wks ago','Tm 2 wks ago','home_away 2 wks ago',
            'Opp 2 wks ago','Result 2 wks ago','player_wk_year 2 wks ago',
            #'team_wk_year 2 wks ago',
            'Player  3 wks ago','Date 3 wks ago',
            'Week 3 wks ago','Tm 3 wks ago','home_away 3 wks ago',
            'Opp 3 wks ago','Result 3 wks ago','player_wk_year 3 wks ago',
            #'team_wk_year 3 wks ago',
            'Player  4 wks ago','Date 4 wks ago',
            'Week 4 wks ago','Tm 4 wks ago','home_away 4 wks ago',
            'Opp 4 wks ago','Result 4 wks ago','player_wk_year 4 wks ago',
            #'team_wk_year 4 wks ago',
            'Player  5 wks ago','Date 5 wks ago',
            'Week 5 wks ago','Tm 5 wks ago','home_away 5 wks ago',
            'Opp 5 wks ago','Result 5 wks ago','player_wk_year 5 wks ago',
            #'team_wk_year 5 wks ago',
            'Player  6 wks ago','Date 6 wks ago',
            'Week 6 wks ago','Tm 6 wks ago','home_away 6 wks ago',
            'Opp 6 wks ago','Result 6 wks ago','player_wk_year 6 wks ago',
            #'team_wk_year 6 wks ago',
            #'Team',
            'Week','Sack','FR','INT','DefTD','PA','PaYD','RuYd',
            'Safety','KickTD','FPts','week_num','year','away flag',
            'opp Team 1wks ago','opp CITY 1wks ago','opp away flag 1wks ago',
            'opp Team 2wks ago','opp CITY 2wks ago','opp away flag 2wks ago',
            'opp Team 3wks ago','opp CITY 3wks ago','opp away flag 3wks ago',
            'opp Team 4wks ago','opp CITY 4wks ago','opp away flag 4wks ago',
            'opp Team 5wks ago','opp CITY 5wks ago','opp away flag 5wks ago',
            'opp Team 6wks ago','opp CITY 6wks ago','opp away flag 6wks ago',
            'opp wk year','CITY','Opp','team_wk_year',#'team_wk_year 1 wks ago',
            #'team_wk_year 2 wks ago','team_wk_year 3 wks ago','team_wk_year 4 wks ago',
            #'team_wk_year 5 wks ago','team_wk_year 6 wks ago',
            'def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','player_wk_year_team',
            'season',#'club_code',
            'week','game_type',#'depth_team',
            'position',
            #'full_name',
            'player_name','team','depth_chart_position',
            'status_description_abbr','game_type',
            'sum ScoringXP% 2wk trend','sum ScoringXP% 3wk trend',
            'sum ScoringXP% 4wk trend','sum ScoringXP% 5wk trend',
            'sum ScoringXP% 6wk trend','sum ScoringFG% 2wk trend',
            'sum ScoringFG% 3wk trend','sum ScoringFG% 4wk trend',
            'sum ScoringFG% 5wk trend','sum ScoringFG% 6wk trend'
        ])
    elif(position=='D'):
        df = df[df['FPts'].isnull()]
        df = df.drop(columns = [
            'Team',
            #'CITY','Week',
            'FPts','week_num',#'year',
            #'Opp',#'team_wk_year',
            'opp_wk_year','Year',
            'TEAM','Opponent','team_wk_year 1 wks ago','team_wk_year 2 wks ago',
            'team_wk_year 3 wks ago','team_wk_year 4 wks ago',
            'team_wk_year 5 wks ago','team_wk_year 6 wks ago',
            'def matchup Opp 1wks ago','def matchup away flag 1wks ago',
            'def matchup team_wk_year 1wks ago','def matchup opp_wk_year 1wks ago',
            'def matchup Opp 2wks ago','def matchup away flag 2wks ago',
            'def matchup team_wk_year 2wks ago','def matchup opp_wk_year 2wks ago',
            'def matchup Opp 3wks ago','def matchup away flag 3wks ago',
            'def matchup team_wk_year 3wks ago','def matchup opp_wk_year 3wks ago',
            'def matchup Opp 4wks ago','def matchup away flag 4wks ago',
            'def matchup team_wk_year 4wks ago','def matchup opp_wk_year 4wks ago',
            'def matchup Opp 5wks ago','def matchup away flag 5wks ago',
            'def matchup team_wk_year 5wks ago','def matchup opp_wk_year 5wks ago',
            'def matchup Opp 6wks ago','def matchup away flag 6wks ago',
            'def matchup team_wk_year 6wks ago','def matchup opp_wk_year 6wks ago',
            'opp_wk_year 1 wks ago','opp_wk_year 2 wks ago','opp_wk_year 3 wks ago',
            'opp_wk_year 4 wks ago','opp_wk_year 5 wks ago','opp_wk_year 6 wks ago',
            'opp matchup CITY 1wks ago','opp matchup CITY 2wks ago',
            'opp matchup CITY 3wks ago','opp matchup CITY 4wks ago',
            'opp matchup CITY 5wks ago','opp matchup CITY 6wks ago',
            'opp matchup away flag 1wks ago','opp matchup team_wk_year 1wks ago',
            'opp matchup opp_wk_year 1wks ago',
            'opp matchup away flag 2wks ago','opp matchup team_wk_year 2wks ago',
            'opp matchup opp_wk_year 2wks ago',
            'opp matchup away flag 3wks ago','opp matchup team_wk_year 3wks ago',
            'opp matchup opp_wk_year 3wks ago',
            'opp matchup away flag 4wks ago','opp matchup team_wk_year 4wks ago',
            'opp matchup opp_wk_year 4wks ago',
            'opp matchup away flag 5wks ago','opp matchup team_wk_year 5wks ago',
            'opp matchup opp_wk_year 5wks ago',
            'opp matchup away flag 6wks ago','opp matchup team_wk_year 6wks ago',
            'opp matchup opp_wk_year 6wks ago'
            
        ])
        
            
        
    return df

def data_prep_for_curr_wk_player_pull(year, week):

    test_fun = update_player_weekly_stats()
    nfl_sched = get_nfl_sched()#pd.read_csv('C:/Users/bobbr/OneDrive/Documents/The Plan/NFL/NFL Schedule.csv')

    test = def_weekly_stats_scrape(first_yr = 2015, last_yr = year, nfl_sched = nfl_sched)
    
    def_weekly = def_curr_wk_for_positions(def_df = test,
                    nfl_sched = nfl_sched,
                    curr_wk = week,
                    curr_yr = year)
    
    return year, week, test_fun, nfl_sched, test, def_weekly

    
def qb_curr_wk_data_pull(year, week, test_fun, nfl_sched,
                         def_weekly):
    
    df_qb = create_curr_wk_oot_qb(nfl_sched = nfl_sched,
                                   year= year, 
                                   week = week,
                                   player_df=test_fun,
                                   position = 'QB',
                                  def_df = def_weekly)
    
    test_final = create_qb_trend_var(qb_df=df_qb,
                                 position = 'QB')
    
    test_final2 = curr_wk_cleanup_final_df(df=test_final, position='QB')
    file_save = str(year) + "week" + str(week) + 'qb_final.csv'
    test_final2.to_csv(file_save)
    
    return test_final2

def wr_curr_wk_data_pull(year, week, test_fun, nfl_sched,
                         def_weekly):
    
    df_qb = create_curr_wk_oot_qb(nfl_sched = nfl_sched,
                                   year= year, 
                                   week = week,
                                   player_df=test_fun,
                                   position = 'WR',
                                  def_df = def_weekly)
    
    test_final = create_qb_trend_var(qb_df=df_qb,
                                 position = 'WR')
    
    test_final2 = curr_wk_cleanup_final_df(df=test_final, position='WR')
    file_save = str(year) + "week" + str(week) + 'wr_final.csv'
    test_final2.to_csv(file_save)
    
    return test_final2

def rb_curr_wk_data_pull(year, week, test_fun, nfl_sched,
                         def_weekly):
    
    df_qb = create_curr_wk_oot_qb(nfl_sched = nfl_sched,
                                   year= year, 
                                   week = week,
                                   player_df=test_fun,
                                   position = 'RB',
                                  def_df = def_weekly)
    
    test_final = create_qb_trend_var(qb_df=df_qb,
                                 position = 'RB')
    
    test_final2 = curr_wk_cleanup_final_df(df=test_final, position='RB')
    file_save = str(year) + "week" + str(week) + 'rb_final.csv'
    test_final2.to_csv(file_save)
    
    return test_final2

def te_curr_wk_data_pull(year, week, test_fun, nfl_sched,
                         def_weekly):
    
    df_qb = create_curr_wk_oot_qb(nfl_sched = nfl_sched,
                                   year= year, 
                                   week = week,
                                   player_df=test_fun,
                                   position = 'TE',
                                  def_df = def_weekly)
    
    test_final = create_qb_trend_var(qb_df=df_qb,
                                 position = 'TE')
    
    test_final2 = curr_wk_cleanup_final_df(df=test_final, position='TE')
    file_save = str(year) + "week" + str(week) + 'te_final.csv'
    test_final2.to_csv(file_save)
    
    return test_final2


def k_curr_wk_data_pull(year, week, test_fun, nfl_sched,
                         def_weekly):
    
    df_qb = create_curr_wk_oot_qb(nfl_sched = nfl_sched,
                                   year= year, 
                                   week = week,
                                   player_df=test_fun,
                                   position = 'K',
                                  def_df = def_weekly)
    
    test_final = create_qb_trend_var(qb_df=df_qb,
                                 position = 'K')
    
    test_final2 = curr_wk_cleanup_final_df(df=test_final, position='K')
    file_save = str(year) + "week" + str(week) + 'k_final.csv'
    test_final2.to_csv(file_save)
    
    return test_final2


def def_curr_wk_data_pull(year, week, def_df):
    
    def_temp = def_curr_wk_oot(def_df = def_df,
                              curr_wk = week,
                              curr_yr = year)
    
    def_final = curr_wk_cleanup_final_df(df=def_temp, position='D')
    file_save = str(year) + "week" + str(week) + 'D_final.csv'
    def_final.to_csv(file_save)

    return def_final


def run_curr_wk_update_weekly_player_stats(year, week):
    
    year, week, test_fun, nfl_sched, test, def_weekly = data_prep_for_curr_wk_player_pull(year, week)
    print("QB Curr Wk Data Pull Start")
    test_final_qb = qb_curr_wk_data_pull(year, week, test_fun, 
                                   nfl_sched, def_weekly)

    
    print("RB Curr Wk Data Pull Start")
    test_final_rb = rb_curr_wk_data_pull(year, week, test_fun, 
                                   nfl_sched, def_weekly)
    
    print("WR Curr Wk Data Pull Start")
    test_final_wr = wr_curr_wk_data_pull(year, week, test_fun, 
                                   nfl_sched, def_weekly)   
    print("TE Curr Wk Data Pull Start")
    test_final_te = te_curr_wk_data_pull(year, week, test_fun, 
                                   nfl_sched, def_weekly)
    
    print("K Curr Wk Data Pull Start")
    test_final_k = k_curr_wk_data_pull(year, week, test_fun,
                                  nfl_sched, def_weekly)
    
    print("D Curr Wk Data Pull Start")
    test_final_d = def_curr_wk_data_pull(year, week, def_df= test)
    
    del year
    del week
    del test_fun
    del nfl_sched
    del test
    del def_weekly
    
    return test_final_qb, test_final_rb, test_final_wr, test_final_te, test_final_k, test_final_d
    