#!/usr/local/bin/python3
from sys import argv
import argparse

# argv is a list of command line arguments
# argv[0] is the script name
# Arguments are strings by default

print("Script name:", argv[0])
print("Argument Length:", len(argv))

# Handle more complicated arguments with ArgumentParser module
# Shows help when the script is run with -h, --help
def create_parser():
    # Show required arguments if none are given
    parser = argparse.ArgumentParser()
    parser.add_argument("firstname", help="User's name")
    parser.add_argument("--lastname", help="optional last name", default=None)
    # Set arg to integer
    # parser.add_argument("age", help="Age in whole years", type=int)
    # Set verbose flag to true
    parser.add_argument("-v", "--verbose", help="Display more information", action="store_true")
    args = parser.parse_args()

    print(args.firstname) if args.lastname == None else print(args.firstname + " " + args.lastname)

    return parser

p = create_parser()

