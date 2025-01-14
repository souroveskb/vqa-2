import os
import json
import csv


IMAGE_DIR = r'/mnt/c/Users/User/Desktop/images/'


image_filenames = [f for f in os.listdir(IMAGE_DIR) if os.path.isfile(os.path.join(IMAGE_DIR, f))]


json_data = []
for filename in image_filenames:
    json_data.append({
        'filename': filename,
        'progress': 0,
        'relevance': None
    })


with open('resource/progress.json', 'w') as json_file:
    json.dump(json_data, json_file, indent=4)


with open('resource/progress.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    
    csv_writer.writerow(['filename', 'progress', 'relevance'])
    
    for filename in image_filenames:
        csv_writer.writerow([filename, 0, None])