

import os
from collections import defaultdict

def count_file_types(directory):
    file_type_counts = defaultdict(int)

    for root, _, files in os.walk(directory):
        for file in files:
            file_extension = os.path.splitext(file)[1]
            file_type_counts[file_extension] += 1

    return file_type_counts

def main():
    directory = r"D:\Alpine Wave\scraper\falcon 9"
    if os.path.exists(directory):
        file_type_counts = count_file_types(directory)
        print("\nFile type counts in the given directory:")
        for file_type, count in file_type_counts.items():
            print(f"{file_type}: {count}")
    else:
        print("Invalid directory path. Please check the path and try again.")

if __name__ == "__main__":
    main()