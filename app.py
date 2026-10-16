
import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration (Professional look)
st.set_page_config(page_title="iPhone Analytics Dashboard", page_icon="📱", layout="wide")

# Title and Description
st.title("📱 iPhone Performance & Analytics Dashboard")
st.markdown("Explore insights, pricing trends, and top-rated iPhones based on Flipkart dataset.")

# Load Dataset (Ensure 'apple_products.csv' is in the same folder)
@st.cache_data
def load_data():
    df = pd.read_csv("apple_products.csv")
    return df

data = load_data()

# Sidebar Filters
st.sidebar.header("Filter Options")
selected_brand = st.sidebar.selectbox("Select Brand", data['Brand'].unique())
filtered_data = data[data['Brand'] == selected_brand]

# Display Raw Data checkbox
if st.sidebar.checkbox("Show Raw Dataset"):
    st.subheader("Dataset Overview")
    st.dataframe(filtered_data)

# Layout Columns for Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total iPhones Listed", len(data))
col2.metric("Average Sale Price", f"₹ {data['Sale Price'].mean():,.2f}")
col3.metric("Average Star Rating", f"{data['Star Rating'].mean():.2f} ⭐")

st.markdown("---")

# Section 1: Top 10 Highest Rated iPhones
st.subheader("🏆 Top 10 Highest Rated iPhones")
highest_rated = data.sort_values(by=["Star Rating"], ascending=False).head(10)

fig_bar = px.bar(
    highest_rated, 
    x='Product Name', 
    y='Number Of Ratings', 
    color='Star Rating',
    title="Number of Ratings for Top-Rated iPhones"
)
fig_bar.update_layout(xaxis_tickangle=-45, height=500)
st.plotly_chart(fig_bar, use_container_width=True)

# Section 2: Scatter Plot Analysis (Price vs Ratings)
st.subheader("📊 Price vs. Ratings & Discount Analysis")
fig_scatter = px.scatter(
    data_frame=filtered_data,
    x="Number Of Ratings",
    y="Sale Price",
    size="Mrp",
    color="Star Rating",
    hover_name="Product Name",
    title="Relationship between Sale Price and Number of Ratings"
)
st.plotly_chart(fig_scatter, use_container_width=True)
