import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('ip_expr', nargs='?',
                    help="input expression to be evaluated")
parser.add_argument('-f', type=int,
                    help="specify floating point output precision")
parser.add_argument('-b', action="store_true",
                    help="output in binary format")
parser.add_argument('-o', action="store_true",
                    help="output in octal format")
parser.add_argument('-x', action="store_true",
                    help="output in hexadecimal format")
parser.add_argument('-v', action="store_true",
                    help="verbose mode, shows both input and output")
args = parser.parse_args()

if args.ip_expr in (None, '-'):
    args.ip_expr = sys.stdin.readline().strip()

try:
    result = eval(args.ip_expr)

    if args.f:
        result = f'{result:.{args.f}f}'
    elif args.b:
        result = f'{int(result):#b}'
    elif args.o:
        result = f'{int(result):#o}'
    elif args.x:
        result = f'{int(result):#x}'

    if args.v:
        print(f'{args.ip_expr} = {result}')
    else:
        print(result)
except (NameError, SyntaxError):
    sys.exit("Error: Not a valid input expression")
