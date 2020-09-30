import argparse

def greet(args):
    output = '{0}, {1}!'.format(args.greeting, args.name)
    if args.caps:
        output = output.upper()
    print(output)

parser = argparse.ArgumentParser()
parser.add_argument('--version', action='version', version='1.0.0')
subparsers = parser.add_subparsers()

bull_parser = subparsers.add_parser('bull')
bull_parser.add_argument('name', help='name of the animal to greet')
bull_parser.add_argument('--greeting', default='bull', help='word to use for the greeting')
bull_parser.add_argument('--caps', action='store_true', help='uppercase the output')
bull_parser.set_defaults(func=greet)

bear_parser = subparsers.add_parser('bear')
bear_parser.add_argument('name', help='name of the animal to greet')
bear_parser.add_argument('--greeting', default='bear', help='word to use for the greeting')
bear_parser.add_argument('--caps', action='store_true', help='uppercase the output')
bear_parser.set_defaults(func=greet)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)