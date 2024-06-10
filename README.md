# NBA Shot Analysis and Predictive Modeling

## Project Structure
The project consists of the following components:

1. **Data Extraction and Preprocessing**:
   - `NBA_API_pulls.py`: Python script utilizing the NBA API to extract shot chart data for specific seasons and players. Libraries used include `nba_api`, `pandas`, `json`, and `requests`.

2. **Machine Learning Model Creation**:
   - `Creating_ML_Model.py`: Python script for preprocessing the extracted data and creating a machine learning model using logistic regression. It includes feature engineering techniques such as time-related feature conversion and one-hot encoding of categorical variables. Libraries used include `pandas`, `numpy`, `matplotlib`, `seaborn`, and `sklearn`.

3. **Model Testing and Analysis**:
   - `Testing_Model.py`: Python script for testing and analyzing the performance of the machine learning model. It involves player performance analysis, team statistics, and game-level insights based on model predictions. Libraries used include `pandas`, `numpy`, `matplotlib`, and `seaborn`.

## Project Workflow
The workflow of the project is as follows:

1. **Data Extraction**: 
   - Utilize `NBA_API_pulls.py` to extract shot chart data from the NBA API.

2. **Data Preprocessing**:
   - Preprocess the extracted data in `NBA_API_pulls.py`, including feature engineering such as time-related feature conversion and one-hot encoding of categorical variables.

3. **Model Creation**:
   - Use `Creating_ML_Model.py` to preprocess the data further and create a logistic regression model for predicting shot outcomes. Model training involves utilizing the `sklearn` library.

4. **Model Testing and Analysis**:
   - Apply the trained model on test data using `Testing_Model.py`.
   - Analyze player performance, team statistics, and game-level insights based on model predictions.

## Future Work
Currently working towards further enhancing the machine learning model by incorporating additional factors that affect the outcome of a shot. This includes exploring advanced feature engineering techniques and experimenting with different machine learning algorithms. Additionally, planning to implement feature selection techniques to improve model performance.

## Conclusion
This project demonstrates the extraction, preprocessing, modeling, and analysis of NBA shot data using Python scripts. It leverages the NBA API for data extraction, utilizes machine learning techniques for predictive modeling, and provides insights into player performance and game-level statistics.

## Example Output
I tested the model on data from the 2022/23 NBA Regular Season to see who the top performing players were.

![Points Added Per game (1)](https://github.com/AtharvaBeesen/BasketBallExpectedPoints/assets/86427671/da29bea8-b36a-4932-89b3-c604f94c7a59){:height="50%" width="50%"}
