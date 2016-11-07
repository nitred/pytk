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

1. split dataframe into chunks of fixed size
```python
# choose chunk_size, and chunk is of type pd.Dataframe
for chunk_index, chunk in df.groupby(np.arange(len(df)) // chunk_size):
    print chunk_index, chunk
```
