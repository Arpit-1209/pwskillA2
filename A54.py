def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("Decorator one before")
        result = func(*args, **kwargs)
        print("Decorator one after")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("Decorator two before")
        result = func(*args, **kwargs)
        print("Decorator two after")
        return result
    return wrapper

@decorator_one
@decorator_two
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
