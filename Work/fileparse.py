# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=","):
    """
    Parse a csv file into a list of records
    """

    # if select and not has_headers:
    #     raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read header if there is any
        headers = next(rows) if has_headers else None

        # If a column selector was given, find indices of the specified columns
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in headers]
            headers = select

        records = []
        for rownum, row in enumerate(rows):
            if row:
                # Filter the row if specific columns were selected
                if select:
                    row = [row[index] for index in indices]
                # Apply type connversion to row
                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        print(f"Row {rownum + 1}: Couldn't convert {row}")
                        print(f"Row {rownum + 1}: Reason {e}")

                # Make a dictionary if a header is presen, tuple if none
                record = dict(zip(headers, row)) if headers else tuple(row)

                records.append(record)

    return records


portfolio = parse_csv("Data/missing.csv", types=[str, int, float])
