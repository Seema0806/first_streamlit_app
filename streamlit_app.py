
import streamlit 

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites') 
streamlit.text('🍜Omega 3 & Blueberry Oatmeal') 
streamlit.text('🍵Kale,Spinach & Rocket Smoothie') 
streamlit.text('🥚Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')

streamlit.header('🍌🍓Build Your Own Fruit Smoothie🥝🍇')


import pandas 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list) 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('fruityvice Fruit Advice!')


import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)
streamlit.tex(fruityvice_response.json())
