import unittest

import pytest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertEqual(node, node2)

    def test_eq_url_blank(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This node has bold!", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        self.assertNotEqual(node, node2)

    def test_unique_url_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.yahoo.com")
        self.assertNotEqual(node, node2)

    def test_text_to_html_raw_text(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_text_to_html_raw_text_empty_val(self):
        node = TextNode("", TextType.NORMAL)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "")

    def test_text_to_html_bold(self):
        node = TextNode("This is a BOLD text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a BOLD text node")

    def test_text_to_html_bold_empty_val(self):
        node = TextNode("", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "")

    def test_text_to_html_italics(self):
        node = TextNode("This is a Italicized text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a Italicized text node")

    def test_text_to_html_italics_empty_val(self):
        node = TextNode("", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "")

    def test_text_to_html_code_snippet(self):
        node = TextNode("This is a Code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a Code text node")

    def test_text_to_html_code_snippet_empty_val(self):
        node = TextNode("", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "")

    def test_text_to_html_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "www.google.com")

    def test_text_to_html_link_empty_val(self):
        node = TextNode("", TextType.LINK, "www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["href"], "www.google.com")

    def test_text_to_html_link_empty_url(self):
        node = TextNode("This is a link", TextType.LINK, "")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"], "")

    def test_text_to_html_link_none(self):
        node = TextNode("This is a link", TextType.LINK)
        with pytest.raises(ValueError):
            text_node_to_html_node(node)

    def test_text_to_html_img(self):
        node = TextNode("This is an image", TextType.IMAGE, "www.sillylittleimage.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt-text"], "This is an image")
        self.assertEqual(html_node.props["src"], "www.sillylittleimage.com")

    def test_text_to_html_img_empty_val(self):
        node = TextNode("", TextType.IMAGE, "www.sillylittleimage.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt-text"], "")
        self.assertEqual(html_node.props["src"], "www.sillylittleimage.com")

    def test_text_to_html_img_empty_url(self):
        node = TextNode("This is an image", TextType.IMAGE, "")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt-text"], "This is an image")
        self.assertEqual(html_node.props["src"], "")

    def test_text_to_html_img_url_none(self):
        node = TextNode("This is an image", TextType.IMAGE)
        with pytest.raises(ValueError):
            text_node_to_html_node(node)




if __name__ == "__main__":
    unittest.main()
