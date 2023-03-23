import streamlit as st

#Text elements:

#side bar
st.sidebar.text('Daftar Hadir')
nama = st.sidebar.text_input('Masukkan nama anda :', value='')
email = st.sidebar.text_input('Masukkan email anda :', value='')
umur = st.sidebar.selectbox('Masukkan umur anda', ['<20','20 - 30', '30 - 40', '40 - 50', '50 - 60'])

st.sidebar.text('Terima kasih, data anda adalah :')
st.sidebar.text('Nama ' + nama)  
st.sidebar.text(' email ' + email)
st.sidebar.text(' umur ' + umur)


# Title
st.title('Streamlit app 1st attempt')
# Header
st.header('ini bagian headernya')
# Subheader
st.subheader(" Ini bagian subheader ")
# Markdown
st.markdown(' # markdown1 ')
st.markdown(' ## markdown2 ')
st.markdown(' ### markdown3 ')
st.markdown(' ##### markdown4 ')

# markdown multi baris 
st.markdown("""
  # test1
  ## test 2
  ### test 3
  """, True)


# Caption


# Code block

st.code("y = mx + c")

# Text
st.text("This is a trial project !")

# LaTeX

st.latex("\ int a y^2 \ , dy")



# Dataframe 

import pandas as pd
#students names
students = ["Amelia Kami", "Antoinne Mark", "Peter Zen", "North Kim"]
#marks
marks = [82, 76, 96, 68]

df = pd.DataFrame()

df["Student Name"] = students

df["Marks"] = marks


#Save to dataframe
df.to_csv("students.csv", index = False)


#display dataframe
st.text("DataFrame")
st.dataframe(df)

#Static table
st.text("Static Table")
st.table(df)

#Metrics
st.text("Metrix")
st.metric("KPI", 56, 3)


#Display Code average of a list
st.text("Display Code")

code = '''def cal_average(numbers):
    sum_number = 0
    for t in numbers:
        sum_number = sum_number + t           

    average = sum_number / len(numbers)
    return average'''
st.code(code, language='python')


st.text("Show an error message")
st.error("An Error was encountered")

st.text("Display a warning message")
st.warning("Incompatible data point!")

st.text("Display informational messages")
st.info("Page is refreshed every 2 hours")

st.text("Display success messages")
st.success("Record found!")

st.text("Display an exception in your application")
exp = ValueError('This is an exception of type ValueError')
st.exception(exp)


st.text("plotly")
import plotly.express as px
# This data frame has 244 rows, but 4 unique entries for the `day` variable
df = px.data.tips()
fig = px.pie(df, values='tip', names='day')
# Plot!
st.plotly_chart(fig, use_container_width=True)

st.text("Dispkay Altair/scatter ")
import altair as alt
import streamlit as st
import numpy as np

df = pd.DataFrame(
     np.random.randn(300, 4),
     columns=['a', 'b', 'c', 'd'])

chrt = alt.Chart(df).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c', 'd'])

st.altair_chart(chrt, use_container_width=True)


#Progress bar
import time

st.text("Progress Bar")
bar_p = st.progress(0)

for percentage_complete in range(100):
    time.sleep(0.1)
    bar_p.progress(percentage_complete + 1)
#Status message
#display a temporary message when executing a block of code
with st.spinner('Please wait...'):
    time.sleep(5)
st.write('Complete! Show celebratory balloons')

st.balloons()


st.text("Matplotlib")
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=1000)
fig, ax = plt.subplots()
ax.hist(arr, bins=30)
plt.grid()
st.pyplot(fig)

#vega-lite
#st.vega_lite_chart(data)
#matplotlib
st.pyplot(fig)
#deck.gl
#st.deck_gl_chart(data)
#pyDeck
#st.pydeck_chart(data)


st.text("button")
st.button("Click here")

st.text("Check Box")
selected = st.checkbox("Accept terms")

st.text("select Box")
option = st.selectbox(
     'How would you like to receive your package?',
     ('By air', 'By sea', 'By rail'))

st.write('You selected:', option)

st.text("Date")
import datetime
day = st.date_input(
     "When is your birthday?",
     datetime.date(2022, 7, 6))
st.write('Your birthday is:', day)


#Multi select
selections = st.multiselect("Purchase", ["oranges", "apples", "bananas"])
#Number input
choice = st.number_input("Choose a number", 0, 50)
#Text area
text = st.text_area("Start typing")
#Time input
time = st.time_input("Dinner time")
#file upload
data = st.file_uploader("Share excel file")
#Slider
num = st.slider("Pick a number", 0, 5)
#Select slider
fruit = st.select_slider("Pick a fruit", ["Apple", "Orange", "Berries"])
