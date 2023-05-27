import pandas as pd
import csv
import sqlite3
import streamlit as st

def read_excel_data(upload_file, default_file_path):
    if upload_file is not None:
        # Read from the uploaded Excel sheet
        df = pd.read_excel(upload_file)
        # st.success("Reading data from uploaded Excel sheet...")
    else:
        # Read from the default Excel sheet
        df = pd.read_excel(default_file_path)
        # st.info("Reading data from default Excel sheet...")

    # Process the data
    # ...

    return df

# Example usage:
default_file_path = "fest.xlsx"

uploaded_file = st.file_uploader("Upload Excel sheet", type=["xlsx"])
# db = read_excel_data(uploaded_file, default_file_path)
db = pd.read_excel(default_file_path)


# inserting the pandas dataframe values into sqlite

connection = sqlite3.connect('members.db')
c = connection.cursor()

# inserting the pandas dataframe values into sqlite

# db.to_sql(
#     name = 'members',
#     con = connection,
#     if_exists = 'replace',
#     index = False,
#     dtype = {
#         'Student Name' : 'text',
#         'Designation in club': 'text',
#         'MIS No' : 'integer',
#         'Year':'text',
#         'Mob no':'integer'
#     }
# )

# c.execute("""ALTER TABLE members
#             ADD COLUMN 'Funding_Brought' 'integer';
# """)
# c.execute("""ALTER TABLE members
#             ADD COLUMN 'Task_to_Complete' 'text';
# """)
# c.execute("""ALTER TABLE members
#             ADD COLUMN 'Event_Area' 'text';
# """)
# c.execute("""ALTER TABLE members
#             ADD COLUMN 'task_completed'  'text';
# """)



connection.commit()
connection.close()
