summa = float(input("Сумма заказа: "))
gorod = input("Город: ")

if summa >= 5000 and gorod.lower() == "алматы":
    print("Доставка бесплатно")
else:
    print("Доставка 1000 тенге")
