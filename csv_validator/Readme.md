# CSV Validator 

A rule-based CSV validation tool that checks CSV files against a JSON configuration and reports **all findings**—clearly separating **errors** from **warnings**—with a structured summary.

This project is intentionally designed as a **core validation library**, with clean separation between:

* configuration parsing
* data loading
* validation logic
* reporting

CLI integration and advanced rules are deliberately out of scope for v1.

---

## 🎯 Project Goals

This project was built to practice and demonstrate:

* Reading and enforcing a written specification
* Rule-based validation without short-circuiting
* Clear distinction between **configuration errors** and **data errors**
* Deterministic, structured error reporting
* Test-driven development for validation logic

The design prioritizes **correctness, clarity, and extensibility** over feature count.

---

##  Inputs

### 1. CSV File

* Must contain a header row
* Data rows follow standard CSV rules
* UTF-8 encoded

### 2. Rules File (`rules.json`)

Defines required and optional columns.

Example:

```json
{
  "required_columns": ["id", "email"],
  "optional_columns": ["age"]
}
```

---

##  Validation Rules (v1)

### Header Validation

* Missing **required** column → **ERROR**
* Missing **optional** column → **WARNING**
* Rules are never applied to non-existent columns

### Row Validation

* Required column present but empty → **ERROR**
* Optional column present but empty → **ERROR**
* Multiple issues in the same row are all reported
* No short-circuiting

---

##  Output Model

Validation returns structured data:

```python
{
  "errors": [ ... ],
  "warnings": [ ... ],
  "summary": {
    "missing_required_columns": [...],
    "missing_optional_columns": [...],
    "rows_with_errors": <int>,
    "total_errors": <int>,
    "total_warnings": <int>
  }
}
```

Each finding includes:

* severity (`ERROR` / `WARNING`)
* stable error code
* human-readable message
* column name
* row number (for row-level issues)

---

## Design Principles

* **Pure functions** for validation logic
* **Strict config validation** (invalid rules stop execution)
* **No printing, no exits** inside core logic
* **All independent checks run**
* **Tests define behavior**

This design allows:

* easy CLI integration
* JSON output support
* future schema extensions
* safe refactoring

---

##  Testing

All core behavior is covered by tests using `pytest`.

Tests include:

* valid and invalid rule configurations
* header validation cases
* row-level validation cases
* integration-level validation behavior

Run tests with:

```bash
pytest
```

Tests are part of the public repository and treated as first-class artifacts.

---

## Project Structure

```
csv-validator/
├── validator.py
├── tests/
│   └── test_validator.py
└── README.md
```

---

## Intentional Limitations (v1)

The following are intentionally **out of scope** for this version:

* CLI interface
* Type / regex / range validation
* Streaming large CSV files
* Performance optimization
* Auto-correction of data

These are planned as future extensions.

---

##  Status

**Project #2 — Complete**

This project serves as a foundation for:

* CLI tooling
* schema-driven validation
* scalable data validation systems


