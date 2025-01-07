import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

def train_model():
    st.write("## Model Training and Evaluation")
    
    # Load the dataset
    data = pd.read_csv("D:\\Mutahir Ahmad\\fcit docs\\semester V\\IDS\\project\\IMBD.csv\\IMBD.csv")
    
    # Preprocess the data
    data['votes'] = data['votes'].str.replace(',', '').astype(float)
    data['year'] = data['year'].astype(str).str.extract(r'(\d{4})').astype(float)
    data['duration'] = data['duration'].str.extract(r'(\d+)').astype(float)
    
    # Drop rows with NaN values in the target variable
    data = data.dropna(subset=['rating'])
    
    X = data[['year', 'duration', 'votes']]
    y = data['rating']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = HistGradientBoostingRegressor(random_state=42)
    model.fit(X_train, y_train)
    
    # Save the trained model
    joblib.dump(model, 'trained_model.pkl')
    
    # Evaluate the model
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    st.write(f"### Mean Squared Error: {mse:.4f}")
    
    # Evaluate the model using cross-validation
    cv_scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    cv_mse = -cv_scores.mean()
    st.write(f"### Cross-Validation Mean Squared Error: {cv_mse:.4f}")
    
    # Feature Importance
    feature_importance = model.feature_importances_
    features = X.columns
    importance_df = pd.DataFrame({'Feature': features, 'Importance': feature_importance})
    importance_df = importance_df.sort_values(by='Importance', ascending=False)
    st.write("### Feature Importance")
    st.write(importance_df)
    
    # Plot predictions vs actual values
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title('Actual vs Predicted Ratings')
    st.pyplot(plt)
    
    # Display sample predictions
    st.write("### Sample Predictions")
    sample_predictions = pd.DataFrame({'Actual': y_test, 'Predicted': predictions}).head(10)
    st.write(sample_predictions)