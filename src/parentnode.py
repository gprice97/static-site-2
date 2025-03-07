from htmlnode import HTMLNode
from htmlnode import is_valid_tag
from htmlnode import html_escape


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not is_valid_tag(tag):
            raise ValueError(f"Invalid tag: {tag}")
        escaped_props = {html_escape(k): html_escape(v) for k, v in props.items()} if props else None
        super().__init__(tag, None, children, escaped_props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid Tag")
        elif self.children is None:
            raise ValueError("Invalid Child Node")
        prop_list = self.props_to_html()
        if prop_list:
            html = f"<{self.tag} {prop_list}>"
        else:
            html = f"<{self.tag}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
