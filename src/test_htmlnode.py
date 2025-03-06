import unittest

import pytest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    #Test that props_to_html outputs the proper string
    def test_props_to_html(self):
        node = HTMLNode("a", 'This is my link', None, {"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        test_string = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node, test_string)

    #Test that the to_html function is  not implemented, and outputs the proper error
    def test_to_html(self):
        node = HTMLNode()
        with pytest.raises(NotImplementedError):
            node.to_html()

    #Verify that when the props field is empty, the props_to_html function handles it appropriately
    def test_props_to_html_empty_props(self):
        node = HTMLNode("a", "This is my link", None, None).props_to_html()
        test_string = ''  # No props means no attributes
        self.assertEqual(node, test_string)

    #Verify that the __repr__ function outputs the proper value
    def test_html_repr(self):
        my_html_node = HTMLNode("a", "Click here", [], {"href": "https://boot.dev"}).__repr__()
        actual_text = "HTMLNode(a, Click here, None, {'href': 'https://boot.dev'})"
        self.assertEqual(my_html_node, actual_text)

    #Verify that the Constructor takes in and handles the values appropriately
    def test_htmlnode_constructor(self):
        node = HTMLNode("p", 'This is America', [], {"class": "text"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is America")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "text"})

    #Verify that htmlnode can take children values, and that they can be accessed appropriatedly
    def test_htmlnode_with_children(self):
        child1 = HTMLNode("h1", "This is a Child", None, None)
        child2 = HTMLNode("p", "This is another Child", None, None)
        parent = HTMLNode("div", None, [child1, child2], {"class": "container"})

        # Test parent properties
        self.assertEqual(parent.tag, "div")
        self.assertEqual(parent.value, None)
        self.assertEqual(len(parent.children), 2)
        self.assertEqual(parent.props, {"class": "container"})

        # Test child nodes
        self.assertEqual(parent.children[0].tag, "h1")
        self.assertEqual(parent.children[1].value, "This is another Child")


if __name__ == "__main__":
    unittest.main()
