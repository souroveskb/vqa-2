import os
import re

def rename_images(folder_path, prefix):
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            end_name = filename.split('_')[-1]
            new_name = f"{prefix}_{end_name}"
            # print(end_name, new_name)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))



def find_duplicates(folder_path, pattern):    
        duplicates = [filename for filename in os.listdir(folder_path) if pattern.search(filename)]
        for filename in duplicates:
            file_path = os.path.join(folder_path, filename)
            print(file_path)
            os.remove(file_path)




if __name__ == "__main__":
    # pattern = re.compile(r'\(\d+\)\.jpg$')
    
    # find_duplicates('/mnt/c/Users/User/Downloads/Bornon', pattern)
    
    rename_images('/mnt/c/Users/User/Downloads/Bornon', 'BORNON')