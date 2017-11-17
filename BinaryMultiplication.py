import math
#performs ks multiplication given two lists representing two binary numbers
def ksMult(x, y, length):
    if len(x) == 1 and len(y) == 1: return x[0] * y[0]


    x = pad_zero(x, y)[0]
    y = pad_zero(x, y)[1]
    xl = x[:math.ceil(len(x)/2)] #left half
    xr = x[math.ceil(len(x)/2):] #right half

    x1 = pad_zero(xl, xr)[0]
    xr = pad_zero(xl, xr)[1]

    yl = y[:math.ceil(len(y)/2)] #left half
    yr = y[math.ceil(len(y)/2):] #right half

    y1 = pad_zero(yl, yr)[0]
    yr = pad_zero(yl, yr)[1]

    P1 = ksMult(xl, yl, length)
    P2 = ksMult(xr, yr, length)
    sumX = add(xl, xr)
    sumY = add(yl, yr)


    P3 = ksMult(sumX, sumY, length)

    n = len(x)
    if(n == length):
        n -= 1
    total = P1 * 2**n + (P3 - P1 - P2) * 2**(n//2) + P2
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

        print(result)
        print(product)

        product = add(result, product)
        print(product)
        num_appends += 1

    print(product)
    print(int(''.join([str(n) for n in product]), 2))



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

# print(ksMult(bin_list(10), bin_list(10), len(bin_list(4))))
# print(ksMult([1,0,1,1,0,0,1,0],[0,1,1,0,0,0,1,1]))$
# print(len([1]))

# print(add([0,1],[1,0]))

# print(gsMult(bin_list(5), bin_list(6)))
gsMult(bin_list(9), bin_list(9))


