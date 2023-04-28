import matplotlib.pyplot as plt 
from matplotlib import collections

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

line_1 = [(1, 10), (6, 9)]
line_2 = [(1, 7), (3, 6)]

collection_1_2=collections.LineCollection([line_1, line_2], color=["red","green"])

ax1.add_collection(collection_1_2)
ax1.autoscale()
plt.show()

