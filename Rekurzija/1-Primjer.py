def sum_recursive(n):
    if n==1:
        return 1
    else:
        return n + sum_recursive(n-1)


def sum_loop(n):
    result = 0
    for i in range(n+1):
        result += i
    return result


def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)



def fact_loop(n):
    if n==0:
        return 1
    else:
        result = 1
        for i in range(n):
            result *= (i+1)
        return result
