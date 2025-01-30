import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from text_node_to_html_node import text_node_to_html_node


class TestTextNode(unittest.TestCase):
   
    def test_leaf_rendering1(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        b = leaf.to_html()
        desired_output = "<p>This is a paragraph of text.</p>"
        self.assertEqual(b, desired_output)


    def test_leaf_rendering2(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        b = leaf.to_html()
        desired_output = '<a href="https://www.google.com">Click me!</a>'
        #print(f"Leaf node is: \n {leaf}\n leaf props is: {leaf.props}")
        #print(f"b is:\n{b}")
        self.assertEqual(b, desired_output)
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a  third node", TextType.ITALIC)
        node_url = node.url
        #print(node_url)
        self.assertEqual(node_url, None)


    def test_html_node_no_eq_(self):
        html_node = HTMLNode('p', "This is a simple sentence for my html node", {"href":"https://wwww.google.com", "target":"_blank"},4 )
        html_node2 = HTMLNode('p', "This is a simple sentence for my html node", {"href":"https://wwww.google.com", "target":"_blank"},3)
        self.assertNotEqual(html_node, html_node2)

    def test_html_node_eq_(self):
        html_node = HTMLNode('p', "This is a node testing the repr sentence for my html node", {"href":"https://wwww.google.com", "target":"_blank"},4 )
        print(html_node)
        a = html_node.props_to_html()
        print(a)   


    def test_leaf_rendering3(self):
        leaf = LeafNode(None, "Click me!")
        print(f"your 3rd leaf is: {leaf}")
        b = leaf.to_html()
        print(f"your leaf to html is: {leaf}")
        desired_output = "Click me!"
        self.assertEqual(b, desired_output)


    def test_recursion1(self):
        node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

        
        print(f"your parent node for recursion is {node} and the children are {node.children}")
        parent_to_html = node.to_html()
        desired_output = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(parent_to_html, desired_output)

    def test_recursion2(self):
        node = ParentNode(
        "div",
        [LeafNode(None, "test")]
)
        
        print(f"your parent node for recursion is {node} and the children are {node.children}")
        parent_to_html = node.to_html()
        desired_output = "<div>test</div>"
        self.assertEqual(parent_to_html, desired_output)

    def test_nested_parent_nodes(self):
    # Create a nested structure:
    # <div>
    #     <p>Some text<b>bold text</b></p>
    #     <p>More text</p>
    # </div>
    
        inner_p1 = ParentNode(
            "p",
            [
                LeafNode(None, "Some text"),
                LeafNode("b", "bold text")
            ]
        )
        
        inner_p2 = ParentNode(
            "p",
            [LeafNode(None, "More text")]
        )
        
        outer_div = ParentNode(
            "div",
            [inner_p1, inner_p2]
        )
        
        result = outer_div.to_html()
        expected = "<div><p>Some text<b>bold text</b></p><p>More text</p></div>"
        self.assertEqual(result, expected)

        
    def test_text_node_to_html_node(self):
        # Test TEXT type
        node = TextNode("Just plain text", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag , None)
        self.assertEqual(html.value , "Just plain text")
        self.assertEqual(html.props , None)
    
    def test_text_node_to_html_node2(self):
        # Test BOLD type
        node = TextNode("Bold text", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag , "b")
        self.assertEqual(html.value , "Bold text")
        self.assertEqual(html.props , None)

    def test_text_node_to_html_node3(self):
       # Test ITALIC type
        node = TextNode("Italic text", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual( html.tag , "i")
        self.assertEqual(html.value, "Italic text")
        self.assertEqual(html.props, None)

    def test_text_node_to_html_node4(self):
        # Test CODE type
        node = TextNode("Code block", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag , "code")
        self.assertEqual(html.value , "Code block")
        self.assertEqual(html.props , None)

    def test_text_node_to_html_node5(self):    
        # Test LINK type
        node = TextNode("Click me", TextType.LINK, "https://www.boot.dev")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag , "a")
        self.assertEqual(html.value , "Click me")
        self.assertEqual(html.props , {"href": "https://www.boot.dev"})

    def test_text_node_to_html_node6(self):
        # Test IMAGE type
        node = TextNode("Alt text", TextType.IMAGE, "https://boot.dev/img.png")
        html = text_node_to_html_node(node)
        self.assertEqual( html.tag , "img")
        self.assertEqual( html.value , "")
        self.assertEqual( html.props , {"src": "https://boot.dev/img.png", "alt": "Alt text"})

        
   

if __name__ == "__main__":
    unittest.main()