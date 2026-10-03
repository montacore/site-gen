import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode
from text_type import TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("This is some text with **inline** Markdown", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, [
            TextNode("This is some text with ", TextType.TEXT),
            TextNode("inline", TextType.BOLD),
            TextNode(" Markdown", TextType.TEXT),
        ])

    def test_no_delimiter(self):
        node = TextNode("This is a text node with no inline MD delimiter", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertEqual(split_node, [node])

    def test_empty_start_of_delimited_string(self):
        node = TextNode("`code` in this inline text", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(split_node, [
            TextNode("code", TextType.CODE),
            TextNode(" in this inline text", TextType.TEXT),
        ])

