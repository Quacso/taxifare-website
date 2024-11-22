import streamlit as st
import requests

'''
# TaxiFareModel front
'''

# Title and description
st.title("Taxi Fare Prediction")
st.markdown("Provide the details of your taxi ride below, and get an estimated fare.")


## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

datetime = st.text_input("Pickup Datetime (YYYY-MM-DD HH:MM:SS)", "2014-07-06 17:18:00")
pickup_longitude = st.number_input("Pickup Longitude", value=-73.950655)
pickup_latitude = st.number_input("Pickup Latitude", value=40.783282)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.984365)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.769802)
passenger_count = st.number_input("Passenger Count", value=1, step=1)

'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

url = 'https://taxifare.lewagon.ai/predict'

if st.button("Get Fare Estimate"):
    params = {
        "pickup_datetime": datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

# Let's call our API using the `requests` package...

    try:
        # Attempt to call the API
        with st.spinner("Fetching the prediction..."):  # Show a spinner while waiting
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for HTTP status codes >= 400
            #Let's retrieve the prediction from the **JSON** returned by the API.
            prediction = response.json().get("fare", "Error")

## Finally, we can display the prediction to the user
        # Display the result if no exception occurred
        st.success(f"The estimated fare is: ${prediction:.2f}")

    except requests.exceptions.RequestException as e:
        # Handle API call errors (e.g., bad URL, timeout, invalid response)
        st.error(f"Error fetching prediction: {e}")
