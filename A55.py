def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called")
        return result
    return wrapper

@my_decorator
def say_hello(name, age=None):
    if age:
        print(f"Hello, {name}. You are {age} years old.")
    else:
        print(f"Hello, {name}!")

say_hello("Alice", age=30)
