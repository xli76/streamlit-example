import streamlit as st
from data.dataset import *
from data.sql_str import *
from common.chart import get_chart
from common.conn import init_connection

st.title("⬇ mysql connection ")
st.sidebar.markdown("# Page 2 ❄️")

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")

space(1)

conn = init_connection()
st.write("mysql connected")

def save_mysql_data():
    data = get_data()
    data['date'] = data['date'].astype('str')
    create_table(create_sql, conn)
    save_data(data, insert_sql, conn)

def load_mysql_data():
    query = stock_sql
    data = run_query(query, conn)
    return data

save_mysql_data()
source = load_mysql_data()
chart = get_chart(source)

st.altair_chart(chart, use_container_width=True)