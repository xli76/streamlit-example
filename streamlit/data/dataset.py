import streamlit as st
import pandas as pd
from vega_datasets import data

@st.experimental_memo
def get_data():
    source = data.stocks()
    source = source[source.date.gt("2004-01-01")]
    return source

@st.experimental_memo(ttl=600)
def run_query(query, _conn):
    return pd.read_sql(query, _conn)

def save_data(df, insert_sql, conn):
    cursor = conn.cursor()
    val = list(map(tuple, df.values.tolist()))
    cursor.executemany(insert_sql, val)

def create_table(create_sql, conn):
    cursor = conn.cursor()
    cursor.execute(create_sql)