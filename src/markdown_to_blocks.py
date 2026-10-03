from textnode import TextNode
from text_type import TextType


def markdown_to_blocks(markdown: str) -> list[str]:
    res = []
    split_md = markdown.split("\n\n")
    for i in split_md:
        stripped = i.strip()
        if stripped != "":
            res.append(stripped)
    return res
