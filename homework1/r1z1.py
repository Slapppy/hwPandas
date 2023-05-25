import csv
import numpy as np

# считываем данные из файла csv
data = []
with open('/Users/maratahmetov/PycharmProjects/Math_stat/homework1/1/r1z1.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(float(row[0]))

# вычисляем статистические показатели
sample_size = len(data)
minimum = min(data)
maximum = max(data)
range = maximum - minimum
mean = sum(data) / sample_size
biased_variance = sum([(x - mean) ** 2 for x in data]) / sample_size  # смещенная дисперсия
unbiased_variance = sum([(x - mean) ** 2 for x in data]) / (sample_size - 1)  # несмещенная дисперсия
standard_deviation = biased_variance ** 0.5  # стандартное отклонение
skewness = sum([(x - mean) ** 3 for x in data]) / (sample_size * standard_deviation ** 3)  # асимметрию
median = sorted(data)[sample_size // 2]
print(np.median(data))
q1 = sorted(data)[:sample_size // 2][sample_size // 4]
q3 = sorted(data)[sample_size // 2:][sample_size // 4]

interquartile_range = q3 - q1  # интерквартильную широту

# выводим результаты
print('Размер:', sample_size)
print('Минимум:', minimum)
print('Максимум:', maximum)
print('Размах:', range)
print('Среднее арифметическое:', mean)
print('смещенная дисперсия:', biased_variance)
print('несмещенная дисперсия:', unbiased_variance)
print('стандартное отклонение:', standard_deviation)
print('Ассиметрия:', skewness)
print('Медиана:', median)
print('Интерквартильную широту:', interquartile_range)
