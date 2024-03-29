import streamlit
##import pandas
##import requests
##import snowflake.connector
##from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

##import pandas
##my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
##my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
##fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
##fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
##streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
##streamlit.header("Fruityvice Fruit Advice!")
#try:
fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
 # if not fruit_choice:
 #     streamlit.error("Please select a fruit to get information.")
 # else:
 #     fruityvice_response = requests.get.("https://fruityvice.com/api/fruit/" + fruit_choice)
 #     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
 #     streamlit.dataframe(fruityvice_normalized)
 
#except URLError as e:
 #   streamlit.error()
  
##import requests
##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# normalise json output 
##fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output as table
##streamlit.dataframe(fruityvice_normalized)

# Stop here for troublshooting
##streamlit.stop()

##import snowflake.connector

##my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
##my_cur = my_cnx.cursor()
##my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
##my_data_row = my_cur.fetchone()
##streamlit.text("The fruit load list contains:")
##streamlit.text(my_data_row)

##fruit_add = streamlit.text_input('What fruit would you like to add?','jackfruit')
##streamlit.write('Thanks for adding ', fruit_add)

##my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
