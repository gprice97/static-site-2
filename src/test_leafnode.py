import unittest

import pytest

from leafnode import LeafNode, HTMLNode


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Yahoo!", {"href": "https://www.yahoo.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.yahoo.com">Yahoo!</a>')

    def test_leaf_to_html_a_multi_prop(self):
        node = LeafNode("a", "Yahoo!", {"href": "https://www.yahoo.com", "alt-text": "I love the internet!"})
        self.assertEqual(node.to_html(), '<a href="https://www.yahoo.com" alt-text="I love the internet!">Yahoo!</a>')

    def test_tag_regex(self):
        with pytest.raises(ValueError):
            node = LeafNode("<>a", "Yahoo!", {"href": "https://www.yahoo.com", "alt-text": "I love the internet!"})

    def test_leaf_to_html_none_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_empty_tag(self):
        with pytest.raises(ValueError):
            node = LeafNode("", "Hello, world!")
