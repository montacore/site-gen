from markdown_to_html_node import markdown_to_html_node
from parentnode import ParentNode
from extract_title import extract_title
import os
import sys

def generate_page(from_path: str, template_path: str, dest_path: str, base_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
    
    convert_md = markdown_to_html_node(content)
    html = convert_md.to_html()
    title = extract_title(content)
    edited_content = template.replace("{{ Title }}", title).replace("{{ Content }}", html).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as fr:
        fr.write(edited_content)

    
