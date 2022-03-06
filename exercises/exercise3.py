# CAC-102-3 Exercise 3 - Strings
# On page 25 of your book, In the Try it Yourself section do the following tasks.
# Put all your code in your exercise3.py file.
# 2-3 Personal Message
first_name = "monty, "
msg1 = f"Hello {first_name.title()} please check my messy code."
print(msg1)

# 2-4 Name Cases
name = "tim donnelley"
print(name.lower())
print(name.upper())
print(name.title())

# 2-5 Famous Quotes
message1 = 'Coach Karbo once said, "You only get out what you put in."'
print(message1)


# 2-6 Famous Quotes 2
famous_person = "-elon musk"
message2 = '"I think it matters whether someone has a good heart."'
combine = message2 + " " + famous_person.title()
print(combine)


# 2-7 Stripping Names
name = '    tim\tdonnelley '
print(name.title())
name2 = '    tim\ndonnelley '
name2 = name2.rstrip()
print(name2)
name3 = 'Tim Donnelley  '
name3.lstrip()
print(name3)
name4 = '  tim\tdonnelley '
print(name4.upper())
name4 = name4.title()



