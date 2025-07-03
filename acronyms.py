
look_up = input("What software acronym would you like to look up?\n")

found = False
with open('acronums.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if not found:
    print('The acronym does not exist')
    