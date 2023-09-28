import pandas as pd
import numpy as np

def task(graph):
    # Создание матрицы с нулевыми значениями
    matrix = np.zeros((graph['child'].max(), 5), dtype=int)

    for i in range(1, graph['child'].max() + 1):
        node = i
        children = graph[graph['parent'] == node]['child'].count()
        parents = graph[graph['child'] == node]['parent'].count()
        grandchildren = graph[graph['parent'].isin(graph[graph['parent'] == node]['child'])]['child'].count()
        grandparents = graph[graph['child'].isin(graph[graph['child'] == node]['parent'])]['parent'].count()
        podchinenie = graph[graph['parent'].isin(graph[graph['child'] == node]['parent'])]['child'].count()
        
        if podchinenie != 0:
            podchinenie -= 1

        # Запись в матрицу
        matrix[node - 1] = [children, parents, grandchildren, grandparents, podchinenie]

    return matrix

# Считывание CSV-файла и создание DataFrame
df = pd.read_csv('graph.csv', sep=',')
df.columns = ['parent', 'child']

# Вызов функции task и получение матрицы
result_matrix = task(df)

# Вывод матрицы
print(result_matrix)
