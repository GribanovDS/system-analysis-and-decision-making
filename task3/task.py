import pandas as pd
import numpy as np

def task(var)->float:
    matrix = np.array(var)

    # Получаем количество строк n
    n = matrix.shape[0]

    # Инициализируем переменную для хранения общей энтропии
    total_entropy = 0

    # Проходим по каждой строке матрицы
    for row in matrix:
        # Вычисляем вероятности исходов в строке
        probabilities = row / (n - 1)

        # Исключаем нулевые вероятности, чтобы избежать log(0)
        probabilities = probabilities[probabilities != 0]

        # Вычисляем энтропию строки
        entropy = -np.sum(probabilities * np.log2(probabilities))

        # Добавляем к общей энтропии
        total_entropy += entropy

    return total_entropy

# Считываем файл CSV
matrix = pd.read_csv('graph.csv', header=None)

# Вычисляем энтропию
entropy = task(matrix)
print(f'Общая энтропия графа: {entropy}')
