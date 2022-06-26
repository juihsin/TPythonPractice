import os
import sys

print("這行永遠會執行")
print(f"__name__是什麼: {__name__}")

if __name__ == '__main__':

    print(f"我的工作目錄: {os.getcwd()}")
    print(f"目前的python是: {sys.executable}")

    # __XXX__ 有底線底線的這種是內建變數
