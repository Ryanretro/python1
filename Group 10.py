""" In ABC premier league, there are 10 teams. This program that  generates
fixtures for these teams"""
import json

# Define the teams and their local towns. By Jossy
teams = ["CKlein Stars",
         "Dolphins FC",
         "Wolves FC",
         "Sea Horses FC",
         "Sharks United",
         "Lake Basin FC",
         "Thika United",
         "Mavuno Comrades FC",
         "Nakuru FC",
         "Ostrich Associates"]

teams_local_towns = {
    "CKlein Stars": "Nairobi",
    "Dolphins FC": "Mombasa",
    "Wolves FC": "Nairobi",
    "Sea Horses FC": "Mombasa",
    "Sharks United": "Kisumu",
    "Lake Basin FC": "Kisumu",
    "Thika United": "Thika",
    "Mavuno Comrades FC": "Thika",
    "Nakuru FC": "Nakuru",
    "Ostrich Associates": "Nakuru"}

stadium_town = [
    "Cklein Arena",
    "Wolves",
    "Dolphins",
    "SHorses Arena",
    "Sharks Field",
    "LBasin",
    "Thika Field",
    "Vuno Grounds",
    "Nakuru Field",
    "OAssociates"]

teams_stadium = dict(zip(teams, stadium_town))

# Sorting the teams based on their local towns
teams = sorted(teams, key=lambda team: teams_stadium[team])


# Generate the round-robin fixtures By Josh
def generate_round_robin_fixtures(teams):
    if len(teams) % 2:
        teams.append(None)
    rotation = list(teams)
    fixtures = []
    for i in range(len(teams) - 1):
        fixtures.append(rotation)
        rotation = [rotation[0]] + [rotation[-1]] + rotation[1:-1]
    return fixtures


fixtures = generate_round_robin_fixtures(teams)


# Organize the fixtures into weekends
def organize_into_weekends(fixtures):
    weekends = []
    for i in range(0, len(fixtures), 1):
        weekends.append(fixtures[i:i + 1])
    return weekends


weekends = organize_into_weekends(fixtures)


# Generate the final table By Ryan
def generate_final_table(weekends):
    final_table = []
    for i, weekend in enumerate(weekends, start=1):
        for fixture in weekend:
            for match in zip(fixture[::2], fixture[1::2]):
                if match[0] and match[1]:  # Ignore matches with None
                    final_table.append({
                        "Home Team": match[0],
                        "Away Team": match[1],
                        "Venue": teams_stadium[match[0]],
                        "Weekend": f"Weekend #{i}"
                    })
    return final_table

final_table = generate_final_table(weekends)

# Write the final table to a JSON file
with open('final_table.json', 'w') as f:
    json.dump(final_table, f, indent=1)