class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_string = ''
        for key, value in self.props.items():
            props_string += f' {key}="{value}"'
        return props_string

    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("leaf nodes must have a value")
        elif self.tag is None:
            return self.value
        elif self.props != None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


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
        
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"