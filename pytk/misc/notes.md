The notes here are intended to be a collection of snippets from miscellaneous topics.

# Notes

### ignoring warnings  
```python
import warnings
warnings.filterwarnings("ignore")
```

### easy logging customization
follow instructions mentioned in the file [logging.md](logging.md).

### increasing jupyter notebook width
  follow instructions mentioned in the [link](http://stackoverflow.com/questions/21971449/how-do-i-increase-the-cell-width-of-the-ipython-notebook-in-my-browser)

### cPickle dump
```python
import cPickle
with open("myfile.pkl", 'w') as f:
    cPickle.dump(x, f, protocol=cPickle.HIGHEST_PROTOCOL)
```

### pretty print
```python
from pprint import pprint
sample_dict = {
    'a':1,
    'b': {
      'ba': 2,
      'bb': 3
    }
}
pprint(sample_dict)
```

### List, Generator, Set, Dict Comprehensions
```python
a = [1,2,3]

# list comprehension
[i for i in a]

# generator comprehension  
(i for i in a)

# set comprehension
{i for i in a}

# dict comprehension
{i:i**2 for i in a}
```

### python interfaces
notes in the following [link](http://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python)

### returning multiple values in python (NamedTuple)
notes in the following [link](http://stackoverflow.com/questions/354883/how-do-you-return-multiple-values-in-python)

### file_name, filename, file conventions
notes in the following [link](http://english.stackexchange.com/questions/5366/which-is-correct-filename-file-name-or-filename)

## TODO
* command line arguments
