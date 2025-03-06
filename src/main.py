from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode
from textnode import TextType


def main():
    my_text_node = TextNode("This is my Text", TextType.NORMAL, "www.google.com")
    print(my_text_node.__repr__())
    my_html_node = HTMLNode("a", "Click here", [], {"href": "https://boot.dev"})
    print(my_html_node.__repr__())
    to_html_test = LeafNode("a", "Yahoo!", {"href": "https://www.yahoo.com", "alt-text": "I love the internet!"})
    print(to_html_test)



if __name__ == "__main__":
    main()
