from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    CODE = "code"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(md):
    lines = md.split("\n")
    if md.startswith("#") and " " in md:
        return BlockType.HEADING
    elif all(line.startswith("- ") for line in lines if line.strip()):
        return BlockType.UNORDERED_LIST
    elif check_ordered_list(md):
        return BlockType.ORDERED_LIST
    elif all(line.startswith(">") for line in lines if line.strip()):
        return BlockType.QUOTE
    elif md.startswith("```") and md.endswith("```"):
        return BlockType.CODE
    else:
        return BlockType.PARAGRAPH


def check_ordered_list(md):
    lines = md.split("\n")
    is_ordered_list = True
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        if not line.startswith(f"{i}. "):
            is_ordered_list = False
            break
    return is_ordered_list
