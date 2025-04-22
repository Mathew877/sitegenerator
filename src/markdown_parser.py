from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            #TEXT type; perform split and parse new nodes
            split_text = node.text.split(delimiter)
            if len(split_text) != 3:
                raise Exception("invalid Markdown syntax")
            
            # based on split, the second item [1] will always be the new text type
            # however the first [0] or last [2] might be empty
            if split_text[0] != "":
                new_nodes.append(TextNode(split_text[0], TextType.TEXT))
            
            new_nodes.append(TextNode(split_text[1], text_type))

            if split_text[2] != "":
                new_nodes.append(TextNode(split_text[2], TextType.TEXT))

    return new_nodes

