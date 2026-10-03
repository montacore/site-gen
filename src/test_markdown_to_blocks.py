import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


        def test_another_md_to_blocks(self):
            md = """
This is a line with `code` and **bold** text.

This is a paragraph by its lonesome. Just hanging out.

- Here's a list.
- here's still a list.
- listo mixto.



                """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a line with `code` and **bold** text.",
                    "This is a paragraph by its lonesome. Just hanging out.",
                    "- Here's a list.\n- here's still a list.\n- listo mixto.",
                ]
            )
