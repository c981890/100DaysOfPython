s = "foo"
print(s in "That\'s food for thought.")
print(s in "that\'s good for now.")

print("z" not in "abc")
print("z" not in "xyz")

print(ord("a"))
print(ord("#"))
print(ord("€"))
print(ord("∑"))

print(chr(97))
print(chr(35))
print(chr(8364))
print(chr(8721))

s = "foobar"

s = s[:3] + 'x' + s[4:]
print(s)

s = "foobar"
s = s.replace('b', 'x')
print(s)

print("FOO Bar 123 baz qUX".swapcase())

print("the sun also rises".title())

print("foo goo moo".count('oo', 0, 3))

print('foobar'.endswith('bar'))
print('foobar'.endswith('far'))

print('foo bar foo baz foo qux'.find('foo', 4))
