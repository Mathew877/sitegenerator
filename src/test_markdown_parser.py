import unittest

from textnode import TextNode, TextType
from markdown_parser import *


class TestMarkdownParser(unittest.TestCase):
    def test_split_nodes_delimiter_start(self):
        node = TextNode("This is text with _italics_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected_nodes = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_mid(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)
        #maybe it needs to use assertAlmostEqual as these are objects?
    
    def test_split_nodes_delimiter_end(self):
        node = TextNode("**This is** text with bold words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected_nodes = [
            TextNode("This is", TextType.BOLD),
            TextNode(" text with bold words", TextType.TEXT)
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_missing(self):
        node = TextNode("**This is bold text that is missing the end delimiter", TextType.TEXT)
        with self.assertRaises(Exception) as ex:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(ex.exception), "invalid Markdown syntax")

    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multiple(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
	    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    def test_extract_markdown_links(self):
        text = "This is text with a link [to google](https://google.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to google", "https://google.com")], matches)
    
    def test_extract_markdown_links_multiple(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)



if __name__ == "__main__":
    unittest.main()