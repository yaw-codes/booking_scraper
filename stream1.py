import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
# import time
from datetime import time
import datetime
#learning streamlit

#st.text(This is just a text"")
# st.write("this is **just** a _word_ ")

dc = {"a":10,"b":20,"c":30}
# st.write(dc)

fig,ax = plt.subplots()
# ax.scatter(np.arange(5),np.arange(5)**2)

# st.write(fig)

# st.write(st.write)
# st.write(st.error)
#u dont always have to write st.write
# dc

# st.title("this is a title")
# st.header("This is a header")
# st.subheader("subs")

#if you want to show some code
code = """ def func():
    print(np.arange(10)) """

# st.code(code, language = "python")
#dataframe, table, metric, json

# df = pd.DataFrame(
#     np.random.randn(50,20),
#     columns= ["cols"+str(i) for i in range(20)]
# )
# st.write(df)
# st.dataframe(df)
# st.dataframe(df, width =200, height = 100)
#u can ust take the main part and run it
#st.dataframe(np.random.randn(50,20))



#in the table no customization
# st.table(df)

#metric (ex, stock data, inc/dec)

# delta_color ,normal,inverse, off
# st.metric("TCS stock", value = "3220.70", delta = "19.10", delta_color = "normal")
# f = open(r"D:\datum\aa_chatbot\simple_chatbot\prac\all_intents_js.json")
# dt = json.load(f)
# st.json(dt , expanded = False)

df = pd.DataFrame(np.random.randn(10,2), columns=['prices','diff'])
#line chart 
# st.line_chart(df)

# st.line_chart(df, y = ["prices"])
# st.area_chart(df)
# st.area_chart(df, y = ['prices'])
# st.bar_chart(df)

#matplot lib in streamlit
# st.pyplot(fig)

# ax.hist(np.random.randn(100), bins= (10))
# st.pyplot(fig)

# maps
#you can pass longitudes and lattitudes 
places = pd.DataFrame({
    "lat":[19.07,28.64],
    'lon':[72.87, 77.21]
})

# st.map(places)

#to have the info under the button u use this
# press = st.button("click this")
# if press == True:
#     st.write(time.time())

#on click_ always on top
# def fn ():
#     st.write(time.time())


# st.button("Click me",on_click = fn)

# df = pd.DataFrame(np.random.randn(10,2), columns=["col1", "col2"])

# #download button
# data = df.to_csv().encode("utf-8")
# st.download_button(
#     label = "Download file",
#     data = data,
#     file_name ="new_file.csv",
#     mime = "text/csv"
# )

# #what happens if you dont have a dataframe but u have text.. 
# txt = "This is a sample text"

# st.download_button(
#     label = "Downlaod the file",
#     data = txt
# )

# #opening an img file
# file = open("doggo.jpg","rb")
# btn = st.download_button(
#     label = "Download image",
#     data = file,
#     file_name = "doggo_img.jpg",

# )

# #checkbox
# ck = st.checkbox("I agree to the terms and conditions")
# if ck == True:
#     st.write("agreement done")

    #checkbox, value
# ck = st.checkbox("I agree to the terms and conditions",value = False)
# if ck == True:
#     st.write("agreement done")
# else:
#     st.write("agreement not done")

##radioboxes, use index to change the preselected option
# option = st.radio(
#     label = "Order your food",
#     options = ("Pizza","Burger","Chips"),
#     index = 1
# )

# if option == "Pizza":
#     st.write("You ordered Pizza")
# elif option == "Burger":
#     st.write("You ordered Burger")
# elif option == "Chips":
#     st.write("You ordered Chips")

# #select box
# option = st.selectbox(
#     label = "Where do you live",
#     options = ("Moscow","New York","Istanbul"),
#     index = 1
# )

# if option == "Moscow":
#     st.write("You Live in  Moscow")
# elif option == "New York":
#     st.write("You Live in  New York")
# elif option == "Istanbul":
#     st.write("You Live in  Istanbul")

# option = st.multiselect(
#     label = "Which places have you been ",
#     options = ('sydney','Tokyo','New Dehi','Paris','Cape Twon'),
#     default  = ('Tokyo','Paris')
# )
# st.write(option)

##slider
# num = st.slider(
#     label = "Your age",
#     min_value = 18,
#     max_value = 120,
#     step = 1
# )
# st.write(num)

# #slider,range
# num = st.slider(
#     label = "Your age",
#     min_value = 18,
#     max_value = 120,
#     value = (40,60),
#     step = 1
# )
# st.write(num)

# #slider,time range
# visiting_time = st.slider(
#     label = "Your appointment time",
#     value = (time(11,30),time(12,45)),
# )
# st.write(visiting_time)

# #select slider
# option = st.select_slider(
#     label = "Select the best color",
#     options = ("Violet","Indigo","Blue","Green","Yellow","Orange","Red")
# # )
# # st.write(option)

# #select slider,range
# start_color, end_color = st.select_slider(
#     label = "Select  color range",
#     options = ("Violet","Indigo","Blue","Green","Yellow","Orange","Red") ,
#     value = ("Blue","Orange")
# )
# st.write("from", start_color, "to ", end_color)


# #text input
# txt = st.text_input(
#     label = "Please enter your email",
#     max_chars = 20,
#     placeholder = "someone@email.com"

# )

# st.write(txt)

# #text input password
# txt = st.text_input(
#     label = "Please enter your password",
#     max_chars = 20,
#     placeholder = "Password here",
#     type = "password"
 
# )
# st.write(txt)

# num = st.number_input(
#     label = "Enter your weight",
#     min_value = 40,
#     max_value = 250,
#     value = 65,
#     step = 1
# )

# st.write(num)

# txt = st.text_area(
#     label = "write something",
#     height = 200,
#     max_chars = 100,
#     placeholder = "Whats on your mind"
# )

# st.write(txt)

date = st.date_input("Enter your birthday", value = datetime.date(2024,7,11))
st.write(date)

time_set = st.time_input("Enter you meal time", value = datetime.time(14,00))