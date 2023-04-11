def get_primes(param):
    for num in param:
        if num == 2 or num == 3 or num == 5:
            yield num
        if num % 2 == 1 and num % 5 != 0 and num % 3 != 0 and num != 1:
            yield num


print(list(get_primes([59, 61, 67, 71, 73, 79, 83, 89])))