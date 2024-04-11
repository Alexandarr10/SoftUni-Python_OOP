def get_primes(numbers: list):
    for number in numbers:
        if number < 2:
            continue
        for num in range(2, number):
            if number % num == 0:
                break
        else:
            yield number

# Test code

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))