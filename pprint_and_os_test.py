# ==========[Test pprint]==========
import sys

print(sys.path)

import pprint

pprint.pprint(sys.path)
print("*" * 80)

from pprint import pprint

pprint(sys.path)
print("-" * 80)

from pprint import pprint as pp

pp(sys.path)

# ==========[Test OS]==========
print("*" * 80)
from pprint import pprint as pp
import os
import shutil

print(os.name)
pprint(os.listdir())
os.mkdir("temp")
print("mkdir done")
os.rmdir("temp")

cur_dir = os.getcwd()
DEEP_DIRECTORY = "data/factory/node1"
os.makedirs(DEEP_DIRECTORY)
os.chdir(DEEP_DIRECTORY)  # 進到目錄裡面
print(os.getcwd())
print(os.listdir())
os.chdir(cur_dir)
shutil.rmtree("data")
