# import streamlit as st

# # Upload the image file
# uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg"])

# # Display the uploaded image if available
# if uploaded_file is not None:
#     st.image(uploaded_file, width=200, caption="Uploaded Image", use_column_width=True)
# # Function to set or get the title value from session state
# def get_title_value():
#     if "title_input" not in st.session_state:
#         st.session_state["title_input"] = ""
#     return st.session_state["title_input"]

# # Retrieve or set the title value
# title_input = get_title_value()
# title_input = st.text_input("Enter the title of the page", title_input)
# submit = st.button("Submit")

# if submit:
#     st.session_state["title_input"] = title_input

# # Display the title of the page with increased text size
# st.markdown(f"<h1 style='font-size: 12rem; text-align: center;'>{get_title_value()}</h1>", unsafe_allow_html=True)



import streamlit as st
import pandas as pd


st.title('Organising Team')
# Upload the image file
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg"])

# Display the uploaded image and caption if available
# if uploaded_file is not None:
#     st.image(uploaded_file, width=200, caption="Uploaded Image", use_column_width=True)
# Function to set or get the title value from session state
def get_title_value():
    if "title_input" not in st.session_state:
        st.session_state["title_input"] = ""
    return st.session_state["title_input"]

# Retrieve or set the title value
title_input = get_title_value()
title_input = st.text_input("Enter the title of the page", title_input)
submit = st.button("Submit")

if submit:
    st.session_state["title_input"] = title_input

#Displaying text and image
if uploaded_file is not None:
    st.image(uploaded_file, width=200, caption="Uploaded Image", use_column_width=True)
st.markdown(f"<h1 style='font-size: 12rem;text-align: center;;'>{get_title_value()}</h1>", unsafe_allow_html=True)





def main():

    
    # File upload section
    st.subheader("Upload Datasheet of the Fest")
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        file_extension = uploaded_file.name.split(".")[-1]
        
        # Read the uploaded file based on the file extension
        if file_extension == "csv":
            df = pd.read_csv(uploaded_file)
        elif file_extension == "xlsx":
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Invalid file format. Please upload a CSV or Excel file.")
            return
        
        # Display the dataset
        st.dataframe(df)
        
        # Perform data visualization on the dataset (e.g., using matplotlib, seaborn, or any other library)
        # ...
        # Your data visualization code goes here
    
if __name__ == "__main__":
    main()



