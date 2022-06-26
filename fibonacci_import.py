# [Import Way 1] 這樣 import 可呼叫 protected 的 functions (有底線的那種 function)
from fibonacci import fib1
from fibonacci import __get_sys_argv
from fibonacci import _get_fib_default_parm

# [Import Way 2] 這樣 import 也可呼叫 protected 的 functions (有底線的那種 function)
# import fibonacci as fib

# [Import Way 3] 這樣就不行
# from fibonacci import *

if __name__ == '__main__':
    # [Import Way 1, Import Way 3]
    fib1(5)
    _get_fib_default_parm(__get_sys_argv(), 5)

    # [Import Way 2]
    # fib.fib1(5)
    # fib._get_fib_default_parm(fib.__get_sys_argv(), 5)
