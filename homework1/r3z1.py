import csv

data = []

with open('/Users/maratahmetov/PycharmProjects/Math_stat/homework1/1/r3z1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        data.append(float(row[0]))

data_square = [x ** 2 for x in data]

n = len(data)
mean = sum(data) / n
teta = mean * 3

mean_square = sum(data_square) / n
variance = mean_square - mean

print(f'Значение оценки: {teta}')
