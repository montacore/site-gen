import re

EXAMPLE_IMG = "This is text with a ![rick roll](https://i.imgur.com/aKaqIh.gif)"
EXAMPLE_TEXT = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

def extract_markdown_images(text):
    img_reg = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"

    matches = re.findall(img_reg, text)
    return matches

def extract_markdown_link(text):
    url_reg = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(url_reg, text)
    return matches



print(extract_markdown_images(EXAMPLE_IMG))
print(extract_markdown_link(EXAMPLE_TEXT))
