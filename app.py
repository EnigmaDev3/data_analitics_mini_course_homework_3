import dash
from dash import html
from dash.dependencies import Input, Output
import data_processing
import visualizations

df = data_processing.load_data()
mean_glucose, overweight_patients, high_risk_patients = data_processing.calculate_metrics(df)

app = dash.Dash(__name__)

glucose_trend = visualizations.create_glucose_trend(df)


app.layout = html.Div([
    html.H1('Информационная панель мониторинга здоровья'),
    html.Div([
        html.H2('Метрики'),
        html.Div([
            html.Div([
                html.H3('Средний уровень глюкозы в крови:'),
                html.P(f'{mean_glucose:.2f}')
            ], className='metric'),
            html.Div([
                html.H3('Процент пациентов с избыточным весом/ожирением:'),
                html.P(f'{overweight_patients:.2f}%')
            ], className='metric'),
            html.Div([
                html.H3('Пациенты с высоким риском по возрастным группам:'),
                html.P(f'{high_risk_patients:.2f}%')
            ], className='metric')
        ], className='metrics-container')
    ], className='metrics-section'),
    html.Div([
        html.H2('Визуализация'),
        html.Div([
            html.Div([
                glucose_trend
            ], className='visualization'),
            # Добавьте остальные графики здесь
        ], className='visualizations-container')
    ], className='visualizations-section')
])

if __name__ == '__main__':
    app.run_server(debug=True)
