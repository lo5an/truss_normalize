#!/usr/bin/env python3

import sys
import io
import csv

def main():

    csv_out = csv.writer(sys.stdout)

    # Make sure that we're dealing with utf8 from stdin
    utf8_stdin = io.TextIOWrapper(sys.stdin.buffer,
                                  encoding='utf-8',
                                  errors="replace")

    # process line at a time, not filewise
    csvlines = csv.reader(iter(utf8_stdin.readline, ''))
    for row in csvlines:
        out_row = row
        csv_out.writerow(out_row)

if __name__=='__main__':
    rc = 1
    try:
        main()
        rc=0
    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
    sys.exit(rc)
