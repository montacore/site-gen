from text_type import TextType
from textnode import TextNode
from copy_to_public import copy_static
from generate_page import generate_page
def main() -> None:
    copy_static()
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    

if __name__ == "__main__":
    main()
