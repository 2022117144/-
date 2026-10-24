#!/usr/bin/env python3
"""Small reproducible CSV/JSON converter using only Python 3.10+ stdlib."""
import argparse
import csv
import io
import json
import sys
from pathlib import Path


def json_to_csv(text: str) -> str:
    data = json.loads(text)
    if not isinstance(data, list) or any(not isinstance(row, dict) for row in data):
        raise ValueError("Expected a JSON array of flat objects")
    columns = list(dict.fromkeys(key for row in data for key in row))
    if any(not isinstance(k, str) for k in columns):
        raise ValueError("Object keys must be strings")
    if any(isinstance(v, (dict, list)) for row in data for v in row.values()):
        raise ValueError("Nested JSON values are not supported")
    if not columns:
        return ""
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(columns)
    for row in data:
        writer.writerow([
            "" if row.get(key) is None else
            json.dumps(row[key], ensure_ascii=False) if isinstance(row[key], bool) else
            str(row[key]) if key in row else ""
            for key in columns
        ])
    return output.getvalue()


def csv_to_json(text: str) -> str:
    reader = csv.reader(io.StringIO(text, newline=""))
    try:
        headers = next(reader)
    except StopIteration:
        return "[]\n"
    if not headers or any(not key.strip() for key in headers):
        raise ValueError("CSV headers must be nonempty")
    if len(headers) != len(set(headers)):
        raise ValueError("Duplicate CSV headers")
    rows = []
    for index, cells in enumerate(reader, start=2):
        if len(cells) != len(headers):
            raise ValueError(f"CSV record {index} has {len(cells)} cells, expected {len(headers)}")
        rows.append(dict(zip(headers, cells)))
    return json.dumps(rows, ensure_ascii=False, indent=2) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("direction", choices=("json-to-csv", "csv-to-json"))
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args(argv)
    try:
        source = args.input.read_text(encoding="utf-8-sig")
        result = json_to_csv(source) if args.direction == "json-to-csv" else csv_to_json(source)
        args.output.write_text(result, encoding="utf-8", newline="")
    except (OSError, ValueError, json.JSONDecodeError, csv.Error) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
