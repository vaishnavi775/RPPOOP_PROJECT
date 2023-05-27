
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

def get_title_value():
 if "title_input" not in st.session_state:
        st.session_state["title_input"] = ""
 return st.session_state["title_input"]


            
 
#initial values for image and title
uploaded_file = None
submit = None

if st.sidebar.checkbox('HomePage Customize Option'):
    
     # Retrieve or set the title value
    title_input = get_title_value()
    title_input = st.sidebar.text_input("Enter the title of the page", title_input)
    submit = st.sidebar.button("Submit")
    # Upload the image file
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg"])
    
    if submit:
        st.session_state["title_input"] = title_input



#Displaying text and image
if submit is not None:
  st.markdown(f"<h1 style='font-size: 12rem;text-align: center;;'>{get_title_value()}</h1>", unsafe_allow_html=True)
else:
     st.title('Organising Team')
if uploaded_file is not None:
 st.image(uploaded_file, width=200, caption="Uploaded Image", use_column_width=True)


## upload jpeg and title to database when presistent

# File upload section
st.subheader("Upload Datasheet of the Fest to Analyze")
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
 if st.sidebar.checkbox('Display DataSheet?'):
        # Display the dataset
        st.dataframe(df)
        
      
           

 if st.sidebar.checkbox('Analyze Element Density as Bar Graph?'):
     def count_elements(df, column):
      """Count the number of occurrences of each element in a column of a DataFrame."""
      element_counts = df[column].value_counts()
      return element_counts

     def plot_bar_graph(element_counts,selected_column):
   
      fig, ax = plt.subplots()
      ax.bar(element_counts.index, element_counts.values)
      ax.set_xlabel('Elements')
      ax.set_ylabel('Count')
      ax.set_title(f'Number of occurences in a {selected_column}:')
      plt.xticks(rotation=45)
      st.pyplot(fig)

     

     # Select the column for analysis
     selected_column = st.sidebar.selectbox('Select a column', [col for col in df.columns if 1 < df[col].nunique() <= 20])
     # Count the elements in the selected column
     element_counts = count_elements(df, selected_column)



     # Plot the bar graph
     st.write(f'Bar Graph of {selected_column} Counts:')
     plot_bar_graph(element_counts,selected_column)
     
     if st.checkbox('Table Form?'):
        # Display the element counts as a DataFrame
        st.write(f'{selected_column} Counts:')
        st.write(element_counts)
        if st.button('Download as Excel'):
        # Export DataFrame to Excel file
          excel_data = element_counts.to_excel(index=False)

        # Create a download button for the Excel file
          st.download_button(label='Download Excel', data=excel_data, file_name='element_counts.xlsx', mime='application/vnd.ms-excel')
 



#  if st.sidebar.checkbox('Analyze Element Density as Pie Chart?'):

#    def count_elements(df, column):
#      """Count the number of occurrences of each element in a column of a DataFrame."""
#      element_counts = df[column].value_counts()
#      return element_counts

#    def plot_pie_chart(element_counts, selected_column):
#      fig, ax = plt.subplots()
#      ax.pie(element_counts.values, labels=element_counts.index, autopct='%1.1f%%')
#      ax.set_title(f'Element Distribution in {selected_column}')
#      return fig

#   # Select the column for analysis 
#    selected_column = st.sidebar.selectbox('Select a column', [col for col in df.columns if df[col].nunique() <= 30 and df[col].nunique() > 1], key="select_column")

#   # Count the elements in the selected column
#    element_counts = count_elements(df, selected_column)

#   # Plot the pie chart
#    fig = plot_pie_chart(element_counts, selected_column)
#    st.write(f'Pie Chart of {selected_column} Distribution:')
#    st.pyplot(fig)

#    if st.checkbox('Table Form?', key="select_ecount"):
#     # Display the element counts as a DataFrame
#     st.write(f'{selected_column} Counts:')
#     st.write(element_counts)

#     if st.button('Download as Excel'):
#         # Export DataFrame to Excel file
#         excel_data = element_counts.to_excel(index=False)

#         # Create a download button for the Excel file
#         st.download_button(label='Download Excel', data=excel_data, file_name='element_counts.xlsx', mime='application/vnd.ms-excel')
 
#    # Download option
#    st.write('Download Chart')
#    # Convert the plot to JPEG image
#    img_buffer = io.BytesIO()
#    plt.savefig(img_buffer, format='jpeg')
#    plt.close(fig)
#    img_buffer.seek(0)
#    # Create a download button
#    st.download_button(label='Download', data=img_buffer, file_name='pie_chart.jpeg', mime='image/jpeg')

#  if st.sidebar.checkbox('Analyze Element Density as Line Graph?'):

#     def count_elements(df, column):
#         """Count the number of occurrences of each element in a column of a DataFrame."""
#         element_counts = df[column].value_counts()
#         return element_counts

#     # Select the column for analysis
#     selected_column = st.sidebar.selectbox('Select a column', [col for col in df.columns if df[col].nunique() <= 18 and df[col].nunique() > 1], key="select_column4line")

#     # Count the elements in the selected column
#     element_counts = count_elements(df, selected_column)

#     # Plot the line graph
#     st.write(f'Line Graph of {selected_column} Distribution:')
#     st.line_chart(element_counts)

#     if st.checkbox('Table Form?', key="select_ecount"):
#         # Display the element counts as a DataFrame
#         st.write(f'{selected_column} Counts:')
#         st.write(element_counts)

#         if st.button('Download as Excel'):
#             # Export DataFrame to Excel file
#             excel_data = element_counts.to_excel(index=False)

#             # Create a download button for the Excel file
#             st.download_button(label='Download Excel', data=excel_data, file_name='element_counts.xlsx', mime='application/vnd.ms-excel')

#  # Download option
#     st.write('Download Chart')
#     # Convert the line chart to PNG image
#     fig, ax = plt.subplots()
#     ax.plot(element_counts.index, element_counts.values)
#     ax.set_xlabel('Elements')
#     ax.set_ylabel('Count')
#     ax.set_title(f'Line Graph of {selected_column} Distribution')
#     plt.xticks(rotation=45)
    
#     # Save the line chart as a PNG image
#     img_buffer = io.BytesIO()
#     plt.savefig(img_buffer, format='png')
#     plt.close(fig)
#     img_buffer.seek(0)

#     # Create a download button for the PNG image
#     st.download_button(label='Download', data=img_buffer, file_name='line_chart.png', mime='image/png')


 
 