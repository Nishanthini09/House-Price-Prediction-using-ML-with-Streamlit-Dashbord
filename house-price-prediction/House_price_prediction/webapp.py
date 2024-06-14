"""
Created on Thu May 12 2024
@author: nishanthini mani
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

# Load the saved model
loaded_model = pickle.load(open("house_price_prediction_model.sav", 'rb'))

# Create a function for prediction
def house_price_prediction(input_data):
    # Convert the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting on a single instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make prediction
    prediction = loaded_model.predict(input_data_reshaped)

    return prediction[0]

# Main function to run the app
def main():
    # Set page configuration
    st.set_page_config(page_title="House Price Prediction", page_icon="🏠", layout="wide")

    # Sidebar for navigation
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # required
            options=["Home", "Predict"],  # required
            icons=["house", "calculator"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
        )

    # Home Page
    if selected == "Home":
        st.title('Welcome to the House Price Prediction WebApp')
        st.image("C:\\Users\\HAI\\Downloads\\house-price-prediction\\House_price_prediction\\house-image.jpeg", use_column_width=True)
        st.markdown("""
            This web application predicts the price of a house based on various input features.
            Navigate to the "Predict" section to enter the details of the house and get the predicted price.
        """)

    # Prediction Page
    if selected == "Predict":
        st.title('Predict House Price')

        with st.form(key='prediction_form'):
            col1, col2, col3 = st.columns(3)

            with col1:
                SquareMeters = st.number_input("🏠 Size of house in square meters", min_value=0)
            with col2:
                NumberOfRooms = st.number_input("🛏️ Number of Rooms", min_value=0)
            with col3:
                HasYard = 1 if st.selectbox('🌳 Has Yard', ('Yes', 'No')) == 'Yes' else 0
            with col1:
                HasPool = 1 if st.selectbox('🏊 Has Pool', ('Yes', 'No')) == 'Yes' else 0
            with col2:
                Floors = st.number_input("🧱 Number of Floors", min_value=0)
            with col3:
                CityCode = st.number_input("🏙️ City Code", min_value=0)
            with col1:
                CityPartRange = st.number_input("🏡 City Part Range (0 - cheapest, 10 - most expensive)", min_value=0, max_value=10)
            with col2:
                NumPrevOwners = st.number_input("👨‍👩‍👦 Number of Previous Owners", min_value=0)
            with col3:
                Made = st.number_input('📅 Year Built', min_value=1800, max_value=2024, step=1)
            with col1:
                IsNewBuilt = 1 if st.selectbox('🆕 Is New Built', ('Yes', 'No')) == 'Yes' else 0
            with col2:
                HasStormProtector = 1 if st.selectbox('🌪️ Has Storm Protector', ('Yes', 'No')) == 'Yes' else 0
            with col3:
                Basement = st.number_input('🏠 Basement Size (square meters)', min_value=0)
            with col1:
                Attic = st.number_input('🏠 Attic Size (square meters)', min_value=0)
            with col2:
                Garage = st.number_input('🚗 Garage Size (square meters)', min_value=0)
            with col3:
                HasStorageRoom = 1 if st.selectbox('🏢 Has Storage Room', ('Yes', 'No')) == 'Yes' else 0
            with col1:
                HasGuestRoom = st.number_input('🛌 Number of Guest Rooms', min_value=0)

            submit_button = st.form_submit_button(label='Predict House Price')

        if submit_button:
            input_data = [
                SquareMeters, NumberOfRooms, HasYard, HasPool, Floors, CityCode, 
                CityPartRange, NumPrevOwners, Made, IsNewBuilt, HasStormProtector, 
                Basement, Attic, Garage, HasStorageRoom, HasGuestRoom
            ]
            price = house_price_prediction(input_data)
            st.success(f'The Predicted Price: ${price}')

if __name__ == '__main__':
    main()
