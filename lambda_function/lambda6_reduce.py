from functools import reduce
lst = [26, 67, 2, 1, 90, 34, 17]
cnt = 0
fl = reduce((lambda x,y: x+1 if y%2 == 0 else x), lst, 0)
print(fl)

# reduce document
# reduce(function, iterable[, initializer])
# Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable. If the optional initializer is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty. If initializer is not given and iterable contains only one item, the first item is returned.