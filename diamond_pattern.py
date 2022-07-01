# def pyfunc(r):
#     for x in range(r):
#         print(' '*(r-x-1)+'*'*(2*x+1))
#     for x in range(r):
#         print(' '*(x)+'*'*((r-x)*2-1))

# pyfunc(4)


def pyfunc(r):
    for x in range(r):
        # printint space
        print(' '*(r-x-1),end="")
        # printint star
        print('*'*(2*x+1))
    for x in range(r):
        print(' '*(x)+'*'*((r-x)*2-1))

pyfunc(4)