import plotly.graph_objs as go
from dash import dcc

def create_glucose_trend(df):
    glucose_trend = dcc.Graph(
        id='glucose-trend',
        figure={
            'data': [
                go.Scatter(
                    x=df['id'],
                    y=df['Chol'],
                    mode='lines+markers',
                    marker=dict(color='blue'),
                    name='Glucose Trend'
                )
            ],
            'layout': go.Layout(
                title='Тенденции уровня глюкозы в крови',
                xaxis={'title': 'Patient ID'},
                yaxis={'title': 'Glucose Level'}
            )
        }
    )
    return glucose_trend


def create_bmi_distribution(df):
    bmi_distribution = dcc.Graph(
        id='bmi-distribution',
        figure={
            'data': [
                go.Histogram(
                    x=df['BMI'],
                    marker=dict(color='green')
                )
            ],
            'layout': go.Layout(
                title='Распредение BMI ',
                xaxis={'title': 'BMI'},
                yaxis={'title': 'Count'}
            )
        }
    )
    return bmi_distribution

def create_cholesterol_histogram(df):
    cholesterol_histogram =dcc.Graph(
        id='cholesterol-histogram',
        figure={
            'data': [
                go.Histogram(
                    x=df['Chol'],
                    opacity=0.75,
                    name='Cholesterol',
                    marker=dict(color='blue')
                ),
                go.Histogram(
                    x=df['LDL'],
                    opacity=0.75,
                    name='LDL',
                    marker=dict(color='red')
                ),
                go.Histogram(
                    x=df['HDL'],
                    opacity=0.75,
                    name='HDL',
                    marker=dict(color='green')
                )
            ],
            'layout': go.Layout(
                title='Уровень холестерина',
                xaxis={'title': 'Уровень холестерина'},
                yaxis={'title': 'Count'},
                barmode='overlay'
            )
        }
    )
    return cholesterol_histogram

def create_blood_pressure_vs_bmi(df):
    blood_pressure_vs_bmi = dcc.Graph(
        id='blood-pressure-vs-bmi',
        figure={
            'data': [
                go.Scatter(
                    x=df['BMI'],
                    y=df['Chol'],
                    mode='markers',
                    marker=dict(
                        size=10,
                        color='rgba(152, 0, 0, .8)',
                        line=dict(
                            width=2,
                            color='rgb(0, 0, 0)'
                        )
                    ),
                    name='Blood Pressure vs BMI'
                )
            ],
            'layout': go.Layout(
                title='Артериальное давление сравнительно с  ИМТ',
                xaxis=dict(title='BMI'),
                yaxis=dict(title='Cholesterol Level')
            )
        }
    )
    return blood_pressure_vs_bmi
