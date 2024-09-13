'''create a folder in the desktop dedicated to this ipd project
here we will save the work
we are writing this in the jupyter notebook one can also do it in google collab or directly in vscode/python
before that we pip install the streamlit for showing the work in form of application before import
'''
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import time
import streamlit as st
page_icon=":seedling:"
def recommendation(n,p,k,temp,hum,ph,rain):
    features = np.array([[n,p,k,temp,hum,ph,rain]])
    transformed_features = ms.fit_transform(features)
    transformed_features = sc.fit_transform(transformed_features)
    prediction = rfc.predict(transformed_features).reshape(1,-1)
    return prediction[0] 

st.title("Welcome to CRS")

st.header('Crop Recommendation System')
st.markdown('<hr style="border:2px solid rainbow">', unsafe_allow_html=True)



from PIL import Image

image = Image.open('crop.jpg')
st.image(image, caption='Please enter the given details')
n = st.number_input('Nitrogen')

p = st.number_input('phousporos')

k = st.number_input('pottasium')
temp = st.number_input('temp')
hum= st.number_input('humitity')
ph = st.number_input('ph levels')
rain = st.number_input('rain')

crop=pd.read_csv(r'C:/Users/Asfiy/OneDrive/Desktop/My trainings/IPD projects/ipd1/Crop_recommendation.csv')
crop_dict = {
    'rice':1,
    'maize':2,         
    'jute':3,          
    'cotton':4, 
    'coconut':5,
    'papaya':6,
    'orange':7,
    'apple':8,
    'muskmelon':9, 
    'watermelon':10,
    'grapes':11,
    'mango':12,
    'banana':13,
    'pomegranate':14,
    'lentil':15,
    'blackgram':16,
    'mungbean':17,
    'mothbeans':18,  
    'pigeonpeas':19, 
    'kidneybeans':20,
    'chickpea':21,
    'coffee':22
    
}
crop['crop_num']=crop['label'].map(crop_dict)
x=crop.drop(['crop_num','label'],axis=1)
y=crop['crop_num']
#training and testing the data
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)


ms = MinMaxScaler()
x_train = ms.fit_transform(x_train)
x_test = ms.transform(x_test)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

rfc = RandomForestClassifier()
rfc.fit(x_train,y_train)
ypred = rfc.predict(x_test)

with st.form("my_form"):
    submitted = st.form_submit_button("Submit")

predict = recommendation(n,p,k,temp,hum,ph,rain)

crop_dict = {1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut", 6: "Papaya", 7: "Orange",
                 8: "Apple", 9: "Muskmelon", 10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
                 14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean", 18: "Mothbeans",
                 19: "Pigeonpeas", 20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"}
if submitted:
    if predict[0] in crop_dict:
        crop = crop_dict[predict[0]]
        
    
        st.title("{} is a best crop to be cultivated ".format(crop))
        image = Image.open('crops-growing-in-thailand.jpg')
        st.image(image,caption='Happy farming')
    else:
        st.title("Sorry are not able to recommend a proper crop for this environment")
        image2 = Image.open('smiley.jpg')
        st.image2(image, caption='please change the inputs and try again')