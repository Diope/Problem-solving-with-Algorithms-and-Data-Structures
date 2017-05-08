# Recursion

Recursion is a method of solving problems that involves breaking a problem down into smaller and smaller subproblems until you get to a small enough problem that it can be solved trivially. Most forms of recursion involves a function calling itself.

Example of how recursion makes things simpler.

Finding the sum of numbers iteratively
```python
def list_sum(num_list):
    the_sum = 0
    for i in num_list:
        the_sum += i
    return the_sum
```

Recursive method
```python
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])
```

## The Three Laws of Recursion
1. A recursive algorithm must have a base case - A base case is the condition that allows the algorithm to stop recursing. A base case is typically a problem that is small enough to solve directly. In the list_sum algorithm the base case is a list of length 1

2. A recursive algorithm must change its state and move towards the base case. - A change of state means that some data that the algorithm is using is modified.

3. A recursive algorthim must call itself...recursively.

