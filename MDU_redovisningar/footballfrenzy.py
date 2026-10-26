import requests
url = 'https://football-frenzy.s3.eu-north-1.amazonaws.com/api'

def get_games(year:int) -> list:
    curr_url = url + '/' + str(year)
    res = requests.get(curr_url)
    year_data = res.json()
    game_days = []
    days = year_data['gamedays']
    
    for day in days:
        new_url = curr_url + '/' + day
        new_res = requests.get(new_url)
        day_data = new_res.json()
        game_days.append(day_data)    
    return game_days

def get_results(year:int, home_goals:int, away_goals:int) -> list:
    base_list = get_games(year)
    matched_games = []
    
    for b in base_list:
        games_dict = b['games']
        curr_date = b['date']
        for game in games_dict:
            scores_dict = game['score']
            home = scores_dict['home']
            away = scores_dict['away']
            
            if home['goals'] == home_goals and away['goals'] == away_goals:
                curr_str = f"({home_goals}) {home['team']} - ({away_goals}) {away['team']}"
                send_dict = {'date': curr_date, 'result': curr_str}
                matched_games.append(send_dict)
    return matched_games  

while True:
    year = int(input('Enter year:'))
    home_goals = int(input('Enter home goals:'))
    away_goals = int(input('Enter away goals:'))
    results = get_results(year, home_goals, away_goals)
    for r in results:
        print(f"[{r['date']}] {r['result']}")
    
    
