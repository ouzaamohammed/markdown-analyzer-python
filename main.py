import sys


def get_markdown(path):
    try:
        with open(path) as f:
            markdown = f.read()
            return markdown
    except:
        print("path don't exists")
        sys.exit(0)


def is_heading(block):
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
        if is_heading(block):
            # remove any leading # and leading/trailing whitespaces
            stripped_block = block.lstrip("#").strip()
            count += len(stripped_block.split())
    return count


def is_unordered_list(block):
    lines = block.split("\n")
    for line in lines:
        if not line:
            continue
        if not line.startswith("- "):
            return False
    return True


def is_ordered_list(block):
    lines = block.split("\n")
    i = 1
    for line in lines:
        if not line:
            continue
        if not line.startswith(f"{i}. "):
            return False
        i += 1
    return True


def count_list_words(markdown):
    count = 0
    blocks = markdown.split("\n\n")
    for block in blocks:
        if is_unordered_list(block):
            # remove any leading - and leading/trailing whitespaces
            for line in block.split("\n"):
                stripped_line = line.lstrip("-").strip()
                count += len(stripped_line.split())
        if is_ordered_list(block):
            # remove any leading 1. and leading/trailing whitespaces
            i = 1
            for line in block.split("\n"):
                stripped_line = line.lstrip(f"{i}.").strip()
                count += len(stripped_line.split())
                i += 1
    return count


def count_paragraph_words(markdown):
    count = 0
    blocks = markdown.split("\n\n")
    for block in blocks:
        if is_heading(block) or is_ordered_list(block) or is_unordered_list(block):
            continue
        count += len(block.split())
    return count


def main():
    # check if path is passed
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_markdown>")
        sys.exit(1)

    filepath = sys.argv[1]
    markdown = get_markdown(filepath)

    heading_words = count_heading_words(markdown)
    list_words = count_list_words(markdown)
    paragraph_words = count_paragraph_words(markdown)
    total_words = heading_words + list_words + paragraph_words

    print("============ MARKDOWNBOT ============")
    print(f"Analyzing markdown found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Heading Count -------")
    print(f"Found {heading_words} heading words")
    print("--------- List Count -------")
    print(f"Found {list_words} list words")
    print("--------- Paragraph Count -------")
    print(f"Found {paragraph_words} paragraph words")


if __name__ == "__main__":
    main()
