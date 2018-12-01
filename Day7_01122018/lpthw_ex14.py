from sys import argv
from string import Template

script, user_name = argv
prompt = '>>>'

temp_string = """
Hi $user_name, I'm the $script script.
I'd like to ask you a few questions.
Do you like me $user_name?
"""

print(Template(temp_string).substitute(user_name=user_name, script=script))
likes = input(prompt)

print("Where do you live?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

temp_string = """
Alright, so you said "$likes" about liking me.
You live in $lives. Not sure where that is.
And you have a $computer. Nice.
"""
print(Template(temp_string).substitute(
likes=likes,
lives=lives,
computer=computer,
))

# temp_string = "Hey $name, there is $errror error!"
# Template(temp_string).substitute(name=name, error=errno)
