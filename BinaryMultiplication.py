import math
#performs ks multiplication given two lists representing two binary numbers
def ksMult(x, y):
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

    P1 = ksMult(xl, yl)
    P2 = ksMult(xr, yr)
    sumX = add(xl, xr)
    sumY = add(yl, yr)


    P3 = ksMult(sumX, sumY)

    n = len(x)
    total = P1 * 2**n + (P3 - P1 - P2) * 2**(n//2) + P2
    return total


#performs grade school multipliaction given two lists representing binary numbers.
def gsMult(x, y):
    return 0

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

# print(ksMult(bin_list(6), bin_list(5))
print(ksMult(bin_list(3), bin_list(4)))
# print(ksMult([1,0,1,1,0,0,1,0],[0,1,1,0,0,0,1,1]))$
# print(len([1]))

print(add([0,1],[1,0]))