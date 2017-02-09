# Notes

1. pandas timezone localization (timezone aware)
```python
df.tz_localize('UTC', level=0)
```

1. pandas rename column
```python
df = df.rename(columns={'old_name': 'new_name'})
```

1. replace subset of dataframe based on condition
```python
df.loc[df.var==-999999] = 0   # replace subset
# this is done inplace but make sure it works first
```

1. basic numerical statistics of a column
```python
df.column_name.describe()
```

1. Convert `COV` df to `Flat` df
```python
df.pivot_table()  # Lookup documentation.
```

1. Timeseries Offset Objects and Offset Strings
[Offset Objects](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#dateoffset-objects)  
[Offset Strings](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries-offset-aliases)

### Split dataframe / index into chunks
1. split dataframe into chunks of fixed size
```python
# choose chunk_size, and chunk is of type pd.Dataframe
for chunk_index, chunk in df.groupby(np.arange(len(df)) // chunk_size):
    print(chunk_index, chunk)
```

1. split TimeIndex into chunk
```python
ts_periods = 100
chunk_periods = 10
ts = pd.DatetimeIndex(periods=ts_periods, start='01.01.1990', end=None, freq='1D')
for chunk_index, chunk in ts.groupby(np.arange(ts_periods) // chunk_periods).iteritems():
    print(chunk_index, chunk)
```

1. Group by time [Timegrouper](http://stackoverflow.com/questions/26646191/pandas-groupby-month-and-year)
```python
df = pd.DataFrame(data=np.zeros(10), index=pd.DatetimeIndex(periods=10, start='01.01.1990', end=None, freq='1D'))
chunks_df = groupby(pd.TimeGrouper("2D")).sum()
# `chunks_df` index will now contain the start of every
```

## Cumulative + Consecutive
1. Assign unique groups to consecutive numbers and get count of consecutive number
```python
df = pd.DataFrame(data=(np.array(range(10)*2) // 3), columns=['val'])
# [0 0 0 1 1 1 2 2 2 3 0 0 0 1 1 1 2 2 2 3]

df['val_grp'] = (df['val'].diff() != 0).astype(int).cumsum()
# [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8]

df.groupby('val_grp').count()
# [3, 3, 3, 1, 3, 3, 3, 1]
```
