from text_type import TextType
from textnode import TextNode
from copy_to_public import copy_static

def main() -> None:
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn)
    copy_static()

if __name__ == "__main__":
    main()
