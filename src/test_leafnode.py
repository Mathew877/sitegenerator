import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertTrue(node.to_html(), '<a href="https://www.google.com">Click me!</a>')    

if __name__ == "__main__":
    unittest.main()