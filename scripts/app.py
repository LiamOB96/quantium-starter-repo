import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("../data/processed_sales.csv")

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
app = Dash()

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=line_chart)
])

if __name__ == "__main__":
    app.run(debug=True)

