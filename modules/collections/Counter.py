"""
Demonstrates the use of Counter

https://docs.python.org/3/library/collections.html#collections.Counter
"""
from collections import Counter

cnt = Counter(["red", "blue", "red", "green", "blue", "blue"])
print("string counter -> ", cnt)

cnt = Counter("sdadsdddsssaa")
print("most common (2) -> ", cnt.most_common(2))

cnt = Counter([1, 2, 3, 4, 5, 5, 5, 6, 6, 6, 6, 67, 77])  # Mode calculation?
print("integer counter -> ", cnt)

def counter():
    return Counter(a=4, b=2, c=0, d=-2)

c = counter()
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print("substract c - d -> ", c)

print("total of all counts -> ", sum(c.values()))

c = counter()
c.clear()
print("reset all counts -> ", c)

print("list unique elements -> ", list(counter()))

print("convert to set -> ", set(Counter(a=1, c=2, b=3, d=5)))  # Random order result

print("convert to a regular dict -> ", dict(counter()))

print("convert to a list of (elem, cnt) pairs -> ", counter().items())

n = 3
print("n least common elements -> ", counter().most_common()[:-n-1: -1])

c = counter()
print("remove zero and negative counts -> ", +c)