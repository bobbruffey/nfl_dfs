import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os 
from tensorflow.keras.losses import MeanSquaredError
from kerastuner.tuners import RandomSearch
from sklearn.model_selection import RandomizedSearchCV
import shutil
import pandas as pd
import numpy as np
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import xgboost as xgb
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBClassifier

import seaborn as sns
import warnings 
warnings.simplefilter('ignore')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)

def prepare_modeling_df(df, position):

    if (position == 'QB'):
        df = df.fillna(0)
        df['FantasyPoints'] = -df['Fumbles FL']*1 - df['Passing Int']*2 + df['Passing TD']*4 + df['Passing Yds']*0.05 +df['Rushing Yds']*0.1 + df['Rushing TD']*6+df['Scoring 2PM']*2
        df['FantasyPoints2'] = np.where(df['FantasyPoints']>=20,1,0)
        df = df[df['FantasyPoints'] > 0]
        
        df = df.drop(columns = ['Unnamed: 0',
                            'Fumbles FF','Fumbles FL',
                            'Fumbles FR','Fumbles Fmb','Fumbles TD',
                            'Fumbles Yds','Off. Snaps Num','Off. Snaps Pct',
                            'Passing AY/A','Passing Att','Passing Cmp',
                            'Passing Cmp%','Passing Int','Passing Rate',
                            'Passing Sk','Passing TD','Passing Y/A',
                            'Passing Yds','Passing Sack Yds Lost',
                            'Rushing Att','Rushing TD','Rushing Y/A',
                            'Rushing Yds','Scoring 2PM','Scoring Pts',
                            'Scoring TD','Year','Age','Week','Sack','FR','INT',
                            'DefTD','PA','PaYD','RuYd','Safety','KickTD','FPts'
                            ])
    
    return df