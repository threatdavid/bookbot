def read_file(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def main():
    path = "book/frankenstein.txt"
    content = read_file(path)

if __name__ == "__main__":
    main()