def fibonacci():
    current_number, next_number = 0, 1
    while True:
        yield current_number
        current_number, next_number = next_number, current_number + next_number


# Test code
generator = fibonacci()

for i in range(5):

 print(next(generator))