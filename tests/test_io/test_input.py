import pandas as pd
import pytest
from app import io

def test_read_from_file_simple_text(tmp_path):
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is test content", encoding="utf-8")
    result = io.read_from_file(str(test_file))
    assert result == "This is test content"


def test_read_from_file_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        io.read_from_file("/path/to/nonexistent/file.txt")


def test_read_from_file_empty_file(tmp_path):
    test_file = tmp_path / "empty.txt"
    test_file.write_text("", encoding="utf-8")
    result = io.read_from_file(str(test_file))
    assert result == ""


def test_read_from_file_pandas_simple_csv(tmp_path):
    test_file = tmp_path / "data.csv"
    csv_content = "name,age\nJohn,25\nMary,30"
    test_file.write_text(csv_content, encoding="utf-8")
    result = io.read_from_file_pandas(str(test_file))
    assert isinstance(result, pd.DataFrame)
    assert len(result) == 2
    assert list(result.columns) == ["name", "age"]
    assert result.iloc[0]["name"] == "John"
    assert result.iloc[0]["age"] == 25


def test_read_from_file_pandas_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        io.read_from_file_pandas("/path/to/nonexistent/file.csv")


def test_read_from_file_pandas_empty_csv(tmp_path):
    test_file = tmp_path / "empty.csv"
    csv_content = "column1,column2"
    test_file.write_text(csv_content, encoding="utf-8")
    result = io.read_from_file_pandas(str(test_file))
    assert len(result) == 0
    assert list(result.columns) == ["column1", "column2"]