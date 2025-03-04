from enum import Enum


class TextType(Enum):
    NORMAL_TEXT = "Normal Text"
    BOLD_TEXT = "Bold Text"
    ITALIC_TEXT = "Italic Text"
    CODE_TEXT = "Code Text"
    LINK_TEXT = "Link Text"
    IMAGE_TEXT = "Image Text"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        if self.text == other.text:
            if self.text_type == other.text_type:
                if self.url == other.url:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url if self.url else 'None'})"
