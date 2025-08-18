import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
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
    k = st.slider("Select number of clusters (k)", 2, 10, 3)
    # Run clustering
    X = df[features]
    model = KMeans(n_clusters=k, random_state=42)
    df['Cluster'] = model.fit_predict(X)

    st.subheader("Cluster Summary")
    summary = df.groupby("Cluster")[features].mean()
    st.write(summary)

    # Visualization (2D case)
    if len(features) == 2:
        plt.figure(figsize=(6,4))
        sns.scatterplot(x=features[0], y=features[1], hue="Cluster", data=df, palette="tab10")
        plt.scatter(model.cluster_centers_[:,0], model.cluster_centers_[:,1], 
                    s=200, c="black", marker="X", label="Centers")
        plt.legend()
        st.pyplot(plt)

    # --- Marketing Campaign Suggestions ---
    st.subheader("Suggested Marketing Campaigns")

    for cluster_id, row in summary.iterrows():
        ratio = row[features[0]]
        spending = row[features[1]]

        # Basic logic for recommendations
        if ratio >= summary[features[0]].mean() and spending >= summary[features[1]].mean():
            campaign = "VIP program, exclusive offers, early access to products."
        elif ratio < summary[features[0]].mean() and spending >= summary[features[1]].mean():
            campaign = "Discounts, coupons, referral bonuses for loyal but budget-conscious customers."
        elif ratio >= summary[features[0]].mean() and spending < summary[features[1]].mean():
            campaign = "Awareness campaigns, personalized recommendations to encourage more spending."
        else:
            campaign = "Entry-level bundles, social media ads, broad promotions to drive engagement."

        st.markdown(f"""
        **Cluster {cluster_id}:**
        - Avg {features[0]} = {ratio:.2f}  
        - Avg {features[1]} = {spending:.2f}  
        - 📢 *Recommended Campaign:* {campaign}
        """)
