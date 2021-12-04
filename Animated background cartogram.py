#Анимированная фоновая картограмма

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
df = df.rename(columns={'Country/Region': 'Страна'})
df = df.rename(columns={'ObservationDate': 'Дата'})
df = df.rename(columns={'Confirmed': 'Подтверждено'})

# Манипуляции с оригиналом Dataframe
df_countrydate = df[df['Подтверждено'] > 0]
df_countrydate = df_countrydate.groupby(['Дата', 'Страна']).sum().reset_index()
df_countrydate

# Создание фоновой картограммы
fig = px.choropleth(df_countrydate,
                    locations="Страна",
                    locationmode="country names",
                    color="Подтверждено",
                    hover_name="Страна",
                    animation_frame="Дата"
                    )
fig.update_layout(
    title_text='Глобальное распространение короновируса',
    title_x=0.5,
    geo=dict(
        showframe=False,
        showcoastlines=False,
    ))

fig.write_html('Animated_background_cartogram.html', auto_open=True)