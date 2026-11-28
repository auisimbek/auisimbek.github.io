summa = 0
print("Вводите числа. Чтобы закончить, введите 0. ")

while True:
    chislo = int(input("Введите число: "))
    if chislo == 0: 
        break 
    summa = summa + chislo 

print ("Сумма:", summa)