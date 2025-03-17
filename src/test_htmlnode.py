import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node2 = HTMLNode("p", "this is the text inside the tag", None, {"href": "https://www.google.com","target": "_blank"})
        assert node2.props_to_html() == ' href="https://www.google.com" target="_blank"'
    
    def test_repr(self):
        node = HTMLNode("p", "What a strange world", None, {"class": "primary"})
        self.assertEqual(node.__repr__(), "HTMLNode(p, What a strange world, None, {'class': 'primary'})")

    def test_values(self):
        node = HTMLNode("div", "I wish I could read")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "I wish I could read",)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)
        
if __name__ == "__main__":
    unittest.main()