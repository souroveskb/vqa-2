import streamlit as st
import os
import json
# from streamlit_keydown import keydown
# from relevant_generator import append_to_json

st.set_page_config(page_title="Image Viewer", layout="centered")



if "current_folder" not in st.session_state:
    st.session_state.current_folder = ""
if "images" not in st.session_state:
    st.session_state.images = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "json_progress" not in st.session_state:
    st.session_state.json_progress = []
if "relevant_data" not in st.session_state:
    st.session_state.relevant_data = []
if "show_relevant_form" not in st.session_state:
    st.session_state.show_relevant_form = False


st.sidebar.title("Image Viewer Controls")

folder_path = st.sidebar.text_input(
    "Folder path:", 
    value="", 
    help="Enter the absolute path to your image folder."
)

json_progress_file = st.sidebar.file_uploader(
    "Upload the JSON file", 
    type=['json'],
    help="Select the JSON file containing progress info."
)

relevant_json_file = st.sidebar.file_uploader(
    "Upload the JSON file", 
    type=['json'],
    help="Select the JSON file containing relevant and annotated data."
)

# csv_progress = st.sidebar.file_uploader("Upload the CSV file", type=['csv'])
# json_progress_file = st.sidebar.file_uploader("Upload the JSON file", type=['json'])

if relevant_json_file is not None:
    st.session_state.relevant_data = json.load(json_progress_file)    
    
if json_progress_file is not None:
    st.session_state.json_progress = json.load(json_progress_file)    
    # st.sidebar.write(st.session_state.json_progress)
  

if folder_path != st.session_state.current_folder and json_progress_file is not None:
    st.session_state.current_folder = folder_path
    st.session_state.current_index = 0
    
    
    if os.path.isdir(folder_path):
        images_list = [item["filename"] for item in st.session_state.json_progress if item["progress"] == 0]
        st.session_state.images = images_list
        # print(images_list)
    else:
        st.session_state.images = []
        


st.title("Image Viewer")


if not st.session_state.images:
    st.write("No images found in the specified folder, or all image annotation is completed.")
else:    
    total_images = len(st.session_state.images)
    
    if st.session_state.current_index < total_images:
        image_name = st.session_state.images[st.session_state.current_index]
        image_path = os.path.join(st.session_state.current_folder, image_name)
    
    else:
        st.session_state.images = []
        # image_name = st.session_state.images[st.session_state.current_index % total_images]
        # image_path = os.path.join("") #st.session_state.current_folder, image_name
        st.subheader("No more images available.")
        st.rerun()
        
    st.subheader(f"{image_name}")
    st.write(f"Folder path--> **{folder_path}**")

    st.image(image_path, use_container_width=True)
    
    if not st.session_state.show_relevant_form:
    
        relevant_btn = st.button("Relevant")
        irrelevant_btn = st.button("Irrelevant")
    
        if relevant_btn:
            st.session_state.show_relevant_form = True
            st.rerun()
        
        elif irrelevant_btn:
            st.session_state.current_index = st.session_state.current_index + 1
            st.rerun()
    
    if st.session_state.show_relevant_form:
              
        json_data = {}        
        questions = st.text_input(label="Insert Question", value="")
        answers = st.text_input(label="Insert Answer", value="")
        category = st.selectbox(label="Category", options=['Nature', 'Food and Cooking', 'Festival', 'Clothing'])
        
        json_data ={
            "filename": image_name,
            "question": questions,
            "answer": answers,
            "category": category
        }
        
        
        if questions != "" and answers != "":
            if st.button("Save"):
                st.session_state.relevant_data.append(json_data)   
                                
                st.session_state.json_progress[:]["filename" == image_name]["progress"] = 1
                st.session_state.json_progress[:]["filename" == image_name]["relevance"] = 1
                print("saved current index: " , st.session_state.current_index)

                st.session_state.current_index = st.session_state.current_index + 1
                st.session_state.show_relevant_form = False
                st.rerun()
                
            else:
                pass
 
    st.write(f"Image {st.session_state.current_index} of {len(st.session_state.images)}")
    



st.sidebar.download_button(
    label="Download Progress JSON",
    data=json.dumps(st.session_state.json_progress),
    file_name="progress.json",
    mime="application/json"
)

st.sidebar.download_button(
    label="Download Relevant JSON",
    data=json.dumps(st.session_state.relevant_data),
    file_name="relevant.json",
    mime="application/json"
)