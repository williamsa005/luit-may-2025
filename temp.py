acronym = input('What acronym do you want to add?')
definition = input('What is the definition?\n')
with open('acronyms.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')