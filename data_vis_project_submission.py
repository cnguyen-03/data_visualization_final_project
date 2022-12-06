# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:09:46 2022
Final Project for Data Visualization
"""

import streamlit as st
import pandas as pd
import altair as alt

pop_df = pd.read_csv("https://raw.githubusercontent.com/ifrankandrade/data-visualization/main/datasets/population/population_total.csv")


#get top five countries based on year
def top_five(df, year):
    ans = df[df.year == year].nlargest(5, 'population')
    return ans.country.to_list()

#inpts: df of population data, lst: list of countries, years: tuple of year range
#output: population during given years of 5 largest countries
def get_years(df, lst, years):
    if years[0] == years[1]:
        df1 = df[df['year'] == years[0]]
    else:
        df1 = df[(df['year'] >= years[0]) & (df['year'] <= years[1])]
    return df1[df1['country'].isin(lst)]

#input pop_df, years: tuple of range
#output: df of population during given years of 5 largest countries
def get_result_df(df, years):
    return get_years(pop_df, top_five(df, years[1]), years)

#make chart out of get_results_df
def make_chart(df, years):
    result_chart = alt.Chart(get_result_df(df, years), title = 'Top 5 Countries by Population').mark_line().encode(
        x='year',
        y='population',
        color='country',
        strokeDash='country',
    )
    return result_chart

def make_bar_chart(df, year):
    result_chart = alt.Chart(get_result_df(df, (year, year)), title = 'Top 5 Countries by Population').mark_bar().encode(
        x = 'country',
        y = 'population')
    return result_chart

st.title('Data Visualization Final Project')
'This project looks at the efficacy of Line Charts versus Bar Charts for displaying world population data over time.'

st.header('Part 1: Finding Data')
'The dataset I chose is a part of a group of datasets meant for use in practicing data visualization.'
'Data Source: https://github.com/ifrankandrade/data-visualization/blob/main/datasets/population/population_total.csv'
'The dataset contains population data of each country in the world for every five years from 1955 to 2020. I wanted to look at ways to look at which countries had the greatest population at any given year as well as the trends.'
'The dataset has about 4000 entries and he population ranged from 644 to 1.4 million.'
st.header('Part 2: Sketching Data') 

'My goal for this visualization is to look at the population of the most populous countries at a given time and identify trends.'
'To do so, I am going to create two charts.'
'One a line chart that will show the top five countries during a selected year and show the populations of those countries during the entered time range.'
'The second will be a bar chart that shows the top five countries in a single year.'
'Sketches are attached as separate files to the submission.'


st.header('Part 3: Evaluation')
'For the experiment, I had a group of three people use the visualizations I made to see which one was better at being an aide for answering questions about the data.'
'The questions were:'
'1. What country had the greatest population for the most years?'
'2. What country will likely have the greatest population in 2030?'
'2. What country had the greatest population in 2000?'

'I chose these questions because the first two will show which one is better at showing trends over time, while the third will show which one is better at showing data for a single year.'          
'The independent variable is the type of visualization and the dependent variable is the time it takes to get the correct answer.'
'The dataset is kept the same for both visualizations and each person will use both visualizations becuase I was only able to get three people to try it. If possible I would have had one group only look at one visualization and the other group looking at the other.'
'Below are the visualizations that were used:'

year_range = st.slider('Select the year range',1955, 2020, (1955, 2020), step = 5)

st.altair_chart(make_chart(pop_df, year_range), use_container_width=True)                
    
year_val = st.slider('Select the year',1955, 2020, 2020, step = 5)

st.altair_chart(make_bar_chart(pop_df, year_val), use_container_width=True)  

st.header('Evaluation Results and Discussion')
'For all three questions the participants were able to come up with the correct answer the fastest using the line chart with a range of years. They commented that using multiple years allowed them to look at more data at one time. Also having multiple years in one graphic helped visualize trends.'
'In the future, I could look into adding somehwere for the user to input the number of countries they want to see at once. This would be good because some people are able to take in more data at one time. One participant mentioned that they did not like how the marker for each country changed through every iteration. Keeping the saeme marker for each country in the future will help the users keep track of each country.'