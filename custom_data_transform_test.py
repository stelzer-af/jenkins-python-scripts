import json

data = '''
[
    {
        "entity_id": 1,
        "entity_type": "student",
        "field": "dog_name",
        "type": "string",
        "value": "Fido",
        "display_page": "student_profile",
        "display_label": "Dog's Name",
        "display_product": "advising",
        "created_at": "2023-06-23 20:46:16.658976",
        "updated_at": null,
        "deleted_at": null
    },
    {
        "entity_id": 1,
        "entity_type": "student",
        "field": "favourite_color",
        "type": "string",
        "value": "Blue",
        "display_page": "student_profile",
        "display_label": "Favourite Color",
        "display_product": "advising",
        "created_at": "2023-06-23 20:46:16.658976",
        "updated_at": null,
        "deleted_at": null
    },
    {
        "entity_id": 2,
        "entity_type": "student",
        "field": "dog_name",
        "type": "string",
        "value": "Lola",
        "display_page": "student_profile",
        "display_label": "Dog's Name",
        "display_product": "advising",
        "created_at": "2023-06-23 20:46:16.658976",
        "updated_at": null,
        "deleted_at": null
    },
    {
        "entity_id": 2,
        "entity_type": "student",
        "field": "favourite_color",
        "type": "string",
        "value": "Green",
        "display_page": "student_profile",
        "display_label": "Favourite Color",
        "display_product": "advising",
        "created_at": "2023-06-23 20:46:16.658976",
        "updated_at": null,
        "deleted_at": null
    }
]
'''

# Parse the JSON data
json_data = json.loads(data)

# Group objects by entity_id
grouped_data = {}
for obj in json_data:
    entity_id = obj['entity_id']
    if entity_id not in grouped_data:
        grouped_data[entity_id] = []
    grouped_data[entity_id].append(obj)

# Create separate JSON arrays
json_arrays = []
for entity_id, objects in grouped_data.items():
    json_array = json.dumps(objects)
    json_arrays.append(json_array)

# Print the JSON arrays
for json_array in json_arrays:
    print(json_array)
    print()
