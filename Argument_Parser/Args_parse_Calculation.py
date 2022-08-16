import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--x",type=float,default=3,help="first number")
# We can use only x in place of --x but using --x allows us to provide commands line argument in any manner.
# parser.add_argument("x",type=float,default=3,help="first number")
# For this line we will submit program like this
# python Args_parse_Calculation.py 3 4 add

parser.add_argument("--y",type=float,default=3,help="first number")
parser.add_argument("--o",type=str,default="add",help="first number")
args=parser.parse_args()
# python Args_parse_Calculation.py --x 3 --o add --y 4
print(args.x)
print(args.y)
print(args.o)