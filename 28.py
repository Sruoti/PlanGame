#timeit模块

import timeit as t
print(dir(t))

print(t.__all__)
t1 = t.Timer()
print(t1.timeit())






