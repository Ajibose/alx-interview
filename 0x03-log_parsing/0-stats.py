#!/usr/bin/python3
"""Log parsing"""
import sys
import signal
import os
import re


def pipe_handler(signum, frame):
    signame = signal.Signals(signum).name
    devnull = os.open(os.devnull, os.O_WRONLY)
    os.dup2(devnull, sys.stdout.fileno())
    sys.stdout.flush()
    sys.exit(1)


signal.signal(signal.SIGPIPE, pipe_handler)


def output_display(total_size, status_codes):
    """display output"""
    sys.stdout.write("File size: {}\n".format(total_size))
    for status in status_codes:
        if status_codes[status] > 0:
            sys.stdout.write("{}: {}\n".format(status, status_codes[status]))


def convert_to_int(num):
    try:
        val = int(num)
    except Exception:
        val = None
    finally:
        return val


def log_parse():
    """reads stdin line by line and computes metrics"""
    i = 1
    total_size = 0
    pattern = r"[0-9a-zA-Z.]+( )?-( )?\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}" \
        r":\d{2}\.\d+\] \"GET \/projects\/260 HTTP\/1.1\" " \
        r"([0-9a-zA-Z]+)? (\d+)"
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.fullmatch(pattern, line)

            if match:
                _, _, status_code, size = match.groups()
                total_size += int(size)

                status_code = convert_to_int(status_code)
                if status_code:
                    status_codes[status_code] += 1

            if i == 10:
                i = 0
                output_display(total_size, status_codes)
            i += 1
    except Exception:
        output_display(total_size, status_codes)
        sys.stdout.flush()
        raise

    finally:
        output_display(total_size, status_codes)


if __name__ == '__main__':
    log_parse()
