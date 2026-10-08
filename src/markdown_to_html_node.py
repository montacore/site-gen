from blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_type import TextType
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node


def markdown_to_html_node(markdown: str) -> HTMLNode:
   
    html_node = ParentNode(tag="div", children=[])
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        #NOTE: convert blocks to BlockType
        if html_node.children is not None:
            html_node.children.append(create_html_node_from_block(block))
    return html_node


def text_to_children(text: str) -> list[HTMLNode]:
    """
        function for use by each different type of htmlnode instance to pass text to the child nodes below the parent node being created.

        args:
            text: str - block text provided to the function after greater markdown string is seperated into blocks based on markdown type.

        returns:
            list[ParentNodes] 

        Methodology:
            create empty result list
            create text node using text_to_textnodes(text)[passing the entire text string]
            for each node within those created text nodes, append the result of calling text_node_to_html_node on each individual node within the iteration.
    """
    res = []
    create_text_node = text_to_textnodes(text)
    for node in create_text_node:
        res.append(text_node_to_html_node(node))

    return res

def create_html_node_from_block(block: str) -> HTMLNode:
    convert_block = block_to_block_type(block)
    if convert_block == BlockType.quote:
        cleaned_lines = []
        for line in block.strip().split("\n"):
            cleaned_line = line.lstrip("> ")
            cleaned_lines.append(cleaned_line)

        cleaned_text = "\n".join(cleaned_lines)
        return ParentNode(tag="blockquote", children=text_to_children(cleaned_text))
    elif convert_block == BlockType.unordered_list:
        items = block.split("\n")
        return ParentNode("ul", children=[i for i in [ParentNode("li", children=text_to_children(item.strip('-').strip())) for item in items]])
    elif convert_block == BlockType.ordered_list:
        items = block.split("\n")
        return ParentNode("ol", children=[i for i in [ParentNode("li", children=text_to_children(item.strip("0123456789.").strip())) for item in items]])
    elif convert_block == BlockType.code:
        code_slice = block[4:-3]
        text_node = TextNode(code_slice, TextType.TEXT)
        return ParentNode("pre", children=[ParentNode("code", children=[text_node_to_html_node(text_node)])])
    elif convert_block == BlockType.heading:
        heading_level = len(block) - len(block.lstrip("#"))
        return ParentNode(tag=f"h{heading_level}", children=text_to_children(block[heading_level:].strip()))
    elif convert_block == BlockType.paragraph:
        sp = block.split("\n")
        j = " ".join(sp)
        return ParentNode(tag="p", children=text_to_children(j))
    else:
        raise Exception("Unsupported block type: " + str(convert_block))

