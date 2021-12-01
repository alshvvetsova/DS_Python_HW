chislo = int(input('Vvedite celoe polozhitelnoe chislo: '))
dop = 0
while chislo > 0:
    if chislo % 10 > dop:
        dop = chislo % 10
        if dop == 9:
            break
    chislo = chislo//10

print ('Naibolshchee chislo = ', dop)