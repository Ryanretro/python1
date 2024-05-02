import itertools
import csv
def generate_fixtures(teams):
    fixtures = []
    local_towns = ["Retro Town", "Sleek Town", "Brad Town", "Jojo street Town"]
    for town in local_towns:
        town_teams = [team for team in teams if town in team]
        other_teams = [team for team in teams if town not in team]
        for leg in range(1, 3):
            for weekend in range(1, len(teams)):
                matchups = list(itertools.combinations(town_teams, 2))
                matchups += list(itertools.combinations(other_teams, 2))
                for match in matchups:
                    fixture = {
                        "Team1": match[0],
                        "Team2": match[1],
                        "LocalTown": town,
                        "Stadium": f"Stadium_{town}",
                        "Leg": leg,
                        "Weekend": f"Weekend #{weekend}"
                    }
                    fixtures.append(fixture)

    return fixtures
def save_fixtures_to_csv(fixtures, filename="fixtures.csv"):
    with open(filename, "w", newline="") as csvfile:
        fieldnames = ["Team1", "Team2", "LocalTown", "Stadium", "Leg", "Weekend"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for fixture in fixtures:
            writer.writerow(fixture)
def display_fixtures(fixtures):
    for fixture in fixtures:
        print(f"Team1: {fixture['Team1']}, Team2: {fixture['Team2']}, LocalTown: {fixture['LocalTown']}, "
              f"Stadium: {fixture['Stadium']}, Leg: {fixture['Leg']}, Weekend: {fixture['Weekend']}")
if __name__ == "__main__":
    teams = ["Retro FC", "SLeek FC", "Brad FC", "Jojo FC", "Ryan FC", "Turbo FC", "Vowlks FC", "Jossy FC", "Nitro FC", "Apex FC"]
    fixtures = generate_fixtures(teams)
    # Save fixtures to CSV
    save_fixtures_to_csv(fixtures)
    # Display fixtures on screen
    display_fixtures(fixtures)