import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import data_processing
import visualizations

df = data_processing.load_data()
mean_glucose, overweight_patients, high_risk_patients = data_processing.calculate_metrics(df)

app = dash.Dash(__name__)

# Создаем список графиков
charts = [
    visualizations.create_glucose_trend(df),
    visualizations.create_bmi_distribution(df),
    visualizations.create_cholesterol_histogram(df),
    visualizations.create_blood_pressure_vs_bmi(df)
]



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
            html.Div(id='chart-container', className='visualization'),
            html.Div([
                dbc.Button("Назад", id="back-button", className="mr-2", style={'font-size': '20px'}),
                dbc.Button("Вперед", id="forward-button", className="mr-2", style={'font-size': '20px'}),
            ], style={'text-align': 'center'}),
            html.Div(id='button-output-container'),
        ], className='visualizations-container')
    ], className='visualizations-section')
])

@app.callback(
    Output('chart-container', 'children'),
    [Input('back-button', 'n_clicks'), Input('forward-button', 'n_clicks')],
    [State('chart-container', 'children')])
def update_output(back_clicks, forward_clicks, current_chart):
    chart_index = charts.index(current_chart) if current_chart in charts else 0

    if back_clicks is not None and back_clicks > 0:
        chart_index = (chart_index - 1) % len(charts)
    elif forward_clicks is not None and forward_clicks > 0:
        chart_index = (chart_index + 1) % len(charts)

    return charts[chart_index]

if __name__ == '__main__':
    app.run_server(debug=True)
