import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode
from text_type import TextType
class TestTextToTextNodes(unittest.TestCase):

    def Test_Text_To_Textnodes(self):
        text = "Here is some text with **bold** some _italics_ and a little `code`"
        res = text_to_textnodes(text)
        self.assertEqual(res, [
            TextNode("Here is some text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" some ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" and a little ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ])

    def another_test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        res = text_to_textnodes(text)
        self.assertEqual(res, [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ])
