# global keyword:
# The global keyword allows you to modify a variable defined in the global scope (outside of any function) from within a function. Without it, any assignment to a variable inside a function would create a local variable, even if a global variable with the same name exists.
# Usage Example:


variable = "Text from global scope"  # This variable is declared in the Global scope


def fun():
    # global variable  # Without this we would not be able to change the variable value
    global variable
    variable = "Text from inside the function!"
    # print(variable)


fun()
print(variable)  # "hello 2"

# nonlocal keyword:
# The nonlocal keyword allows you to modify a variable in the nearest enclosing scope (not the global scope) from a nested function. It’s used in nested functions to access variables from the outer (enclosing) function's scope.
x = 20


def outer_function():
    x = 10  # Enclosing scope variable / # This variable is declared in a Local scope

    def inner_function():
        nonlocal x  # Refers to x in the outer function
        x += 5
        print("Inside inner_function:", x)

    inner_function()  # Output: Inside inner_function: 15
    print("Inside outer_function:", x)  # Output: Inside outer_function: 15


outer_function()
print("Outside outer_function:", x)
