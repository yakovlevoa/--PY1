def life(money_capital, salary, spend, increase, month):
    while money_capital > spend:
        money_capital += salary
        money_capital -= spend
        spend = spend * (1 + increase)
        month += 1
    print(month)


life(money_capital=10000, salary=5000, spend=6000, increase=0.05, month=0)
