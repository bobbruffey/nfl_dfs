import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def qb_player_points(df):

    df = df.fillna(0)
    df['FantasyPoints'] = -df['Fumbles FL'].astype(int)*1 #- df['Passing Int'].astype(float)*2 + df['Passing TD'].astype(int)*4 + df['Passing Yds'].astype(int)*0.05 + df['Rushing Yds'].astype(int)*0.1 + df['Rushing TD'].astype(int)*6 + df['Scoring 2PM'].astype(int)*2
    #df['FantasyPoints'] = - df['Fumbles FL']*1 - df['Passing Int']*2 + df['Passing TD']*4 + df['Passing Yds']*0.05 + df['Rushing Yds']*0.1 + df['Rushing TD']*6 + df['Scoring 2PM']*2
    df['Position'] = 'QB'
    df = df[['FantasyPoints',
        'Player ', 'Position','Year','Date','G#','Tm',
                    'home_away','Result','Team','CITY','Passing Att','Off. Snaps Num','Off. Snaps Pct']]
    df = df.rename(columns = {'Team':'Opp','CITY':'Opp_City'})
    return df

def qb_player_points_curr_wk(df, year, week):

    df = df.fillna(0)
    df['FantasyPoints'] = -df['Fumbles FL']*1 - df['Passing Int']*2 + df['Passing TD']*4 + df['Passing Yds']*0.05 +df['Rushing Yds']*0.1 + df['Rushing TD']*6+df['Scoring 2PM']*2
    df['Position'] = 'QB'
    df = df[['FantasyPoints','Player  1 wks ago', 'Position','Year','Date','G#','Tm 1 wks ago',
                    'home_away','Result','Team','CITY']]
    df = df.rename(columns = {'Team':'Opp','CITY':'Opp_City',
                                                'Player  1 wks ago':'Player ',
                                                'Tm 1 wks ago':'Tm'})
    df['Year'] = year
    df['G#'] = week
    df = df.drop_duplicates()
    return df

