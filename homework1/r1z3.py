import csv
import matplotlib.pyplot as plt
data = []

with open('/Users/maratahmetov/PycharmProjects/Math_stat/homework1/1/r1z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        data.append(float(row[0]))

data_sorted = sorted(data)
n = len(data)
ecdf = [i / n for i in range(1, n+1)]


plt.step(data_sorted, ecdf)
plt.xlabel('Значение')
plt.ylabel('Эмпирическая функция распределения')
plt.title('График эмпирической функции распределения')
plt.show()
