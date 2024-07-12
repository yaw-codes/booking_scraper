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

# # st.write(txt)

# date = st.date_input("Enter your birthday", value = datetime.date(2024,7,11))
# st.write(date)

# time_set = st.time_input("Enter you meal time", value = datetime.time(14,00))
# #
# fl = st.file_uploader(
#     label = "upload here"
# )
# if fl:
#     st.write(fl.type)
#     if "image" in fl.type:
#         img = Image.open(fl)
#         st.write(np.array(img).shape)
#     elif fl.type =="text/plain":
#         stringio = StringIO(fl.getvalue().decode("utf-8"))
#         string_data = stringio.read()
#         st.write(string_data)

#using the camera as input
# picture = st.camera_input("Take a pic")
# if picture:
#     img = Image.open(picture)
#     st.write(np.array(img).shape) 

#color picker
# color = st.color_picker("Pick a color")
# if color:
#     st.write("YOu selected", color)


# img = Image.open("doggo.jpg")
# #cv2 uses the bgr format
# # img = cv2.imread("doggo.jpg")

# st.image(
#     img,
#     caption = "Image of a dog, bicycle and a truck",
#     width = 800,
#     channels = "RGB"
# )

# st.image(
#     img,
#     caption = "Image of a dog, bicycle and a truck",
#     width = 800,
#     channels = "BGR"
# )
# st.audio("audio_file.mp3")
# st.audio("audio_file.mp3",start_time = 10)
#st.video("doggo_video.mp4")


# # layout containers

# # sidebar
# choice = st.sidebar.radio(
#     label = "Choose the option",
#     options = ("audio","video")
# )
# if choice == "audio":
#     st.audio("audio_file.mp3")
#     st.write("This is audio")
# elif choice == "video":
#     st.video("video_file.mp4")
#     st.write("This is a video file")

# #colums - vertical columns
# col1,col2 = st.columns(2, gap = "small")
## col1,col2 = st.columns([1,3], gap = "small")
# col1.audio("audio_file.mp3")
# col1.write("This is audio")
# col2.video("dog_video.mp4")

# tab1,tab2  = st.tabs(["audio","video"])
# tab1.audio("audio_file.mp3")
# tab1.write("hi")
# tab2.video("doggo_vid.mp4")

# #expander
# exp = st.expander("See pic")
# exp.write("Video and image")
# exp.image("doggo.jpg", width = 400)


# cont = st.container()
# cont.write("One")
# st.write("Two")
# cont.write("Three")
# st.write("This is last")
# cont.write("Last")

# #progress bar
# txt = "% completed"
# my_bar = st.progress(0 , text = txt)
# for pr in range(100):
#     time.sleep(0.1)
#     my_bar.progress(pr + 1 , text = txt)

# #spinner
# with st.spinner("wait for it..."):
#     time.sleep(5)
# st.write("wait over")

# st.balloons()

# st.snow()
#st.error("this is an error")
# st.warning("this is a warning")
# st.info("This is an infromational msg")
# st.success("This is a sucess msg")

# e = RuntimeError("Exp")
# st.exception(e)
# email = st.text_input("Enter mail")
# if not email:
#     st.warning("Enter your email please")
#     st.stop()
# st.success("go ahead")

# form = st.form("Basic form")
# name = form.text_input("Name")
# age = form.slider("Age", min_value = 18, max_value = 100, step =1)
# date = form.date_input("Birthday", value = datetime.date(2024,7, 9))
# submitted = form.form_submit_button("Submit")

# # if submitted:
# #     st.write(name , age , date)

# st.set_page_config(
#     page_title = "New app" ,
#     layout = "wide"
# )  
# st.write("hi")

# def summ(a , b):
#     return a + b

# with st.echo():
#     def mult(a , b):
#         return a * b
#     a = 10
#     b = 20
#     su = summ(a , b)
#     mu = mult(a , b)
#     st.write(su , mu)
# st.write("This is outside")


# # st.help(datetime.time)

# df1 = pd.DataFrame(
#     np.random.randn(10 , 2) ,
#     columns = ["col1" , "col2"]
# )
# my_table = st.table(df1)

# df2 = pd.DataFrame(
#     np.random.randn(1 , 2) ,
#     columns = ["col1" , "col2"]
# )

# my_table.add_rows(df2)

# my_chart = st.line_chart(df1)
# my_chart.add_rows(df2)

# my_chart = st.line_chart(df1)
# for i in range(5):
#     time.sleep(1)
#     df2 = pd.DataFrame(
#         np.random.randn(1 , 2) ,
#         columns = ["col1" , "col2"]
#     )
#     my_chart.add_rows(df2)
