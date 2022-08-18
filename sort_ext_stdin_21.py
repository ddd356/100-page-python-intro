# sort_ext_stdin_21.py
import argparse, sys

parser = argparse.ArgumentParser()
parser.add_argument('file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="input file to be sorted")
parser.add_argument('-u', '--unique', action = 'store_true', help = "sort uniquely")
parser.add_argument('-o', '--output', type=argparse.FileType('w'))
args = parser.parse_args()

ip_lines = args.file.readlines()
if args.unique:
    ip_lines = set(ip_lines)

op_lines = sorted(ip_lines, key=lambda s: (s.rsplit('.', 1)[-1], s))
if args.output:
    for line in op_lines:
        args.output.write(line)
else:
    for line in op_lines:
        print(line, end='')
