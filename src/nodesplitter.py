from textnode import TextType, TextNode
import re


class NodeSplitter:
    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if delimiter not in node.text:
                new_nodes.append(TextNode(node.text, node.text_type))
            else:
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

    @staticmethod
    def split_nodes_link(old_nodes):
        new_nodes = []
        for node in old_nodes:
            # If node is not text type normal then append it and start a new loop
            if node.text_type != TextType.NORMAL:
                new_nodes.append(node)
                continue
            link_text = NodeSplitter.extract_markdown_links(node.text)
            if not link_text:
                new_nodes.append(node)
                continue
            current_node_text = node.text
            for text, url in link_text:
                sections = current_node_text.split(f"[{text}]({url})", 1)
                if sections[0]:
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                new_nodes.append(TextNode(text, TextType.LINK, url))
                if len(sections) > 1:
                    current_node_text = sections[1]
                else:
                    current_node_text = ""
            if current_node_text:
                new_nodes.append(TextNode(current_node_text, TextType.NORMAL))
        return new_nodes

    @staticmethod
    # Defines the function split_nodes_image and takes in a list of TextNodes
    def split_nodes_image(old_nodes):
        # Creates an empty list that we can save our processed TextNodes to
        new_nodes = []
        # Loops through the list of TextNodes one at a time
        for node in old_nodes:
            # If node is not text type normal then we don't process it, append it to new_nodes and check the next node
            if node.text_type != TextType.NORMAL:
                new_nodes.append(node)
                continue
            # Utilize my extract_markdown_imagers function to gather the alt-text and url from the TextNode's Text
            # The image_text of the node will be in the format [(alt-text, url)] Ex. [("Cute Armadillo", "www.pic.com/Armadillo.png")]
            image_text = NodeSplitter.extract_markdown_images(node.text)
            # If there is no image inside the text of the TextNode, we append it to new_nodes and check the next node
            if not image_text:
                new_nodes.append(node)
                continue
            # We take in the text of the current node, so we can process it in the following for loop
            current_node_text = node.text
            # This for loop will loop through each match that was found within the current node
            for alt_text, url in image_text:
                # This will split the current node's text at the first occurence of the image markdown ![this](format)
                # The 1 limits the split function to one split, so output of this will look like [text_before_image, text_after_image]
                sections = current_node_text.split(f"![{alt_text}]({url})", 1)
                # If the first element in the sections array is "" this indicates that the image markdown was the first thing found in the text
                if sections[0]:
                    # If there IS a sections[0] present then we add it as a normal text node to new_nodes
                    new_nodes.append(TextNode(sections[0], TextType.NORMAL))
                # Adds a node for the detected image, inserting the alt text and url
                new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
                # Updates the current_node_text by setting it to the "text_after_image" portion, we can restart the processing with that text
                if len(sections) > 1:
                    current_node_text = sections[1]
                else:
                    current_node_text = ""
            # If there is remaining text after processing all the images in a node, then we add that as a normal text node
            if current_node_text:
                new_nodes.append(TextNode(current_node_text, TextType.NORMAL))
        return new_nodes

    def text_to_text_nodes(text):
        nodes = [TextNode(text, TextType.NORMAL)]
        nodes = NodeSplitter.split_nodes_delimiter(nodes, '**', TextType.BOLD)
        nodes = NodeSplitter.split_nodes_delimiter(nodes, '_', TextType.ITALIC)
        nodes = NodeSplitter.split_nodes_delimiter(nodes, '`', TextType.CODE)
        nodes = NodeSplitter.split_nodes_image(nodes)
        nodes = NodeSplitter.split_nodes_link(nodes)
        return [node for node in nodes if node.text != ""]

    # Working on this part
    def markdown_to_blocks(markdown):
        blocks = markdown.split('\n\n')
        clean_blocks = []

        for block in blocks:
            stripped_block = block.strip()
            if not stripped_block:
                continue

            lines = stripped_block.split('\n')
            cleaned_lines = [line.strip() for line in lines]
            clean_block = '\n'.join(cleaned_lines)
            clean_blocks.append(clean_block)

        return clean_blocks
