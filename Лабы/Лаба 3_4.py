def money(sal, sp, m, inc, me, ml):
    for _ in range(m):
        ml += sp
        me += sal
        sp *= (1 + inc)
    return (ml - me)


print(round(money(sal=5000, sp=6000, m=10, inc=0.03, me=0, ml=0)))
