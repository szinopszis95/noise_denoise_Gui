import csv
import numpy as np
import matplotlib.pyplot as plt

with open('valami.csv', 'r', encoding='utf-8-sig') as f:
    data = np.transpose(np.genfromtxt(f, delimiter=';'))
    print(np.max(data[0]))

plt.hist(data[0], weights=data[1], bins=256)
plt.xlim(np.min(data[0]), np.max(data[0]))
plt.show()