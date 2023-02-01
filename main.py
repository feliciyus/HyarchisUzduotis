import os
import json


def read_file_contents(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return "The file does not exist."


def count_symbols(file_contents):
    symbol_count = {}
    for symbol in file_contents:
        if symbol in symbol_count:
            symbol_count[symbol] += 1
        else:
            symbol_count[symbol] = 1
    return symbol_count


def sort_symbols(sort_by, symbol_count):
    if sort_by == "count":
        return sorted(symbol_count.items(), key=lambda x: x[1], reverse=True)
    return sorted(symbol_count.items())


def save_results(sorted_symbols, output_file):
    with open(output_file, "w") as f:
        for symbol, count in sorted_symbols:
            f.write(f"{symbol}: {count}\n")


def main():
    with open("settings.json", "r") as settings_file:
        data = json.load(settings_file)

    sort_by = data['sort_by']
    file_path = data['path_to_file']
    file_contents = read_file_contents(file_path)
    symbol_count = count_symbols(file_contents)
    sorted_symbols = sort_symbols(sort_by, symbol_count)
    save_results(sorted_symbols, "results.txt")


if __name__ == "__main__":
    main()
