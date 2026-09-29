import unittest
from textnode import TextNode
from text_type import TextType

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

if __name__ == "__main__":
    unittest.main()
