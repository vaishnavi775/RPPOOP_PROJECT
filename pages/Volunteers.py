import streamlit as st
import sqlite3
import pandas as pd
import numpy as np
connection = sqlite3.connect('members.db')
c = connection.cursor()



st.title(':blue[Volunteer Interface] :hand:')
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(c.execute('SELECT * FROM members'))

    chart_data

  
    st.line_chart(chart_data)