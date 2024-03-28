import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def player_points(df,position, file_save=None):

    df = df.fillna(0)
    if (position == 'QB'):
        df['FantasyPoints'] = (-df['Fumbles FL'].astype(int)*1 - df['Passing Int'].astype(float)*2 
                               + df['Passing TD'].astype(int)*4 + df['Passing Yds'].astype(int)*0.05 
                               + df['Rushing Yds'].astype(int)*0.1 + df['Rushing TD'].astype(int)*6 
                               + df['Scoring 2PM'].astype(int)*2)
        #df['FantasyPoints'] = - df['Fumbles FL']*1 - df['Passing Int']*2 + df['Passing TD']*4 + df['Passing Yds']*0.05 + df['Rushing Yds']*0.1 + df['Rushing TD']*6 + df['Scoring 2PM']*2
        df['Position'] = position
        df = df[['FantasyPoints',
            'Player ', 'Position','Year','Date','G#','Tm',
            'home_away','Result','Team','CITY','Passing Att',
            'Off. Snaps Num','Off. Snaps Pct']]
        df = df.rename(columns = {'Team':'Opp','CITY':'Opp_City'})

    elif ((position == 'RB') |
          (position == 'WR') |
          (position == 'TE')):
        df['FantasyPoints'] = (-df['Fumbles FL'].astype(int)*1 + df['Rushing Yds'].astype(int)*0.1 +
                                df['Rushing TD'].astype(int)*6+df['Scoring 2PM'].astype(int)*2
                            + df['Receiving Rec'].astype(int)*0.5 + df['Receiving Yds'].astype(int)*0.1 +
                              df['Receiving TD'].astype(int)*6) 
        df['Position'] = position

        df = df[['FantasyPoints','Player ','Position','Year',
                 'Date','G#','Tm','home_away','Result','Team',
                 'CITY','Rushing Att','Receiving Tgt',
                 'Off. Snaps Num','Off. Snaps Pct']]
        df = df.rename(columns = {'Team':'Opp','CITY':'Opp_City'})

    elif (position == 'K'):
        df['FantasyPoints'] = (df['ScoringXPM'].astype(int)*1 +
                                df['ScoringFGM'].astype(int)*4 ) 
        df['Position'] = position

        df = df[['FantasyPoints','Player ','Position','Year','Date',
                 'G#','Tm','home_away','Result','Team',
                 'CITY','ScoringFGA','ScoringXPA']]
        df = df.rename(columns = {'Team':'Opp','CITY':'Opp_City'})

    elif (position == 'D'):
        df = df[['week_num','FPts','year','Opp','team_wk_year']]
        df[['Tm', 'Week','Year']] = df.team_wk_year.str.split(" ", expand = True)
        df = df.rename(columns= {'week_num':'G#','FPts':'FantasyPoints'})
        df['Player '] = df['Tm']
        df['Date'] = ''
        df['home_away'] = ''
        df['Result'] = ''
        df['Opp_City'] = df['Opp']
        df['Position'] = 'D'
        df = df[['FantasyPoints','Player ','Position','Year',
                 'Date','G#','Tm','home_away','Result','Opp','Opp_City']]

    if (file_save != None):
        df.to_csv(file_save)

    return df


def player_points_curr_wk(df, position, year, week, file_save=None):

    df = df.fillna(0)
    df['FantasyPoints'] = 0
    df['Position'] = position
    if ((position == 'QB') |
        (position == 'RB') |
        (position == 'WR') |
        (position == 'TE')):

        df = df[['FantasyPoints','Player ',#'Player  1 wks ago', 
                 'Position','Year','Date','G#','Tm',#'Tm 1 wks ago',
                    'home_away','Result','Team','CITY']]
        df = df.rename(columns = {'Team':'Opp','CITY':'Opp_City'#,
                               # 'Player  1 wks ago':'Player ',
                               # 'Tm 1 wks ago':'Tm'
                                  })
        df['Year'] = year
        df['G#'] = week
        df = df.drop_duplicates()
    elif (position == 'D'):
        df = df[['Week','year','Opp','team_wk_year']]
        df['FPts'] = 0
        df[['Tm', 'Week','Year']] = df.team_wk_year.str.split(" ", expand = True)
        df = df.rename(columns= {'Week':'G#','FPts':'FantasyPoints'})
        df['Player '] = df['Tm']
        df['Date'] = ''
        df['home_away'] = ''
        df['Result'] = ''
        df['Opp_City'] = df['Opp']
        df['Position'] = 'D'
        df = df[['FantasyPoints','Player ','Position',
                 'Year','Date','G#','Tm','home_away',
                 'Result','Opp','Opp_City']]

    if (file_save != None):
        df.to_csv(file_save)

    return df

def combine_player_points(qb_points, rb_points,
                          wr_points, te_points,
                          k_points, d_points,
                          file_save=None):
    df = qb_points.append(rb_points)
    df = df.append(wr_points)
    df = df.append(te_points)
    df = df.append(k_points)
    df = df.append(d_points)

    if (file_save != None):
        df.to_csv(file_save)

    return df
