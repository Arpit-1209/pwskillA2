def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is about to be called")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} has been called")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
