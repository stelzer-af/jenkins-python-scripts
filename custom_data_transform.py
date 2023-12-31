import boto3
import json
import datetime
from tqdm import tqdm

# Set your S3 bucket and object key
s3_bucket = 'studentcustomdata'
s3_object_key = 'custom_data.json'

# Initialize the S3 client
s3_client = boto3.client('s3')

# Download file from S3 to memory
s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_object_key)
file_content = s3_object['Body'].read().decode('utf-8')

# Print the file content
# print("File content:", file_content)

# Parse the JSON content
json_data = json.loads(file_content)

# Group objects by entity_id
grouped_data = {}
for obj in json_data:
    entity_id = obj['entity_id']
    if entity_id not in grouped_data:
        grouped_data[entity_id] = []
    if obj['deleted_at'] is None:
        grouped_data[entity_id].append(obj)

# Get the current date
today = datetime.date.today()
# Calculate yesterday's date
yesterday = today - datetime.timedelta(days=1)

for entity_id, objects in tqdm(grouped_data.items()):
    for obj in tqdm(objects):
        print(objects)
        # Check if created_at > yesterday or updated_at > yesterday or if deleted_at > yesterday
        if (obj['created_at'] is not None and datetime.datetime.strptime(obj['created_at'], '%Y-%m-%d %H:%M:%S.%f').date() > yesterday) or \
            (obj['updated_at'] is not None and datetime.datetime.strptime(obj['updated_at'], '%Y-%m-%d %H:%M:%S.%f').date() > yesterday) or \
            (obj['deleted_at'] is not None and datetime.datetime.strptime(obj['deleted_at'], '%Y-%m-%d %H:%M:%S.%f').date() > yesterday):
                json_array = json.dumps(obj)
                file_name = f"{entity_id}.json"
                
                # Write the data to a file
                with open(file_name, 'w') as file:
                    file.write(json_array)

                # Upload the file to S3
                s3_client.upload_file(file_name, s3_bucket, file_name)

# We can use sync. It will be faster. Not supported in boto3
# s3_client.sync(local_directory, s3_bucket)