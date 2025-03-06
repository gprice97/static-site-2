from htmlnode import HTMLNode
from htmlnode import html_escape
from htmlnode import is_valid_tag


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Validate the tag
        if tag is not None and not is_valid_tag(tag):
            raise ValueError(f"Invalid tag: {tag}")
        # Escape Values for Safe Rendering
        escaped_value = html_escape(value)
        # Escape Props for Safe Rendering
        escaped_props = {html_escape(k): html_escape(v) for k, v in props.items()} if props else None
        super().__init__(tag, escaped_value, None, escaped_props)

    def to_html(self):
        # Ensure that if my value is set to None, this is an invalid LeafNode
        if not self.value:
            raise ValueError("All Leaf Nodes must have a Value")
        # Ensure that if I do not have a tag, the LeafNode is rendered as raw Text
        elif self.tag is None:
            return self.value
        # Using my method from HTMLNode, I generate a prop_list and include that in my LeafNode
        prop_list = self.props_to_html()
        if prop_list:
            return f'<{self.tag} {prop_list}>{self.value}</{self.tag}>'
        # If there are no properties on my LeafNode, output a basic html element
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

