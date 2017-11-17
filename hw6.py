def generateNumbers(n):
    return [i for i in range(2**n) if i >= 2**(n-1)]

bits = [(i+1) for i in range(29)]

import timeit
import random
runtime_ks = []
runtime_gs = []
for i in bits:
    nums = generateNumbers(i)
    num1 = random.choice(nums)
    num2 = random.choice(nums)
    start = timeit.default_timer()
    ksMult(bin_list(num1), bin_list(num2), 0)
    stop = timeit.default_timer()
    runtime_ks.append(stop-start)
    
    start = timeit.default_timer()
    gsMult(bin_list(num1), bin_list(num2))
    stop = timeit.default_timer()
    runtime_gs.append(stop-start)