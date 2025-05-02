# Визуализация функций с использованием Python

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

## 📝 Описание
Проект предназначен для новичков, изучающих Python с целью научится визуализировать математические функции с использованием профессиональных инструментов программирования и различных Python-библиотек. Поддерживает создание как статических, так и интерактивных графиков.

## ✨ Возможности
- Построение статических графиков с помощью Matplotlib
- Создание интерактивных визуализаций через Plotly
- Работа в Jupyter Notebook/Lab
- Поддержка различных математических функций

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.6+
- Git

### Установка

1. Клонируйте репозиторий:
```bash
mkdir ~/git/matvey_mgri
cd ~/git/matvey_mgri
```

2. Создайте и активируйте виртуальное окружение:
```bash
python3 -m venv venv_mgri
source venv_mgri/bin/activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## 📦 Зависимости

| Библиотека  | Назначение |
|-------------|------------|
| **Matplotlib** | Комплексная библиотека для создания статических и анимированных графиков. Применяется для построения визуализаций. |
| **NumPy** | Библиотека для работы с массивами, векторами и математическими функциями. |
| **Pandas** | Упрощает работу с табличными данными. Используется в основном в аналитике. |
| **SymPy** | Библиотека символьной математики. Подходит для логарифмов и алгебраических выражений. |
| **Plotly** | Интерактивные графики. Можно экспортировать в HTML. |
| **IPython** | Улучшенная оболочка Python с поддержкой интерактивного режима. |
| **OpenPyXL** | Работа с Excel (.xlsx). Не используется в этом задании, но полезна при отчётности. |
| **Seaborn** | Статистическая визуализация на базе Matplotlib. Необязательна, но может быть использована позже. |
| **JupyterLab** | Интерактивная среда для запуска блокнотов Jupyter. Позволяет работать с кодом и графикой через браузер. |

## 💻 Использование

### Вариант 1: Статический график (Matplotlib)
```python
import numpy as np
import matplotlib.pyplot as plt

# Задаём диапазон значений x от -5 до 15 с шагом 1.4
x_values = np.arange(-5, 15, 1.4)

# Вычисляем значения y = log base 3 (x), исключая некорректные x ≤ 0
x_valid = x_values[x_values > 0]
y_values = np.log(x_valid) / np.log(3)  # логарифм по основанию 3

# Строим график
plt.plot(x_valid, y_values, color='red', label='y = log₃(x)')
plt.title('График функции y = log₃(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# Сохраняем результат в файл
plt.savefig("graph_log3.png")
```

### Вариант 2: Интерактивный график (Plotly)
```python
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
```

### Вариант 3: Jupyter Notebook

1. Запустите сервер:

```bash
jupyter notebook
```

Или с JupyterLab:

```bash
jupyter lab
```

2. Перейдите по адресу `http://localhost:8888` и создайте новый файл.
3. Введите код, выполните ячейки.
4. Для запуска ячейки нажмите `Shift + Enter`.
5. Для копирования/вставки кода нажимайте правую кнопку мыши по ячейке или используйте `Ctrl+C` / `Ctrl+V`.

## ⚙️ Настройка

### Настройка алиасов
Для удобства работы добавьте следующие алиасы в ваш `~/.bashrc`:

```bash
nano ~/.bashrc
```

Добавьте в конец файла:

```bash
alias activate_mgri='source ~/git/matvey_mgri/venv_mgri/bin/activate'
alias deactivate_mgri='deactivate && echo "Окружение venv_mgri отключено."'
```

Примените изменения:

```bash
source ~/.bashrc
```

## 🎨 Кастомизация
### Тёмная тема JupyterLab

Для установки темы:

```bash
pip install jupyterthemes
jt -t monokai -T -N -kl
```

Перезапустите `jupyter lab` после установки.

## 🤝 Вклад в проект
Мы приветствуем ваш вклад в проект! Пожалуйста, ознакомьтесь с нашими правилами для контрибьюторов.

## 📝 Лицензия
Этот проект распространяется под лицензией MIT. Подробности смотрите в файле [LICENSE](LICENSE).

Лицензия MIT - это разрешительная лицензия, которая позволяет:
- ✅ Использовать код в коммерческих целях
- ✅ Модифицировать код
- ✅ Распространять код
- ✅ Использовать код в частных целях
При условии сохранения текста лицензии и указания авторских прав.

## 👥 Авторы
- Золотенков Матвей Викторович - [GitHub](https://github.com/MatVikZol)

## 📞 Поддержка
Если у вас возникли вопросы или проблемы, пожалуйста:
1. Проверьте раздел с известными проблемами
2. Создайте Issue в репозитории
3. Свяжитесь с автором
