import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run_eda():
    st.write("## Exploratory Data Analysis")
    
    # Load the dataset
    data = pd.read_csv("D:\\Mutahir Ahmad\\fcit docs\\semester V\\IDS\\project\\IMBD.csv\\IMBD.csv")
    
    st.write("### Dataset Preview")
    st.write(data.head())
    
    st.write("### Summary Statistics")
    st.write(data.describe())
    
    st.write("### Missing Values")
    st.write(data.isnull().sum())
    
    st.write("### Distribution of Ratings")
    plt.figure(figsize=(10, 6))
    sns.histplot(data['rating'], bins=10)
    st.pyplot(plt)
    
    st.write("### Correlation Heatmap")
    data['votes'] = data['votes'].str.replace(',', '').astype(float)
    correlation = data[['rating', 'votes']].corr()
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm')
    st.pyplot(plt)
    
    st.write("### Missing Values Heatmap")
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.isnull(), cbar=False, cmap='viridis')
    st.pyplot(plt)
    
    st.write("### Outliers in Ratings")
    plt.figure(figsize=(10, 6))
    sns.boxplot(data['rating'])
    st.pyplot(plt)
    
    st.write("### Feature Distributions")
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data['rating'], label='Rating', fill=True)
    sns.kdeplot(data['votes'], label='Votes', fill=True)
    plt.legend()
    st.pyplot(plt)
    
    st.write("### Trend of Movie Releases Over Years")
    data['year'] = data['year'].str.extract(r'(\d{4})').astype(float)
    release_trends = data['year'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.plot(release_trends.index, release_trends.values, marker='o')
    plt.title('Trend of Movie Releases Over Years')
    plt.xlabel('Year')
    plt.ylabel('Number of Movies Released')
    plt.grid(True)
    st.pyplot(plt)
    
    st.write("### Average Ratings by Genre")
    average_ratings = data.groupby('genre')['rating'].mean().sort_values(ascending=False)
    st.write(average_ratings.head(10))
    
    st.write("### Pairwise Feature Relationships")
    sns.pairplot(data[['rating', 'votes', 'year']])
    st.pyplot(plt)