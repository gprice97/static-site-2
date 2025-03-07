import unittest

import pytest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node_2 = LeafNode("span", "child 2")
        child_node_3 = LeafNode("span", "child 3")
        parent_node = ParentNode("div", [child_node, child_node_2])
        parent_node_2 = ParentNode("div", [child_node_3, parent_node])
        self.assertEqual(parent_node_2.to_html(), "<div><span>child 3</span><div><span>child</span><span>child 2</span></div></div>")

    def test_to_html_with_multiple_parents(self):
        child_node = LeafNode("span", "child")
        child_node_2 = LeafNode("span", "child 2")
        child_node_3 = LeafNode("span", "child 3")
        child_node_4 = LeafNode("span", "child 4")
        parent_node = ParentNode("div", [child_node, child_node_2])
        parent_node_2 = ParentNode("div", [child_node_3, parent_node])
        parent_node_3 = ParentNode("p", [parent_node_2])
        parent_node_4 = ParentNode("div", [parent_node_3, child_node_4])
        self.assertEqual(parent_node_4.to_html(),
                         "<div><p><div><span>child 3</span><div><span>child</span><span>child 2</span></div></div></p><span>child 4</span></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><span>child</span></div>')

    def test_to_html_no_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_tag_none(self):
        with pytest.raises(ValueError):
            parent_node = ParentNode(None, []).to_html()

    def test_children_none(self):
        with pytest.raises(ValueError):
            parent_node = ParentNode("div", None).to_html()
