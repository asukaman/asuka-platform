import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # ファイル

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')
# グラフにフォーマットを指定する。
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
