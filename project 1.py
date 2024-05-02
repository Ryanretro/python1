import itertools
import pandas as pd
import random

# Define teams and local towns
teams = ["Cklein", "Wolves", "Dolphi", "Sea Hors", "Sharks", "Lake B", "Thikaaaaa", "Mavuno", "Nakuruuuu", "Ostrich"]
local_towns = {
    "Nairobi": ["Cklein", "Wolves"],
    "Mombasa": ["Dolphi", "Sea Hors"],
    "Kisumu": ["Sharks", "Lake B"],
    "Thika": ["Thikaaaaa", "Mavuno"],
    "Nakuru": ["Nakuruuuu", "Ostrich"]
}

# Create DataFrame to store fixtures
fixtures = pd.DataFrame(columns=["Home Team", "Away Team", "Local Town", "Stadium", "Leg", "Weekend"])

# Function to generate fixtures for a given local town
def generate_fixtures_for_town(town_teams):
    global weekend_counter  # Use the global keyword to modify the global variable

    # Shuffle the teams list
    random.shuffle(town_teams)

    # Generate fixtures for each team in the town
    for team1, team2 in itertools.combinations(town_teams, 2):
        # Play each pair twice, once at home and once away
        for leg in range(1, 3):
            fixtures.loc[len(fixtures)] = [team1, team2, town, "Home Stadium", leg, weekend_counter]
            weekend_counter += 1

            fixtures.loc[len(fixtures)] = [team2, team1, town, "Away Stadium", leg, weekend_counter]
            weekend_counter += 1

# Generate fixtures for each local town
weekend_counter = 1
for town, town_teams in local_towns.items():
    # Generate fixtures for teams from other towns first
    for other_town, other_town_teams in local_towns.items():
        if town != other_town:
            for team1 in town_teams:
                for team2 in other_town_teams:
                    generate_fixtures_for_town([team1, team2])

    # Generate fixtures for teams within the same town
    generate_fixtures_for_town(town_teams)

# Display fixtures on the screen
print("Generated Fixtures:")
print(fixtures)

# Save fixtures to CSV file
fixtures.to_csv('fixtures.csv', index=False)
print("Fixtures saved to fixtures.csv")