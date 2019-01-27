# https://realpython.com/python-sets/

x = set(['foo', 'bar', 'baz', 'foo', 'qux'])
print(x)

x = set(('foo', 'bar', 'baz', 'foo', 'qux'))
print(x)

s = 'quux'
print(list(s))
print(set(s))

h = set(s)
print('Hulk:', h)

h = list(h)
print('Järjend:', h)

x = {'foo', 'bar', 'baz', 'foo', 'qux'}
print(x)

s = {'q', 'u', 'u', 'x'}
print(s)

print({'foo'})
print(set('foo'))

x = set()
print(type(x))

x = {}
print(type(x))

x = {'foo', 'bar', 'baz'}
print(len(x))
print('bar' in x)
print('qux' in x)

x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1 | x2)
print(x1.union(x2))

print(x1 & x2)
print(x1.intersection(x2))

print(x1 - x2)
print(x1.difference(x2))
