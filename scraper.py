from bs4 import BeautifulSoup
import requests
import csv


nba_teams = {
    'ATL': 'Atlanta Hawks',
    'BOS': 'Boston Celtics',
    'BRK': 'Brooklyn Nets',
    'CHO': 'Charlotte Hornets',
    'CHI': 'Chicago Bulls',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'LAC': 'LA Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHX': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}



victim = requests.get("https://www.basketball-reference.com/leaders/")

my_players = {"Fred VanVleet": {"Team": "Houston Rockets", "Abbreviation": "HOU"}, "Ausar Thompson": {"Team": "Detroit Pistons", "Abbreviation": "DET"}, "Jimmy Butler": {"Team": "Miami Heat", "Abbreviation": "MIA"},
            "Jaren Jackson Jr.": {"Team": "Memphis Grizzlies", "Abbreviation": "MEM"}, "Myles Turner": {"Team": "Indiana Pacers", "Abbreviation": "IND"}, "Aaron Gordon": {"Team": "Denver Nuggets", "Abbreviation": "DEN"},
            "Kawhi Leonard": {"Team": "Los Angeles Clippers", "Abbreviation": "LAC"}, "Brook Lopez": {"Team": "Milwaukee Bucks", "Abbreviation": "MIL"}, "Kevin Durant": {"Team": "Phoenix Suns", "Abbreviation": "PHO"},
            "Jrue Holiday": {"Team": "Boston Celtics", "Abbreviation": "BOS"}, "OG Anunoby": {"Team": "Toronto Raptors", "Abbreviation": "TOR"},
            "Jalen Duren": {"Team": "Detroit Pistons", "Abbreviation": "DET"}, "Anthony Davis": {"Team": "Los Angeles Lakers", "Abbreviation": "LAL"}}


soup = BeautifulSoup(victim.text, "html.parser")
current_stat_leaders = soup.findAll("div", attrs={"class": "tabular_row"})

req = input("Enter the player on your team you want the stats for: ")
for player, info in my_players.items():
    if req == player:
        print(player, info)

# prompt = input("Enter what stat you want to find, and we will find the current leader of the leaugue in that stat: ")

# for l in current_stat_leaders:
#     if req in l.text:
#         print(req + " is the leader of " + l.text)



teampage = requests.get(f"https://www.basketball-reference.com/teams/{my_players[req]['Abbreviation']}/2024.html")
teamsoup = BeautifulSoup(teampage.text, "html.parser")
# player_link = teamsoup.findAll("td", attrs={"class": "left"})
# Assuming you have BeautifulSoup installed and 'teamsoup' as the parsed HTML
# player_links = [a['href'] for a in teamsoup.select('td.left a[href^="/players/"]')]

player_info = teamsoup.select('td.left a[href^="/players/"]')
playerlink = ''
for player in player_info:
    reference = player["href"]
    name = player.text
    if name == req:
        playerlink += reference
        break
stop_point = playerlink.find(".html")
newlink = ''
for i in range(len(playerlink)):
    if i == 20:
        break
    newlink += playerlink[i]

playerpage = requests.get(f"https://www.basketball-reference.com{newlink}/gamelog/2024")
# print(f"https://www.basketball-reference.com{playerlink}/gamelog/2024")
psoup = BeautifulSoup(playerpage.text, "html.parser")

fg_element = psoup.findAll('td', {'class': 'right', 'data-stat': 'fg'})
most_recent_fg = fg_element[-1]
fga_element = psoup.findAll('td', {'class': 'right', 'data-stat': 'fga'})
most_recent_fga = fga_element[-1]
opposition = psoup.findAll('td', {'class': 'left', 'data-stat': 'opp_id'})
most_recent_opposition = opposition[-1]

print(f"In his most recent game against the {nba_teams[most_recent_opposition.text]}, {req} went {most_recent_fg.text} for {most_recent_fga.text} from the field.")










