#!/usr/bin/env python3

import sys
import io
import csv
import datetime
import pytz



def normalize_timestamp(ts_text):

    time_fmt = "%m/%d/%y %I:%M:%S %p"
    time = datetime.datetime.strptime(ts_text, time_fmt)
    # Input timezone is US/Pacific
    time_pt = pytz.timezone('US/Pacific').localize(time)

    # Desired output timezone is US/Eastern
    return time_pt.astimezone(pytz.timezone('US/Eastern')).isoformat()


def normalize_postal(postal):
    if (len(postal) > 5):
        raise ValueError('Zip colume should contain 5 or fewer digits')
    return postal.zfill(5)

def normalize_fullname(fname):
    return fname.upper()

def normalize_duration(dur_str):
    hrs,mins,remainder = dur_str.split(":")
    secs,mics = remainder.split(".")

    dur = datetime.timedelta(hours = int(hrs),
                             minutes = int(mins),
                             seconds = int(secs),
                             microseconds = int(mics))


    return dur.total_seconds()

def truss_normalize(row):

    timestamp = normalize_timestamp(row[0])
    address = row[1]
    postal = normalize_postal(row[2]) #  Zip in row headers
    fullname = normalize_fullname(row[3])
    fooduration = normalize_duration(row[4])
    barduration = normalize_duration(row[5])
    totalduration = fooduration+barduration
    notes = row[7]

    normal_row = [ timestamp, address, postal, fullname, fooduration,
                  barduration,totalduration,notes ]
    return(normal_row)

def main():

    csv_out = csv.writer(sys.stdout)

    # Make sure that we're dealing with utf8 from stdin
    utf8_stdin = io.TextIOWrapper(sys.stdin.buffer,
                                  encoding='utf-8',
                                  errors="replace")

    # process line at a time, not filewise
    csvlines = csv.reader(iter(utf8_stdin.readline, ''))
    for row in csvlines:
        try:
            out_row = truss_normalize(row)
            csv_out.writerow(out_row)
        except Exception as e:
            print('Error: %s' % e, file=sys.stderr)

if __name__=='__main__':
    rc = 1
    try:
        main()
        rc=0
    except Exception as e:
        print('Error: %s' % e, file=sys.stderr)
    sys.exit(rc)
