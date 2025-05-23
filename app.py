import streamlit as st
import numpy as np

st.title("Streamlit Squadbase Sample[feature/test]")

# Sample data creation
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = np.random.randint(100, 1000, 6)
costs = np.random.randint(50, 500, 6)

# Display a simple bar chart
st.subheader("Monthly Sales Chart")
st.bar_chart({
    'Sales': sales
})

# Display a simple line chart
st.subheader("Monthly Sales Trend")
st.line_chart({
    'Sales': sales,
    'Costs': costs
})
