import csv

from matplotlib import pyplot as plt

with open('/Users/maratahmetov/PycharmProjects/Math_stat/homework1/1/r4z2.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    data = [(float(row[0]), float(row[1])) for row in reader]

n = len(data)

# Вычисление среднего значения
mean_x = sum([x for x, y in data]) / n
mean_y = sum([y for x, y in data]) / n

#
biased_variance_x = sum([(x - mean_x) ** 2 for x, y in data]) / n
standard_deviation_x = biased_variance_x ** 0.5

biased_variance_y = sum([(y - mean_y)**  2 for x, y in data]) / n
standard_deviation_y = biased_variance_y ** 0.5

# Выборочный коэф кореляции
r = sum([(x - mean_x) * (y - mean_y) for x, y in data]) / (n * standard_deviation_x * standard_deviation_y)
print(r)
# Коэф регрессии

b_yx = r * standard_deviation_y / standard_deviation_x

x_1 = 105
y_1 = mean_y + b_yx * (x_1 - mean_x)
x_2 = 130
y_2 = mean_y + b_yx * (x_2 - mean_x)

X = 118
Y = mean_y + b_yx * (X - mean_x)
print(Y)
list_x = [x_1,x_2]
list_y = [y_1, y_2]


# Построение графика рассеяния данных и линии регрессии
plt.scatter([x for x, y in data], [y for x, y in data], color='blue', label='Данные')
plt.plot(list_x, list_y, color='red', label='Регрессия')
plt.plot(x_1, y_1, 'o', color='black')
plt.plot(x_2, y_2, 'o', color='black')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()