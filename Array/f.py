def fac(n):
    if n == 0:
        result = 1
    else:
        result =n*fac(n-1)
    return result


print(fac(1))