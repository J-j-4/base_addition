#!/usr/bin/env python
# -*- coding: utf-8 -*-

# base_addition - 2014-10-19 - ejb

from __future__ import print_function
import argparse
import sys

__version__ = '0.1'
'''
Revision history
0.1 Initial version
'''



DIGITS = '0123456789ABCDEF'
debug = False


def parse_args():
    parser = argparse.ArgumentParser(description="Add two numbers in a given base (default 10).")
    parser.add_argument("-b", "--base", type=int, dest="base", choices=xrange(2, 17), default=10, help="base (2-16); default = %(default)s")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--addends", type=str, metavar="NUM", nargs='+', help="addends")
    group.add_argument("--test", action="store_true", help="run test suite")
    parser.add_argument('--version', action='version', version='%(prog)s v' + str(__version__))
    parser.add_argument("--debug", "--verbose", action="store_true", dest="debug", help="enable debugging output")
    return parser.parse_args()

def log_debug(debug_str):
    if debug:
        print("DEBUG (addition): ", debug_str)

def log_error(error_str):
    # EJB: I originally had 'print >> sys.stderr, "ERROR: ", error_str' here
    #       and it was getting buffered, even followed by sys.stderr.flush().
    sys.stderr.write("ERROR: {}.\n".format(error_str))

def run_tests():
    assert(base_addition(debug=False, base=2, addends=[11, 1]) == '100')
    assert(base_addition(debug=False, base=5, addends=[0, 0, 4, 1, 0, 0]) == '10')
    assert(base_addition(debug=False, base=8, addends=[4, 4, 4, 4]) == '20')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    # assert(base_addition(debug=False, base=, addends=[, ]) == '')
    print ('All tests passed.')

def base_addition(debug, base, addends):
    digits = DIGITS[0:base]
    accumulator = 0  # Additive identity

    # Validate that input digits are valid in given base
    valid = True
    for addend in addends:
        for digit in str(addend).upper():
            if not str(digit).upper() in digits:
                valid = False
                log_error('Invalid number {} for base {}'.format(addend, base))
                break
    if not valid:
        sys.exit(-1)


    if len(addends) == 0:
        return str(addends[0])
    else:
        accumulator = str(addends.pop())

    while len(addends) > 0:
        x = str(accumulator).upper()
        y = str(addends.pop()).upper()

        log_debug('x input: {}: '.format(x))
        log_debug('y input: {}: '.format(y))
        x = x[::-1]  # Reverse string so we can do right-to-left processing left-to-right
        y = y[::-1]
        log_debug('x reversed: {}'.format(x))
        log_debug('y reversed: {}'.format(y))
        # right-pad (because reversed) to make same number of digits, for simplicity
        max_len = max(len(x), len(y))
        x += (max_len - len(x)) * '0'
        y += (max_len - len(y)) * '0'
        log_debug('x padded: {}'.format(x))
        log_debug('y padded: {}'.format(y))

        out_str = ''
        carry_in = 0
        for i in range(max_len):
            (carry_out, output) = divmod(digits.index(x[i]) + digits.index(y[i]), base)
            output += carry_in
            if output >= base:
                (carry_out, output) = divmod(output, base)
            assert(output < base)
            out_str = '{}{}'.format(digits[output], out_str)
            carry_in = carry_out
        if carry_out:
            out_str = '{}{}'.format(digits[carry_out], out_str)

        accumulator = out_str

    log_debug('Answer: {}'.format(accumulator))
    return accumulator


if __name__ == "__main__":
    args = parse_args()
    debug = args.debug
    log_debug(args)

    if args.test:
        run_tests()
    else:
        base = args.base
        addends = args.addends

        answer = base_addition(debug=debug, base=base, addends=addends)
        print('Answer: {}'.format(answer))
