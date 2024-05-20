import pandas as pd

def load_data():
    df = pd.read_csv('Diabetes Classification.csv')
    return df

def calculate_metrics(df):
    mean_glucose = df['Chol'].mean()
    overweight_patients = (df['BMI'] >= 25).sum() / len(df) * 100
    high_risk_patients = df[df['Age'] > 40]['Diagnosis'].sum() / len(df[df['Age'] > 40]) * 100
    return mean_glucose, overweight_patients, high_risk_patients
