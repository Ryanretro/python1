import csv

# Read the CSV file into a list of rows
with open('teams_csvFile.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
# Extract the team names from the CSV file
team_names = [row[0] for row in data]

# Generate the round-robin fixtures
fixtures = generate_round_robin_fixtures(team_names)

# Organize the fixtures into weekends
weekends = organize_into_weekends(fixtures)

# Generate the final table
final_table = generate_final_table(weekends)

# Write the final table to a JSON file
with open('final_table.json', 'w') as f:
    json.dump(final_table, f, indent=1)