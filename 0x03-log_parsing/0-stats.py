#!/usr/bin/python3
"""
log parsing
"""

import sys
import re


def print_stats(log: dict) -> None:
    """
    Helper function to display stats
    """
    print("Total file size: {}".format(log["total_file_size"]))
    for code in sorted(log["status_code_counts"]):
        if log["status_code_counts"][code]:
            print("{}: {}".format(code, log["status_code_counts"][code]))


if __name__ == "__main__":
    regex_pattern = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')

    line_count = 0
    log = {}
    log["total_file_size"] = 0
    log["status_code_counts"] = {
        str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex_pattern.fullmatch(line)
            if match:
                line_count += 1
                status_code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log["total_file_size"] += file_size

                # Status code
                if status_code.isdecimal():
                    log["status_code_counts"][status_code] += 1

                if line_count % 10 == 0:
                    print_stats(log)
    finally:
        print_stats(log)
