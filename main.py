from app import io

def main():
    text_from_console = io.read_from_console()

    io.write_to_console(text_from_console)
    io.write_to_file("data/result_console.txt", text_from_console)

    text_from_file = io.read_from_file("data/test.txt")

    io.write_to_console(text_from_file)
    io.write_to_file("data/result_file.txt", text_from_file)

    text_from_file_pandas = io.read_from_file_pandas("data/test.csv")

    io.write_to_console(text_from_file_pandas.to_csv(index=False))
    io.write_to_file("data/result_file_pandas.txt", text_from_file_pandas.to_csv(index=False))

if __name__ == "__main__":
    main()