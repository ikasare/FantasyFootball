import requests
import json
import pandas as pd

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
        
        team1 = 'Chelsea' #input('Please enter the home team: ')
        team2 = 'Arsenal' #input('Please enter the away team: ')
        player = 'Mason Mount' #input("Please enter the midfielder's name: ")

        querystring = {'team1': team1, 'team2': team2, 'player': player}

        headers = {
            'x-rapidapi-key': "d1d4b18bb8mshb6f0f40d2cc89ddp13206bjsnaa6185b9070d",
            'x-rapidapi-host': "heisenbug-premier-league-live-scores-v1.p.rapidapi.com"
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()['stats']
        print(player)
        stats = {'touches': response.get('touches', 0),
                 'Passes Completed': response.get('passesSuccessful', 0),
                 'Dribbles Won': response.get('dribblesWon', 0),
                 'Goals': response.get('goals', 0)}
        print(stats)
get_stats_for_game()