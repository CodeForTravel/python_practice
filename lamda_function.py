# A lambda function is a type of anonymous function(it has no name).
# This function can take as many parameters as you want, but just one statement.

# Program to show the use of lambda functions
make_sume = lambda x,y,z,m,n: f"Sum of the given values is : {x+y+z+m+n}"
print(make_sume(5,6,76,7,3))


lamda_with_args = lambda *args: f"Sum of the given values is : {sum(args)}"
print(lamda_with_args(5,6,76,7,3))


lamda_with_kargs = lambda **kwargs: f"Sum of the given values is : {sum([i for i in kwargs.values()])}"
print(lamda_with_kargs(x=5,y=5,z=7))


my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
