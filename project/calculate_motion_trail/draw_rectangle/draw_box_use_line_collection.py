import matplotlib.pyplot as plt
from matplotlib import collections

def create_box(x, y, width, height):
    left = x - width/2
    right = x + width/2
    top = y + height/2
    bottom = y - height/2
    line1 = [(left, bottom), (left, top)]
    line2 = [(right, bottom), (right, top)]
    line3 = [(left, bottom), (right, bottom)]
    line4 = [(left, top), (right, top)]
    box = collections.LineCollection([line1, line2, line3, line4], color=["green"]*4)
    return box


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
box = create_box(x=2.5, y=4, width=3, height=4)
ax1.add_collection(box)
plt.xlim(-1, 6)
plt.ylim(1, 7)
plt.show()

