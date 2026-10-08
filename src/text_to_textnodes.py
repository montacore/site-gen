from textnode import TextNode
from split_nodes import *
from split_nodes_delimiter import split_nodes_delimiter
from text_type import TextType

def text_to_textnodes(text) -> list[TextNode]:
    text_node = TextNode(text, TextType.TEXT)
    node_list = [text_node]
    bold_nodes = split_nodes_delimiter(node_list, "**", TextType.BOLD)
    italic_nodes = split_nodes_delimiter(bold_nodes, "_", TextType.ITALIC)
    code_nodes = split_nodes_delimiter(italic_nodes, "`", TextType.CODE)
    image_nodes = split_nodes_image(code_nodes)
    final_nodes = split_nodes_link(image_nodes)
    return final_nodes

