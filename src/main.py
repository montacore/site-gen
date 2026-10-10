from text_type import TextType
from textnode import TextNode
from copy_to_public import copy_static
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
import sys

def main() -> None:
    if sys.argv[1]:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static()
    generate_pages_recursive("./content/", "./template.html", "./docs/", basepath)

if __name__ == "__main__":
    main()
