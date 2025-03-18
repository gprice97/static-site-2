from textnode import TextType, TextNode
import re


class NodeSplitter:
    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if delimiter not in node.text:
                new_nodes.extend(TextNode(node.text, node.text_type))
            node_text_list = node.text.split(delimiter)
            if len(node_text_list) % 2 != 1:
                raise Exception("There is a delimiter present without it's matching pair")
            for index, node_text in enumerate(node_text_list):
                if index % 2 == 1:
                    new_nodes.append(TextNode(node_text, text_type))
                else:
                    new_nodes.append(TextNode(node_text, node.text_type))
        return new_nodes

    # Example text: "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
    # Example return: # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    @staticmethod
    def extract_markdown_images(text):
        match_image_text = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
        return match_image_text

    # Example text: "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # Example return [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    @staticmethod
    def extract_markdown_links(text):
        match_image_text = re.findall(r"\[(.*?)\]\((.*?)\)", text)
        return match_image_text
