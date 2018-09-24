import os

path = "./Effects.txt"
if not os.path.exists(path):
    raise ValueError()

file = open(path, "r")
effects = ",".join(sorted(file.readline().split(",")))
print(effects)
