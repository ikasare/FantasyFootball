import requests
import json
import pandas as pd
import os
from sqlalchemy import create_engine

#make user input team to look up its midfielders


def get_team_midfielders():
        url = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/players"

        querystring = {"team": input('Please enter a team whose midfielders you want to see: ')}

        headers = {
            'x-rapidapi-key': "d1d4b18bb8mshb6f0f40d2cc89ddp13206bjsnaa6185b9070d",
            'x-rapidapi-host': "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()['players']
        print(str(querystring['team']) + " midfelders: ")
        for player in response:
            if 'Midfield' in player['position']:
                print(player)

                
#get_team_midfielders()


def get_stats_for_game():
        url = "https://heisenbug-premier-league-live-scores-v1.p.rapidapi.com/api/premierleague/match/player"
        col_names = ['Player Name', 'Touches', 'Passes Completed', 'Dribbles Won', 'Goals', 'Home Team', 'Away Team']
        df = pd.DataFrame(columns=col_names)
        
        exit = ""
        while exit != 'Q':
            team1 = input('Please enter the home team: ')# 'Chelsea' 
            team2 = input('Please enter the away team: ') #'Arsenal' 
            player = input("Please enter the midfielder's name: ") #'Mason Mount' 

            querystring = {'team1': team1, 'team2': team2, 'player': player}

            headers = {
                'x-rapidapi-key': "d1d4b18bb8mshb6f0f40d2cc89ddp13206bjsnaa6185b9070d",
                'x-rapidapi-host': "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
                }
            response = requests.request("GET", url, headers=headers, params=querystring)
            response = response.json()['stats']
            stats = {'Player Name': player,
                     'Touches': response.get('touches', 0),
                     'Passes Completed': response.get('passesSuccessful', 0),
                     'Dribbles Won': response.get('dribblesWon', 0),
                     'Goals': response.get('goals', 0)}
            df.loc[len(df.index)] = [stats['Player Name'], stats['Touches'], stats['Passes Completed'], stats['Dribbles Won'], stats['Goals'], team1, team2]
            exit  = input('Enter Q to exit, C to continue: ')
        return df
        
        
def createdb():
        df = get_stats_for_game()
        os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' + 'Premier_League' + ';"')
        engine = create_engine('mysql://root:codio@localhost/Premier_League')
        df.to_sql('Midfielders', con=engine, if_exists='replace', index=False)

def savedb():
    os.system("mysqldump -u root -pcodio Premier_League > epl.sql")

def loaddb():
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' +
              'Premier_League' + ';"')
    os.system("mysql -u root -pcodio Premier_League < epl.sql")

createdb()
savedb()
                  