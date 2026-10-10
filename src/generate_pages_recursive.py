from generate_page import generate_page
from pathlib import Path
import os

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    for item in os.listdir(dir_path_content):
        current = os.path.join(dir_path_content, item)
        if os.path.isfile(current) and item.endswith(".md"):
            entry = item.replace(".md", ".html")
            complete_entry = os.path.join(dest_dir_path, entry)
            generate_page(current, template_path, complete_entry)
        else:
            if os.path.isdir(current):
                next_dir_path_content = current
                
                next_dest_path = os.path.join(dest_dir_path, item)
                os.makedirs(next_dest_path, exist_ok=True)
                generate_pages_recursive(next_dir_path_content, template_path, next_dest_path)
