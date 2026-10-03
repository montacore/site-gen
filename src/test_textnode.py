import unittest
from textnode import TextNode, text_node_to_html_node
from text_type import TextType
from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK, "https://boot.dev")
        node2 = TextNode("This is a text Node", TextType.LINK, "https://google.com")
        self.assertNotEqual(node, node2)

    def test_img_eq(self):
        node = TextNode("This is a text image node", TextType.IMAGE, "https://image.com")
        node2 = TextNode("This is a text image node", TextType.IMAGE, "https://image.com")
        self.assertEqual(node, node2)

    def test_diff_tt(self):
        node = TextNode("this is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("This is a link node", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def text_img(self):
        node = TextNode("This is an img node", TextType.IMAGE, "https://image.com/image")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, TextType.IMAGE)
        self.assertEqual(html_node.value, "This is an img node")
        self.assertEqual(html_node.props, {"src":"https://image.com/image","alt": "This is an img node" })


if __name__ == "__main__":
    unittest.main()
