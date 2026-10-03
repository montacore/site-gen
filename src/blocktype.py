from enum import Enum
import re

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote" 
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"


def block_to_block_type(block) -> "BlockType":
    heading_re = r"^#{1,6} "
    lines = block.split("\n")
    if re.match(heading_re, block):
        return BlockType.heading
    if block.startswith("```") and block.endswith("```"):
        return BlockType.code
    is_quote = True
    for line in lines:

        if not re.findall(r"^>\s?", line):
            is_quote = False
    if is_quote:
        return BlockType.quote
    is_unordered_list = True
    for line in lines:

        if not re.findall(r"^[\-]\s", line):
            is_unordered_list = False
    if is_unordered_list:
        return BlockType.unordered_list
    is_ordered_list = True
    for i, line in enumerate(lines):
        expected_number = i + 1
        if not line.startswith(f"{expected_number}. "):
            is_ordered_list = False
    if is_ordered_list == True:
        return BlockType.ordered_list
    else:
        return BlockType.paragraph
        
