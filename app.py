import os
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Water Quality Assistant", layout="wide", page_icon="💧")

# Load the model
model_path = 'D:/projects/water/water_model.sav'
water_model = pickle.load(open(model_path, 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Water Quality Prediction System',
        ['Water Potability Prediction'],
        menu_icon='water',
        icons=['droplet'],
        default_index=0)

# Water Potability Prediction Page
if selected == 'Water Potability Prediction':

    # Page title
    st.title('Water Potability Prediction')

    # Getting user input for water quality features
    col1, col2, col3 = st.columns(3)

    with col1:
        pH = st.text_input('pH Value')

    with col2:
        Hardness = st.text_input('Hardness (mg/L)')

    with col3:
        Solids = st.text_input('Solids (ppm)')

    with col1:
        Chloramines = st.text_input('Chloramines (ppm)')

    with col2:
        Sulfate = st.text_input('Sulfate (mg/L)')

    with col3:
        Conductivity = st.text_input('Conductivity (µS/cm)')

    with col1:
        Organic_carbon = st.text_input('Organic Carbon (ppm)')

    with col2:
        Trihalomethanes = st.text_input('Trihalomethanes (µg/L)')

    with col3:
        Turbidity = st.text_input('Turbidity (NTU)')

    # Code for Prediction
    water_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Check Water Potability'):

        # Collect user input and convert to float
        user_input = [pH, Hardness, Solids, Chloramines, Sulfate,
                      Conductivity, Organic_carbon, Trihalomethanes, Turbidity]
        user_input = [float(x) for x in user_input]

        # Change the input data to a numpy array
        input_data_as_numpy_array = np.asarray(user_input)

        # Reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

        # Make prediction
        water_prediction = water_model.predict(input_data_reshaped)

        # Display the result
        if water_prediction[0] == 0:
            water_diagnosis = 'Unsafe Drinking Water!'
        else:
            water_diagnosis = 'Safe Drinking Water!'

    st.success(water_diagnosis)
