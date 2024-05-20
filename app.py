import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import data_processing
import visualizations

df = data_processing.load_data()
mean_glucose, overweight_patients, high_risk_patients = data_processing.calculate_metrics(df)

app = dash.Dash(__name__)

# Создайте графики
graphs = [
    visualizations.create_glucose_trend(df),
    visualizations.create_bmi_distribution(df),
    visualizations.create_cholesterol_histogram(df),
    visualizations.create_blood_pressure_vs_bmi(df)
]

app.layout = dbc.Container([
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
            html.Div(id='graph-container'),
        ], className='visualizations-container'),
        html.Div([
            dbc.Button('Назад', id='back-button', disabled=True),
            dbc.Button('Вперед', id='forward-button', disabled=False)
        ], className='button-container')
    ], className='visualizations-section')
], fluid=True)

@app.callback(
    [Output('graph-container', 'children'),
     Output('back-button', 'disabled'),
     Output('forward-button', 'disabled')],
    [Input('back-button', 'n_clicks'),
     Input('forward-button', 'n_clicks')],
    [State('graph-container', 'children')]
    

)

def update_graph(back_clicks, forward_clicks, current_graph):
    ctx = dash.callback_context
    if not ctx.triggered:
        return graphs[0], True, False
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        current_index = graphs.index(current_graph)
        if button_id == 'back-button':
            new_index = current_index - 1
        elif button_id == 'forward-button':
            new_index = current_index + 1
        new_graph = graphs[new_index]
        return new_graph, new_index == 0, new_index == len(graphs) - 1

if __name__ == '__main__':
    app.run_server
