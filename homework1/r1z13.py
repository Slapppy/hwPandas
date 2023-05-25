import csv
import matplotlib.pyplot as plt

# Считываем данные
data = []
with open('/Users/maratahmetov/PycharmProjects/Math_stat/homework1/1/r1z1.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(float(row[0]))

# Сортируем данные
data_sorted = sorted(data)

# Вычисляем эмпирическую функцию распределения
n = len(data_sorted)
ecdf_x = []
ecdf_y = []
for i in range(n):
    ecdf_x.append(data_sorted[i])
    ecdf_y.append((i+1)/n)

# Строим график
plt.plot(ecdf_x, ecdf_y)
plt.xlabel('Значение')
plt.ylabel('Эмпирическая функция распределения')
plt.title('Эмпирическая функция распределения')
plt.show()
