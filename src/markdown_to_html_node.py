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
   
    html_node = HTMLNode(tag="div", children=[])
    #TODO: 1.Split the markdown into blocks(BlockType) using markdown_to_blocks
    blocks = markdown_to_blocks(markdown)
    #TODO:Loop over each block
    for block in blocks:
        #NOTE: convert blocks to BlockType
        if html_node.children is not None:
            html_node.children.append(create_html_node_from_block(block))
    return html_node
    #TODO: Based on the type of block, create a new HTMLNode object with the proper data
    #TODO: Assign the proper child HTMLNode objects to the block node.
    #NOTE: Created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions. (Think TextNode -> HTMLNode)


def text_to_children(text: str) -> list[HTMLNode]:
    """
        function for use by each different type of htmlnode instance to pass text to the child nodes below the parent node being created.

        args:
            text: str - block text provided to the function after greater markdown string is seperated into blocks based on markdown type.

        returns:
            list[HTMLNodes] 

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

    #TODO: Make all the block nodes children under a single parent HTML node, which should just be a div and return it.
    #TODO: Create unit tests: 


    #FIXME: Quote blocks should be surrounded by a <blockquote> tag
    # unordered list blocks should be surrounded by a <ul> tag and each list item should be surrounded by a <li< tag.
    # Ordered list blocks should be surrounded by a <ol> tag and each list  item should be surrounded by a <li> tag.
    # Code bl ocks should be surrounded by a <code> tag nested inside a <pre> tag.
    # Heading should be surrounded by a <h1> to <h6> tag depending on the number of # characters.
    # Paragraphs should be surrounded by a <p> tag. I removed thewlines and replaced them with spaces

def create_html_node_from_block(block: str) -> HTMLNode:
    convert_block = block_to_block_type(block)
    if convert_block == BlockType.quote:
        cleaned_lines = []
        for line in block.strip().split("\n"):
            cleaned_line = line.lstrip("> ")
            cleaned_lines.append(cleaned_line)

        cleaned_text = "\n".join(cleaned_lines)
        return HTMLNode(tag="blockquote", children=text_to_children(cleaned_text))
    elif convert_block == BlockType.unordered_list:
        items = block.split("\n")
        return HTMLNode("ul", children=[i for i in [HTMLNode("li", children=text_to_children(item.strip('-').strip())) for item in items]])
    elif convert_block == BlockType.ordered_list:
        items = block.split("\n")
        return HTMLNode("ol", children=[i for i in [HTMLNode("li", children=text_to_children(item.strip("0123456789.").strip())) for item in items]])
    elif convert_block == BlockType.code:
        text_node = TextNode(block, TextType.TEXT)
        return HTMLNode("pre", children=[HTMLNode("code", children=[text_node_to_html_node(text_node)])])
    elif convert_block == BlockType.heading:
        heading_level = len(block) - len(block.lstrip("#"))
        return HTMLNode(tag=f"h{heading_level}", children=text_to_children(block[heading_level:].strip()))
    elif convert_block == BlockType.paragraph:
        return HTMLNode(tag="p", children=text_to_children(block))
    else:
        raise Exception("Unsupported block type: " + str(convert_block))

md = """
### This is a heading

- This is a list item
- This is another list item
- and another
"""
print(type(markdown_to_html_node(md)))
