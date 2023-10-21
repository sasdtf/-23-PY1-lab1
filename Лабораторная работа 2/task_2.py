salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  

for month in range(months):
    total_spend = spend * ((1 + increase) ** month)  
    deficit = total_spend - salary
    money_capital += deficit  

money_capital=round(money_capital, 2)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
