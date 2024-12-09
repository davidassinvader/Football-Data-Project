# Football data project

import json

# This code is responsible for actually requesting a fresh dataset from the API we're using.
# For now, just load the example dataset while we build out the app
#url = 'https://api.football-data.org/v4/matches'
#personal_oauth_token = '8628fc9dddc84b7c8ebde7d3bbd4398a'
#
#request_headers = { 'X-Auth-Token': personal_oauth_token }
#
#match_data = req.get(url, headers=request_headers)
#
#with open('match_data.json', 'w') as data:
#    json.dump(match_data.json(), data)


# Read in the example dataset.
with open('match_data.json','r') as match_data:
    matches = json.load(match_data)


# This function takes the .json file and parses it for all matches in the league specified by the "league" argument of the function.
# It then returns a list containing the home & away teams, score and result of each game as a string.
def basic_results(match_results_json: json, league: str) -> list:
    
    relevant_matches = [ result for result in match_results_json['matches'] if result['competition']['name'] == league]
    matches_output_list = []
    
    for match in relevant_matches:
        matches_output_list.append(f'Game {relevant_matches.index(match)+1} - Winner: {match['score']['winner']}\nHome: {match["homeTeam"]["name"]} - {match['score']['fullTime']['home']}\nAway: {match["awayTeam"]["name"]} - {match['score']['fullTime']['away']}\n')

    return matches_output_list

# Demonstrating output of basic_results function
if __name__ == "__main__":
    for i in basic_results(matches, "Premier League"):
        print(i)
