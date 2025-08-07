import json

# Load JSON from file
with open('habit_tracker_simulation_5users_30days.json', 'r') as f:
    data = json.load(f)

results = {}

# Process each entry
for entry in data:
    user = entry['user_id']
    habit = entry['habit_name']
    status = entry['status'].strip().lower()

    if user not in results:
        results[user] = {}

    if habit not in results[user]:
        results[user][habit] = {
            "days_completed": 0,
            "days_skipped": 0
        }

    if status == "completed":
        results[user][habit]["days_completed"] += 1
    elif status == "skipped":
        results[user][habit]["days_skipped"] += 1

# Add success_rate
for user in results:
    for habit in results[user]:
        comp = results[user][habit]["days_completed"]
        skip = results[user][habit]["days_skipped"]
        total = comp + skip
        results[user][habit]["success_rate"] = round((comp / total) * 100, 2) if total else 0.0

# Output result
print(json.dumps(results, indent=2))
