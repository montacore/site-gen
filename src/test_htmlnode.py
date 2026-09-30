import unittest
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):
     def test_eq(self):
        node = HTMLNode("span", "this is a text node", None, {"target":"_target"})
        node2 = HTMLNode("span", "this is a text node", None, {"target":"_target"})
        self.assertEqual(node, node2)

     def test_not_eq(self):
        node = HTMLNode("div", "this is a text node", None, {"target":"_target"})
        node2 = HTMLNode("span", "this is not a text node", None, {"type":"None"})
        self.assertNotEqual(node, node2)

     def test_props_eq(self):
        node = HTMLNode("div", "this is a text node", None, {"target": "_target"})
        prop_props = node.props_to_html()
        node2 = HTMLNode("div", "this is a text node", None, {"target": "_target"})
        node2_props = node2.props_to_html()
        self.assertEqual(prop_props, node2_props)
