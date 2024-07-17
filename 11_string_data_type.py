msg = 'my name is "smile"'

msg = 'my name is \'smile\''

msg = 'my name is \\smile\\'

msg = "Hello. \nmy name is more"

msg = "hey man"
msg = "hey" + " " + "man"
# print(msg)

print("\n---------------- concept f-string")

name = "mor"
family = "Teza"
nick_name = "more"
# print(f"{name}{family}")
# print(f"My nick name is {nick_name}")

text = "my name is {} {}"
# print(text.format(name, family))

text_2 = "my name is {a} {b}"
# print(text_2.format(a = name, b = family))


print("\n---------------- concept index")

text_3 = "you are awesome"
#      = "012 456 89 10 11 12 13 14"
# print(text_3[9])
# print(text_3[8:15])
# print(text_3[-1])


print("\n---------------- concept slicing index")

description = """
hello, how are you?
my name is more
"""
# print(description)
# print(description[1:10])
# print(description[1:]) # look like print(description)
# print(description[:])
# print(description[-5:])

print("\n---------------- concept methods in string variable")

res = description.count("a")
res = description.find("o")

res = description.upper()
res = description.lower()

res = description.replace(",", "!")

res = description.title()

res = description.isupper()
res = description.islower()
res = description.isnumeric()
res = description.istitle()
res = description.strip() # like trim in php

res = description.split(" ")

res = description.capitalize() # just first chararcter to upper



print(res)
