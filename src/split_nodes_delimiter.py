from text_type import TextType
from textnode import TextNode


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    res = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            res.append(old_node)
        elif delimiter in old_node.text:
            sp = old_node.text.split(delimiter)
            if len(sp) % 2 != 0:
                for i, s in enumerate(sp):
                    if s == "":
                        continue
                    if i % 2 == 0:
                        node = TextNode(s, TextType.TEXT)
                    else:
                        node = TextNode(s, text_type)
                    res.append(node)
            else:
                raise ValueError("Invalid Markdown Syntax: No matching closing delimiter found")
        else:
            res.append(old_node)
    return res

