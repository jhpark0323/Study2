for i in range(3, 0, -1):
    X = input()
    if X not in ['Fizz', 'Buzz', 'FizzBuzz']:
        N = int(X) + i
        break

print('Fizz'*(N % 3 == 0) + 'Buzz'*(N % 5 == 0) or N)