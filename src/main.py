from textnode import *
from markdown_parser import *

def main():
	'''
	text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(text_node)
	print("this string has a `code block` in it.".split("`"))
	print("**this string** starts with bold".split("**"))
	print("this string ends with _italics_".split("_"))
	'''
	text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
	print(extract_markdown_images(text))
	# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

	text2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
	print(extract_markdown_links(text2))
	# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]


#main()

