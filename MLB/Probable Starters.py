# Required packages
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make request to baseball-reference webpage
url = 'https://www.baseball-reference.com/previews/index.shtml'
response = requests.get(url)

# Create soup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the game summary elements
game_summaries = soup.find_all('div', class_='game_summary nohover')

# Create empty lists for storing data
teams = []
starters = []
starter_ids = []

# Loop through each game summary element and extract the data
for game in game_summaries:
    team_tags = game.find_all('strong')
    team1 = team_tags[0].text.strip()
    team2 = team_tags[1].text.strip()
    
    starter_tags = game.find_all('table')[1].find_all('a')
    starter1 = starter_tags[0].text.strip()
    starter2 = starter_tags[1].text.strip()
    
    starter_id_tags = game.find_all('table')[1].find_all('a')
    starter_id1 = starter_id_tags[0]['href'].split('/')[-1].split('.')[0]
    starter_id2 = starter_id_tags[1]['href'].split('/')[-1].split('.')[0]
    
    teams.extend([team1, team2])
    starters.extend([starter1, starter2])
    starter_ids.extend([starter_id1, starter_id2])

# Create dataframe from extracted data
probable_starter_df = pd.DataFrame({
    'Team': teams,
    'Starter': starters,
    'Starter_ID': starter_ids
})