from textnode import TextNode
from textnode import TextType


def main():
    my_text_node = TextNode("This is my Text", TextType.NORMAL_TEXT, "www.google.com")
    print(my_text_node.__repr__())


if __name__ == "__main__":
    main()
