import math
import random
#performs ks multiplication given two lists representing two binary numbers
def ksMult(x, y):
    if len(x) == 1 and len(y) == 1: return x[0] * y[0]

    x = pad_zero(x, y)[0]
    y = pad_zero(x, y)[1]
    xl = x[:len(x)//2] #left half
    xr = x[len(x)//2:] #right half

    x1 = pad_zero(xl, xr)[0]
    xr = pad_zero(xl, xr)[1]

    yl = y[:len(y)//2] #left half
    yr = y[len(y)//2:] #right half

    y1 = pad_zero(yl, yr)[0]
    yr = pad_zero(yl, yr)[1]

    P1 = ksMult(xl, yl)
    P2 = ksMult(xr, yr)
    sumX = add(xl, xr)
    sumY = add(yl, yr)


    P3 = ksMult(sumX, sumY)

    n = len(x)
    total = P1 * (1 << (2*math.ceil(n/2))) + (P3 - P1 - P2) * (1 << math.ceil(n/2)) + P2

    return total


#performs grade school multipliaction given two lists representing binary numbers.
def gsMult(x, y):
    product = [0]
    y.reverse()
    num_appends = 0
    for bit in y:
        if(bit == 1):
            result = x[:]
        else:
            result = [0]

        for i in range(0, num_appends):
            result.append(0)


        result = pad_zero(result, product)[0]
        product = pad_zero(result, product)[1]

        product = add(result, product)
        num_appends += 1

    # print(product)
    print(int(''.join([str(n) for n in product]), 2))
    return int(''.join([str(n) for n in product]), 2)



#add two binary numbers represented as a list
def add(x, y):
    x = [str(n) for n in x]
    x = ''.join(x)
    x = int(x, 2)

    y = [str(n) for n in y]
    y = ''.join(y)
    y = int(y, 2)

    sum = x+y

    return [int(x) for x in list("{0:b}".format(sum))]

#takes an integer and converts to a binary encoded list
def bin_list(x):
    return [int(i) for i in list("{0:b}".format(x))]

#pads zero to the list with less digits
def pad_zero(list_x, list_y):

    while(len(list_x) < len(list_y)):
        list_x.insert(0,0)
    while(len(list_x) > len(list_y)):
        list_y.insert(0,0)

    return (list_x, list_y)

# print(ksMult(bin_list(10), bin_list(10), 0))
# print(ksMult([1,0,1,1,0,0,1,0],[0,1,1,0,0,0,1,1]))$
# print(len([1]))

# print(add([0,1],[1,0]))

print(gsMult(bin_list(2**32), bin_list(2**32)))
# gsMult(bin_list(2**15), bin_list(2**16))


# def generateNumbers(n):
#     return [i for i in range(2 ** n) if i >= 2 ** (n - 1)]


bits = [(i + 1) for i in range(100)]
print(bits)

import timeit
import random

runtime_ks = []
runtime_gs = []

for i in bits:
    x = random.randint(2**(i-1), 2**i)
    y = random.randint(2**(i-1), 2**i)

    start = timeit.default_timer()
    ksMult(bin_list(x), bin_list(y))
    stop = timeit.default_timer()
    runtime_ks.append(stop-start)

    start2 = timeit.default_timer()
    gsMult(bin_list(x), bin_list(y))
    stop2 = timeit.default_timer()
    runtime_gs.append(stop2-start2)

import matplotlib.pyplot as plt
plt.plot([i for i in bits], [i for i in runtime_ks], 'ro')
plt.plot([i for i in bits], [i for i in runtime_gs],'bo')
plt.legend(['runtime_gs', 'runtime_ks'], loc='upper left')
plt.xlabel('number of bits')
plt.ylabel('runtime for performing multiplication')
plt.show()