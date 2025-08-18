import streamlit as st
import pandas as pd
#from sklearn.cluster import KMeans 
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
# File upload
uploaded_file = st.file_uploader("Upload your dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:", df.head())

    # Feature selection
    features = st.multiselect("Select features for clustering", df.columns, 
                              default=["Income to Price Ratio", "Spending Score"])

