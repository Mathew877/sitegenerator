from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)


    def to_html(self):
        if self.tag == None:
            raise ValueError("parent nodes must have a tag")
        elif self.children == None or len(self.children) == 0:
            raise ValueError("parent nodes must have children")
        else:
            html_text = f"<{self.tag}"
            if self.props != None:
                html_text += self.props_to_html()
            html_text += ">"
            for child in self.children:
                html_text += child.to_html()
            html_text += f"</{self.tag}>"
            return html_text

