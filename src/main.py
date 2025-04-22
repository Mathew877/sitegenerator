from textnode import *

def main():
	text_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(text_node)
	print("this string has a `code block` in it.".split("`"))
	print("**this string** starts with bold".split("**"))
	print("this string ends with _italics_".split("_"))

#main()
