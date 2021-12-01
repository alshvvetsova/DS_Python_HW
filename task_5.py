viruchka = float(input('Vvedite znachenie viruchku: '))
izderzhki = float(input('Vvedite znachenie izderzhki: '))

if izderzhki>viruchka:
    print ("Finansoviy rezultat - ubitok")
elif izderzhki<viruchka:
    pribil = viruchka - izderzhki
    rent = pribil / viruchka
    sotrudnuki = (int(input(" Vvedite kol-vo sotrudnikov: ")))
    na_1= pribil/sotrudnuki
    print ('Finansoviy rezultat - pribil = ',pribil, ' na kazhdogo sotrudnika = ',na_1, 'rentabelnost = ', rent )

else:
    print ('viruchka = izderzhki')

