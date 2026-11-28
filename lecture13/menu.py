while True:
    days = int(input("Дней просрочки (0 выход): "))
    if days == 0:
        break
    print("Пеня:", 500000 * 0.001 * days)

print("До свидания") 