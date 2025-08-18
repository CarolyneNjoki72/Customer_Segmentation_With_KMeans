import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt
import seaborn as sns

# Theme toggle
mode = st.sidebar.radio("Choose Theme:", ["Light", "Dark"])

if mode == "Dark":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0e1117;
            color: #fafafa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

st.title("Customer Segmentation Dashboard")


