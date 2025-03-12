from textnode import TextType, TextNode


class NodeSplitter:
    @staticmethod
    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        new_nodes = []
        for node in old_nodes:
            if delimiter not in node.text:
                raise Exception("Delimiter does not match provided text")
            if node.text_type is TextType.NORMAL:
                new_nodes.append(node)
            elif node.text_type is TextType.BOLD:
                text_list = node.text.split(delimiter)
                new_nodes.extend(
                    [TextNode(text_list[0], TextType.NORMAL),
                     TextNode(text_list[1], text_type),
                     TextNode(text_list[2], TextType.NORMAL)
                     ])
            elif node.text_type is TextType.ITALIC:
                text_list = node.text.split(delimiter)
                new_nodes.extend(
                    [TextNode(text_list[0], TextType.NORMAL),
                     TextNode(text_list[1], text_type),
                     TextNode(text_list[2], TextType.NORMAL)
                     ])
            elif node.text_type is TextType.CODE:
                text_list = node.text.split(delimiter)
                new_nodes.extend(
                    [TextNode(text_list[0], TextType.NORMAL),
                     TextNode(text_list[1], text_type),
                     TextNode(text_list[2], TextType.NORMAL)
                     ])
        return new_nodes





