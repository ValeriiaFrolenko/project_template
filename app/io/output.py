def write_to_console(text: str) -> None:
    print(text)

def write_to_file(filepath: str, text: str) -> None:
    with open(filepath, mode="w", encoding="utf-8") as file:
        file.write(text)