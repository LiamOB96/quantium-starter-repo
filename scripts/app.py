import pandas as pd
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_sales.csv")

# Make sure 'date' is a datetime type
df['date'] = pd.to_datetime(df['date'])
# Sort by date
df = df.sort_values('date')

# Create line chart
line_chart = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date", "sales": "Sales ($)"}
)

# Initialise Dash app
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser",
            style={"textAlign": "center", "color": "#4A90E2", "fontFamily": "Arial, sans-serif", "marginBottom": "30px"
                   }),
    dbc.RadioItems(
        id='region-selector',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'}
        ],
        value='all',  # default selection
        inline=True,
        inputStyle={"marginRight": "5px"},
        labelStyle={"marginRight": "15px", "padding": "5px 10px", "borderRadius": "5px"}
    ),
    dcc.Graph(id='sales-graph', figure=line_chart)
])


# Callback to update graph
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    line_chart = px.line(
        filtered_df,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.capitalize()}",
        labels={"date": "Date", "sales": "Sales ($)"}
    )
    return line_chart


if __name__ == "__main__":
    app.run(debug=True)
