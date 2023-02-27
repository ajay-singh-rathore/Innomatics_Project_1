import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard - Customer_List")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "customer.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Customer List.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

job = st.selectbox("Select the Job_Title :", df['job_title'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['job_title'] == job], x="tenure")
col1.plotly_chart(fig_1, use_container_width=True)
print("\n")
fig_2 = px.box(df[df['job_title'] == job], y="postcode")
col2.plotly_chart(fig_2, use_container_width=True)