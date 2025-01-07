import json
import os

def append_to_json(old_data, new_data):
    data = json.load(old_data)    
    # if os.path.exists(file_path):
    #     with open(file_path, 'r') as file:
    #         data = json.load(file)
    # else:        
    #     data = []

    return data.append(new_data)

    
    # with open(file_path, 'w') as file:
    #     json.dump(data, file, indent=4)
