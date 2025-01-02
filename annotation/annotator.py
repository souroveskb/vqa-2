import streamlit as st
import os
import json
# from streamlit_keydown import keydown
from relevant_generator import append_to_json

st.set_page_config(page_title="Image Viewer", layout="centered")


if "current_folder" not in st.session_state:
    st.session_state.current_folder = ""
if "images" not in st.session_state:
    st.session_state.images = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "relevant" not in st.session_state:
    st.session_state.relevant = False


st.sidebar.title("Image Viewer Controls")

folder_path = st.sidebar.text_input("Folder path:", value="", help="Enter the absolute or relative path to your image folder.")

# csv_progress = st.sidebar.file_uploader("Upload the CSV file", type=['csv'])
json_progress_file = st.sidebar.file_uploader("Upload the JSON file", type=['json'])

if json_progress_file is not None:
    json_progress = json.load(json_progress_file)

    st.sidebar.write(json_progress)


if folder_path != st.session_state.current_folder and json_progress_file is not None:
    st.session_state.current_folder = folder_path
    st.session_state.current_index = 0
    
    
    if os.path.isdir(folder_path):
        # valid_extensions = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp")
        # all_files = os.listdir(folder_path)
        # images_in_folder = [
        #     f for f in json_progress["filename"]
        # ]
        images_list = [item["filename"] for item in json_progress]
        st.session_state.images = images_list
    else:
        st.session_state.images = []
        


st.title("Image Viewer")


if not st.session_state.images:
    st.write("No images found in the specified folder, or folder doesn't exist.")
else:
    
    current_index = st.session_state.current_index
    print("current index: " , current_index)
    image_file = st.session_state.images[current_index]
    
    if json_progress[:]["filename" == image_file]["progress"] == 0:
        image_path = os.path.join(st.session_state.current_folder, image_file)

    # print(image_path)
    
    st.subheader(f"{folder_path}")
    st.write(f"Image name--> **{image_file}**")

    st.image(image_path, use_container_width=True)

    
    if st.session_state.relevant or st.button("Relevant"):
        st.session_state.relevant = True        
        json_data = {}
        
        questions = st.text_input(label="Insert Question", value="")
        answers = st.text_input(label="Insert Answer", value="")
        category = st.selectbox(label="Category", options=['Nature', 'Food and Cooking', 'Festival', 'Clothing'])
        
        json_data ={
            "filename": image_file,
            "question": questions,
            "answer": answers,
            "category": category
        }
        
        json_progress[:]["filename" == image_file]["progress"] = 1
        json_progress[:]["filename" == image_file]["relevance"] = 1
        
        if questions != "" and answers != "":
            if st.button("Save"):
                append_to_json("relevant.json", json_data)    
                
                with open("progress.json", "w") as f:
                    json.dump(json_progress, f)
                
                st.session_state.relevant = False
                st.session_state.current_index = (current_index + 1)
                print("saved current index now: " , current_index)
                
            else:
                pass
                
                
    elif st.button("Irrelevant"):
        json_progress[:]["filename" == image_file]["progress"] = 1
        json_progress[:]["filename" == image_file]["relevance"] = 0
        
        current_index = current_index + 1
        st.session_state.current_index = current_index 
        print("Irrelevant current index now: " , current_index)
        with open("progress.json", "w") as f:
            json.dump(json_progress, f)
            # json.dump(json_progress, "progress.json")

    
    # with col1:
    #     if st.button("Previous"):
    #         st.session_state.current_index = (current_index - 1) % len(st.session_state.images)
    # with col2:
    #     if st.button("Next"):
    #         st.session_state.current_index = (current_index + 1) % len(st.session_state.images)

    # elif st.button("Irrevelevant"):
    #     json_progress[:]["filename" == image_file]["progress"] = 1
    
    st.write(f"Image {current_index+1} of {len(st.session_state.images)}")
    

