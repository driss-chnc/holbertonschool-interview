#!/usr/bin/python3
"""Log parsing module."""

import sys


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    """Read stdin and compute log metrics."""
    total_size = 0
    status_codes = {}
    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) < 9:
                continue

            try:
                status = int(parts[-2])
                file_size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            if status not in valid_codes:
                continue

            total_size += file_size
            status_codes[status] = status_codes.get(status, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
