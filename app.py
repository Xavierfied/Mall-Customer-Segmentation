import streamlit as st
import joblib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------
# Load trained model & scaler
# ----------------------
kmm = joblib.load("K_mean_model.joblib")
scaler = joblib.load("encoder.joblib")

cluster_labels = {
    0: "Cluster 0 – Regular Customers (Average Earners & Spenders)",
    1: "Cluster 1 – VIP Customers (High Earners & High Spenders)",
    2: "Cluster 2 – Reckless Spenders (Low Earners & High Spenders)",
    3: "Cluster 3 – Frugal Spenders (High Earners & Low Spenders)",
    4: "Cluster 4 – Essential Needs Spenders (Low Earners & Low Spenders)"
}

st.title("Customer Segmentation (KMeans)")

# ----------------------
# User Input
# ----------------------
st.write("### Enter customer details:")
income = st.slider("Annual Income (k$)", min_value=10, max_value=150, value=60)
score = st.slider("Spending Score (1-100)", min_value=1, max_value=100, value=50)

# ----------------------
# Predict Button
# ----------------------
if st.button("Predict Cluster"):
    # Prepare input (MUST match training order)
    customer = pd.DataFrame(
        [[income, score]],
        columns=["Annual Income (k$)", "Spending Score (1-100)"]
    )

    # Debug: show raw input
    st.write("🔍 Raw Input:", customer)

    # Scale input
    customer_scaled = scaler.transform(customer)

    # Debug: show scaled input
    st.write("🔍 Scaled Input:", customer_scaled)

    # Predict cluster
    cluster = kmm.predict(customer_scaled)[0]

    # Debug: show raw cluster number
    st.write("🔍 Predicted Cluster (numeric):", cluster)

    # Display result
    st.success(f"👉 This customer belongs to **{cluster_labels[cluster]}**")

    # ----------------------
    # Optional: Show clusters with new customer highlighted
    # ----------------------
    data = pd.read_csv("Mall_Customers.csv")
    X = data[["Annual Income (k$)", "Spending Score (1-100)"]]
    X_scaled = scaler.transform(X)
    data["Cluster"] = kmm.predict(X_scaled)

    fig, ax = plt.subplots(figsize=(7, 5))
    sns.scatterplot(
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Cluster",
        palette="tab10",
        data=data,
        ax=ax,
        s=60
    )

    # Highlight the new customer
    ax.scatter(
        income, score,
        color="red", s=200,
        edgecolor="black", marker="X",
        label="New Customer"
    )
    ax.legend()
    st.pyplot(fig)
