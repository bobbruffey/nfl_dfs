# nfl_dfs
NFL DFS modeling, lineup optimization, and lineup creation library

This library is designed to help in the creation of optimal NFL lineups for Daily Fantasy Sports. The overall strategy here is to build x amount of lineups with variety to increase your chances of hitting the big one, while at the same time minimizing your risk and expected loss. With the help of advanced machine learning modelling techniques and other outside sources (e.g. vegas odds, weather, and injury designations) this library can be your one-stop shop at streamlining the creation of infinite (there is an eventually cap here) of unique lineups for any given DFS contest.

Note (1): Current version of the nfl_dfs library is developed strictly for Fanduel contests. Draftkings will be handled in future versions. 

## Contents

I. player_data_scraping
  - This folder contains the process to scrape current player weekly data and process it through a feature engineering process that can later be used for modeling.
  - Along with historical data, the upcoming weeks player information will be pulled as well so we can score players and provide projections for the current week.
  - During the football season, this script will need to be ran on a weekly basis.

II. 2023 Folder
  - Backtesting: This folder mostly contains research in understanding how previous DFS lineups and entries have performed. A backtesting process was created to be able to see how well a lineup would perform if entered into a single game contest.
  - Modelling: Data pulled from the player_data_scraping contest will be leveraged here. XGBoost modelling and scoring processes have been created to predict a players fantasy points for a given week. There is a model per position (QB, RB, WR, TE, and DEF)
  - Weekly folders (e.g., Week 1, Week 2, etc.): The weekly folders track the lineup creation process for contests within a given week.

