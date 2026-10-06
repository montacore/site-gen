from blocktype import BlockType, block_to_block_type
from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_type import TextType
from text_to_textnode import text_to_textnode 


def markdown_to_html_node(markdown: str) -> HTMLNode:
   
    
    #TODO: 1.Split the markdown into blocks(BlockType) using markdown_to_blocks
    blocks = markdown_to_blocks(markdown)
    #TODO:Loop over each block
    for block in blocks:
        #NOTE: convert blocks to BlockType
        block_type = block_to_block_type(block)

        #TODO: Based on the type of block, create a new HTMLNode object with the proper data
        if block_type == BlockType.HEADING:
            heading = HTMLNode(tag=f"h{block.level}", children=text_to_children(block.text))

        #TODO: Assign the proper child HTMLNode objects to the block node.
        #NOTE: Created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions. (Think TextNode -> HTMLNode)

        #TODO: The "code" blck is a bit of a special case. It should not do any inline markdown parsing of its children. 
        #NOTE: Do not use text_to_children() for this block type. Manually make a TextNode and use text_node_to_html_node

    #TODO: Make all the block nodes children under a single parent HTML node, which should just be a div and return it.
        convert_block = block_to_block_type(block)
        if convert_block == "BlockType.quote":
            quote_node = HTMLNode(tag="blockquote", children=text_to_children(block.text))
        if convert_block == "BlockType.unordered_list":
            ul_node = HTMLNode("ul", children=text_to_children(convert_block))
        if convert_block == "ordered_list":
            ol_node = HTMLNode("ol", convert_block.text, children=text_to_children(convert_block ))



    #TODO: Create unit tests: 


    #FIXME: Quote blocks should be surrounded by a <blockquote> tag
    # unordered list blocks should be surrounded by a <ul> tag and each list item should be surrounded by a <li< tag.
    # Ordered list blocks should be surrounded by a <ol> tag and each list  item should be surrounded by a <li> tag.
    # Code bl ocks should be surrounded by a <code> tag nested inside a <pre> tag.
    # Heading should be surrounded by a <h1> to <h6> tag depending on the number of # characters.
    # Paragraphs should be surrounded by a <p> tag. I removed thewlines and replaced them with spaces.
    #
