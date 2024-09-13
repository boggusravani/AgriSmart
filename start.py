import streamlit as st
import webbrowser
# Set page configuration including background image
st.set_page_config(
    page_title="Crop Recommendation -A smart help for farmers using Machine Learning",
    page_icon=":rocket:",
    initial_sidebar_state="expanded",
)
 

# Add content to your app

st.title("Welcome")


st.header('Crop Recommendation System', divider='rainbow')

st.write('A crop recommendation system is a technology that helps farmers choose the right crops to grow by analyzing data like climate, soil, and past performance. It aims to boost productivity, save resources, reduce risk, and increase profits in agriculture. These systems are vital for sustainable and efficient farming.Agricultural production heavily relies on crop selection.Our goal is to develop an intelligent system that accurately recommends the best crops for specific conditions, maximizing yields and profitability while minimizing environmental impact.')
st.write('crop recommendation systems represent a critical advancement in modern agriculture. By harnessing data and technology, they empower farmers to make informed decisions, optimize resource use, and adapt to changing conditions. These systems are pivotal for enhancing agricultural productivity, sustainability, and the well-being of farming communities in our ever-evolving world.We tried to bring the best for farmers for them to give recommendation for the crop and as well as which fertilizer to be used in order to maintain that type of crop .It gives a better insides for the farmer for better decision making and also better way of getting the maximum profit.Here farmer have to give sertain data for the prediction like the most important neutients present in the soil ie nitrogen,phosphorous and pottasium ')
st.write('In this project We have two modules.We have crop recommendation system and also the fertilizer recommentation system .here note that both are not link logically but we here created a main page so that to get there where that system probably work')
st.sidebar.title("Our Services")

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Which one  would you like to Try?",
    ("About", "Crop Recommendations", "Fertilizer Recommendations")
)
if add_selectbox == "Crop Recommendations":
    webbrowser.open(' http://192.168.127.24:8502')
    
if add_selectbox == "Fertilizer Recommendations":
    webbrowser.open('http://localhost:8502')


    