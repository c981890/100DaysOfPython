# collections.Counter lets you find the most common
# elements in an iterable:

import collections
c = collections.Counter('pastauniversum')

print(c)

print(c.most_common(2))
