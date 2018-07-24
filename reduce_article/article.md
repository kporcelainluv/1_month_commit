# Problem
1. You need to shorten your code and make operation on an iterable object (list etc)
2. You want to apply a function to all iterables on the list and return a single result
3. ???


## Example

```
from functools import reduce
numbers = [2, 3, 4, 5, 6]
reduce(lambda result, x: result*x, numbers)
```

"result" is the accumulated value, basically
where we store passing result and the value we return at the end;

"x" is the next value from the list;

### How does it work?

```
((((2*3)*4)*5)*6)
>>>> 720
```

```
enter a video here
```

### Third argument
Third argument - 1 - is the starting point.

```
numbers = [2, 3, 4, 5, 6]
reduce(lambda result, x: result*x, numbers, 1)
```

```
(((((1*2)*3)*4)*5)*6)
>>>> 720
```


## Quick and cool examples

### copy list
```
from functools import reduce
numbers = [2, 3, 4, 5, 6]
result = reduce(lambda res, x: res + [x], numbers, [])

```

### max (min)
```
from functools import reduce
finding_max = lambda a,b: a if (a > b) else b
max_num = reduce(finding_max, [55, 34, 414, 48, 18])

```

### sum
```
from functools import reduce
sum = reduce(lambda x, y: x+y, range(1,101))
```

### concatenating
```
from functools import reduce
phrases = ['Floating-point', 'calculations','in', 'python', 'are', 'innacure']
sentense = reduce(lambda x, y: x+" "+y, phrases)

```

### unpack list of lists
```
from functools import reduce
list_of_vals = [[1, 2, 3], [4, 5], [6, 7, 8]]
result = reduce(lambda x,y: x+y, list_of_vals, [])
```

### get rid of join method, although it takes more time

```
from functools import reduce
list_of_vals = [1, 2, 3, 4, 5, 6, 7, 8]
result = reduce(lambda a,d: str(a)+str(d), list_of_vals)
```

### replacing JSON path (found on stackoverflow)

```
You could replace value = json_obj['a']['b']['c']['d']['e'] with:

value = reduce(dict.__getitem__, 'abcde', json_obj)
```

### union and intersection of a set (found on stackoverflow)
```
>>> reduce(operator.or_, ({1}, {1, 2}, {1, 3}))  # union
{1, 2, 3}
>>> reduce(operator.and_, ({1}, {1, 2}, {1, 3}))  # intersection
{1}
```

