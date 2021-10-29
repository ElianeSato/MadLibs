#! python3
# MadLibs.py lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears
# in the text file.
# Usage: the user should provide words that will replace those in the text.
# A text file will be generated and the text with the given words will be printed.

adjective = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
verb = input("Enter a verb: ")
noun2 = input("Enter a noun: ")
user = input("Enter your username: ")

text = f'The {adjective} panda walked to the {noun1} and then {verb}. ' \
       f'A nearby {noun2}\n' \
       f' was\n' \
       f' unaffected by these events.'

with open(f'{user}file.txt', 'w') as file:
    file.write(text)

with open(f'{user}file.txt') as file:
    print(file.read())
