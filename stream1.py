import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import time
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

ax.hist(np.random.randn(100), bins= (10))
# st.pyplot(fig)

# maps
#you can pass longitudes and lattitudes 
places = pd.DataFrame({
    "lat":[19.07,28.64],
    'lon':[72.87, 77.12]
})
# st.map(places)


press = st.button("click this")
if press == True:
    st.write(time.time())