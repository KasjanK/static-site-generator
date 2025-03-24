from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        
        first_delimiter_index = old_node.text.find(delimiter)

        if first_delimiter_index == -1:
            new_nodes.append(old_node)
            continue

        if first_delimiter_index != -1:
            second_delimiter_index = old_node.text.find(delimiter, first_delimiter_index + len(delimiter))

            if second_delimiter_index == -1:
            # If we found an opening delimiter but no closing one, that's invalid
                raise ValueError("Invalid markdown: formatted section not closed")
    
            if second_delimiter_index != -1:
                before = old_node.text[:first_delimiter_index]

                inside = old_node.text[first_delimiter_index + len(delimiter):second_delimiter_index]

                after = old_node.text[second_delimiter_index + len(delimiter):]
                if before: 
                    new_nodes.append(TextNode(before, TextType.NORMAL))
                
                new_nodes.append(TextNode(inside, text_type))

                if after:
                    temp_node = TextNode(after, TextType.NORMAL)

                    result_nodes = split_nodes_delimiter([temp_node], delimiter, text_type)
                    new_nodes.extend(result_nodes)
    return new_nodes
node = TextNode("This is text with a `code block` word", TextType.NORMAL)
new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
print(new_nodes)