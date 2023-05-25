import pandas as pd
import plotly.express as px

# Загрузка DataFrame
df = pd.read_csv('spotify-streaming-top-50-usa.csv')

# Построение гистограммы
fig = px.histogram(df, x='song')
fig.show()

# Построение круговой диаграммы
fig = px.pie(df, names='popularity')
fig.show()
