def write_to_console(text: str) -> None:
    """
    Write text to the console.

    Args:
        text (str): The text to print to the console.
    """
    print(text)


def write_to_file(filepath: str, text: str) -> None:
    """
    Write text to a file.

    Args:
        filepath (str): Path to the file to write.
        text (str): The text content to write to the file.

    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    with open(filepath, mode="w", encoding="utf-8") as file:
        file.write(text)