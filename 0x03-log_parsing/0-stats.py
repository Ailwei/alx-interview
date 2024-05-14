#!/usr/bin/python3
"""Log Parser"""
import sys
import re


TOTAL_LINES_THRESHOLD = 10

def print_statistics(total_file_size, status_code_counts):
    """ Print statistics """
    print("Total file size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code]:
            print("{}: {}".format(code, status_code_counts[code]))

def parse_log_line(line, total_file_size, status_code_counts):
      """ Checks the line for matches """
    try:
        match = re.match(r'(\S+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)', line)
        if match:
            status_code = int(match.group(2))
            file_size = int(match.group(3))
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        return total_file_size, status_code_counts
    except Exception:
        return total_file_size, status_code_counts

def main():
    total_file_size = 0
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_number = 0

    try:
        for line in sys.stdin:
            line_number += 1
            total_file_size, status_code_counts = parse_log_line(line.strip(), total_file_size, status_code_counts)
            if line_number % TOTAL_LINES_THRESHOLD == 0:
                print_statistics(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        sys.exit(0)

if __name__ == "__main__":
    main()
