import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_eq(self):
        node = LeafNode("a", "this is some text", {"color":"red"})
        node2 = LeafNode("a", "this is some text", {"color":"red"})
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = LeafNode("div", "div test text", {"color": "green"})
        node2 = LeafNode("span", "span test text", {"color": "red"})
        self.assertNotEqual(node, node2)

    def test_leaf_to_html(self):
        node = LeafNode("p", "paragraph", {"target":"_target"})
        node2 = LeafNode("p", "paragraph", {"target":"_target"})
        res = node.to_html()
        res2 = node2.to_html()
        self.assertEqual(res, res2)
