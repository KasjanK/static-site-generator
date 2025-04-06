from enum import Enum


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
    return stripped_blocks

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(md_block):
    lines = md_block.split("\n")
    if md_block.startswith("# ") or md_block.startswith("## ") or md_block.startswith("### ") or md_block.startswith("#### ") or md_block.startswith("##### ") or md_block.startswith("###### "):
        return BlockType.HEADING
    if md_block.startswith("```") and md_block.endswith("```"):
        return BlockType.CODE
    
    lines_are_quotes = True
    for line in lines:
        if not line.startswith(">"):
            lines_are_quotes = False
            break
    if lines_are_quotes and lines:
        return BlockType.QUOTE

    lines_are_unordered = True
    for line in lines:
        if not line.startswith("- "):
            lines_are_unordered = False
            break
    if lines_are_unordered and lines:
        return BlockType.UNORDERED_LIST
    
    lines_are_ordered = True
    for i, line in enumerate(lines, 1):
        start = f"{i}. "
        if not line.startswith(start):
            lines_are_ordered = False
            break
    if lines_are_ordered and lines:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

print(block_to_block_type(">this is a quote \n>but this isnt a quote"))