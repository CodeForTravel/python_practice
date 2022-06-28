
def function_name(*var_list):
    """Function with random argument, It's type will be touple"""
    print(var_list)

    # wring syntax
    # var_list[2] = 5
    print(type(var_list))

function_name(5,4,7,3)
function_name(5,7,3)
function_name(5,4,6,43,37,3)


def new_function(**var_list):
    """Function with random keyword argument, It's type will be dictionary"""
    print(var_list)
    print(type(var_list))

new_function(a=5,b=4,c=7,d=3)


# in Python, Functions Are First-class Objects.” What Do You Infer from This

# It means that a function can be treated just like an object. 
# You can assign them to variables, or 
# pass them as arguments to other functions. 
# You can even return them from other functions.

def first_class_function(funct_):
    funct_()
    def return_function():
        print("Return function....................")
    return return_function

def funct_():
    print("Argument function....................")

function_response =  first_class_function(funct_)
function_response()