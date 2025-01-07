import streamlit as st
from eda import run_eda
from model import train_model
from conclusion import show_conclusion
from introduction import show_introduction

def main():
    st.title("Data Science Project Showcase")
    st.sidebar.title("Navigation")
    
    # Dropdown for navigation
    page = st.sidebar.selectbox("Choose a section", ["Introduction", "EDA", "Model", "Conclusion"])
    
    if page == "Introduction":
        show_introduction()
    
    elif page == "EDA":
        st.subheader("Exploratory Data Analysis")
        run_eda()
    
    elif page == "Model":
        st.subheader("Model Training and Evaluation")
        train_model()
    
    elif page == "Conclusion":
        show_conclusion()

if __name__ == "__main__":
    main()