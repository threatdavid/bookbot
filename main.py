def read_file(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def word_count(text: str) -> int:
    return len(text.split())


def get_char_f(text: str) -> dict[str, int]:
    f_table = {}
    for char in (c.lower() for c in text if c.isalpha()):
        f_table[char] = f_table.get(char, 0) + 1
    return f_table


def main():
    path = "book/frankenstein.txt"
    content = read_file(path)
    word_count_result = word_count(content)
    char_f = get_char_f(content)
    

if __name__ == "__main__":
    main()