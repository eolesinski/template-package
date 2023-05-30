# create a new function with type annotation that returns the string hello world
def hello() -> str:

    return "Hello, world!"

# create a function with type annotation that prints the the hello function
def print_hello() -> None:

    print(hello())
