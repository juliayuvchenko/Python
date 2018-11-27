print('Hello world!')


def compare(a, b):
    if (a < 0):
        raise Exception('a is negative: %s.' % a)
    if (b < 0):
        raise Exception('b is negative: %s.' % b)

    return a % b == 0

print(compare(5, 3))


def function(a, b):
    numbers = []
    if a < b:
        for num in range(a, b):
            if all(num % i != 0 for i in range(2, num)):
                numbers.append(num)
        return numbers
    if a > b:
        print("NoSimpleDigits")




print(function(1,10 ))

