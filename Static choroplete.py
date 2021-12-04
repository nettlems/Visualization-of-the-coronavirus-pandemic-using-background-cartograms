#Статический хороплет


# Импорт библиотек
import numpy as np
import pandas as pd
import plotly as py
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# Чтение данных
df = pd.read_csv("data/covid_19_data.csv")

# Переименуем колонки
df = df.rename(columns={'Country/Region':'Страна'})
df = df.rename(columns={'ObservationDate':'Дата'})
df = df.rename(columns={'Confirmed':'Подтверждено'})

# Манипуляции с оригиналом Dataframe
df_countries = df.groupby(['Страна', 'Дата']).sum().reset_index().sort_values('Дата', ascending=False)
df_countries = df_countries.drop_duplicates(subset = ['Страна'])
df_countries = df_countries[df_countries['Подтверждено']>0]

# Создание фоновой картограммы
fig = go.Figure(data=go.Choropleth(
    locations = df_countries['Страна'],
    locationmode = 'country names',
    z = df_countries['Подтверждено'],
    colorscale = 'Reds',
    marker_line_color = 'black',
    marker_line_width = 0.5,
))
fig.update_layout(
    title_text = 'Подтверждённые заболевания 28 марта 2020',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
        projection_type = 'equirectangular'
    )
)

fig.write_html('Static_choroplete.html', auto_open=True)