import sys


# List approach
def square_list(n):
    return [i * i for i in range(1, n + 1)]


# Generator approach
def square_generator(n):
    for i in range(1, n + 1):
        yield i * i


n = 10000000  # Ten million

# Memory usage for list
squares_list = square_list(n)
list_memory = sys.getsizeof(squares_list)
print(f"Memory used by list: {list_memory} bytes ({list_memory / (1024 ** 2):.6f} MB)")

# Memory usage for generator
squares_gen = square_generator(n)
generator_memory = sys.getsizeof(squares_gen)
print(f"Memory used by generator: {generator_memory} bytes ({generator_memory / (1024 ** 2):.6f} MB)")
