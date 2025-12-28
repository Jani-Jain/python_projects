import json
import csv


def load_rules(path):
    
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("Rules file must contain a JSON object")
    if "required_columns" not in data:
        raise ValueError("Missing 'required_columns' in rules")
    if "optional_columns" not in data:
        raise ValueError("Missing 'optional_columns' in rules")
    required = data["required_columns"]
    optional = data["optional_columns"]

    if not isinstance(required, list):
        raise ValueError("'required_columns' must be a list")
    if not isinstance(optional, list):
        raise ValueError("'optional_columns' must be a list")
    
    for col in required:
        if not isinstance(col, str):
            raise ValueError("All required column names must be strings")
    for col in optional:
        if not isinstance(col, str):
            raise ValueError("All optional column names must be strings")
    required_set = set(required)
    optional_set = set(optional)
    if len(required_set) != len(required):
        raise ValueError("Duplicate entries in 'required_columns'")

    if len(optional_set) != len(optional):
        raise ValueError("Duplicate entries in 'optional_columns'")

    overlap = required_set & optional_set
    if overlap:
        raise ValueError(
            f"Columns cannot be both required and optional: {sorted(overlap)}"
        )
    return {
        "required": required_set,
        "optional": optional_set,
    }

#READ CSV READING DATA


def read_csv(path):
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)

        try:
            header = next(reader)
        except StopIteration:
            raise ValueError("CSV file is empty; no header found")

        rows = list(reader)

    return header, rows

#Checking Header 

def validate_header(header, rules):
    errors = []
    warnings = []

    header_set = set(header)

    for column in rules["required"]:
        if column not in header_set:
            errors.append({
                "level": "ERROR",
                "code": "MISSING_REQUIRED_COLUMN",
                "message": f"Required column '{column}' is missing",
                "column": column,
            })

    for column in rules["optional"]:
        if column not in header_set:
            warnings.append({
                "level": "WARNING",
                "code": "MISSING_OPTIONAL_COLUMN",
                "message": f"Optional column '{column}' is missing",
                "column": column,
            })

    return errors, warnings

def validate_rows(header, rows, rules):
    errors = []
    warnings = []

    column_index = {col: idx for idx, col in enumerate(header)}

    for row_num, row in enumerate(rows, start=1):

        for column in rules["required"]:
            if column not in column_index:
                continue  

            idx = column_index[column]
            value = row[idx] if idx < len(row) else ""

            if value == "":
                errors.append({
                    "level": "ERROR",
                    "code": "EMPTY_REQUIRED_VALUE",
                    "message": f"Required column '{column}' is empty",
                    "column": column,
                    "row": row_num,
                })

        for column in rules["optional"]:
            if column not in column_index:
                continue

            idx = column_index[column]
            value = row[idx] if idx < len(row) else ""

            if value == "":
                errors.append({
                    "level": "ERROR",
                    "code": "EMPTY_OPTIONAL_VALUE",
                    "message": f"Optional column '{column}' is empty",
                    "column": column,
                    "row": row_num,
                })

    return errors, warnings



# ----------final function----------------
csv_path = "sample.csv"
rules_path = "rules.json"
def validate(csv_path, rules_path):
    rules = load_rules(rules_path)
    header,_ = read_csv(csv_path)

    all_errors = []
    all_warnings = []

    header_errors, header_warnings = validate_header(header, rules)
    all_errors.extend(header_errors)
    all_warnings.extend(header_warnings)

    summary = {
        "missing_required_columns": [
            f["column"]
            for f in header_errors
            if f["code"] == "MISSING_REQUIRED_COLUMN"
        ],
        "missing_optional_columns": [
            f["column"]
            for f in header_warnings
            if f["code"] == "MISSING_OPTIONAL_COLUMN"
        ],
        "rows_with_errors": 0,  
        "total_errors": len(all_errors),
        "total_warnings": len(all_warnings),
    }

    return {
        "errors": all_errors,
        "warnings": all_warnings,
        "summary": summary,
    }
