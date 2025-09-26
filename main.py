import sys


def get_markdown(path):
    try:
        with open(path) as f:
            markdown = f.read()
            return markdown
    except:
        print("path don't exists")
        sys.exit(0)


def isHeading(block):
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return True
    return False


def count_heading_words(markdown):
    count = 0
    blocks = markdown.split("\n\n")
    for block in blocks:
        if isHeading(block):
            # remove any leading # and leading/trailing whitespaces
            stripped_block = block.lstrip("#").strip()
            count += len(stripped_block.split())
    return count


def main():
    # check if path is passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_markdown>")
        sys.exit(1)

    path = sys.argv[1]
    markdown = get_markdown(path)

    heading_words_count = count_heading_words(markdown)
    print(f"heading words count: {heading_words_count}")


if __name__ == "__main__":
    main()
