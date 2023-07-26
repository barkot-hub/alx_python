#import sys

args = sys.argv[1:]
num_args = len(args)
print("Number of argument" + ("s" if num_args != 1 else "") + ": " + str(num_args) + ("" if num_args == 0 else ":"))
print()
for i in range(num_args):
    print(str(i+1) + ": " + args[i])