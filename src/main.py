from text_type import TextType
from textnode import TextNode
from copy_to_public import copy_static
from generate_page import generate_page
from generate_pages_recursive import generate_pages_recursive
def main() -> None:
    copy_static()
    generate_pages_recursive("./content/", "./template.html", "./public/")

if __name__ == "__main__":
    main()
