import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
# import time
from datetime import time
import datetime
from PIL import Image
from io import StringIO
# import cv2

st.title('Book a ride')
st.write("""
         #### Reservation Form
         """)

with st.form (key = "Booking Form"):


    #select box
    service_type = st.selectbox(
        label = "Select Service Type ",
        options = ('From Airport','To Airport','Point-to-Point','Hourly/As Directed'),
        index = 1
    )
    date = st.date_input("Pick-Up Date", value = datetime.date(2024,7, 22))

    pick_up_time = st.time_input("Pick-Up Time", value = datetime.time(14,00))

    pkup_loc = st.text_input("Pickup_location")

    drpoff_loc = st.text_input("Drop of location")

    col1, col2 = st.columns(2)


    with col1:
        pass_num = st.number_input(
        label = "No of passengers",
        min_value = 1,
        max_value = 60,
        value = 1,
        step = 1
        )

    with col2:
        lag_num = st.number_input(
        label = "No of Luggage",
        min_value = 1,
        max_value = 60,
        value = 1,
        step = 1
        )


    submit_button = st.form_submit_button("Submit")