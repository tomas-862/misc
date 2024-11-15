import argparse

parser=argparse.ArgumentParser(description="container")

parser.add_argument("num1", type=int, help="This is integer No 1")
parser.add_argument("num2", type=int, help="This is integer No 2")
parser.add_argument("num3", type=int, help="This is integer No 3")

args=parser.parse_args()

print(f"{args.num1} is Integer No 1")
print(f"{args.num2} is Integer No 2")
print(f"{args.num3} is Integer No 3")

