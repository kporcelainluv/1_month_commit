напиши ламбда функцию, которая переворачивает строку
```
from functools import reduce
numbers = [2, 3, 4, 5, 6]
print(reduce(lambda res, x: [x] + res, numbers, []))
```
