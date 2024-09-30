import os
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="ML ASSIST", layout="wide", page_icon="🫡")

# Load the model
model_path = 'water_model.sav'
water_model = pickle.load(open(model_path, 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Water Quality Prediction System',
        ['Water Potability Prediction'],
        menu_icon='water',
        icons=['droplet'],
        default_index=0)

# Water Potability Prediction
if selected == 'Water Potability Prediction':

    # Page title
    st.title('Water Potability Prediction')

    # Getting user input
    col1, col2, col3 = st.columns(3)

    with col1:
        ph = st.text_input('pH Value')

    with col2:
        Hardness = st.text_input('Hardness')

    with col3:
        Solids = st.text_input('Solids')

    with col1:
        Chloramines = st.text_input('Chloramines')

    with col2:
        Sulfate = st.text_input('Sulfate')

    with col3:
        Conductivity = st.text_input('Conductivity')

    with col1:
        Organic_carbon = st.text_input('Organic Carbon')

    with col2:
        Trihalomethanes = st.text_input('Trihalomethanes')

    with col3:
        Turbidity = st.text_input('Turbidity')

    # Prediction result
    water_quality = ''

    # Create a button for prediction
    if st.button('Water Potability Test Result'):

        # Exception handling for missing inputs
        try:
            # Ensure all inputs are provided
            if not all([ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]):
                raise ValueError("Please enter all values.")

            # Convert inputs to float and store in a list
            user_input = [float(ph), float(Hardness), float(Solids), float(Chloramines), float(Sulfate),
                          float(Conductivity), float(Organic_carbon), float(Trihalomethanes), float(Turbidity)]

            # Convert to numpy array and reshape for model input
            input_data_as_numpy_array = np.asarray(user_input).reshape(1, -1)

            # Prediction
            prediction = water_model.predict(input_data_as_numpy_array)

            # Result interpretation
            if prediction[0] == 0:
                water_quality = 'Unsafe Drinking Water!'

                # Advice when water is unsafe
                st.warning("""
                The water is unsafe for drinking! Here's what you can do:
                - **Boil the water**: Boiling water kills harmful bacteria, viruses, and parasites.
                - **Use a water purifier**: Consider using a purifier with UV, RO, or activated carbon filtration.
                - **Add chlorine or iodine tablets**: These chemicals can help purify the water and make it safe to drink.
                - **Avoid drinking untreated water**: Unsafe water can cause diseases such as diarrhea, cholera, and typhoid.
                """)
            else:
                water_quality = 'Safe Drinking Water!'

        except ValueError as e:
            st.error(f"Error: {e}")

    st.success(water_quality)
