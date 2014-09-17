#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2014 Stefan Müller-Klieser, PHYTEC Messtechnik GmbH

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Summons the software platform landscape of PHYTEC from concepts into '
                                                 'actual bits existing in memory.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                       help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                       const=sum, default=max,
                       help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args.accumulate(args.integers)

