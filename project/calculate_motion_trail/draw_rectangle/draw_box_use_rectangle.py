import matplotlib.pyplot as plt

def create_box(x, y, width, height):
    rect = plt.Rectangle(
            (x-width/2, y-height/2),
            width,
            height,
            facecolor='none', 
            edgecolor='green',
            linewidth=1)
    return rect


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
box = create_box(x=2.5, y=4, width=3, height=4)
ax1.add_patch(box)
plt.xlim(-1, 6)
plt.ylim(1, 7)
plt.show()

