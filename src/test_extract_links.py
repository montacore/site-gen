import unittest
from extract_links import extract_markdown_images, extract_markdown_link

class Test_Extract_Markdown(unittest.TestCase):

    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def text_extract_markdown_link(self):
        matches = extract_markdown_link(
            "This is text with a [link](https://youtube.com/bootdotdev) annnnnd this [right here](https://mytube.co)"
        )
        self.assertListEqual(["link", "https://youtube.com/bootdotdev", "right here", "https://mytube.co"], matches)

    def test_extract_invalid_link(self):
        example = "here is a string that contains both ![image](https://i.imgur.com/zjjcJKZ.png) [link](https://youtube.com/bootdotdev) and [link](https://youtube.com/bootdotdev)"
        matches = extract_markdown_link(
            example
        )
        matches2 = extract_markdown_images(
            example
        )
        self.assertNotEqual(matches2, matches)

