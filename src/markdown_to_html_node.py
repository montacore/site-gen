from blocktype import BlockType, block_type_to_html
from markdown_to_blocks import markdown_to_blocks
from textnode import TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_type import TextType
from text_to_textnode import text_to_textnode 


def markdown_to_html_node(markdown: str) -> HTMLNode:
    pass
    #TODO: 1.Split the markdown into blocks(BlockType) using markdown_to_blocks

    #TODO:Loop over each block

        #TODO: Determine the type of block(existing function)
        
        #TODO: Based on the type of block, create a new HTMLNode object with the proper data                      o

        #TODO: Assign the proper child HTMLNode objects to the block node.
        #NOTE: Created a shared text_to_children(text) function that works for all block types. It takes a string of text and returns a list of HTMLNodes that represent the inline markdown using previously created functions. (Think TextNode -> HTMLNode)

        #TODO: The "code" blck is a bit of a special case. It should not do any inline markdown parsing of its children. 
        #NOTE: Do not use text_to_children() for this block type. Manually make a TextNode and use text_node_to_html_node

    #TODO: Make all the block nodes children under a single parent HTML node, which should just be a div and return it.
    




    #TODO: Create unit tests: 


    #FIXME: Quote blocks should be surrounded by a <blockquote> tag
    # unordered list blocks should be surrounded by a <ul> tag and each list item should be surrounded by a <li< tag.
    # Ordered list blocks should be surrounded by a <ol> tag and each list  item should be surrounded by a <li> tag.
    # Code bl ocks should be surrounded by a <code> tag nested inside a <pre> tag.
    # Heading should be surrounded by a <h1> to <h6> tag depending on the number of # characters.
    # Paragraphs should be surrounded by a <p> tag. I removed thewlines and replaced them with spaces.
    #
