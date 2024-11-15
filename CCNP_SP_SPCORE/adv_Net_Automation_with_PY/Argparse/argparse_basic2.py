import argparse

parser=argparse.ArgumentParser(description="container")

parser.add_argument("num1", type=int, help="This is integer No 1")
parser.add_argument("num2", type=int, help="This is integer No 2")
parser.add_argument("num3", type=int, help="This is integer No 3")
parser.add_argument("calc", help="This will do the calc, use 'add', 'substract' or 'multiply' arguments for math")

args=parser.parse_args()

n1= int(args.num1)
n2= int(args.num2)
n3= int(args.num3)
result = None

if args.calc == "add":
    result = n1 + n2 + n3
elif args.calc == "substract":
    result = n1 - n2 - n3
elif args.calc == "multiply":
    result = n1 * n2 * n3
else:
    print("wrong option")
    exit()  # Exit if there's an invalid calculation option

print(result)
