import os
import requests
from dotenv import load_dotenv

load_dotenv()

MLB_API_URL = "https://statsapi.mlb.com/api/v1/"
TEAM_METS_ID = 121  # New York Mets
TEAM_BLUE_JAYS_ID = 141  # Toronto Blue Jays

def fetch_team_stats(team_id):
    response = requests.get(f"{MLB_API_URL}teams/{team_id}/stats")
    response.raise_for_status()
    return response.json()

def main():
    mets_stats = fetch_team_stats(TEAM_METS_ID)
    blue_jays_stats = fetch_team_stats(TEAM_BLUE_JAYS_ID)
    
    mets_losses = mets_stats['stats'][0]['splits'][0]['stat']['losses']
    blue_jays_wins = blue_jays_stats['stats'][0]['splits'][0]['stat']['wins']
    
    if mets_losses > 0 and blue_jays_wins > 0:
        print(f"Mets Losses: {mets_losses}, Blue Jays Wins: {blue_jays_wins}")
        # Send GIFs to trigger a Mets fan (placeholder for GIF sending logic)

if __name__ == '__main__':
    main()