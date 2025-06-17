import streamlit as st
import pandas as pd
import joblib
import os
import sklearn
import xgboost

def interpretation(prediction):
    try:
        value = prediction[0]
        if value == 0:
            return "Neutral or Dissatisfied"
        elif value == 1:
            return "Satisfied"
    except Exception as e:
        print(f'Error occurred: {e}')
        return "Prediction Error"

def show():
    st.title("✈️ Predict Customer Satisfaction")
    # Load trained model
    model_path = os.path.join(os.path.dirname(__file__), "..", "deployment/model_xgb.pkl")
    with open(model_path, "rb") as f:
        model = joblib.load(f)

    with st.form("prediction_form"):
        st.subheader("👤 Passenger Information")
        st.markdown("Fill in basic personal and flight-related information.")
        col1, col2, col3 = st.columns(3)
        with col1:
            gender = st.selectbox("Gender", ["Male", "Female"])
            customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])
        with col2:
            travel_class = st.selectbox("Class", ["Eco", "Eco Plus", "Business"])
            travel_type = st.selectbox("Type of Travel", ["Business travel", "Personal Travel"])
        with col3:
            age = st.slider("Age", 18, 85, 35)
            flight_distance = st.slider("Flight Distance", 100, 5000, 1000)

        st.subheader("🎛️ Service Rating (0 = Worst, 5 = Best)")
        st.write("Rate each aspect of the flight experience from 0 to 5 based on your experience.")
        col1, col2, col3 = st.columns(3)
        with col1:
            inflight_wifi = st.slider("Inflight WiFi Service", 0, 5, 3)
            departure_convenience = st.slider("Departure/Arrival Convenience", 0, 5, 3)
            online_booking = st.slider("Ease of Online Booking", 0, 5, 3)
            gate_location = st.slider("Gate Location", 0, 5, 3)
            inflight_service = st.slider("Inflight Service", 0, 5, 3)
        with col2:
            food_drink = st.slider("Food and Drink", 0, 5, 3)
            online_boarding = st.slider("Online Boarding", 0, 5, 3)
            seat_comfort = st.slider("Seat Comfort", 0, 5, 3)
            inflight_entertainment = st.slider("Inflight Entertainment", 0, 5, 3)
            cleanliness = st.slider("Cleanliness", 0, 5, 3)
        with col3:
            onboard_service = st.slider("On-board Service", 0, 5, 3)
            leg_room_service = st.slider("Leg Room Service", 0, 5, 3)
            baggage_handling = st.slider("Baggage Handling", 0, 5, 3)
            checkin_service = st.slider("Check-in Service", 0, 5, 3)

        st.subheader("⏱️ Flight Timing and Delays")
        st.markdown("Provide details on flight delays to help evaluate satisfaction.")
        col1, col2 = st.columns(2)
        with col1:
            departure_delay = st.slider("Departure Delay (Minutes)", 0, 1000, 0)
        with col2:
            arrival_delay = st.slider("Arrival Delay (Minutes)", 0, 1000, 0)

        submit = st.form_submit_button("Predict")

    if submit:
        user_data = pd.DataFrame([{
            'Gender': gender,
            'Customer Type': customer_type,
            'Age': age,
            'Type of Travel': travel_type,
            'Class': travel_class,
            'Flight Distance': flight_distance,
            'Inflight wifi service': inflight_wifi,
            'Departure/Arrival time convenient': departure_convenience,
            'Ease of Online booking': online_booking,
            'Gate location': gate_location,
            'Food and drink': food_drink,
            'Online boarding': online_boarding,
            'Seat comfort': seat_comfort,
            'Inflight entertainment': inflight_entertainment,
            'On-board service': onboard_service,
            'Leg room service': leg_room_service,
            'Baggage handling': baggage_handling,
            'Checkin service': checkin_service,
            'Inflight service': inflight_service,
            'Cleanliness': cleanliness,
            'Departure Delay in Minutes': departure_delay,
            'Arrival Delay in Minutes': arrival_delay
        }])

        prediction = model.predict(user_data)
        result = interpretation(prediction)
        st.success(f"The customer is **{result}** with their experience.")
