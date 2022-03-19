import pandas as pd

data = pd.read_csv("A11x34.csv", header = None).values
print(data.shape)
# print(data)
type(data)

import numpy as np
answer = np.zeros(shape = (34, 12, 60))
#answer is from 6:30-7:29, 7:30-8:29, .., , 17:30-18:29
for date in range(34):
  for i in range(12):
    for j in range(60):
      if i!=11:
        answer[date][i][j] = (data[i][date]*(60-j)+data[i+1][date]*j)/60
      else:
        answer[date][i][j] = data[i][date]*(60-j)/60
answer[5][11][:]

answer = np.reshape(answer, newshape = (34, 720))
answer = answer[:, 30:-30]
# answer = np.reshape(answer, (34, 11, 60))
import csv
with open("A_sun.csv", 'w') as csvfile:
  writer = csv.writer(csvfile)
  # print(type(results))
  for i in answer:
    writer.writerow(i)

sun_data = pd.read_csv("A_out.csv", header = None).values

import matplotlib.pyplot as plt
date = 31
# idx = [14, 15, 16, 17, 20, 21, 25, 26, 30, 31, 32, 33]
idx = range(34)
sun_data = sun_data[idx, :]
answer = answer[idx, :]
data1 = np.reshape(sun_data, len(idx)*660)
data2 = np.reshape(answer, len(idx)*660)
plt.scatter(data1, data2)
print(np.corrcoef(np.concatenate(([data1], [data2]), axis = 0)))