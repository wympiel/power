#TODO: create power function


def power(base, exp):
    if exp == 0:
        return 1

    temp =  power(base, exp // 2)
    temp *= temp
    return temp if exp % 2 == 0 else temp * base

def neg_power(base, exp):
    neg = exp < 0
    pos_result = pos_pow(base, abs(exp))
    return 1/pos_result if neg else pos_result

