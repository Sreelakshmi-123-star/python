string=input('enter a word: ')
first_char=string[0]
new_char=first_char+string[1:].replace(first_char,'$')
print("the string is",new_char)