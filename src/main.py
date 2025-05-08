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
    text = "[This link has [brackets] in it](http://example.com)"
    text_2 = "[link](http://example.com/with-stuff)"
    print(splitter.extract_markdown_links(text))
    print(splitter.extract_markdown_links(text_2))
    text_3 = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.NORMAL)
    print(splitter.split_nodes_link([text_3]))
    text_4 = TextNode(
            "![Armadillo](https://i.imgur.com/armadillo.png) This is a picture of a Armadillo and ![RolyPoly](https://i.imgur.com/rolypoly.png) a picture of a Roly Poly",
            TextType.NORMAL,
        )
    print(splitter.split_nodes_image([text_3, text_4]))

    md = """
    This is **bolded** paragraph

    This is another paragraph with _italic_ text and `code` here
    This is the same paragraph on a new line

    - This is a list
    - with items
    """
    print(NodeSplitter.markdown_to_blocks(md))



if __name__ == "__main__":
    main()
