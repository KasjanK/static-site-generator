import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node2, node3)
    
    def test_url_difference(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "this is a link")
        self.assertNotEqual(node, node2)
    
    def test_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()