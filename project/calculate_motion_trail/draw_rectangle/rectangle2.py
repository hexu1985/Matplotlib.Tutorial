import matplotlib.pyplot as plt

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
rect=plt.Rectangle(
        (1, 2),  # (x,y)矩形左下角
        3,  # width长
        4,  # height宽
        facecolor='none', 
        edgecolor='green',
        linewidth=1)
ax1.add_patch(rect)
plt.xlim(-1, 6)
plt.ylim(1, 7)
plt.show()

