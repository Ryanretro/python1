import pandas as pd
import random

# Define the teams
teams = ["CKlein Stars", "Dolphins FC", "Wolves FC", "Sea Horses FC", "Sharks United", "Lake Basin FC", "Thika United", "Mavuno Comrades FC", "Nakuru FC", "Ostrich Associates"]

# Create an empty DataFrame to store the fixtures
fixtures = pd.DataFrame(columns=["Week", "Game A", "Game B"])

# Define the number of weeks
num_weeks = 18

# Define the local towns
local_towns = {
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

# Generate fixtures for the first half of the season
for week in range(1, num_weeks // 2 + 1):
    # Create a list of available teams
    available_teams = teams.copy()

    # Schedule matches between teams from different local towns
    for i in range(4):
        # Choose the first team deterministically based on its index in the available_teams list
        team_a_index = i % len(available_teams)
        team_a = available_teams[team_a_index]

        # Choose the second team deterministically based on its index in the available_teams list
        team_b_index = (i + 1) % len(available_teams)
        team_b = available_teams[team_b_index]

        # Check if the teams are from different local towns
        if local_towns[team_a] != local_towns[team_b]:
            game_a = f"{team_a} vs {team_b}"
            game_b = f"{team_b} vs {team_a}"  # Add Game B
            fixtures = fixtures.append({"Week": week, "Game A": game_a, "Game B": game_b}, ignore_index=True)

# Generate fixtures for the second half of the season
for week in range(num_weeks // 2 + 1, num_weeks + 1):
    # Randomly shuffle the teams to get different pairings
    random.shuffle(teams)

    # Schedule matches between paired teams
    for i in range(0, len(teams), 2):
        team_a, team_b = teams[i], teams[i + 1]
        game_a = f"{team_a} vs {team_b}"
        game_b = f"{team_b} vs {team_a}"  # Add Game B
        fixtures = fixtures.append({"Week": week, "Game A": game_a, "Game B": game_b}, ignore_index=True)

# Export fixtures to CSV file
fixtures.to_csv("fixtures.csv", index=False)