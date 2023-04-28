import matplotlib.pyplot as plt 
from matplotlib import collections

line_1 = [(1, 10), (6, 9)]
line_2 = [(1, 7), (3, 6)]

collection_1_2=collections.LineCollection([line_1, line_2], color=["red","green"])

fig,axes=plt.subplots(1,1)
axes.add_collection(collection_1_2)
axes.autoscale()
plt.show()
