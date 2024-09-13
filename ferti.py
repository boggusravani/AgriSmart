import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
df = pd.read_csv("fertilizer_recommendation_dataset.csv")

# Define the model
model = RandomForestRegressor()

# Train the model
X = df.drop('fertilizer_recommendation', axis=1)
y = df['fertilizer_recommendation']
model.fit(X, y)

# Create the Streamlit app
def main():
    st.title("Fertilizer Recommendation System")

    # Inputs
    nitrogen = st.slider("Nitrogen", 0, 100, 50)
    phosphorus = st.slider("Phosphorus", 0, 100, 50)
    potassium = st.slider("Potassium", 0, 100, 50)
    pH = st.slider("pH", 0, 14, 7)

    # Prediction
    new_data = pd.DataFrame({'Nitrogen': [nitrogen], 'Phosphorus': [phosphorus], 'Potassium': [potassium], 'pH': [pH]})
    recommendation = model.predict(new_data)
    st.write("The recommended fertilizer is:", recommendation)

if __name__ == '__main__':
    main()