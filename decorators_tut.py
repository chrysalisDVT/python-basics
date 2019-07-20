from functools import wraps

#Using @decorator_name over the fucntion we want to decorate
def log_decorator(f):
    #To specify that the function details and docstring are not overridden
    @wraps(f)
    def log_decorated(*args):
        print("Pre-decorating the function f")
        for i in args:
            print(i)
        f(*args)
        print("post-decorating function f")
    return log_decorated

#Chaining decorators
def star_decoration(f):
    @wraps(f)
    def add_star(*args):
        print("*" * 30)
        f(*args)
        print("*"*30)
    return add_star

#Traditional way which explains the working of decorators
def function_needs_decoration():
    print("I need decoration")

needs_decoration=log_decorator(function_needs_decoration)
needs_decoration()


#Using @decorator_name over the fucntion we want to decorate
@star_decoration
@log_decorator
def get_details(name):
    print("Fetching details")

get_details("dharm")
print("Function name:{0}".format(get_details.__name__))

#Using @wrap with decorators