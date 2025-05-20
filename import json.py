import json
def convert_to_json(data):
    structured_data = []
    
    for category_name, category_entries in data.items():
        category = {
            "category": category_name,
            "entries": []
        }
        
        for entry_number, entry in enumerate(category_entries, start=1):
            entry_data = {
                "entry": entry_number,
                "title": entry['title'],
                "thoughts": entry['thoughts']
            }
            category["entries"].append(entry_data)
        
        structured_data.append(category)
    
    return json.dumps(structured_data, indent=2)

data = {
    "Health & Well-being": [
        {
            "title": "Waking Up Drained Again",
            "thoughts": [
                "Barely slept — only four hours.",
                "Body feels sore, like after a wrestling match.",
                "Mind is foggy, low physical and mental energy."
            ]
        },
        {
            "title": "End of a Long Day",
            "thoughts": [
                "Chest tightness and recurring shoulder pain.",
                "Body is physically exhausted by end of day."
            ]
        }
    ],
    "Family & Relationships": [
        {
            "title": "Waking Up Drained Again",
            "thoughts": [
                "Kids woke up early, adding to the fatigue."
            ]
        },
        {
            "title": "Family Dinner Reflections",
            "thoughts": [
                "Dinner time was joyful with kids laughing.",
                "Wife questions whether community work is taking too much time."
            ]
        }
    ],
    "Work Stress": [
        {
            "title": "Waking Up Drained Again",
            "thoughts": [
                "Upcoming sprint review at 10 a.m.",
                "Integration build is flaky.",
                "Didn’t have time or clarity to prepare well."
            ]
        }
    ]
}
json_output = convert_to_json(data)
print(json_output)

####