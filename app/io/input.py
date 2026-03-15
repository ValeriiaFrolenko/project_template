import pandas as pd

def read_from_console() -> str:
    text = input("Please enter your input: ")
    return text

def read_from_file(filepath: str) -> str:
    with open(filepath, mode="r", encoding="utf-8") as file:
        content = file.read()
        return content

def read_from_file_pandas(filepath: str) -> pd.DataFrame:
    dataframe = pd.read_csv(
        filepath,
        encoding="utf-8"
    )
    return dataframe