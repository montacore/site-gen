from extract_links import extract_markdown_images, extract_markdown_link
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode
from text_type import TextType


"""
TODO:Tips for success:
- Make use of the extraction function extract_markdown_images and extract_markdown_link
- If there are no images or links, just return a list with the original TextNode in it. 
- Don't append any TextNodes that have empty text to the final list.
- The two functions here will be very similar
- Potentially make use of split()'s optional 2nd "maxsplits" parameter which you can set to 1 if you only want to split the string once at most. For each image extracted from the text I split the text before and after the image markdown for example:

"""
#TODO:sections = original_text.split(f"![{image_alt}]({image_link})", 1)
def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    res = []
    for node in old_nodes:
        remaining_text = node.text
        if remaining_text == "":
            continue
        if node.text_type == TextType.TEXT:
            extracted_images = extract_markdown_images(remaining_text)
            for image_alt, image_link in extracted_images:
                sections = remaining_text.split(f"![{image_alt}]({image_link})", 1)
                if sections[0] != "":

                    section = TextNode(sections[0], TextType.TEXT)
                    res.append(section)
                res.append(TextNode(image_alt, TextType.IMAGE, image_link))
                remaining_text = sections[1]
            if remaining_text != "":
                res.append(TextNode(remaining_text, TextType.TEXT))
        else:
            res.append(node)
    return res
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    res = []
    for node in old_nodes:
        remaining_text = node.text
        if remaining_text == "":
            continue
        if node.text_type == TextType.TEXT:
            extracted_links = extract_markdown_link(remaining_text)
            for link_text, link in extracted_links:
                sections = remaining_text.split(f"[{link_text}]({link})", 1)
                if sections[0] != "":

                    section = TextNode(sections[0], TextType.TEXT)
                    res.append(section)
                res.append(TextNode(link_text, TextType.LINK, link))
                remaining_text = sections[1]
            if remaining_text != "":
                res.append(TextNode(remaining_text, TextType.TEXT))
        else:
            res.append(node)
    return res

