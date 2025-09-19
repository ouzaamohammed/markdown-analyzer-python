import sys

def main():
    # check if path is passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_markdown>")
        sys.exit(1)

    print("hello from main")

if __name__ == "__main__":
    main()