import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
    
    def test_normal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_invalid_text_type(self):
        invalid_node = TextNode("Invalid case", "invalid_type")  # Intentionally wrong type
        with self.assertRaises(Exception) as context:
            text_node_to_html_node(invalid_node)
        
        # Check exactly what exception message was raised
        self.assertEqual(str(context.exception), "Invalid text type provided: invalid_type")
    
    def test_link_type(self):
        # Create a TextNode for the LINK type
        link_node = TextNode("Click here", TextType.LINK, "https://example.com")
        # Convert it to an HTMLNode
        html_node = text_node_to_html_node(link_node)
        
        # Assertions to check correctness
        self.assertEqual(html_node.tag, "a")  # Ensure the tag is <a>
        self.assertEqual(html_node.value, "Click here")  # Ensure the text content matches
        self.assertEqual(html_node.props, {"href": "https://example.com"})  # Ensure the href matches

    def test_image_type(self):
        # Create a TextNode for the IMAGE type
        image_node = TextNode("A beautiful image", TextType.IMAGE, "https://example.com/image.png")
        # Convert it to an HTMLNode
        html_node = text_node_to_html_node(image_node)
        
        # Assertions to check correctness
        self.assertEqual(html_node.tag, "img")  # Ensure the tag is <img>
        self.assertEqual(html_node.value, "")  # Ensure value is an empty string for images
        self.assertEqual(html_node.props, {"src": "https://example.com/image.png", "alt": "A beautiful image"})  # Check src and alt props
        
        
if __name__ == "__main__":
    unittest.main()