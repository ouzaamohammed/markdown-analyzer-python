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

    path = sys.argv[1]
    markdown = get_markdown(path)

    heading_words_count = count_heading_words(markdown)
    print(f"heading words count: {heading_words_count}")

    list_words_count = count_list_words(markdown)
    print(f"list words count: {list_words_count}")

    paragraph_words_count = count_paragraph_words(markdown)
    print(f"paragraph words count: {paragraph_words_count}")


if __name__ == "__main__":
    main()
