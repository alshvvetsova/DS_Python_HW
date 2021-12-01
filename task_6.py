a = int(input("Vvedite km v 1 den: "))
b = int(input("Vvedite km itog: "))
day = 1
while a < b:
    a = a * 1.1
    day = day + 1
print ('Na ', day,'sportsmen dostig', b, 'km')