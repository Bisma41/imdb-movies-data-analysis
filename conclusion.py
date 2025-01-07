import streamlit as st

def show_conclusion():
    st.write("""
    ### Conclusion

    This project has successfully explored the IMDb dataset, providing insights into the dynamics of movie ratings. By analyzing genres, votes, duration, and their relationship with ratings, we identified key factors influencing audience reception.

    #### Key Takeaways

    **Exploratory Insights**:
    - Popular genres such as Drama and Action dominate the dataset, reflecting audience preferences.
    - A positive correlation exists between the number of votes and higher ratings, indicating that widely viewed content tends to be better rated.

    **Machine Learning Predictions**:
    - The predictive model exhibited reasonable performance with an MSE of approximately 0.831, effectively estimating ratings based on the provided features.
    - The model highlights the importance of features such as votes and duration in influencing ratings.

    #### Future Directions

    - **Dataset Expansion**: Including additional attributes like cast, directors, and production budgets can enhance the analysis and improve model accuracy.
    - **Advanced Models**: Testing more sophisticated algorithms, such as ensemble methods or neural networks, could lead to better predictions.
    - **Interactivity**: Allowing users to input custom data for prediction can make the model more dynamic and user-friendly.

    This project demonstrates the power of data analysis and machine learning in deriving meaningful insights from real-world datasets. The findings not only highlight audience trends but also pave the way for future research and applications in the entertainment industry.
    """)