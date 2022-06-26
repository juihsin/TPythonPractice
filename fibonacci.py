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


# 前面有一條或兩條底線的是 private function, 其他 class import 的時候應該要拿不到這個 function
def __get_sys_argv():
    sys_argv = sys.argv
    print(f"sys.argv: {sys_argv}")
    return sys_argv


# 前面有一條或兩條底線的是 private function, 其他 class import 的時候應該要拿不到這個 function
def _get_fib_default_parm(sysargv, default=10):
    if len(sysargv) > 1:
        default = int(sysargv[1])
    return default


if __name__ == '__main__':
    # Normal
    fib1(10)
    print()

    # Advanced
    sys_argv = __get_sys_argv()
    default_val = _get_fib_default_parm(sys_argv, 10)
    fib2(default_val)
