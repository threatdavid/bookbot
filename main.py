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


def sort_f(char_f: dict[str, int]): 
    return dict(sorted(char_f.items(), key=lambda char: char[1], reverse=True))


def log_report(book_path: str, word_count: int, char_f: dict[str, int]) -> str:
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")    
    for char in sort_f(char_f):
        print(f"The '{char}' character was found {char_f[char]} times")
    print("--- End report ---")


def main():
    path = "book/frankenstein.txt"
    content = read_file(path)
    word_count_result = word_count(content)
    char_f = get_char_f(content)
    log_report(path, word_count_result, char_f)


if __name__ == "__main__":
    main()