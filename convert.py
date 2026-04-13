 
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(CURRENT_DIR, "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from src.converter import process_article  


def main():
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input.html> <output.xml>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        sys.exit(1)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    process_article(input_path, output_path)
    print(f"XML generated at: {output_path}")


if __name__ == "__main__":
    main()