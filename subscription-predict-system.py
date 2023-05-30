import numpy as np
import pandas as pd
import pickle
import streamlit as st
import warnings
warnings.filterwarnings("ignore")


# Loading the Trained Data
loaded_model = pickle.load(open('subscription-predict-model.sav', 'rb'))

# Predict Function
def bank_deposit_prediction(input_data):

    columns = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week',
      'duration', 'campaign', 'pdays', 'previous', 'poutcome', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx',
      'euribor3m', 'nr.employed']

    input_data_df = pd.DataFrame([input_data], columns=columns)

    ### NEW ATTRIBUTES
    input_data_df['contacted_before'] = (input_data_df['pdays'] != 999).astype(int) # New column with 1 if pdays is not 999, 0 otherwise
    
    if (input_data_df['previous'] > 0).any():
        input_data_df['success_rate'] = (input_data_df['poutcome'].eq('success').astype(int) / input_data_df['previous']) # New column with the ratio of success to previous contacts
    else:
         input_data_df['success_rate'] = 0
    input_data_df['success_rate'] = input_data_df['success_rate'].fillna(0) # Replacing NaN values with 0

    # Make a prediction for the new client.
    prediction = loaded_model.predict(input_data_df)
    return prediction

def main():
    # Title
    st.title('Bank Term Deposit Prediction Web App')

    # User Inputs
    age = st.number_input('Age', step = 1)
    job = st.selectbox('Job', ['unknown','admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed'])
    marital = st.selectbox('Marital Status', ['unknown','divorced', 'married', 'single'])
    education = st.selectbox('Education', ['unknown','basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree'])
    default = st.selectbox('Default', ['unknown','no', 'yes'])
    housing = st.selectbox('Housing', ['unknown','no', 'yes'])
    loan = st.selectbox('Loan', ['unknown','no', 'yes'])
    contact = st.selectbox('Contact', ['cellular', 'telephone'])
    month = st.selectbox('Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
    day_of_week = st.selectbox('Day of Week', ['mon', 'tue', 'wed', 'thu', 'fri'])
    duration = st.number_input('Duration', step = 1)
    campaign = st.number_input('Campaign', step = 1)
    pdays = st.number_input('Pdays', step = 1)
    previous = st.number_input('Previous', step = 1)
    poutcome = st.selectbox('Poutcome', ['failure', 'nonexistent', 'success'])
    emp_var_rate = st.number_input('Employment Variation Rate')
    cons_price_idx = st.number_input('Consumer Price Index')
    cons_conf_idx = st.number_input('Consumer Confidence Index')
    euribor3m = st.number_input('EURIBOR 3 Month Rate')
    nr_employed = st.number_input('Number of Employees')

    # Making Prediction
    deposit_prediction = ''
    if st.button('Predict deposit'):
        input_data = [age, job, marital, education, default, housing, loan, contact, month, day_of_week, duration, campaign, pdays, previous, poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, euribor3m, nr_employed]
        deposit_prediction = bank_deposit_prediction(input_data)

    st.success(f'Client subscribed to a term deposit: {deposit_prediction}')

if __name__ == '__main__':
    main()
