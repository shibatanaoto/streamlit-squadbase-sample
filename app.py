import streamlit as st
import numpy as np

st.title("Streamlit Squadbase Sample[feature/test]")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV file
    import pandas as pd
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("### Uploaded Data")
    st.dataframe(df)

    # Display basic statistics
    st.write("### Basic Statistics")
    st.write(df.describe())

    # Display column names
    st.write("### Column Names")
    st.write(df.columns.tolist())



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
