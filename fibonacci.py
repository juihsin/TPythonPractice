import sys


def fib1(n):
    i, a, b = 0, 0, 1
    print("fib1: ")
    while i < n:
        print(a, end=" ")
        a, b = b, a + b
        i += 1
    print()


def fib2(n):
    res = []
    i, a, b = 0, 0, 1
    while i < n:
        res.append(a)
        a, b = b, a + b
        i += 1
    print(f"fib2: {res}")
    return res


def get_fib_default_parm(default=10):
    sys_argv = sys.argv
    print(f"sys.argv: {sys_argv}")
    if len(sys_argv) > 1:
        default = int(sys_argv[1])
    return default


if __name__ == '__main__':
    # Normal
    fib1(10)
    print()

    # Advanced
    default_val = get_fib_default_parm(10)
    fib2(default_val)
