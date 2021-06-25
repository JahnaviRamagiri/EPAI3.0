## Session 7 - Assignment

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
2. Write a closure that gives you the next Fibonacci number - 100
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250

```python
def add(a: int,b: int):
  """
  a: input 1
  b: input 2
  Adds a and b
  """
  return a+b


def mul(a: int,b: int):
  """
  a: input 1
  b: input 2
  multiplies a and b
  """
  return a*b


def div(a: int,b: int):
  """
  a: input 1
  b: input 2
  divides a by b
  """
  return a/b
```

```python
def closure_fib():
  """
  returns next fibonacci number in the series using closure
  """
  fib = [0,1]
  print(fib[0],'\n'+str(fib[1]))
  def fibo():
    nonlocal fib
    fib.append(fib[-1] + fib [-2])
    return fib[-1]
  return fibo
```

```python
def doc_check(fn):
  """closure that takes a function and then check whether the function passed has a docstring with more than 50 characters.
   50 is stored as a free variable
   fn: input function whose docstring length is calculated"""
  var = 50
  def doc(fn):
    nonlocal var
    if fn.__doc__ == None:
      raise ValueError ("No Docstring")
    elif (len(fn.__doc__)>var):
      return True
    else:
      return False
  return doc(fn)
```
```python

def closure_func_counter():
  """
  Closure to keep a track of how many times add/mul/div functions were called,
  and update a global dictionary variable with the counts
  """
  global dict_count
  dict_count = {}
  func_count = {'add':0, 'mul':0,'div':0}

  def func_counter(fn):
    nonlocal func_count
    func_count[fn.__name__] +=1
    dict_count[fn.__name__] = func_count[fn.__name__]
    return dict_count
  return func_counter
```



```python
def closure_func_counter2():
  """
  Modification of above function such that now we can pass in different dictionary variables to update different
  dictionaries
  """
  func_count2 = {'add':0, 'mul':0,'div':0}

  def func_counter(fn, dict_count: dict):
    nonlocal func_count2
    #print(func_count2,dict_count)
    func_count2[fn.__name__] +=1
    dict_count[fn.__name__] = func_count2[fn.__name__]
    return dict_count
  return func_counter
```