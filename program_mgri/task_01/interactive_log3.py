import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

# Создание значений x
x = np.arange(1, 16, 1)
y = np.log(x) / np.log(3)  # логарифм по основанию 3

# Построение интерактивного графика
trace = go.Scatter(x=x, y=y, mode='lines+markers', name='y = log₃(x)', line=dict(color='red'))
layout = go.Layout(
    title='Интерактивный график функции y = log₃(x)',
    xaxis=dict(title='x'),
    yaxis=dict(title='y'),
    template='plotly_white'
)
fig = go.Figure(data=[trace], layout=layout)

# Сохранение и автоматическое открытие в браузере
pyo.plot(fig, filename='interactive_log3.html')
