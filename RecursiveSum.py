from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED


def suma(array):
    if len(array) == 0:
        return 0
    else:
        return array[-1] + suma(array[:-1])

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))