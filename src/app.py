import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# CONFIG PAGE
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# CSS STYLE (🔥 LOOK PRO)
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
.metric {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# LOAD DATA
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(BASE_DIR, "data", "supermarket_sales.csv")
df = pd.read_csv(file_path)

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

# SIDEBAR
st.sidebar.title("🔎 Filters")

city = st.sidebar.multiselect(
    "City",
    df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Customer Type",
    df["Customer type"].unique(),
    default=df["Customer type"].unique()
)

df = df[
    (df["City"].isin(city)) &
    (df["Customer type"].isin(customer_type))
]

# TITLE
st.markdown("<h1 style='text-align:center;'>📊 Sales Dashboard</h1>", unsafe_allow_html=True)

# KPI SECTION
total_sales = df["Sales"].sum()
avg_sales = df["Sales"].mean()
total_quantity = df["Quantity"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"{total_sales:,.0f}")
col2.metric("📦 Quantity Sold", f"{total_quantity}")
col3.metric("📊 Avg Sale", f"{avg_sales:,.2f}")

st.markdown("---")

# GRAPH 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Sales Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df["Sales"], kde=True, ax=ax, color="#00BFFF")
    st.pyplot(fig)

with col2:
    st.subheader("📊 Sales vs Quantity")
    fig, ax = plt.subplots()
    sns.scatterplot(x="Quantity", y="Sales", data=df, ax=ax, color="#FF4B4B")
    st.pyplot(fig)

# GRAPH 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Product Performance")
    fig, ax = plt.subplots()
    df.groupby("Product line")["Sales"].sum().sort_values().plot(
        kind="barh", ax=ax, color="#00C49F"
    )
    st.pyplot(fig)

with col2:
    st.subheader("👥 Customer Type")
    fig, ax = plt.subplots()
    df.groupby("Customer type")["Sales"].sum().plot(
        kind="bar", ax=ax, color="#FFA500"
    )
    st.pyplot(fig)

# TREND
st.subheader("📅 Sales Trend")
fig, ax = plt.subplots()
df.groupby("Month")["Sales"].sum().plot(marker="o", ax=ax, color="#AB63FA")
st.pyplot(fig)

# DATA TABLE
with st.expander("🔍 Show Dataset"):
    st.dataframe(df)