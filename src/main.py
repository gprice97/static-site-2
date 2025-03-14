from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node
from nodesplitter import NodeSplitter


def main():
    splitter = NodeSplitter
    my_text_node = TextNode("This is my Text", TextType.NORMAL, "www.google.com")
    print(my_text_node.__repr__())
    my_html_node = HTMLNode("a", "Click here", [], {"href": "https://boot.dev"})
    print(my_html_node.__repr__())
    to_html_test = LeafNode("a", "Yahoo!", {"href": "https://www.yahoo.com", "alt-text": "I love the internet!"})
    print(to_html_test)
    node = TextNode("This is a text node", TextType.NORMAL)
    print(text_node_to_html_node(node))
    node_1 = TextNode("This is text with **BOLD** written all over it", TextType.NORMAL)
    new_nodes = splitter.split_nodes_delimiter([node_1], "**", TextType.BOLD)
    print(new_nodes)


if __name__ == "__main__":
    main()
