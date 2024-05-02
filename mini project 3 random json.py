import itertools
import json
import random
# Define the teams and their local towns
teams = ["Retro FC", "SLeek FC", "Brad FC", "Jojo FC", "Ryan FC", "Turbo FC", "Vowlks FC", "Jossy FC", "Nitro FC", "Apex FC"]
local_towns = ["Retro Town", "Sleek Town", "Brad Town", "Jojo street Town"]
# Create a list to store the fixtures
fixtures = []
# Function to generate fixtures for a given team
def generate_fixtures_for_team(team, other_teams):
    global weekend_counter  # Use the global keyword to modify the global variable
    # Shuffle the other teams list
    random.shuffle(other_teams)
    # Play each team twice, once at home and once away
    for other_team in other_teams:
        fixture = {
            "Home Team": team,
            "Away Team": other_team,
            "Local Town": local_towns[teams.index(team)],
            "Stadium": "Home Stadium",
            "Leg": 1,
            "Weekend": weekend_counter
        }
        fixtures.append(fixture)
        weekend_counter += 1
        fixture = {
            "Home Team": other_team,
            "Away Team": team,
            "Local Town": local_towns[teams.index(other_team)],
            "Stadium": "Away Stadium",
            "Leg": 2,
            "Weekend": weekend_counter
        }
        fixtures.append(fixture)
        weekend_counter += 1
# Generate fixtures for each team
weekend_counter = 1
for team in teams:
    other_teams = list(teams)
    other_teams.remove(team)
    generate_fixtures_for_team(team, other_teams)
# Display the fixtures on the screen
print("Generated Fixtures:")
for fixture in fixtures:
    print(fixture)
# Save the fixtures to a JSON file
with open('fixtures.json', 'w') as json_file:
    json.dump(fixtures, json_file)
print("Fixtures saved to fixtures.json")