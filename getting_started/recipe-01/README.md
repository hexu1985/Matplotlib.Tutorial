### 初级绘制

这一节中，我们将从简到繁：先尝试用默认配置在同一张图上绘制正弦和余弦函数图像，然后逐步美化它。

第一步，是取得正弦函数和余弦函数的值：

```python
from pylab import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
```

X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。

你可以在 IPython 的交互模式下测试代码，也可以下载代码（下载链接就是这些示例图），然后执行：

```shell
$ python3 exercise_1.py
```

Matplotlib 的默认配置都允许用户自定义。
你可以调整大多数的默认配置：图片大小和分辨率（dpi）、线宽、颜色、风格、坐标轴、坐标轴以及网格的属性、文字与字体属性等。
不过，matplotlib 的默认配置在大多数情况下已经做得足够好，你可能只在很少的情况下才会想更改这些默认配置。

```python
import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.show()
```
