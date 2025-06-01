

def decorator_function(func):
    def inner(a,b):
        sum = a+b
        print("sum:",sum)
        func()
        print("hello this is after decorator")
    return inner


@decorator_function
def test():
    print("this function will be decorated::")

test(12,34)