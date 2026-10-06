import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="CRM Interaction Counter",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("📊 Customer Interaction Counter")
st.write("CRM dashboard for analyzing customer engagement.")

# Load CSV file
df = pd.read_csv("data/interactions.csv")

# -----------------------------
# SUMMARY
# -----------------------------

st.subheader("📌 CRM Summary")

total_interactions = len(df)
total_customers = df["customer_id"].nunique()

col1, col2 = st.columns(2)

col1.metric(
    "Total Customers",
    total_customers
)

col2.metric(
    "Total Interactions",
    total_interactions
)

# -----------------------------
# INTERACTION TYPES
# -----------------------------

st.subheader("📞 Interaction Types")

interaction_counts = (
    df["interaction_type"]
    .value_counts()
    .reset_index()
)

interaction_counts.columns = [
    "Interaction Type",
    "Count"
]

st.bar_chart(
    interaction_counts,
    x="Interaction Type",
    y="Count"
)

# -----------------------------
# CUSTOMER ENGAGEMENT
# -----------------------------

st.subheader("👥 Customer Engagement")

customer_counts = (
    df.groupby(
        ["customer_id", "customer_name"]
    )
    .size()
    .reset_index(name="Total Interactions")
)

st.dataframe(
    customer_counts,
    use_container_width=True
)

# -----------------------------
# LOW ENGAGEMENT
# -----------------------------

st.subheader("⚠️ Low-Engagement Customers")

threshold = st.slider(
    "Select maximum interactions for low engagement",
    min_value=1,
    max_value=10,
    value=2
)

low_engagement = customer_counts[
    customer_counts["Total Interactions"] <= threshold
]

st.write(
    "Customers with",
    threshold,
    "or fewer interactions:"
)

st.dataframe(
    low_engagement,
    use_container_width=True
)

st.metric(
    "Low-Engagement Customers",
    len(low_engagement)
)

# -----------------------------
# DOWNLOAD REPORT
# -----------------------------

st.subheader("📥 Download Report")

report = low_engagement.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="Download Low-Engagement Report",
    data=report,
    file_name="low_engagement_report.csv",
    mime="text/csv"
)