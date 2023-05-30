# Subscription-Predict-System

This dataset comprises of direct marketing campaigns (phone calls) of a Portuguese banking institution. The dataset used for this project is the Bank Marketing Data Set (bank-additional), which can be found at https://archive.ics.uci.edu/ml/datasets/Bank+Marketing. This is a Classification problem. The dataset has 4119 rows and 21 columns.

This  supported with streamlit web interface for user input.

## Problem 
Predict if the client will subscribe a term deposit.
## System Environment

**The project was developed using:**
 - Python
 - Anaconda
 - Jupyter
 - Streamlit
 - pandas
 - numpy
 - Scikit-learn
 - Matplotlib

## Approach

1. **Data cleaning**: Performed necessary data cleaning operations to make sure the data is in a suitable format for analysis.  
2. **Data preprocessing**: Performed necessary data preprocessing operations such as feature scaling, encoding categorical variables, etc.  
3. **Feature selection**: Most relevant features for the model selected by feature selection techniques.  
4. **Model selection**: Compare the performance of four different models (RandomForestClassifier, SVC, KNeighborsClassifier, DecisionTreeClassifier) and choosed the best one based on evaluation metrics.  
5. **Hyperparameter tuning**: hyperparameters of the selected model tuned to improve its performance.  
7. **Evaluation**: Evaluated the performance of the final model using appropriate evaluation metrics.  
8. **Deployment**: Final model deployed using streamlit and web interface for the model created.  

## Web Interface
Final model deployed using streamlit and an interface created for the making predictions. You can reach web interface from the address: https://ktyolmz-subscription-predict-subscription-predict-system-d4hg3l.streamlit.app/ 
