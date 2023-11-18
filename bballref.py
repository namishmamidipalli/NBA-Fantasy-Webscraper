from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def nbaindex():
    return render_template('nbaindex.html')

@app.route('/scrape', methods=['POST'])
def scrape():
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
    'PHO': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}



    # victim = requests.get("https://www.basketball-reference.com/leaders/")

    my_players = {"Fred VanVleet": {"Team": "Houston Rockets", "Abbreviation": "HOU"}, "Ausar Thompson": {"Team": "Detroit Pistons", "Abbreviation": "DET"}, "Jimmy Butler": {"Team": "Miami Heat", "Abbreviation": "MIA"},
            "Jaren Jackson Jr.": {"Team": "Memphis Grizzlies", "Abbreviation": "MEM"}, "Myles Turner": {"Team": "Indiana Pacers", "Abbreviation": "IND"}, "Aaron Gordon": {"Team": "Denver Nuggets", "Abbreviation": "DEN"},
            "Kawhi Leonard": {"Team": "Los Angeles Clippers", "Abbreviation": "LAC"}, "Brook Lopez": {"Team": "Milwaukee Bucks", "Abbreviation": "MIL"}, "Kevin Durant": {"Team": "Phoenix Suns", "Abbreviation": "PHO"},
            "Jrue Holiday": {"Team": "Boston Celtics", "Abbreviation": "BOS"}, "OG Anunoby": {"Team": "Toronto Raptors", "Abbreviation": "TOR"},
            "Jalen Duren": {"Team": "Detroit Pistons", "Abbreviation": "DET"}, "Anthony Davis": {"Team": "Los Angeles Lakers", "Abbreviation": "LAL"}}


    req = request.form.get('player_name')

    if req not in my_players:
        return render_template('nbaindex.html', error_message='Player not found')

    teampage = requests.get(f"https://www.basketball-reference.com/teams/{my_players[req]['Abbreviation']}/2024.html")
    teamsoup = BeautifulSoup(teampage.text, "html.parser")

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
        if i == stop_point:
            break
        newlink += playerlink[i]

    playerpage = requests.get(f"https://www.basketball-reference.com{newlink}/gamelog/2024")
    psoup = BeautifulSoup(playerpage.text, "html.parser")

    fg_element = psoup.findAll('td', {'class': 'right', 'data-stat': 'fg'})
    most_recent_fg = fg_element[-1]
    fga_element = psoup.findAll('td', {'class': 'right', 'data-stat': 'fga'})
    most_recent_fga = fga_element[-1]
    opposition = psoup.findAll('td', {'class': 'left', 'data-stat': 'opp_id'})
    most_recent_opposition = opposition[-1]
    rebounds = psoup.findAll('td', {'class': 'right', 'data-stat': 'trb'})
    most_recent_rebounds = rebounds[-1]
    assists = psoup.findAll('td', {'class': 'right', 'data-stat': 'ast'})
    most_recent_assists = assists[-1]
    points = psoup.findAll('td', {'class': 'right', 'data-stat': 'pts'})
    most_recent_points = points[-1]
    blocks = psoup.findAll('td', {'class': 'right', 'data-stat': 'blk'})
    most_recent_blocks = blocks[-1]

    result = f"In his most recent game against the {nba_teams[most_recent_opposition.text]}, {req} went {most_recent_fg.text} for {most_recent_fga.text} from the field. He had {most_recent_points.text} points, {most_recent_assists.text} assists, {most_recent_blocks.text} blocks, and {most_recent_rebounds.text} rebounds."

    return render_template('nbaindex.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
