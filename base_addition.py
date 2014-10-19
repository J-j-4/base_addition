#!/usr/bin/env python
# -*- coding: utf-8 -*-

# base_addition - 2014-10-19 - ejb

import sys


DEBUG = True
DIGITS = '0123456789ABCDEF'


def log_debug(debug_str):
    print "DEBUG: ", debug_str

def log_error(error_str):
    # EJB: I originally had 'print >> sys.stderr, "ERROR: ", error_str' here
    #       and it was getting buffered, even followed by sys.stderr.flush().
    assert isinstance(error_str, basestring)
    sys.stderr.write("ERROR: %s.\n" % error_str)

if __name__ == "__main__":
    base = 4
    digits = DIGITS[0:base]
    input_x = '31'
    input_y =  '3'
    log_debug('x input: %s: ' % input_x)
    log_debug('y input: %s: ' % input_y)
    x = input_x[::-1]  # Reverse string so we can to right-to-left processing left-to-right
    y = input_y[::-1]
    log_debug('x reversed: %s' % x)
    log_debug('y reversed: %s' % y)
    # right-pad (because reversed) to make same number of digits, for simplicity
    max_len = max(len(x), len(y))
    x += (max_len - len(x)) * '0'
    y += (max_len - len(y)) * '0'
    log_debug('x padded: %s' % x)
    log_debug('y padded: %s' % y)

    out_str = ''
    carry_in = 0
    for i in range(max_len):
        # Seems odd to be getting the index when we know the index, but necessary for A-F
        (carry_out, output) = divmod(digits.index(x[i]) + digits.index(y[i]), base)
        output += carry_in
        if output >= base:
            (carry_out, output) = divmod(output, base)
        assert(output < base)
        out_str = '%d%s' % (output, out_str)
        carry_in = carry_out
    if carry_out:
        out_str = '%d%s' % (carry_out, out_str)

    print('Answer: %s' % out_str)
