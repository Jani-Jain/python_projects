Below is a **clean, OSS-acceptable README**. You can paste this **as-is** into `README.md`.
It is intentionally concise and professional—no fluff.


# Log File Analyzer

A simple command-line tool that analyzes plain-text log files and summarizes log levels and frequently occurring log messages.

This tool is designed to help quickly extract useful insights from large log files without manually scanning them.

---

## Supported Log Format

Each log entry must be on a single line in the following format:

```
<TIMESTAMP> <LEVEL> <MESSAGE>
```

Example:

```
2025-09-14 09:02:45 ERROR Database connection failed
```

Supported log levels:

* `INFO`
* `WARNING`
* `ERROR`

Malformed lines are ignored safely.

---

## How to Run

### Requirements

* Python 3.x

### Command

```bash
python main.py --file sample.log --top 5
```

### Arguments

* `--file` (required): Path to the log file
* `--top` (optional): Number of most common messages to display

  * Default: `5`

---

## Example Output

```
Log level counts:
INFO: 10
WARNING: 4
ERROR: 5

Top 3 most common messages:
Database connection failed (3)
User logged in (3)
Disk space low (2)
```

---

## Project Structure

```
log_analyzer/
├── analyzer.py     # Core parsing and analysis logic
├── main.py         # CLI entry point
├── sample.log      # Example log file
└── README.md
```

---

## Notes

* The tool is non-interactive and suitable for scripting.
* Input handling is separated from analysis logic.
* Designed as a small, extensible foundation for further enhancements.

---

## Status

✔ Core functionality complete
✔ CLI interface implemented
✔ Sample data provided

