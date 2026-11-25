def fee(amount):
    # Госпошлина: 1% от суммы иска, но не меньше 2000 тенге
    result = amount * 0.01
    if result < 2000:
        return 2000
    return result


def consult(hours, client):
    # Стоимость консультации: 15000 тенге за час
    # Если клиент "студент" — скидка 50%
    cost = hours * 15000
    if client == "студент":
        return cost * 0.5
    return cost


def fine(speed, limit):
    # Штраф за скорость
    excess = speed - limit
    if excess <= 0:
        return 0
    if excess <= 10:
        return 0
    if excess <= 20:
        return 15000
    return 40000


# ===== Проверки части А =====
print(fee(500000))
print(fee(100000))
print(consult(2, "студент"))
print(consult(2, "компания"))
print(fine(65, 60))
print(fine(75, 60))
print(fine(90, 60))