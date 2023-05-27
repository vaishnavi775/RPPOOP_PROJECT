import streamlit as st
import pandas as pd
import numpy as np
import csv
import sqlite3
import plotly.express as px

st.title(':blue[Secretary Interface] :hand:')

##### ENTER MIS NUMBER ########
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("2 Factor Authentication",
                         st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    if my_input == '3':
        #     st.write("You have entered: ", my_input)
        #     st.write("You have entered the right password")
        #    #moving dataframe from excel to pandas dataframe
        #     df = pd.read_excel('db 2/fest2.xlsx',
        #                     header = 0
        #      )
        #      # print(df)

        #      # inserting the pandas dataframe values into sqlite

        #     connection = sqlite3.connect('members.db')
        #     c = connection.cursor()
        #     # inserting the pandas dataframe values into sqlite
        #     df.to_sql(
        #          name = 'members',
        #          con = connection,
        #          if_exists = 'replace',
        #          index = False,
        #          dtype = {
        #              'StudentName' : 'text',
        #              'Designationinclub': 'text',
        #              'MISNo' : 'integer',
        #              'Year':'text',
        #              'Mob no':'integer'
        #          }
        #      )

        #     c.execute("""ALTER TABLE members
        #                  ADD COLUMN 'Funding_Brought' 'integer';
        #      """)
        #     c.execute("""ALTER TABLE members
        #                  ADD COLUMN 'Task_to_Complete' 'text';
        #      """)
        #     c.execute("""ALTER TABLE members
        #                  ADD COLUMN 'Event_Area' 'text';
        #      """)
        #     c.execute("""ALTER TABLE members
        #                  ADD COLUMN 'task_completed'  'text';
        #      """)
        #     c.execute("""ALTER TABLE members
        #                  ADD COLUMN 'personalkey'  'text';
        #      """)

        #     connection.commit()

        #     #c.execute("""UPDATE members SET personalkey = 'Texas' WHERE Year = 'TY Btech' """)
        #     c.execute("""UPDATE members SET Funding_Brought = CAST(abs(random()) / 184467440737095517 AS INTEGER) + 1 """)
        #     st.table(c.execute('SELECT * FROM members'))
        #     chart_data = pd.DataFrame(c.execute("""SELECT MISNo ,Funding_Brought FROM members"""),columns =['A','B'])
        #     csv2 =  chart_data[['B', 'A']].copy()
        #     st.line_chart(csv2)


        # def read_file(file):
        #     if file.type == "text/csv":
        #         df = pd.read_csv(file)
        #     elif file.type == "application/vnd.ms-excel":
        #         df = pd.read_excel(file)
        #     else:
        #         return None

        #     return df


        def main():
            st.subheader(" ")
            st.subheader(" ")
            st.text("Click below to upload a new file or continue in the sidebar with the default file")
            uploaded_file = st.file_uploader(
                "Upload CSV or Excel file", type=["csv", "xls", "xlsx"])
            
            # if uploaded_file is not None:
            #     df = read_file(uploaded_file)
            #     if df is not None:
            #         st.subheader("Dataset")
            #         st.write(df)
            #     else:
            #         st.error("Unsupported file format. Please upload a CSV or Excel file.")


        if __name__ == "__main__":
            main()

    else:
        st.write("You have entered: ", my_input)
        st.write("You have entered the wrong password")
