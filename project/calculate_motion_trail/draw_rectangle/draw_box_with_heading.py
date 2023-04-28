import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections

def rotz(xc, yc, xp, yp, rz):
    c11=np.cos(rz)
    c12=-np.sin(rz)
    c21=np.sin(rz)
    c22=np.cos(rz)
    xpp=(xp-xc)*c11+(yp-yc)*c12    #----relative to xc,yc
    ypp=(xp-xc)*c21+(yp-yc)*c22
    xg=xc+xpp            #----relative to xg,yg
    yg=yc+ypp
    return [xg,yg]

def create_box(x, y, width, height, color, rot_deg):
    left = x - width/2
    right = x + width/2
    top = y + height/2
    bottom = y - height/2
    Rz = np.radians(rot_deg)
    p_left_bottom = rotz(x, y, left, bottom, Rz)
    p_left_top = rotz(x, y, left, top, Rz)
    p_right_bottom = rotz(x, y, right, bottom, Rz)
    p_right_top = rotz(x, y, right, top, Rz)
    line1 = [p_left_bottom, p_left_top]
    line2 = [p_right_bottom, p_right_top]
    line3 = [p_left_bottom, p_right_bottom]
    line4 = [p_left_top, p_right_top]
    box = collections.LineCollection([line1, line2, line3, line4], color=[color]*4)
    return box


fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
box = create_box(x=4, y=4, width=2, height=4, color="green", rot_deg=0)
ax1.add_collection(box)
box = create_box(x=4, y=4, width=2, height=4, color="red", rot_deg=30)
ax1.add_collection(box)
ax1.set_aspect(1)
plt.xlim(0, 9)
plt.ylim(1, 7)
plt.show()


