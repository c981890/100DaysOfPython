from sys import argv
from string import Template

script, filename = argv
txt = open(filename)

templ_string = "Here's your $file:"
print(Template(templ_string).substitute(file=filename))

print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt.close()
