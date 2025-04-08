from enum import Enum
from htmlnode import text_node_to_html_node, ParentNode
from textnode import TextNode, TextType
from splitnode import text_to_textnodes

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_blocks.append(block)
    return stripped_blocks

def block_to_block_type(md_block):
    lines = md_block.split("\n")
    if md_block.startswith("# ") or md_block.startswith("## ") or md_block.startswith("### ") or md_block.startswith("#### ") or md_block.startswith("##### ") or md_block.startswith("###### "):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    block_handlers = {
        BlockType.PARAGRAPH: paragraph_block,
        BlockType.HEADING: heading_block,
        BlockType.QUOTE: blockquote_block,
        BlockType.CODE: code_block,
        BlockType.UNORDERED_LIST: unordered_list_block,
        BlockType.ORDERED_LIST: ordered_list_block
    }

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type in block_handlers:
            handler = block_handlers[block_type]
            children.append(handler(block))
    return ParentNode("div", children, None)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_block(block):
    lines = block.split("\n")
    paragraph_node = " ".join(lines)
    children = text_to_children(paragraph_node)
    return ParentNode("p", children)

def heading_block(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)

def code_block(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code", [child])
    return ParentNode("pre", [code])

def blockquote_block(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid blockquote")
        new_lines.append(line.lstrip(">").strip())

    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def unordered_list_block(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ordered_list_block(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)