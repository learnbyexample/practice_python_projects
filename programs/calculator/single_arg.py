import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('ip_expr',
                    help="input expression to be evaluated")
args = parser.parse_args()

try:
    result = eval(args.ip_expr)
    print(result)
except (NameError, SyntaxError):
    sys.exit("Error: Not a valid input expression")

