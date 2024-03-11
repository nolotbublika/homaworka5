def test (*args):
    print(args)


test(2,"pinta",False)


def faktorial(n):
    if n <= 0:
        return 1
    else:
        return n * faktorial(n - 1)

m = faktorial(5)
print(m)