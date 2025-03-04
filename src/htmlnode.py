class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("This method must be implemented by a subclass")

    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join(f'{k}="{v}"' for k, v in self.props.items())

    def __repr__(self):
        return (f"HTMLNode({self.tag}, "
                f"{self.value if self.value else 'None'}, "
                f"{self.children if self.children else 'None'}, "
                f"{self.props if self.props else 'None'})")

