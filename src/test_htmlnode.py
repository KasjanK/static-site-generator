import unittest

from htmlnode import HTMLNode, LeafNode

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
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_p2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raises_value_error(self):
        node = LeafNode("p", "")  # Create a LeafNode with an empty value
        with self.assertRaises(ValueError):
            node.to_html()  
    
    def test_leaf_empty_tag_returns_value(self):
        node = LeafNode("", "Click me!")
        self.assertEqual(node.to_html(), 'Click me!')
        
        
if __name__ == "__main__":
    unittest.main()