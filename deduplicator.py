import sys
import os

#This file will help to remove duplicate lines in txt file.
# Very Useful active recon

def remove_duplicates(input_file):
    seen = set()
    duplicate_count = 0
    total_lines = 0
    output_file = "final_unique_sites.txt"

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            total_lines += 1
            if line not in seen:
                outfile.write(line)
                seen.add(line)
            else:
                duplicate_count += 1

    print(f"Total lines read: {total_lines}")
    print(f"Duplicate lines removed: {duplicate_count}")
    print(f"Cleaned file saved as: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 remove_duplicates.py <input_file>")
        sys.exit(1)

    input_path = sys.argv[1]

    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        sys.exit(1)

    remove_duplicates(input_path)
