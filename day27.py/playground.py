def add(*args):
    # print(args)
    # print(type(args))

    # for n in args:
    #     print(n)

    sum = 0
    for n in args:
        sum += n   
    return sum

print(add(3, 5, 6))