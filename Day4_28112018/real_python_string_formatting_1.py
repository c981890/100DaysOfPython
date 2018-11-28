# https://realpython.com/python-string-formatting/

errno = 50159747054
name = 'Ülo'
question = 'läheb'

print("String Formatting")
print("Tere {nimi}, köögis on 0x{veanumber:x} viga!".format(nimi=name,
    veanumber=errno))
print("Tere {}, köögis on 0x{} viga!".format(name, errno))

print("f-String")
def greet(name, question):
    print(f"Hello, {name}! Kuidas {question}?")

greet('Ülo', 'läheb')
print(f"Tere {name}, köögis on 0x{errno:x} viga!")

print("Teplate Strings")
from string import Template
t = Template("Tere, $name!")
t.substitute(name=name)

templ_string = "Tere $name, köögis on $error viga!"
print(Template(templ_string).substitute(name=name, error=hex(errno)))
