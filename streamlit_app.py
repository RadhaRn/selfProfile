import streamlit as st
from streamlit_timeline import timeline
import streamlit.components.v1 as components
import plotly.graph_objects as go
from matplotlib import pyplot as plt

# other python files
from constant import *

st.set_page_config(page_title='Radha Ray\'s Profile', layout='wide', page_icon='page_with_curl', initial_sidebar_state='auto')

# hide hamburger menu and footer
hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

with st.sidebar:
        components.html(embed_component['linkedin'], height=320)

st.sidebar.markdown(info['name'], unsafe_allow_html=True)

with open('./pdfs/Radha_Ray_Resume.pdf', 'rb') as pdf_file:
    PDFbyte = pdf_file.read()

st.sidebar.download_button(label='Download Resume', data=PDFbyte, file_name='Radha_Ray_Resume.pdf',
                           mime='application/octet-stream')

st.subheader('Summary')
st.write(info['Brief'])

st.subheader('Career snapshot')

with st.spinner(text="Building line"):
    with open('./timeline.json', "r") as f:
        data = f.read()
        timeline(data, height=500)

st.subheader('Skills & Tools ⚒️')


def skill_tab():
    rows, cols = len(info['skills']) // skill_col_size, skill_col_size
    skills = iter(info['skills'])
    if len(info['skills']) % skill_col_size != 0:
        rows += 1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                columns[index_].button(next(skills))
            except:
                break


with st.spinner(text="Loading section..."):
    skill_tab()

st.subheader('Education 📖')

fig = go.Figure(data=[go.Table(
    header=dict(values=list(info['edu'].columns),
                # fill_color='paleturquoise',
                fill_color='purple',
                align='center', height=65, font_size=20),
    cells=dict(values=info['edu'].transpose().values.tolist(),
               fill_color='lavender',
               # fill_color='darkgreen',
               align='left', height=40, font_size=15))])

fig.update_layout(width=750, height=400)
st.plotly_chart(fig)

st.subheader('A Typical Day at Work 📊')

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = typ_day
sizes = [25, 25, 15, 15, 20]
explode = (0.1, 0.12, 0.14, 0.15, 0)  # only "explode" the 2nd slice

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
my_circle = plt.Circle((0, 0), 0.42, color='white')
fig1 = plt.gcf()
fig1.gca().add_artist(my_circle)
st.pyplot(fig1)
