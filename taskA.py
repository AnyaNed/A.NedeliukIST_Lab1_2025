def travel_calculator():

    distance = float(input("Введіть відстань до пункту призначення (км): "))
    vytrata = float(input("Введіть середню витрату пального (л/100км): "))
    price = float(input("Введіть середню ціну пального (грн/л): "))
    pasengers = int(input("Введіть кількість пасажирів: "))
    total = (distance / 100) * vytrata
    cost = total * price
    cost_per_pasenger = cost / pasengers

    print(f"Загальна вартість пального: {cost:.2f} грн")
    print(f"Вартість пального на одного пасажира: {cost_per_pasenger:.2f} грн")

travel_calculator()