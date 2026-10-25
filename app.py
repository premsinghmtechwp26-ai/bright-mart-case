import streamlit as st
import joblib
import numpy as np

# Load the saved model
model = joblib.load('model.sav')

# Set up the title and description
st.title('Sales Prediction App')
st.write('Predict future sales based on advertising expenditures in TV, Radio, and Newspaper.')

# Create input fields for the user
tv = st.number_input('TV Advertising Budget ($)', min_value=0.0, value=100.0, step=1.0)
radio = st.number_input('Radio Advertising Budget ($)', min_value=0.0, value=20.0, step=1.0)
newspaper = st.number_input('Newspaper Advertising Budget ($)', min_value=0.0, value=10.0, step=1.0)

# Predict button
if st.button('Predict Sales'):
    # Prepare the input for prediction
    features = np.array([[tv, radio, newspaper]])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    # Display the result
    st.success(f'Estimated Sales: {prediction:.2f} M')
