def generator_function():
    n=1
    print("Before first yield")
    yield n

    n = 2
    print("Before second yield")
    yield n
    
    n = 3
    print("Before third yield")
    yield n

yield_func_value = generator_function()
print(yield_func_value)
# print(next(yield_func_value))
# print(next(yield_func_value))
# print(next(yield_func_value))

for i in yield_func_value:
    print(i)


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]

    print("==========================")


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)

my_list = [3,4,6,7,4]
list_comprihension = [i**2 for i in my_list]
print(list_comprihension)

# generator expression/comprihension
generator_expression = (i**2 for i in my_list)
print(generator_expression)
print([i for i in generator_expression])


# Pipelining Generators
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))