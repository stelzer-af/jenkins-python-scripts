import boto3
import json

# Set your S3 bucket and object key
s3_bucket = 'studentcustomdata'
s3_object_key = 'custom_data.json'

# Initialize the S3 client
s3_client = boto3.client('s3')

# Download file from S3 to memory
s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_object_key)
file_content = s3_object['Body'].read().decode('utf-8')

# Print the file content
print("File content:", file_content)

# Parse the JSON content
json_data = json.loads(file_content)

# Group objects by entity_id
grouped_data = {}
for obj in json_data:
    entity_id = obj['entity_id']
    if entity_id not in grouped_data:
        grouped_data[entity_id] = []
    grouped_data[entity_id].append(obj)

# Create separate JSON arrays
# json_arrays = []
for entity_id, objects in grouped_data.items():
    json_array = json.dumps(objects)

    file_name = f"{entity_id}.json"
    
     # Write the data to a file
    with open(file_name, 'w') as file:
        file.write(json_array)

    # Upload the file to S3
    s3_client.upload_file(file_name, s3_bucket, file_name)
    
    # json_arrays.append(json_array)

# # Print the JSON arrays
# for json_array in json_arrays:
#     print(json_array)
#     print()
#     # Convert the data to JSON string
#     json_str = json.dumps(json_array)
    
#     entity_id = data['entity_id']
#     file_name = f"{entity_id}.json"

#     # Write the data to a file
#     with open(file_name, 'w') as file:
#         file.write(json_str)

#     # Upload the file to S3
#     s3_client.upload_file(file_name, s3_bucket, file_name)


# # Process each data object
# for data in json_data:
#     entity_id = data['entity_id']
#     file_name = f"{entity_id}.json"
#     print("Entity ID:", entity_id)
    
#     filtered_data = [obj for obj in data if obj['entity_id'] == entity_id]

#     print("Filtered data:", filtered_data)

    # # Convert the data to JSON string
    # json_str = json.dumps(data)

    # # Write the data to a file
    # with open(file_name, 'w') as file:
    #     file.write(json_str)

    # # Upload the file to S3
    # s3_client.upload_file(file_name, s3_bucket, file_name)

