# Scripts
* Dictionary
```python
d = {
    'bool':True,
    'int': 2,
    'float': 10.2312
    'str': "hello_world",
    'obj': {
        '1': 1,
        'a': "a"
    }
}
```

* Python 3: to_str
```python
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode(‘utf-8’)
    else:
        value = bytes_or_str
      return value # Instance of str
```

* Python 3: to_bytes
```python
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode(‘utf-8’)
    else:
        value = bytes_or_str
    return value # Instance of bytes
```

* Python 2: to_str
```python
def to_str(unicode_or_str):
    if isinstance(unicode_or_str, unicode):
        value = unicode_or_str.encode(‘utf-8’)
    else:
        value = unicode_or_str
    return value # Instance of str
```

* Python 2: to_unicode
```python
def to_unicode(unicode_or_str):
    if isinstance(unicode_or_str, str):
        value = unicode_or_str.decode(‘utf-8’)
    else:
        value = unicode_or_str
    return value # Instance of unicode
```
