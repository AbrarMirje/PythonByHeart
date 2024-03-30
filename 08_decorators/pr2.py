

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}: {v}" for k, v in kwargs.items())
        print(f"Calling: {func.__name__} with args {args_value} and with kwargs {kwargs}")
        return func(*args, **kwargs)    
    return wrapper

@debug
def hello():
    print("Hello")

@debug
def greet(name, greetings = "Hello"):
    print(f"{greetings}, {name}")
    
hello()
greet("Abrar", greetings="Welcome")