import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()