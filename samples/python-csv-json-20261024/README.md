# Reproducible Python CSV ↔ JSON demo

This is an independent **capability demonstration**, not a client contract, approved submission, or payment. Python 3.10+ standard library only.

## Run locally

```bash
python -m unittest discover -v -p "test_*.py"
python convert.py json-to-csv sample.json sample.csv
python convert.py csv-to-json sample.csv roundtrip.json
```

Nine reproducible `unittest` cases passed on Windows with Python 3.10.7 on 2026-10-24. Source and tests are provided; run them yourself to verify.

### Sample input (`sample.json`)

```json
[{"name":"张三","id":"001"},{"name":"A, B","note":"line1\nline2"}]
```

### Generated CSV

```csv
name,id,note
张三,001,
"A, B",,"line1
line2"
```

## Scope and limitations

JSON arrays must contain flat objects; columns follow first-seen key order. Unicode and quoted newlines are handled by the standard `csv` writer. Missing keys and null values become empty cells; therefore JSON → CSV → JSON is **not fully lossless**. CSV cells stay strings (including leading zeros). Duplicate headers, inconsistent rows and nested JSON values fail with explicit errors. No network traffic, credentials, external services, schema inference or promises of client-specific support.
