def iterPower(base, exp):
    res=1
    for _ in range(exp):
        res = res*base
    return(res)
