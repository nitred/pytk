# Basic Scripts For Reuse
### Basic Dataframe with Time index
```python
import pandas as pd
import numpy as np
_data = np.arange(20).reshape(10, 2)
_index = pd.DatetimeIndex(start='1990.11.10', freq='1D', periods=10)
df = pd.DataFrame(_data, index=_index)
df.columns = ['a', 'b']
```
