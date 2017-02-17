### Notes

1. jupyter notebook matplotlib integration  
```python
%matplotlib notebook
```

1. When the xticklabels are clipped on the plot. We have to extend the space given to the bottom of the plot.  
```python
from matplotlib import pyplot as plt
plt.gcf().subplots_adjust(bottom=0.45)
```

1. To manually adjust the size of the figure of the plot.  
```python
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = 10,10
```

1. pandas set display  
```python
import pandas as pd
pd.set_option('display.mpl_style', 'default')
```

1. matplotlib without needing x-server (eg: docker)
```python
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('TKAgg')  # 'Agg' or 'GTKgg' or 'TKAgg'
# import pyplot
from matplotlib import pyplot
```

1. Geometric Brownian Motion
```python
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
def geometric_brownian_motion(T = 1, N = 100, mu = 0.1, sigma = 0.01, S0 = 20):        
    dt = float(T)/N
    t = np.linspace(0, T, N)
    W = np.random.standard_normal(size = N)
    W = np.cumsum(W)*np.sqrt(dt) ### standard brownian motion ###
    X = (mu-0.5*sigma**2)*t + sigma*W
    S = S0*np.exp(X) ### geometric brownian motion ###
    return S

dates = pd.date_range('2012-01-01', '2013-02-22')
T = (dates.max()-dates.min()).days / 365
N = dates.size
start_price = 100
y = pd.Series(
    geometric_brownian_motion(T, N, sigma=0.1, S0=start_price), index=dates)
y.plot()
plt.show()
```

1. Realtime plot
```python
plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)

while True:
    plt.pause(0.05)
```

1. Figures and Axes
```python
figure, axes = plt.subplots(2, 1)
top, bot = axes
top.hist(np.random.rand(1000), 20) # uniform
bot.hist(np.random.normal(0, 1, 1000), 20) # normal
plt.show()
```
