# Customer Segmentation with K-Means

This project demonstrates how businesses can use K-Means Clustering to segment customers based on their income-to-price ratio and spending score. By identifying distinct groups of customers, businesses can design targeted marketing campaigns to improve engagement and retention.

The project is built with Streamlit to provide an interactive interface for exploring clusters and suggested marketing campaigns.

## Features

* Perform K-Means clustering on customer data.

* Visualize clusters using scatter plots.

* Automatically generate marketing campaign suggestions for each cluster.

* Interactive Streamlit dashboard (supports dark mode).

* Evaluate clustering quality using Silhouette Score.


## Output

Clusters generated from the dataset:

* Cluster 0: VIP customers – high ratio & high spending → exclusive offers, early access program
  
* Cluster 1: Budget-conscious but loyal → discounts, referral bonuses

* Cluster 2: High potential but low engagement → awareness & personalized recommendations

* Cluster 3: New/entry-level customers → broad promotions & bundles


## Tech Stack

* Python 3.9+

* scikit-learn (KMeans, silhouette score)

* Pandas & NumPy (data processing)

* Matplotlib & Seaborn (visualizations)

* Streamlit (interactive dashboard)
