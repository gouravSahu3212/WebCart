import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Graphs", 
    page_icon="🌍", 
    layout="centered", 
    initial_sidebar_state="collapsed", 
    menu_items=None
)


# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=["a", "b", "c"])

# st.bar_chart(chart_data)




st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")

# st.subheader('Raw data')
# st.write(data)
# if st.checkbox('Show raw data', True):
#     st.subheader('Raw data')
#     st.write(data)

values = st.slider('Select From and To :-', 0, 23, (0, 23), 1, None, 'Mwh')

st.write('Values:', values)

bin_val = (values[1]-values[0])+1

graph = st.radio(
     "Select graph :- ",
     ('Bar Chart', 'Line Chart', 'Area Chart'))

st.subheader('Number of pickups by hour')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=bin_val, range=(values[0],values[1]))[0]
if graph == 'Bar Chart':
    fig = st.bar_chart(hist_values)
if graph == 'Line Chart':
    fig = st.line_chart(hist_values)
if graph == 'Area Chart':
    fig = st.area_chart(hist_values)

st.table(hist_values)


# st.subheader('Map of all pickups')
# st.map(data)

# hour_to_filter = 17
# hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)

# if st.button("Celebrate"):
#     st.balloons()



# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# Initialize connection.
# Uses st.cache to only run once.
# @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
# def init_connection():
#     return mysql.connector.connect(**st.secrets.mysql)

# conn = init_connection()

# rows = pd.read_sql("select name, pet, id from animals", conn)
# # Print results.
# st.dataframe(rows)
# for row in rows:
#     st.write(row)






# Initialize connection.
# Uses st.cache to only run once.
# @st.cache(allow_output_mutation=True, hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='animals'")
for i in rows:
    st.write(i)
st.table(rows)
