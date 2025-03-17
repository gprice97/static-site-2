import unittest

from textnode import TextNode, TextType
from nodesplitter import NodeSplitter


class TestNodeSplitter(unittest.TestCase):

    def test_bold_text(self):
        splitter = NodeSplitter
        node_1 = TextNode("This is text with **BOLD** written all over it", TextType.NORMAL)
        node_2 = TextNode("Crazy how **BOLD** I am", TextType.NORMAL)
        new_nodes = splitter.split_nodes_delimiter([node_1, node_2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.NORMAL),
            TextNode("BOLD", TextType.BOLD),
            TextNode(" written all over it", TextType.NORMAL),
            TextNode("Crazy how ", TextType.NORMAL),
            TextNode("BOLD", TextType.BOLD),
            TextNode(" I am", TextType.NORMAL)
        ])

    def test_front_back_bold_text(self):
        splitter = NodeSplitter
        node = TextNode("**BOLD** of you to assume I am **Silly like that**", TextType.NORMAL)
        new_nodes = splitter.split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.NORMAL),
            TextNode("BOLD", TextType.BOLD),
            TextNode(" of you to assume I am ", TextType.NORMAL),
            TextNode("Silly like that", TextType.BOLD),
            TextNode("", TextType.NORMAL)
        ])

    def test_just_bold_text(self):
        splitter = NodeSplitter
        node = TextNode("**Bold**", TextType.NORMAL)
        new_nodes = splitter.split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.NORMAL),
            TextNode("Bold", TextType.BOLD),
            TextNode("", TextType.NORMAL)
        ])

    def test_italics_text(self):
        splitter = NodeSplitter
        node_1 = TextNode("This is text with _Italics_ written all over it", TextType.NORMAL)
        node_2 = TextNode("All of these _Italics_ are pretty neat", TextType.NORMAL)
        new_nodes = splitter.split_nodes_delimiter([node_1, node_2], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [
            TextNode("This is text with ", TextType.NORMAL),
            TextNode("Italics", TextType.ITALIC),
            TextNode(" written all over it", TextType.NORMAL),
            TextNode("All of these ", TextType.NORMAL),
            TextNode("Italics", TextType.ITALIC),
            TextNode(" are pretty neat", TextType.NORMAL)
        ])

    def test_code_text(self):
        splitter = NodeSplitter
        node_1 = TextNode('My favorite Code is ```print(Hello World!)``` what is yours?', TextType.NORMAL)
        node_2 = TextNode('I really like ```for item in items: print(str(item))``` I think its really neat', TextType.NORMAL)
        new_nodes = splitter.split_nodes_delimiter([node_1, node_2], "```", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("My favorite Code is ", TextType.NORMAL),
            TextNode("print(Hello World!)", TextType.CODE),
            TextNode(" what is yours?", TextType.NORMAL),
            TextNode("I really like ", TextType.NORMAL),
            TextNode("for item in items: print(str(item))", TextType.CODE),
            TextNode(" I think its really neat", TextType.NORMAL)
        ])
