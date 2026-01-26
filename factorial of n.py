def cal_fact(n):
    # we start with 1 because factorial multiplies numbers
    fact = 1
    # loop from 1 up to n (including n)
    for i in range(1, n+1):
        # multiply fact by each number in the loop
        fact *= i # same as fact = fact * i
    print(fact)

cal_fact(5)
