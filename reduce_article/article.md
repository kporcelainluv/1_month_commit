How many times have you tried but in the end never applied reduce? I hope
my article will help you to understand it better and apply it to places
you never thought reduce is suitable for.


## What is reduce?
Function reduce continually applies the function func() to the iterable parameter.
In the end it returns a single value. We may think of it as of recursion.

## Example
Lets take an example here:
```
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
reduce(lambda result, x: res*x, numbers)
```
The left argument, result, represents the accumulated value, basically
where we store passing result and the value we return at the end.
The right argument, x, is the update value from the iterable.


## So what arguments it takes?

It takes the first two elements of the list and calculates func(A,B).
Then it requests next element C and calculates func(func(A, B), C).
And continues until the iterable is exhausted.

At each step, reduce passes the current product or division, along with
the next item from the list, to the passed-in lambda function.
What we get is

```
(((((1*2)*3)*4)*5)*6)
```


## Third argument
```
numbers = [1, 2, 3, 4, 5, 6]
reduce(lambda result, x: result*x, numbers, 1)
```

```
(((((1*2)*3)*4)*5)*6)
```

Third argument - 1 - is the initial value, starting point.
1 is the first calculation.

## We pass not an iterable

If the iterable returns no values at all,
a TypeError exception is raised.

## Let's take a look at examples now

### Copy a list
```
from functools import reduce
list_of_vals = [1,2,3,4,5]
new_list_copy = list(reduce(lambda xs, x: xs+ x, [], list_of))
print(new_list_copy)
```
if you won't use list in new_list_copy, it will link to already
existing list_of_vals in memory

### max
```
from functools import reduce
f = lambda a,b: a if (a > b) else b
max_num = reduce(f, [47,11,42,102,13])

```

### sum
```
from functools import reduce
sum = reduce(lambda x, y: x+y, range(1,101))
```

### concatenating
```
from functools import reduce
phrases = ['Floating-point', 'calculations', 'are', 'innacure','because', 'of', 'how', 'the', 'underlying', 'platform', 'handles', 'floating-point']
sentense = reduce(lambda x, y: x+" "+y, phrases)

```

### unpack list of lists
```
from functools import reduce
list_of = [[1, 2, 3], [4, 5], [6, 7, 8]]
d = reduce(lambda x,y: x+y, list_of, [])
print(d)
```

### get rid of join method, although it takes more time

```
from functools import reduce
list_of = [1, 2, 3, 4, 5, 6, 7, 8]
d = reduce(lambda a,d: str(a)+str(d), [1,2,3,4,5,6,7,8])
print(d)
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

