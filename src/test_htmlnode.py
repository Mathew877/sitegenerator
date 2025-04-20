import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_empty_node(self):
        node = HTMLNode()
        self.assertEqual(node.tag, None)
        self.assertEqual(node.value, None)
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props = { "href" : "http://example.com", "target": "_blank"}
        node = HTMLNode("a", "click here", None, props)
        expected_value = ' href="http://example.com" target="_blank"'
        value = node.props_to_html()
        self.assertEqual(value, expected_value)

    def test_props_to_html_diff(self):
        props = { "href" : "http://example.com", "target": "_blank"}
        node = HTMLNode("a", "click here", None, props)
        props2 = { "src" : "http://google.com/i/logo.png", "height": "16", "weights": "16"}
        node2 = HTMLNode("img", None, None, props2)
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertTrue(node.to_html(), '<a href="https://www.google.com">Click me!</a>')    

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


if __name__ == "__main__":
    unittest.main()