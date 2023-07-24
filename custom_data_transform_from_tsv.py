import boto3
import json
import datetime

# Set your S3 bucket and object key
s3_bucket = 'studentcustomdata'
s3_object_key = 'all_custom_data/part_0.tsv'

# Initialize the S3 client
s3_client = boto3.client('s3')

# Download file from S3 to memory
response = s3_client.get_object(Bucket=s3_bucket, Key=s3_object_key)
file_content = response['Body'].read().decode('utf-8')

# Read the TSV content from memory
tsv_data = []
for line in file_content.splitlines():
    tsv_data.append(line.split('\t'))

# Get the headers from the first row
headers = tsv_data[0]

print(tsv_data[:1])

# Group objects by entity_id
grouped_data = {}
for row in tsv_data[1:]:
    obj = dict(zip(headers, row))
    entity_id = obj['entity_id']
    if entity_id not in grouped_data:
        grouped_data[entity_id] = []
    grouped_data[entity_id].append(obj)

# Get the current date
today = datetime.date.today()
# Calculate yesterday's date
yesterday = today - datetime.timedelta(days=1)

for entity_id, objects in grouped_data.items():
    for obj in objects:
        # Convert date string to datetime object
        created_at = datetime.datetime.strptime(obj['created_at'], '%Y-%m-%d').date()

        # Check if created_at > yesterday
        if created_at > yesterday:
            # Create a JSON string
            json_str = json.dumps(obj)

            # Upload the file to S3
            file_name = f"{entity_id}.json"
            s3_client.put_object(Body=json_str, Bucket=s3_bucket, Key=file_name)
