import itertools

# Define the teams and their local towns
teams = ["CKlein Stars", "Dolphins FC", "Wolves FC", "Sea Horses FC", "Sharks United", "Lake Basin FC", "Thika United", "Mavuno Comrades FC", "Nakuru FC", "Ostrich Associates"]
local_towns = {"CKlein Stars": "Nairobi", "Dolphins FC": "Mombasa", "Wolves FC": "Nairobi", "Sea Horses FC": "Mombasa", "Sharks United": "Kisumu", "Lake Basin FC": "Kisumu", "Thika United": "Thika", "Mavuno Comrades FC": "Thika", "Nakuru FC": "Nakuru", "Ostrich Associates": "Nakuru"}

# Create a list of all possible pairings of teams
pairings = list(itertools.combinations(teams, 2))

# Function to check if two teams are from the same local town
def same_town(team1, team2):
    return local_towns[team1] == local_towns[team2]

    generate_fixtures_for_town(town_teams)

# Function to filter out pairings of teams from the same local town
def filter_pairings(pairings):
    filtered_pairings = []
    for pairing in pairings:
        if not same_town(pairing[0], pairing[1]):
            filtered_pairings.append(pairing)
    return filtered_pairings

# Filter out pairings of teams from the same local town
filtered_pairings = filter_pairings(pairings)

# Create a list to store the fixtures
fixtures = []

# Weekend counter
weekend_counter = 1

# Iterate over the filtered pairings and assign them to weekends
while filtered_pairings:
    # Select four pairings for the current weekend
    weekend_pairings = filtered_pairings[:4]

    # Remove the selected pairings from the list
    filtered_pairings = filtered_pairings[4:]

    # Iterate over the weekend pairings and add them to the fixtures list
    for pairing in weekend_pairings:
        team1, team2 = pairing
        local_town = local_towns[team1]
        stadium = local_town + " Stadium"
        leg = 1 if weekend_counter % 2 == 1 else 2
        fixtures.append((team1, team2, local_town, stadium, leg, "Weekend #" + str(weekend_counter)))

    # Increment the weekend counter
    weekend_counter += 1

# Print the fixtures
for fixture in fixtures:
    print(fixture)