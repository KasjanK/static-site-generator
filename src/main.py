import os
from splitblocks import markdown_to_blocks, markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if not block.startswith("# "):
            raise Exception("no h1 found")
        else:
            return block[2:].strip()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_file = open(from_path)
    read_markdown_file = markdown_file.read()
    template_file = open(template_path)
    read_template_file = template_file.read()
    html_nodes = markdown_to_html_node(read_markdown_file)
    html_string = html_nodes.to_html()
    page_title = extract_title(read_markdown_file)
    html_with_title = read_template_file.replace("{{ Title }}", page_title)
    full_html = html_with_title.replace("{{ Content }}", html_string)
    full_html_page = open(dest_path, "w")
    full_html_page.write(full_html)

def main():
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    #copy_contents(os.path.abspath(os.path.expanduser("static")), os.path.abspath(os.path.expanduser("public")))


if __name__ =="__main__":
    main()
