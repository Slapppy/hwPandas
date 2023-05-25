import csv
import matplotlib.pyplot as plt
import pandas

data = pandas.read_csv('/Users/maratahmetov/PycharmProjects/Math_stat/homework1/1/r4z2.csv',sep =',' )


x = data['X'].tolist()
y = data['Y'].tolist()
n = len(x)

x_mean = sum(x) / n
y_mean = sum(y) / n
xy_sum = sum([x[i] * y[i] for i in range(n)])
x_squared_sum = sum([x[i] ** 2 for i in range(n)])


a = (n * xy_sum - sum(x) * sum(y)) / (n * x_squared_sum - sum(x) ** 2)
b = y_mean - a * x_mean



plt.scatter(x, y)
plt.plot(x, [a * xi + b for xi in x])
plt.show()

'0.44 * x + 26.7'

x_0 = 2.5
y_0 = a * x_0 + b
print("Значение регрессии в точке x = {}: y = {}".format(x_0, y_0))
