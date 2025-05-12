import unittest

import pytest

from blocknode import BlockType
import blocknode

class TestParentNode(unittest.TestCase):

    def test_paragraph_block(self):
        md = """
        The Great White shark is my favorite shark, I love him
        """
        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        md = """- Shark
- Lion
- Hedgehog
- Lynx
- Whale"""
        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        md = """1. Shark
2. Lion
3. Hedgehog
4. Lynx
5. Whale"""
        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_single_heading(self):
        md = """# The Big Cheese"""
        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_double_heading(self):
        md = """## The Big Cheese"""
        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_triple_heading(self):
        md = """### The Big Cheese"""
        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_code(self):
        md = """```
        print("My little buttercup, has the sweetest smile)
        for butter in butterjar
            butterjar.remove(butter)
        ```"""
        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.CODE)

    def test_quote(self):
        md = """> \"In a few moments he was barefoot, his stockings folded in his pockets and his
> canvas shoes dangling by their knotted laces over his shoulders and, picking a
> pointed salt-eaten stick out of the jetsam among the rocks, he clambered down
> the slope of the breakwater.\""""

        block_type = blocknode.block_to_block_type(md)
        self.assertEqual(block_type, BlockType.QUOTE)
