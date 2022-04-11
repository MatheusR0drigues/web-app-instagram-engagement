# importing the libaries

import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns

# Function to select the number of rows from the data base


def show_number_rows(dataframe):

    number_rows = st.sidebar.slider('Select the number of rows that'
                                    'you want to show', min_value=1,
                                    max_value=len(dataframe), step=1,
                                    key=1)

    return st.dataframe(df[:number_rows])


def show_number_rows_df(dataframe):

    number_rows = st.sidebar.slider('Select the number of rows that'
                                    'you want to show', min_value=2,
                                    max_value=len(dataframe), step=1,
                                    key=2)
    new_df = dynamic_df(dataframe, number_rows)
    figure = plot_chart(new_df)

    return st.pyplot(figure)

# Function that create the chart

def plot_chart(df):

    sns.set_style('whitegrid')
    fig, ax = plt.subplots(figsize=(13, 19))
    ax = sns.barplot(x='Engagement percentagem', y='Category',
                     data=df, palette='viridis')
    ax.set_title('Engagement Percentage by Instagram Category'
                 '(909 most engaged accounts analyzed)', fontsize=20)
    ax.set_xlabel('Percentage (%)', fontsize=14)
    ax.tick_params(rotation=0, axis='both', labelsize=23)
    ax.set_ylabel('Categories', fontsize=14)

    return fig

# Creating a dynamic data frame


def dynamic_df(dataframe, rows):
    df_v2 = dataframe[:rows]

    return df_v2


st.header('Data Analysis - Instagram Engagement')

# Importing data base
df = pd.read_csv('data/df_v4.csv')

st.title('Instagram Categories')
st.write('In this project we will analyze the most engaged'
         ' categories on Instagram')

# Table Filters
option_1 = st.sidebar.checkbox('Show the Table')
if option_1:
    show_number_rows(df)

# Ploting the chart

option_2 = st.sidebar.checkbox('Dynamic Chart')

if option_2:
    show_number_rows_df(df)
else:
    df_v2 = st.dataframe(df[:5])
    figure = plot_chart(df_v2)
    st.pyplot(figure)
