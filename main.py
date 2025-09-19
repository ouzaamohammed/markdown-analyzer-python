import sys

def get_markdown(path):
    with open(path) as f:
        markdown = f.read()
        return markdown

def main():
    # check if path is passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_markdown>")
        sys.exit(1)

    path = sys.argv[1]
    markdown = get_markdown(path)
    print(markdown)

if __name__ == "__main__":
    main()