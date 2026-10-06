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
        block_type = block_to_block_type(block)
        html_node.children.append(create_html_node_from_block(block))

    return html_node.children
        #TODO: Based on the type of block, create a new HTMLNode object with the proper data
        #TODO: Assign the proper child HTMLNode objects to the block node.
        #NOTE: Created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions. (Think TextNode -> HTMLNode)
def text_to_children(text: str) -> list[HTMLNode]:
    res = []
    create_text_node = text_to_textnodes(text)
    for node in create_text_node:
        res.append(text_node_to_html_node(node))

    return res

        #TODO: The "code" blck is a bit of a special case. It should not do any inline markdown parsing of its children. 
        #NOTE: Do not use text_to_children() for this block type. Manually make a TextNode and use text_node_to_html_node

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
        return HTMLNode(tag="blockquote", children=text_to_children(block))
    elif convert_block == BlockType.unordered_list:
        return HTMLNode("ul", children=HTMLNode("li", children=text_to_children(block.strip("-").strip())))
    elif convert_block == BlockType.ordered_list:
        items = block.split("\n")
        return HTMLNode("ol", children=[i for i in [HTMLNode("li", children=text_to_children(item.strip("0123456789.").strip())) for item in items]])
    elif convert_block == BlockType.code:
        text_node = TextNode(block, TextType.text)
        return HTMLNode("pre", children=text_to_children([HTMLNode("code", children=)]))
    elif convert_block == BlockType.heading:
        heading_level = block.count('#')
        return HTMLNode(tag=f"h{heading_level}", children=text_to_children(block.strip('#').strip()))
    elif convert_block == BlockType.paragraph:
        return HTMLNode(tag="p", children=text_to_children(block))
    else:
        raise Exception("Unsupported block type: " + str(convert_block))

