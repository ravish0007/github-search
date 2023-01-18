#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("search_string")

args = parser.parse_args()

print(args.search_string)
