import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        first_delimiter_index = old_node.text.find(delimiter)

        if first_delimiter_index == -1:
            new_nodes.append(old_node)
            continue

        if first_delimiter_index != -1:
            second_delimiter_index = old_node.text.find(delimiter, first_delimiter_index + len(delimiter))

            if second_delimiter_index == -1:
            # If an opening delimiter is found but no closing one, that's invalid
                raise ValueError("Invalid markdown: formatted section not closed")
    
            if second_delimiter_index != -1:
                before = old_node.text[:first_delimiter_index]

                inside = old_node.text[first_delimiter_index + len(delimiter):second_delimiter_index]

                after = old_node.text[second_delimiter_index + len(delimiter):]
                if before: 
                    new_nodes.append(TextNode(before, TextType.TEXT))
                
                new_nodes.append(TextNode(inside, text_type))

                if after:
                    temp_node = TextNode(after, TextType.TEXT)

                    result_nodes = split_nodes_delimiter([temp_node], delimiter, text_type)
                    new_nodes.extend(result_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        image_nodes = extract_markdown_images(old_node.text)
        if not image_nodes:
            new_nodes.append(old_node)
            continue

        # for each image found
        for image_node in image_nodes:
            sections = old_node.text.split(f"![{image_node[0]}]({image_node[1]})", 1)

            # add text before the image if its not empty
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(image_node[0], TextType.IMAGE, image_node[1]))

            # update remaining text to whats after the image
            if len(sections) > 1:
                old_node.text = sections[1]
            else:
                old_node.text = ""
            
        # add any remaining text after the last image
        if old_node.text:
            new_nodes.append(TextNode(old_node.text, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        link_nodes = extract_markdown_links(old_node.text)
        if not link_nodes:
            new_nodes.append(old_node)
            continue

        # for each link found
        for link_node in link_nodes:
            sections = old_node.text.split(f"[{link_node[0]}]({link_node[1]})", 1)

            # add text before the link if its not empty
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))

            new_nodes.append(TextNode(link_node[0], TextType.LINK, link_node[1]))

            # update remaining text to whats after the link
            if len(sections) > 1:
                old_node.text = sections[1]
            else:
                old_node.text = ""
            
        # add any remaining text after the last link
        if old_node.text:
            new_nodes.append(TextNode(old_node.text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    new_node = split_nodes_delimiter([node], '**', TextType.BOLD)
    new_node = split_nodes_delimiter(new_node, '_', TextType.ITALIC)
    new_node = split_nodes_delimiter(new_node, "`", TextType.CODE)
    new_node = split_nodes_image(new_node)
    new_node = split_nodes_link(new_node)
    return new_node