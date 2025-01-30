import os
import json
import csv


# IMAGE_DIR = r'/mnt/c/Users/User/Pictures/sample images'
IMAGE_DIR = r'/media/penta/1270D31B70D303FF/Split_images/chunk_11'
JSON_NAME = IMAGE_DIR.split('/')[-1] + '.json'

image_filenames = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]


json_data = []
for filename in image_filenames:
    json_data.append({
        'filename': filename,
        'progress': 0,
        'relevance': None
    })

# print(JSON_NAME)
with open(f'resource/{JSON_NAME}', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)


# with open(f'resource/{JSON_NAME}', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
    
#     csv_writer.writerow(['filename', 'progress', 'relevance'])
    
#     for filename in image_filenames:
#         csv_writer.writerow([filename, 0, None])