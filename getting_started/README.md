## 初级绘制

这一节中，我们将从简到繁：先尝试用默认配置在同一张图上绘制正弦和余弦函数图像，然后逐步美化它。

第一步，是取得正弦函数和余弦函数的值：

```python
from pylab import *

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
```

X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。
然后执行：

```shell
$ python3 exercise_x.py
```

- [1. 使用默认配置](recipe-01/README.md)
- [2. 绘图配置概览](recipe-02/README.md)
- [3. 改变线条的颜色和粗细](recipe-03/README.md)
- [4. 设置绘图区域](recipe-04/README.md)
- [5. 设置刻度标记](recipe-05/README.md)
- [6. 设置刻度标记的标签](recipe-06/README.md)
- [7. 移动脊柱](recipe-07/README.md)
- [8. 添加图例](recipe-08/README.md)
- [9. 给一些特殊点做注释](recipe-09/README.md)
- [10. 精益求精](recipe-10/README.md)

