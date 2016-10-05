def recurPower(base, exp):
    if exp == 0:   #if exponential is 0 then return 1
        return 1
    if exp != 0:
        return base * recurPower(base, exp-1)
