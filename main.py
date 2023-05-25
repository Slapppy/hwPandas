import csv
import matplotlib.pyplot as plt

# Загрузите данные
x = []
y = []
with open("/Users/maratahmetov/PycharmProjects/Math_stat/homework1/1/r4z2.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        x.append(float(row[0]))
        y.append(float(row[1]))

# Вычислить среднее значение x и y
n = len(x)
x_mean = sum(x) / n
y_mean = sum(y) / n

# Рассчитать наклон и точку пересечения линии регрессии
numerator = 0
denominator = 0
for i in range(n):
    numerator += (x[i] - x_mean) * (y[i] - y_mean)
    denominator += (x[i] - x_mean) ** 2
slope = numerator / denominator
intercept = y_mean - slope * x_mean

# Вычислите предсказанные значения y
y_pred = []
for i in range(n):
    y_pred.append(slope * x[i] + intercept)

# Рассчитать Среднеквадратическую ошибку и Коэффициент детерминации
sse = 0
sst = 0
for i in range(n):
    sse += (y[i] - y_pred[i]) ** 2
    sst += (y[i] - y_mean) ** 2
rmse = (sse / n) ** 0.5
r2 = 1 - sse / sst

# Распечатать результаты
print(f"Уравнение регресии: Y = {slope:.2f}X + {intercept:.2f}")
print("Коэффициент наклона:", slope)
print("Точка пересечения прямой с осью координат:", intercept)
print("Среднеквадратическая ошибка(RMSE):", rmse)
print("Коэффициент детерминации (R2) Value:", r2)

# Постройте данные и линию регрессии
plt.scatter(x, y, s=10)
plt.plot(x, y_pred, color='r')
plt.title('График рассеяния с линией регрессии среднеквадратичного значения')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Вычислить значение регрессии в заданной точке
x_new = 118
y_new = slope * x_new + intercept
print(f"Прогнозируемое значение Y для X = {x_new}:", y_new)