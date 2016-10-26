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
