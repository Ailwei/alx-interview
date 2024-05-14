#!/usr/bin/python3
"""Log Parser"""
import sys

if __name__ == '__main__':
    total_file_size = [0]
    status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                          403: 0, 404: 0, 405: 0, 500: 0}

    def print_statistics():
        """ Print statistics """
        print('Total File Size: {}'.format(total_file_size[0]))
        for code in sorted(status_code_counts.keys()):
            if status_code_counts[code]:
                print('{}: {}'.format(code, status_code_counts[code]))

    def parse_log_line(line):
        """ Parses the log line for relevant data """
        try:
            line = line[:-1]
            words = line.split(' ')
            # File size is the last parameter on stdout
            total_file_size[0] += int(words[-1])
            # Status code comes before file size
            status_code = int(words[-2])
            # Update the status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except Exception:
            pass

    line_number = 1
    try:
        for log_line in sys.stdin:
            parse_log_line(log_line)
            # Print statistics after every 10 lines
            if line_number % 10 == 0:
                print_statistics()
            line_number += 1
    except KeyboardInterrupt:
        print_statistics()
        raise
    print_statistics()
