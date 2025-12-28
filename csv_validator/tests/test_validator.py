import json
import tempfile
import pytest

from validator import load_rules,validate_header,validate,validate_rows

def write_temp_json(data):
    tmp = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".json")
    json.dump(data, tmp)
    tmp.close()
    return tmp.name

def test_load_rules_valid():
    path = write_temp_json({
        "required_columns": ["id", "email"],
        "optional_columns": ["age"]
    })

    rules = load_rules(path)

    assert rules["required"] == {"id", "email"}
    assert rules["optional"] == {"age"}

def test_load_rules_missing_required_key():
    path = write_temp_json({
        "optional_columns": ["age"]
    })

    with pytest.raises(ValueError):
        load_rules(path)

def test_load_rules_overlap():
    path = write_temp_json({
        "required_columns": ["id"],
        "optional_columns": ["id"]
    })

    with pytest.raises(ValueError):
        load_rules(path)

def test_validate_header_missing_columns():
    header = ["id"]
    rules = {
        "required": {"id", "email"},
        "optional": {"age"}
    }

    errors, warnings = validate_header(header, rules)

    assert len(errors) == 1
    assert errors[0]["code"] == "MISSING_REQUIRED_COLUMN"
    assert errors[0]["column"] == "email"

    assert len(warnings) == 1
    assert warnings[0]["code"] == "MISSING_OPTIONAL_COLUMN"
    assert warnings[0]["column"] == "age"

def test_validate_header_all_present():
    header = ["id", "email", "age"]
    rules = {
        "required": {"id", "email"},
        "optional": {"age"}
    }

    errors, warnings = validate_header(header, rules)

    assert errors == []
    assert warnings == []

def write_temp_csv(text):
    tmp = tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".csv")
    tmp.write(text)
    tmp.close()
    return tmp.name
def test_validate_header_only():
    csv_path = write_temp_csv(
        "id,name\n"
        "1,Alice\n"
    )

    rules_path = write_temp_json({
        "required_columns": ["id", "email"],
        "optional_columns": ["age"]
    })

    result = validate(csv_path, rules_path)

    assert result["summary"]["total_errors"] == 1
    assert result["summary"]["total_warnings"] == 1
    assert "email" in result["summary"]["missing_required_columns"]
    assert "age" in result["summary"]["missing_optional_columns"]


#---------data of csv-------
def test_validate_rows_empty_required_value():
    header = ["id", "email"]
    rows = [
        ["1", ""]
    ]
    rules = {
        "required": {"id", "email"},
        "optional": set()
    }

    errors, warnings = validate_rows(header, rows, rules)

    assert len(errors) == 1
    assert errors[0]["code"] == "EMPTY_REQUIRED_VALUE"
    assert errors[0]["column"] == "email"
    assert errors[0]["row"] == 1

def test_validate_rows_empty_optional_value():
    header = ["id", "age"]
    rows = [
        ["1", ""]
    ]
    rules = {
        "required": {"id"},
        "optional": {"age"}
    }

    errors, warnings = validate_rows(header, rows, rules)

    assert len(errors) == 1
    assert errors[0]["code"] == "EMPTY_OPTIONAL_VALUE"
    assert errors[0]["column"] == "age"
    assert errors[0]["row"] == 1
def test_validate_rows_missing_column_skipped():
    header = ["id"]
    rows = [
        ["1"]
    ]
    rules = {
        "required": {"id", "email"},
        "optional": set()
    }

    errors, warnings = validate_rows(header, rows, rules)

    assert errors == []
    assert warnings == []
def test_validate_rows_multiple_errors_same_row():
    header = ["id", "email"]
    rows = [
        ["", ""]
    ]
    rules = {
        "required": {"id", "email"},
        "optional": set()
    }

    errors, warnings = validate_rows(header, rows, rules)

    assert len(errors) == 2
    assert {e["column"] for e in errors} == {"id", "email"}
