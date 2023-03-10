# Introduction

stabledefaults is a small package containing a decorator to allow for the expected behavior of lists, dicts and other mutable arguments in default arguments.

## Explanation

In Python, functions (as anything else) are objects, and the default arguments are stored as attributes that are initialized in definition.

Once this is known and the person understands that variables are references in Python, then it is relatively straightforward to understand the following behavior:

```python
def f(x=[]):
    x.append(2)
    return x
```

```python
>>> a = f()
>>> a
[2]
>>> f()
>>> a
[2, 2]
```

Nevertheless, this is unintuitive. Not only that, but dealing with this requires things such as
```python
def f(x = None):
    if x is None:
        x = []

    x.append(2)
    return x
```
which forces types such as ```list | None``` where just ```list``` should suffice, and also forces code inside the function itself.

This package solves this issue with a decorator. For instance, the example above would become
```python
@stabledefaults()
def f(x=[]):
    x.append(2)
    return x
```
```python
>>> a = f()
>>> a
[2]
>>> f()
>>> a
[2]
```