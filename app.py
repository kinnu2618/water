import os
import pickle
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Water Quality Assistant", layout="wide", page_icon="💧")

# Load model function
def load_model(model_path):
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        return model
    except FileNotFoundError:
        st.error(f"Model file not found at {model_path}. Please check the path.")
        return None

# Function to get user input
def get_user_input():
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

    # Return inputs as a list
    return [ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]

# Function to make prediction
def predict_water_quality(model, user_input):
    try:
        # Ensure all inputs are provided
        if not all(user_input):
            raise ValueError("Please enter all values.")

        # Convert inputs to float and store in a list
        user_input = [float(i) for i in user_input]

        # Convert to numpy array and reshape for model input
        input_data_as_numpy_array = np.asarray(user_input).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data_as_numpy_array)

        # Return prediction result
        return prediction[0]

    except ValueError as e:
        st.error(f"Error: {e}")
        return None

# Function to display result
def display_result(prediction):
    if prediction == 0:
        st.warning("""
        The water is unsafe for drinking! Here's what you can do:
        - **Boil the water**: Boiling water kills harmful bacteria, viruses, and parasites.
        - **Use a water purifier**: Consider using a purifier with UV, RO, or activated carbon filtration.
        - **Add chlorine or iodine tablets**: These chemicals can help purify the water and make it safe to drink.
        - **Avoid drinking untreated water**: Unsafe water can cause diseases such as diarrhea, cholera, and typhoid.
        """)
    elif prediction == 1:
        st.success('Safe Drinking Water!')

# Main app function
def main():
    # Load the model
    model_path = 'water_model.sav'
    water_model = load_model(model_path)

    if water_model:
        # Sidebar navigation
        with st.sidebar:
            selected = option_menu(
                'Water Quality Prediction System',
                ['Water Potability Prediction'],
                menu_icon='water',
                icons=['droplet'],
                default_index=0)

        if selected == 'Water Potability Prediction':
            st.title('Water Potability Prediction')

            # Get user input
            user_input = get_user_input()

            # Button for prediction
            if st.button('Water Potability Test Result'):
                prediction = predict_water_quality(water_model, user_input)

                # Display result
                if prediction is not None:
                    display_result(prediction)

# Run the main function
if __name__ == '__main__':
    main()
