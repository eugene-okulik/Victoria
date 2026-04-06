import argparse
import os
from datetime import datetime


def get_args():
    parser = argparse.ArgumentParser(description="Log file analyzer")
    parser.add_argument("path", help="The full path to the logs directory")
    parser.add_argument("-t", "--text", help="free user text")
    return parser.parse_args()


def print_error(file_name, lines, text):
    for line in lines:
        words = line.lower().split()
        index = words.index(text.lower())
        max_index = index + 5 if index + 5 < len(words) else len(words)
        min_index = index - 5 if index - 5 > 2 else 2
        snippet = ' '.join(words[min_index:max_index])
        time = ' '.join(words[:2])
        print(f'{file_name}\t{time}\t{snippet}')


def is_date(line):
    if len(line) < 23:
        return False
    try:
        datetime.fromisoformat(line[:23])
        return True
    except ValueError:
        return False


def main(path, text):
    base_path = os.path.abspath(path)
    if not os.path.exists(base_path):
        print(f'{base_path} does not exist')
        return
    if text is None or text == '':
        print("Text shouldn't be empty")
        return
    if os.path.isfile(base_path):
        files = [os.path.basename(base_path)]
        base_path = os.path.dirname(base_path)
    else:
        files = os.listdir(base_path)
    for file in files:
        file_path = os.path.join(base_path, file)
        with open(file_path, 'r') as f:
            lines = f.readlines()
        full_lines = []
        for line in lines:
            if is_date(line.strip()):
                full_lines.append(line)
            else:

                full_lines[-1] += line

        relevant_lines = [line for line in full_lines if text.lower() in line.lower().split()]
        if len(relevant_lines) > 0:
            print_error(file, relevant_lines, text)


if __name__ == '__main__':
    # get the arguments from command line
    args = get_args()
    # run main function with arguments
    main(args.path, args.text)
