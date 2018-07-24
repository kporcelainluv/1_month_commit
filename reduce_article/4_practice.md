sum of factorials

```
from functools import reduce
from math import factorial
number = int(input())
k = reduce(lambda x,y: x+y, list(map(factorial, range(1, number+1))))
print(k)
```

Tests

1 1
2 3
3 9
4 33
5 153
6 873
7 5913
8 46233
9 409113
10 4037913
