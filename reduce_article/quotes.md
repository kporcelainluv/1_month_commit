What documentation tells us:

```
Apply function of two arguments cumulatively to the items of iterable,
from left to right, so as to reduce the iterable to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).
The left argument, x, is the accumulated value and the right argument,
y, is the update value from the iterable. If the optional initializer is present,
it is placed before the items of the iterable in the calculation,
and serves as a default when the iterable is empty.
If initializer is not given and iterable contains only one item,
the first item is returned.

It accepts an iterator to process, but it's not an iterator itself. It returns a single result:

At each step, reduce passes the current product or division, along with the next item from the list, to the passed-in lambda function.
 By default, the first item in the sequence initialized the starting value.

```

```
At first the first two elements of seq will be applied to func, i.e. func(s1,s2)
The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
In the next step func will be applied on the previous result and the third element of the list,
i.e. func(func(s1, s2),s3)
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
Continue like this until just one element is left and return this element as the result of reduce()
```

```
The function reduce(func, seq) continually applies the function func() to the sequence seq.
It returns a single value.
```

## first example:
```
from functools import reduce
numbers = [2, 3, 4, 5, 6]
reduce(lambda res, x: res*x, numbers, 1)
what we get

(((((1*2)*3)*4)*5)*6)
```
## else
```
from functools import reduce
numbers = [2, 3, 4, 5, 6]
reduce(lambda res, x: res*x, numbers)
(((((2*3)*4)*5)*6)

```

if the list is empty, you can add additional parameter
(The built-in reduce also allows an optional third argument placed
before the items in the sequence to serve as a default result when the sequence is empty.)
```
print(reduce(lambda res, x: res*x, [], 1))
```

### max
```
Determining the maximum of a list of numerical values by using reduce:
f = lambda a,b: a if (a > b) else b
reduce(f, [47,11,42,102,13])
102

```

## sum
```
reduce(lambda x, y: x+y, range(1,101))
reduce(add, range(1, 11))
```

## concatenating
```
instead of ''.join(L) we could use:
L = ['Testing ', 'shows ', 'the ', 'presence', ', ','not ', 'the ', 'absence ', 'of ', 'bugs']
functools.reduce( (lambda x,y:x+y), L)
'Testing shows the presence, not the absence of bugs'
```
