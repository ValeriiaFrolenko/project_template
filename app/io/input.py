import pandas as pd


def read_from_console() -> str:
    """
    Read text input from the console.

    Returns:
        str: The text entered by the user.
    """
    text = input("Please enter your input: ")
    return text


def read_from_file(filepath: str) -> str:
    """
    Read text content from a file.

    Args:
        filepath (str): Path to the file to read.

    Returns:
        str: The content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    with open(filepath, mode="r", encoding="utf-8") as file:
        content = file.read()
        return content


def read_from_file_pandas(filepath: str) -> pd.DataFrame:
    """
    Read CSV file into a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV file to read.

    Returns:
        pd.DataFrame: DataFrame containing the CSV data.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    dataframe = pd.read_csv(
        filepath,
        encoding="utf-8"
    )
    return dataframe