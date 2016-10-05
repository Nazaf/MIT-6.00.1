def gcdRecur(a,b):
    return b if (a-b) == 0 else gcdRecur(abs(a-b), min(a, b))

