def fee(amount):
    # Госпошлина: 1% от суммы иска, но не меньше 2000 тенге
    result = amount * 0.01
    if result < 2000:
        return 2000
    return result

def consult(hours, client):
    
    cost = hours * 15000
    if client == "студент":
        return cost * 0.5
    return cost

def fine(speed, limit):
    
    excess = speed - limit
    if excess <= 0:
        return 0
    if excess <= 10:
        return 0
    if excess <= 20:
        return 15000
    return 40000


print("--- Проверки части А ---")
print(fee(500000))
print(fee(100000))
print(consult(2, "студент"))
print(consult(2, "компания"))
print(fine(65, 60))
print(fine(75, 60))
print(fine(90, 60))
print("------------------------")



def documents(pages, urgency):

    base = pages * 2000
    if urgency == "срочно":
        return base * 1.5
    return base


print("\n1 госпошлина, 2 консультация, 3 штраф за скорость, 4 ваша функция")

try:
     
    choice = int(input("Что считаем? "))
    
    if choice == 1:
        amount = int(input("Сумма иска: "))
        print("Госпошлина:", fee(amount))
        
    elif choice == 2:
        hours = int(input("Количество часов: "))
        client = input("Кто клиент? (студент/компания): ")
        print("Стоимость консультации:", consult(hours, client))
        
    elif choice == 3:
        speed = int(input("Скорость: "))
        limit = int(input("Ограничение: "))
        print("Штраф:", fine(speed, limit))
        
    elif choice == 4:
        pages = int(input("Количество страниц: "))
        urgency = input("Срочность? (срочно/обычно): ")
        print("Стоимость документов:", documents(pages, urgency))
        
    else:
        print("Нет такого пункта")

except ValueError:
    print("Нужно ввести число")