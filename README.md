# Employee_Salary_Prediction
employe_salary_prediction by comparing different machine leaning algorithms and finally developing a streamlit application for predicting a employee salary
# Salary Prediction

## Introduction
This project aims to predict salaries based on various factors, such as age, gender, education level, job title, and years of experience. We have used a dataset containing 6704 rows and 6 columns to develop and evaluate our salary prediction model.

## Data Preprocessing

### Handling Missing Values
We checked for missing values in the dataset and removed rows with missing data, ensuring a clean dataset for modeling.

## Data Visualization


### Top 10 Highest Earning Professions
<img width="1189" height="790" alt="image" src="https://github.com/user-attachments/assets/83cc2361-e401-4853-b341-fcba184ccc28" />

*A Bar plot depicting the highest paying job titles versus the mean salary.*

### Distribution of Continuous Variables
<img width="1189" height="1489" alt="image" src="https://github.com/user-attachments/assets/43a2f712-c8dd-4da2-bffb-b3ee7ece2010" />

*This histogram shows the distribution of continuous variables in the dataset.*

### Distribution of Education and Gender
<img width="1489" height="490" alt="image" src="https://github.com/user-attachments/assets/22fe1fa0-257c-45b8-a08d-ea5e52310673" />

*A plot displaying the Education Level and Gender.*

### Correlation Heatmap
<img width="831" height="790" alt="image" src="https://github.com/user-attachments/assets/54b080a9-a34d-4826-ae5f-800262a577eb" />

*A heatmap illustrating the correlation between different features.*

## Model Building and Evaluation

### Model Selection
We explored various machine learning algorithms, including Linear Regression, Decision Trees, and Random Forests, to build our salary prediction model. Hyperparameter tuning was performed using GridSearchCV to find the best model configuration.

### Model Evaluation

Each model's performance was evaluated using several regression metrics, including Mean Squared Error (MSE), Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R-squared (R2) score. These metrics help assess the accuracy and reliability of the predictions.

### Feature Importance
<img width="1095" height="699" alt="image" src="https://github.com/user-attachments/assets/a647dcbd-165c-4b02-8ccf-b73769622e2d" />


*A bar chart depicting the importance of different features in predicting salary.*
## Model comparission
1. The Random Forest model achieved the highest R-squared score and the lowest error metrics (MSE, MAE, RMSE), indicating superior predictive performance compared to the other models.
2. The Decision Tree model also performed well but had higher errors than the Random Forest.
3. The Linear Regression model, while simple, had the lowest R-squared score and the highest errors, suggesting limitations in capturing complex relationships.

   
   
<img width="590" height="390" alt="image" src="https://github.com/user-attachments/assets/c2c229b5-1769-4926-b58f-8688b116addd" />


## Streamlit Application
<img width="903" height="824" alt="image" src="https://github.com/user-attachments/assets/be025836-0917-4dc0-9915-a4d90f12ff34" />




<img width="925" height="835" alt="image" src="https://github.com/user-attachments/assets/2a4d24af-360c-403e-94a9-7f84dc2e0f22" />



## Results

1. The Random Forest model achieved the highest R-squared score and the lowest error metrics (MSE, MAE, RMSE), indicating superior predictive performance compared to the other models.
2. The Decision Tree model also performed well but had higher errors than the Random Forest.
3. The Linear Regression model, while simple, had the lowest R-squared score and the highest errors, suggesting limitations in capturing complex relationships.

## Conclusion

In conclusion, the Random Forest model demonstrated the best predictive capability for salary estimation in this dataset. Its feature importance analysis revealed the most influential factors.

The model evaluation and feature importance analysis provided valuable insights for understanding salary determinants and highlighted the importance of choosing the appropriate machine learning model for regression tasks.

This salary prediction model can be used to make informed salary estimates based on individual characteristics, making it a valuable tool for HR analytics and compensation planning.In conclusion, our salary prediction model, trained on a well-preprocessed dataset, successfully predicts salaries based on various factors. This project demonstrates the importance of data preprocessing, feature engineering, and model selection in creating an accurate predictive model.

## Usage

To use our salary prediction model, you can follow these steps:

1. Clone this repository.
2. Install the required libraries listed in the `requirements.txt` file.
3. Run the provided Jupyter notebook or Python script to load the model and make predictions on new data.
