## Big-O Notation

1. Count the number of assignment statements plus the value of `n` denote this by a function `T` where `T(n)` = 1+n the paramter n is referred to as the size of the problem and is read as `T(n) is the time it takes to solve a problem of size N, 1+n steps`

2. Order of magnitude - Part of `T(n)` that increases the fastest as the value of N increases. The order of magnitude is often called Big-O written as `O(f(n))`

### Most Common Big-O Notations
* `1` - constant
* `log n` - logarithmic
* `n` - linear
* `n log n` - log linear
* `n^2` - Quadratic
* `n^3` - Cubic
* `2ª` - Exponential

###Example
```python
a = 5
b = 6
c = 10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * i
        z = i * j
    for k in range(n):
        w = a * k + 45
        v = b * b
    d = 33
```
The number of assignment operations is the sum of 4 terms
1. 3 constant, which are the three assignment statements
2. 3n^2 there are 3 statements that are performed n^2 times due to nested iteration 
3. 2n two statements iterated n times
4. 1 constant, the final assignment statements
`T(n) = 3 + 3n^2 + 2n + 1 = 3n^2 + 2n + 4.`
n^2 will be dominant therefore the example code is O(n^2)(Quadratic)

### Big-O efficiency of List Operators
* indexx[]            - O(1)
* index assignment    - O(1)
* append              - O(1)
* pop()               - O(1)
* pop(i)              - O(n)
* insert(i, item)     - O(n)
* del operator        - O(n)
* iteration           - O(n)
* contains (in)       - O(n)
* get slice[x:y]      - O(k)
* del slice           - O(n)
* set slice           - O(n+k)
* reverse             - O(n)
* concatenate         - O(k)
* sort                - O(n log n)
* multiply            - O(nk)

### Big-O Efficiency of Python Dictionary Operations
* copy                - O(n)
* get item            - O(1)
* set item            - O(1)
* delete item         - O(1)
* contains (in)       - O(1)
* iteration           - O(n)

