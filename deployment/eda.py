import streamlit as st
import pandas as pd
import numpy as np
import plots as pl

train = pd.read_csv('deployment/train.csv', index_col=0)

@st.cache_data
def prepare_summary_table(data):
    combined = data.copy()
    combined['Total Delay'] = combined['Departure Delay in Minutes'].fillna(0) + combined['Arrival Delay in Minutes'].fillna(0)
    
    distance_bins = [0, 500, 1000, 1500, 2000, combined['Flight Distance'].max()]
    distance_labels = ['0–500', '501–1000', '1001–1500', '1501–2000', '2000+']
    combined['FlightRange'] = pd.cut(combined['Flight Distance'], bins=distance_bins, labels=distance_labels)
    
    summary = combined.groupby('FlightRange').agg(
        Total_Flights=('FlightRange', 'count'),
        Total_Delay=('Total Delay', 'sum'),
        Min_Delay=('Total Delay', 'min'),
        Max_Delay=('Total Delay', 'max')
    ).reset_index()
    
    return summary

def show():
    st.title("Exploratory Data Analysis")
    
    st.markdown("""
    <style>
    .custom-base {
    text-align: center;
    color: white;
    padding: 12px;
    border-radius: 8px;
    width: 100%;
    box-sizing: border-box;
    }
    .custom-markdown {
        background-color: #2c2f33;
            font-size: 16px;
    }
    .custom-title {
        background-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

    def custom_md(text):
        st.markdown(f"<div class='custom-base custom-markdown'>{text}</div>", unsafe_allow_html=True)
    def custom_title(text):
        st.markdown(f"<h3 class='custom-base custom-title'>{text}</h3>", unsafe_allow_html=True)
    
    eda_option = st.selectbox("Select EDA View:", [
    "Satisfaction Distribution",
    "Gender vs Satisfaction",
    "Age vs Satisfaction",
    "Class vs Satisfaction",
    "Check-In vs Satisfaction",
    "Distance vs Delay",
    "All Features vs Satisfaction",
    "Arrival Delay vs Departure Delay"
    ])
    
    if eda_option == "Age vs Satisfaction": 
        min_age = int(train['Age'].min())
        max_age = int(train['Age'].max())
        
        custom_title('Age and Satisfaction')
        custom_md("Does different age will have different opinion on the satisfaction in general?")
        st.markdown('---')
        custom_title('Visualization')
        
        left, centerleft, centerright, right = st.columns([0.5, 2.5, 2, 1])
        fig = pl.satisfaction_age()
        with centerright:
            age_range = st.slider("Select Minimum Age", min_value=min_age, value=(min_age))
            filtered_data = train[(train['Age'] >= age_range)]
            filtered = (
            filtered_data.groupby(['Age', 'satisfaction'])
            .size()
            .unstack(fill_value=0)
            .reset_index()
            )
            st.table(filtered.head(11))
        with centerleft:
            st.pyplot(fig, use_container_width=True)
            
        st.markdown('---')
        custom_title('Conclusion')
        custom_md("<li><b>Younger Passengers (Under 20)</b>: This group tends to have a higher dissatisfaction rate, as shown by the dominance of the orange bars. </li><li><b> Middle-Aged Passengers (20–40)</b>: This segment shows a relatively balanced mix, with a slight tendency towards dissatisfaction. </li><li> <b>Older Passengers (40–60)</b>: Satisfaction tends to increase in this range, with a greater proportion of blue bars (satisfied customers). </li><li> <b>Extremes (60+)</b>: These bins have fewer data points, but appear mostly dissatisfied — although the high variability suggests the sample size is small.")
        
    if eda_option == "Gender vs Satisfaction":
        fig = pl.satisfaction_gender()
        custom_title('Gender and Their Satisfaction')
        custom_md("Does a certain gender will have more satisfied passenger compared to the others?")
        st.markdown('---')
        custom_title('Visualization')
        
        left, center, right = st.columns([0.7, 2, 1])
        with center :
            st.pyplot(fig, use_container_width=True)
            
            filtered = (
            train.groupby(['Gender', 'satisfaction'])
            .size()
            .unstack(fill_value=0)
            .reset_index()
            )
            st.table(filtered)
        st.markdown('---')
        custom_title('Conclusion')
        custom_md("From the result, both Male and Female have roughly the same amount of satisfied passenger. <br> But there is more dissatisfied Female passenger compared to Male")
        
    if eda_option == "Arrival Delay vs Departure Delay":
        fig = pl.delay_comparison()
        custom_title('Arrival Delay and Departure Delay')
        custom_md("Does a delayed arrival means the departure is delayed as well?")
        st.markdown('---')
        custom_title('Visualization')
        
        left, center, right = st.columns([1, 2, 1])
        with center :
            st.pyplot(fig, use_container_width=True)
            
        st.markdown('---')
        custom_title('Conclusion')
        custom_md("Based on the visualization, the delay is almost perfectly linear, meaning that <i>if a flight is delayed, or arrive late, its departure also will be delayed</i>")
        
    if eda_option == "Satisfaction Distribution":
        fig = pl.satisfaction_distribution()
        custom_title('Distribution Between Satisfied and Neutral/Dissatisfied')
        custom_md("Does the data that being used, have more satisfied passenger or the other way?")
        st.markdown('---')
        custom_title('Visualization')
        
        left, center, right = st.columns([0.9, 2, 1])
        with center :
            st.pyplot(fig, use_container_width=True) 
            
        st.markdown('---')
        custom_title('Conclusion')
        custom_md("From the graph, 57% of the passenger is either neutral or dissatisfied, while the other 43% is satisfied with the airline service.")
        
    if eda_option == "Class vs Satisfaction":
        fig = pl.satisfaction_class()
        custom_title('Satisfaction for Different Passenger Class')
        custom_md("What is the relationship between <b>travel class</b> and <b>customer satisfaction</b>? Does the different service affect the satisfaction of the passenger?")
        st.markdown('---')
        custom_title('Visualization')
        
        left, center, right = st.columns([0.7, 2, 1])
        with center :
            st.pyplot(fig, use_container_width=True) 
            
        st.markdown('---')
        custom_title('Conclusion')
        custom_md("<li><b>Business class</b> passengers are more likely to be satisfied, with a much higher count of satisfied customers than dissatisfied ones.</li><li><b>Economy class</b> has a high number of dissatisfied or neutral passengers, indicating a potential need for service improvements in this tier.</li><li><b>Eco Plus</b> shows a moderate dissatisfaction rate but has a small overall count, suggesting either fewer customers or limited availability.</li>")
        
    if eda_option == "Check-In vs Satisfaction" :
        fig = pl.satisfaction_checkin()
        custom_title('Satisfaction Based on Check-In')
        custom_md("Does the check-in service score given by the user affect the overall satisfaction?")
        st.markdown('---')
        custom_title('Visualization')
        
        left, center, right = st.columns([0.5, 2, 1])
        with center :
            st.pyplot(fig, use_container_width=True) 
            
        st.markdown('---')
        custom_title('Conclusion')
        custom_md("<li><b>Dissatisfied passengers</b> are more likely to give low to medium ratings (1 to 3) for check-in service.</li><li><b>Satisfied passengers</b> are more concentrated at higher ratings (4 and 5), especially rating 5.</li><li>There is a visible shift in density between the two groups—indicating that better check-in service correlates strongly with overall satisfaction.</li>")
        
    if eda_option == "Distance vs Delay":
        summary_table = prepare_summary_table(train)

        # Generate plot based on summary_table, not full data
        fig = pl.flight_delay()

        # Title and intro
        custom_title('Flight Distance Group and Delay')
        custom_md("Does different flight distance have different delay?<br>Does longer flight mean longer delay?<br>The data is grouped into 5 distance groups to explore this.")

        st.markdown('---')
        custom_title('Visualization')

        left, center, right = st.columns([0.5, 2, 0.5])
        with center:
            st.pyplot(fig, use_container_width=True)
            st.dataframe(summary_table, use_container_width=True, height=240)

        # Conclusion
        st.markdown('---')
        custom_title('Conclusion')
        custom_md(
            "<li>Across all distance categories, the <b>median delay remains fairly low</b>, suggesting most flights are not severely delayed.</li>"
            "<li>The <b>outliers increase slightly in frequency and magnitude</b> in longer-distance flights (especially 2000+), possibly due to the compounding effect of multiple potential delay sources (e.g., international customs, refueling, weather).</li>"
        )
        
    if eda_option == "All Features vs Satisfaction":
        fig = pl.satisfaction_correlation()
        custom_title('Features and their Satisfaction')
        custom_md("Which features scored with rating correlate most with Satisfaction?<br>"
                  "This could show which feature from the surveys have the highest correlation - meaning that it has the biggest impact on the satisfaction itself.")
        st.markdown('---')
        custom_title('Visualization')
        
        left, center, right = st.columns([1.1, 2, 1])
        with center :
            st.pyplot(fig, use_container_width=True) 
            
        st.markdown('---')
        custom_title('Conclusion')
        custom_md("<li>The most positively correlated feature is <b>Online boarding (0.504)</b>, indicating that passengers who had a good boarding experience tend to report higher satisfaction.</li>"
                  "<li>Other highly correlated features include <b>Inflight entertainment (0.398)</b>, <b>Seat comfort (0.349)</b>, and <b>Cleanliness (0.305)</b>.</li>"
                  "<li>Features like <b>Inflight wifi</b>, <b>Food and drink</b>, and <b>Check-in service</b> also show moderate positive correlations (~0.2–0.3).</li>"
                  "<li><b>Departure/Arrival time convenient</b> has a <b>slightly negative correlation (-0.052)</b>, suggesting that time convenience may lower satisfaction in this context.</li>")
        