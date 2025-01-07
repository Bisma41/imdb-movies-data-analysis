# imdb-movies-data-analysis


This project focuses on analyzing and predicting IMDB movie ratings using the IMDB dataset. The dataset includes information about movies, TV shows, and streaming content. The primary goal of this project is to perform exploratory data analysis (EDA), build a machine learning model, and deploy an interactive web application using Streamlit to showcase the insights and predictions.

## Project Structure
The project is organized into the following structure:

```
imdb-movies-data-analysis/
├── src/
│   ├── app.py            # Main Streamlit application
│   ├── eda.py            # Script for exploratory data analysis
│   ├── model.py          # Machine learning model training and prediction
│   ├── conclusion.py     # Text for the app conclusion
│   ├── introduction.py   # Text for the app introduction
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## Features
1. **Exploratory Data Analysis**
   - Summary statistics and visualizations.
   - Correlation analysis and insights into key features.

2. **Machine Learning Model**
   - Predicts movie ratings based on features such as genre, duration, and votes.
   - Includes performance metrics like Mean Squared Error (MSE).

3. **Interactive Streamlit Application**
   - Users can explore the dataset through visualizations.
   - Upload custom datasets for prediction.
   - Download predictions as a CSV file.

## How to Run
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<Bisma41>/imdb-movies-data-analysis.git
   cd imdb-movies-data-analysis

   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required libraries:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/macOS
   venv\Scripts\activate    # On Windows
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Execute the Streamlit app:
   ```bash
   streamlit run src/app.py
   ```

4. **Access the App**:
   Open the URL provided in the terminal (default: [`http://localhost:8501/`](https://github.com/Bisma41/imdb-movies-data-analysis.git)) in your browser.

## Requirements
The project requires the following Python libraries:
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

All dependencies are listed in the `requirements.txt` file.

## Usage
1. **Exploration**:
   - Navigate through the app to explore the dataset.
   - Visualize trends in movie ratings, genres, and more.

2. **Prediction**:
   - Upload a CSV file containing features like `genre`, `duration`, and `votes`.
   - Get predicted ratings for each entry in the uploaded file.
   - Download the results as a CSV file.

## Results
- **EDA**: Key insights into the dataset, such as popular genres and correlations between votes and ratings.
- **Model Performance**: Achieved a Mean Squared Error (MSE) of approximately 0.831 on test data.

## Future Enhancements
- Incorporate additional features like cast and director details.
- Implement advanced models for improved prediction accuracy.
- Add more interactivity for dynamic user inputs.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.



