
# import streamlit as st
# import pandas as pd
# import numpy as np



# st.title(':blue[Head Interface] :hand:')


# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
# }))

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)



# x = st.slider('x')  # 👈 this is a widget
# st.write(x, 'squared is', x * x)

# st.text_input("Your name", key="name")

# # You can access the value at any point with:
# st.session_state.name


# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     chart_data
    
    

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#     })

# option = st.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected: ', option


# # Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

# left_column, right_column = st.columns(2)
# # You can use a column just like st.sidebar:
# left_column.button('Press me!')

# # Or even better, call Streamlit functions inside a "with" block:
# with right_column:
#     chosen = st.radio(
#         'Sorting hat',
#         ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
#     st.write(f"You are in {chosen} house!")
    
#  #import time

# #'Starting a long computation...'

# # Add a placeholder
# #latest_iteration = st.empty()
# #bar = st.progress(0)

# #for i in range(100):
#   # Update the progress bar with each iteration.
#   #latest_iteration.text(f'Iteration {i+1}')
#   #bar.progress(i + 1)
#   #time.sleep(0.1)

# #'...and now we\'re done!'


# df = pd.DataFrame(
#     [
#         {"command": "st.selectbox", "rating": 4, "is_widget": True},
#         {"command": "st.balloons", "rating": 5, "is_widget": False},
#         {"command": "st.time_input", "rating": 3, "is_widget": True},
#     ]
# )


# edited_df = st.experimental_data_editor(df) # 👈 An editable dataframe

# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

# edited_df = st.experimental_data_editor(df, num_rows="dynamic" )


import streamlit as st

if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("2 Factor Authentication", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    if my_input == 'acc':
        st.subheader("Accounts")
        st.write("Welcome to the authenticated user interface!")
    elif my_input == 'aog':
        st.subheader("AOG")
        st.write("Welcome to the authenticated user interface!")
    elif my_input == 'finance':
        st.subheader("Finance")
        st.write("Welcome to the authenticated user interface!")
    else:
        st.write("You have entered: ", my_input)
        st.write("You have entered the wrong password")
    
















