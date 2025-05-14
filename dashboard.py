def create_dashboard():
    import streamlit as st
    import pandas as pd
    from .utils import load_data, process_data

    st.title("Simple Dashboard Application")

    # Load and process data
    data = load_data()
    processed_data = process_data(data)

    # Display data
    st.subheader("Processed Data")
    st.write(processed_data)

    # Add a line chart
    st.subheader("Line Chart")
    st.line_chart(processed_data)

    # Add a bar chart
    st.subheader("Bar Chart")
    st.bar_chart(processed_data)