import streamlit as st

def show():
    # Main content
    st.title("Welcome!")

    st.markdown("""
    ### What is this Dashboard?

    This interactive dashboard helps you:
    - Understand customer feedback using interactive **Exploratory Data Analysis**.
    - Predict customer **satisfaction** using a trained **machine learning model**.
    - Improve your service by targeting **key drivers** of satisfaction.

    ---
    ### Background Problems 
    Airline market is a competitive market. In 2025, the global airline industry is expected to generate a total revenue of $979 billion, according to IATA. \n
    Customer satistfaction can affect the rate of income, as the higher the satistfaction, there is higher chance that the customer will return, or even recommend someone else. \n
    As an data scientist, the aim for the project is to create a model that can predict the satistfaction of the customer. that the company can use to see on which section they can improve on. 
    
    ---

    ### Model Overview
    The app uses XGBoost classification algorithm for prediction. 
    
    **XGBoost**, achieved a **test F1 score of 0.94** and **0.98 F1 score on train**.

    ---
    
    ### Dataset Used for Training
    The model was trained using dataset taken from kaggle, [airline-passenger-satisfaction](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)
    
    ---
    
    ### Dataset Preview
    Column, Feature and the Data Preview.
    | Column Name                         | Data Type | Description                                                                 |
    |------------------------------------|-----------|-----------------------------------------------------------------------------|
    | id                                 | INT64     | Unique identifier for each passenger                                       |
    | Gender                             | STRING    | Gender of the passenger (Female, Male)                                     |
    | Customer Type                      | STRING    | Loyalty classification (Loyal customer, Disloyal customer)                 |
    | Age                                | INT64     | Age of the passenger                                                       |
    | Type of Travel                     | STRING    | Purpose of travel (Personal Travel, Business Travel)                       |
    | Class                              | STRING    | Class of travel (Business, Eco, Eco Plus)                                  |
    | Flight Distance                    | INT64     | Distance of the flight in miles                                            |
    | Inflight wifi service              | INT64     | Satisfaction with inflight wifi (0: Not Applicable, 1–5 scale)             |
    | Departure/Arrival time convenient  | INT64     | Satisfaction with departure/arrival times (1–5 scale)                      |
    | Ease of Online booking             | INT64     | Satisfaction with online booking (1–5 scale)                               |
    | Gate location                      | INT64     | Satisfaction with gate location (1–5 scale)                                |
    | Food and drink                     | INT64     | Satisfaction with food and drink (1–5 scale)                               |
    | Online boarding                    | INT64     | Satisfaction with online boarding process (1–5 scale)                      |
    | Seat comfort                       | INT64     | Satisfaction with seat comfort (1–5 scale)                                 |
    | Inflight entertainment             | INT64     | Satisfaction with inflight entertainment (1–5 scale)                       |
    | On-board service                   | INT64     | Satisfaction with overall onboard service (1–5 scale)                      |
    | Leg room service                   | INT64     | Satisfaction with leg room (1–5 scale)                                     |
    | Baggage handling                   | INT64     | Satisfaction with baggage handling (1–5 scale)                             |
    | Checkin service                    | INT64     | Satisfaction with check-in service (1–5 scale)                             |
    | Inflight service                   | INT64     | Satisfaction with inflight service (1–5 scale)                             |
    | Cleanliness                        | INT64     | Satisfaction with cleanliness of the flight (1–5 scale)                    |
    | Departure Delay in Minutes         | INT64     | Delay at departure in minutes                                              |
    | Arrival Delay in Minutes           | FLOAT64   | Delay at arrival in minutes                                                |
    | satisfaction                       | STRING    | Overall satisfaction (Satisfaction, Neutral or Dissatisfaction)           |
    
    ---

    ### How to Use
    - Navigate using the **sidebar** to explore EDA or make predictions.
    - Try inputting various user profiles to see predicted satisfaction.

    Enjoy exploring and optimizing your airline's customer experience!
    """)