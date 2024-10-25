salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
result = 0

for _ in range(months):
    result += spend-salary
    spend *= 1+increase
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(result))
