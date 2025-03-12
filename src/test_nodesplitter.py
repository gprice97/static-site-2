import unittest

from textnode import TextNode, TextType
from nodesplitter import NodeSplitter


class TestNodeSplitter(unittest.TestCase):

    def test_bold_text(self):
        splitter = NodeSplitter
        node_1 = TextNode("This is text with **BOLD** written all over it", TextType.NORMAL)
        #node_2 = TextNode("Crazy how **BOLD** I am", TextType.NORMAL)
        new_nodes = splitter.split_nodes_delimiter([node_1], "**", TextType.BOLD)
        print(new_nodes)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.NORMAL),
            TextNode("BOLD", TextType.BOLD),
            TextNode(" written all over it", TextType.NORMAL)
            #TextNode("Crazy how ", TextType.NORMAL),
            #TextNode("BOLD", TextType.BOLD),
            #TextNode(" I am", TextType.NORMAL)
        ])

