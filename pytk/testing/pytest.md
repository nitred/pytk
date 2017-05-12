# How to use pytest

## To run all tests

```
cd <path_of_repository>
py.test -v -s
```

```
cd <path_of_repository>
pytest
```

## To run all tests with **coverage**

```
cd <path_of_repository>
py.test --cov-report term-missing  --cov=<package_name> tests/ -s -v
```


## To run individual tests

```
cd <path_of_repository>/tests
py.test -v -s test_file.py
```

```
cd <path_of_repository>/tests
pytest test_file.py
```

## To run individual tests with **coverage**

```
cd <path_of_repository>
py.test --cov-report term-missing  --cov=<package_name> test_file.py -s -v
```
