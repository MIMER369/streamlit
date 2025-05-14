import streamlit as st
from dashboard import create_dashboard

def main():
    st.title("Simple Dashboard Application")
    create_dashboard()

if __name__ == "__main__":
    main()