def read_file(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def word_count(text: str) -> int:
    return len(text.split())


def main():
    path = "book/frankenstein.txt"
    content = read_file(path)
    word_count_result = word_count(content)

if __name__ == "__main__":
    main()