import unittest

from textnode import TextNode, TextType
from nodesplitter import NodeSplitter
from leafnode import LeafNode



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

    def test_extract_markdown_images(self):
        match_extractor = NodeSplitter
        matches = match_extractor.extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_nested_brackets(self):
        match_extractor = NodeSplitter
        matches = match_extractor.extract_markdown_images(
            "This is text with an ![image[2]](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image[2]", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links_multiple_images(self):
        match_extractor = NodeSplitter
        matches = match_extractor.extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_extract_markdown_links(self):
        match_extractor = NodeSplitter
        matches = match_extractor.extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_nested_brackets(self):
        match_extractor = NodeSplitter
        matches = match_extractor.extract_markdown_links(
            "[This link has [brackets] in it](http://example.com)"
        )
        self.assertListEqual([("This link has [brackets] in it", "http://example.com")], matches)

    def test_extract_markdown_links_multiple_links(self):
        match_extractor = NodeSplitter
        matches = match_extractor.extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    def test_split_images_multiple_images(self):
        self.maxDiff = None
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.NORMAL,
        )
        node_2 = TextNode(
            "![Armadillo](https://i.imgur.com/armadillo.png) This is a picture of a Armadillo and ![RolyPoly](https://i.imgur.com/rolypoly.png) a picture of a Roly Poly",
            TextType.NORMAL,
        )
        new_nodes = NodeSplitter.split_nodes_image([node, node_2])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.NORMAL),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.NORMAL),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode("Armadillo", TextType.IMAGE, "https://i.imgur.com/armadillo.png"),
                TextNode(" This is a picture of a Armadillo and ", TextType.NORMAL),
                TextNode("RolyPoly", TextType.IMAGE, "https://i.imgur.com/rolypoly.png"),
                TextNode(" a picture of a Roly Poly", TextType.NORMAL)
            ],
            new_nodes,
        )

    def test_split_images_just_image(self):
        node = TextNode(
            "![Frog](https://www.animalpedia.com/frog.png)",
            TextType.NORMAL)
        new_nodes = NodeSplitter.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Frog", TextType.IMAGE, "https://www.animalpedia.com/frog.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_image(self):
        node = TextNode(
            "I like trains",
            TextType.NORMAL)
        new_nodes = NodeSplitter.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("I like trains", TextType.NORMAL, ),
            ],
            new_nodes,
        )

    def test_split_images_not_text_node(self):
        node = TextNode(
            "How many kinds of frogs are there? Check this out for example! ![Frog](https://www.animalpedia.com/frog.png)",
            TextType.IMAGE)
        new_nodes = NodeSplitter.split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("How many kinds of frogs are there? Check this out for example! ![Frog](https://www.animalpedia.com/frog.png)", TextType.IMAGE)
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL)
        new_nodes = NodeSplitter.split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_links_not_text_node(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.LINK)
        new_nodes = NodeSplitter.split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode(
                    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                    TextType.LINK)
            ],
            new_nodes,
        )

    def test_split_links_just_link(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.NORMAL)
        new_nodes = NodeSplitter.split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_links_no_link(self):
        node = TextNode(
            "Boot Dev Bear",
            TextType.NORMAL)
        new_nodes = NodeSplitter.split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Boot Dev Bear", TextType.NORMAL),
            ],
            new_nodes,
        )

    def test_split_links_multiple(self):
        self.maxDiff = None
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.NORMAL,
        )
        node_2 = TextNode(
            "[Youtube](https://www.youtube.com) is my favorite website, I like it better than [Bing](https://www.bing.com)",
            TextType.NORMAL,
        )
        new_nodes = NodeSplitter.split_nodes_link([node, node_2])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.NORMAL),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.NORMAL),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
                TextNode("Youtube", TextType.LINK, "https://www.youtube.com"),
                TextNode(" is my favorite website, I like it better than ", TextType.NORMAL),
                TextNode("Bing", TextType.LINK, "https://www.bing.com")
            ],
            new_nodes,
        )

    def test_text_to_text_nodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes_list = NodeSplitter.text_to_text_nodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.NORMAL),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.NORMAL),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.NORMAL),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes_list
        )

    def test_text_to_text_nodes_2(self):
        text = "**text**_italic_`code block`![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)[link](https://boot.dev)"
        nodes_list = NodeSplitter.text_to_text_nodes(text)
        self.assertListEqual(
            [
                TextNode("text", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code block", TextType.CODE),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes_list
        )

## Working on This part
    def test_markdown_to_blocks(self):
        md = """
        This is **bolded** paragraph

        This is another paragraph with _italic_ text and `code` here
        This is the same paragraph on a new line

        - This is a list
        - with items
        """
        blocks = NodeSplitter.markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_empty_string(self):
        md = ""
        blocks = NodeSplitter.markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = "Just one block with no newlines"
        blocks = NodeSplitter.markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just one block with no newlines"])

    def test_excessive_newlines(self):
        md = """
        First block


        Second block after too many newlines
        """
        blocks = NodeSplitter.markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block after too many newlines"])

    def test_whitespace_trimming(self):
        md = "  Block with spaces   \n\n   Another with spaces   "
        blocks = NodeSplitter.markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block with spaces", "Another with spaces"])
