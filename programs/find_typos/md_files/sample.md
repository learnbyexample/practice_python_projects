# re introduction

In this chapter, you'll get an introduction of `re` module  
that is part of Python's standard library.

## re.search

Use `re.search` function to tesr if the the given regexp pattern  
matches the input string. Syntax is shown below:

>`re.search(pattern, string, flags=0)`

```python
>>> sentence = 'This is a sample string'
>>> bool(re.search(r'is.*am', sentence))
True
>>> bool(re.search(r'str$', sentence))
False
```

[My book](https://github.com/learnbyexample/py_regular_expressions)  
on Python regexp has more details.

